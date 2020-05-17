from django.db import models
from django.contrib.auth.models import User


class ContainerType(models.Model):
    name = models.CharField(max_length=32, default='')
    function = models.CharField(max_length=32, default='')
    description = models.TextField(default='')
    font_awesome_logo = models.CharField(max_length=32, default='far fa-square')

    def __str__(self):
        return self.name


class Container(models.Model):
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    container_type = models.ForeignKey(ContainerType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32, default='')
    archived = models.BooleanField(default=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def children_list(self):
        children_list = Container.objects.filter(parent=self.id)
        return children_list

    def item_list(self):
        from app.item.models import Item
        item_list = Item.objects.filter(container_id=self.id)
        return item_list

    def __str__(self):
        return self.name


class ContainerPermission(models.Model):
    pass