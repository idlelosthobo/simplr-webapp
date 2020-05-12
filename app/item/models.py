from django.db import models
from app.container.models import Container


class Item(models.Model):
    container = models.ForeignKey(Container, on_delete=models.DO_NOTHING, editable=False)
    name = models.CharField(max_length=32)
    archived = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name