# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeyaab', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='pic_folder/__none/no-img.png', upload_to='pic_folder/'),
        ),
    ]
