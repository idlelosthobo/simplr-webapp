# Generated by Django 3.0.5 on 2020-05-16 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0003_auto_20200516_1425'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_auto_20200516_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='archived',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='container',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='container.Container'),
        ),
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='data_short',
            field=models.CharField(default='', editable=False, max_length=128),
        ),
    ]
