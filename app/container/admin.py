from django.contrib import admin
from app.container import models


admin.site.register(models.Container)
admin.site.register(models.ContainerType)

