# Generated by Django 3.0.5 on 2020-05-13 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0004_auto_20200511_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='container.Container'),
        ),
    ]
