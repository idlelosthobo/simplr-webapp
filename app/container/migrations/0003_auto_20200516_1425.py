# Generated by Django 3.0.5 on 2020-05-16 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('container', '0002_auto_20200516_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='container',
            name='parent',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='container.Container'),
        ),
    ]