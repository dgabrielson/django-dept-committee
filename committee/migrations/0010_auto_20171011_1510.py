# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("committee", "0009_member_data")]

    operations = [
        migrations.AlterModelOptions(
            name="committee",
            options={"base_manager_name": "objects", "ordering": ["ordering", "name"]},
        ),
        migrations.AlterModelOptions(
            name="member",
            options={"base_manager_name": "objects", "ordering": ["-chair", "person"]},
        ),
        migrations.RemoveField(model_name="committee", name="chair"),
        migrations.RemoveField(model_name="committee", name="members"),
        migrations.AlterField(
            model_name="member",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
