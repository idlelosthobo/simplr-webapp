# Generated by Django 3.0.5 on 2020-05-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20200516_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='font_awesome_logo',
            field=models.CharField(default='far fa-circle', max_length=32),
        ),
    ]
