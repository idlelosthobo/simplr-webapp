from django.db import models
from django.contrib.auth.models import User
from app.container.models import Container


class ItemType(models.Model):
    name = models.CharField(max_length=32, default='')
    function = models.CharField(max_length=32, default='')
    description = models.TextField(default='')
    font_awesome_logo = models.CharField(max_length=32, default='far fa-circle')

    def __str__(self):
        return self.name


class Item(models.Model):
    container = models.ForeignKey(Container, on_delete=models.DO_NOTHING, editable=False)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    item_type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32)
    data = models.TextField(default='')
    data_short = models.CharField(max_length=128, default='', editable=False)
    archived = models.BooleanField(default=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name