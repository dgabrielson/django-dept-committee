# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("committee", "0006_auto_20170929_1148")]

    operations = [
        migrations.AlterField(
            model_name="committee",
            name="chair",
            field=models.ForeignKey(
                blank=True,
                help_text='Only people with the "committee" flag are shown',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="committee_chair",
                to="people.Person",
            ),
        )
    ]