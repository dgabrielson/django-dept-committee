# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 14:42
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0001_initial"),
        ("committee", "0002_auto_20170602_1056"),
    ]

    operations = [
        migrations.AlterModelOptions(name="committee", options={"ordering": ["name"]}),
        migrations.RenameField(
            model_name="committee", old_name="Active", new_name="active"
        ),
        migrations.RenameField(
            model_name="committee", old_name="Last_Updated", new_name="last_updated"
        ),
        migrations.RenameField(
            model_name="committee", old_name="Chair", new_name="chair"
        ),
        migrations.RenameField(
            model_name="committee", old_name="Members", new_name="members"
        ),
        migrations.RenameField(
            model_name="committee", old_name="Name", new_name="name"
        ),
        migrations.RenameField(
            model_name="committee", old_name="Short_Name", new_name="slug"
        ),
    ]
