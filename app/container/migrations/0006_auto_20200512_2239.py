# Generated by Django 3.0.5 on 2020-05-13 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0005_auto_20200512_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='container.Container'),
        ),
    ]
