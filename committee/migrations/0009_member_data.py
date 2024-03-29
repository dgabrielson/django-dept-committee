# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 15:03
from __future__ import unicode_literals

from datetime import date

from django.db import migrations
from django.utils.timezone import now


def forward_data(apps, schema_editor):
    """
    Forward data migration: construct 'Member' objects from Committee
    chair and members fields.
    """

    def _get_start_date():
        n = now()
        if n.month >= 7:
            return date(n.year, 7, 1)
        else:
            return date(n.year - 1, 7, 1)

    Committee = apps.get_model("committee", "Committee")
    Member = apps.get_model("committee", "Member")

    for c in Committee.objects.all():
        if c.chair:
            data = {
                "committee": c,
                "person": c.chair,
                "chair": True,
                "start_date": _get_start_date(),
            }
            Member.objects.get_or_create(**data)
        for m in c.members.all():
            data = {
                "committee": c,
                "person": m,
                "chair": False,
                "start_date": _get_start_date(),
            }
            Member.objects.get_or_create(**data)


def backward_data(apps, schema_editor):
    """
    Backward data migration: construct Committee chair and members
    fields from Member objects.
    """
    # Committee = apps.get_model("committee", "Committee")
    # for c in Committee.objects.all():
    #     c.chair = None
    #     c.members.clear()
    #     c.save()

    Member = apps.get_model("committee", "Member")
    for m in Member.objects.all():
        if m.chair:
            m.committee.chair = m.person
            m.committee.save()
        else:
            m.committee.members.add(m.person)


class Migration(migrations.Migration):

    dependencies = [("committee", "0008_member")]

    operations = [migrations.RunPython(forward_data, backward_data)]
