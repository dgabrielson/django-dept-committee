# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("committee", "0005_auto_20170929_1029")]

    operations = [
        migrations.AlterModelOptions(
            name="committee", options={"ordering": ["ordering", "name"]}
        ),
        migrations.AddField(
            model_name="committee",
            name="ordering",
            field=models.PositiveSmallIntegerField(
                default=50,
                help_text="Use this to change the order in which committees appear",
            ),
        ),
    ]
