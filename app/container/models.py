from django.db import models
from django.contrib.auth.models import User


class ContainerType(models.Model):
    name = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.name


class Container(models.Model):
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(ContainerType, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32, default='')
    archived = models.BooleanField(default=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class ContainerPermission(models.Model):
    pass