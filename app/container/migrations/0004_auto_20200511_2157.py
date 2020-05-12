# Generated by Django 3.0.5 on 2020-05-12 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0003_auto_20200511_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='child',
        ),
        migrations.AlterField(
            model_name='container',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='container.Container'),
        ),
    ]