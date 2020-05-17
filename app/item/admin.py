from django.contrib import admin
from app.item import models

# Register your models here.
admin.site.register(models.Item)
admin.site.register(models.ItemType)
