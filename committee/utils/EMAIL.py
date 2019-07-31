#!/usr/bin/env python
"""
EMAIL.py

Generate a listing of committee relevant email addresses/lists
"""

from django.template.defaultfilters import slugify

from committee.models import Committee


def get_email(person):
    if person is not None:
        email_list = person.emailaddress_set.active()
        if email_list:
            return email_list[0].address


def main():
    result = {}

    for committee in Committee.objects.filter(active=True):
        group = []
        chair = []
        for m in committee.member_set.active().current():
            email = get_email(m.person)
            if not email:
                continue
            if m.chair:
                chair.append(email)
            group.append(email)

        chair_slug = committee.slug
        if not chair_slug.endswith("-chair"):
            chair_slug += "-chair"
        slug = committee.slug
        if not slug.endswith("-committee"):
            slug += "-committee"
        chair = list(set(chair))
        group = list(set(group))
        result[chair_slug] = ",".join(chair)
        result[slug] = ",".join(list(set(group)))

    return result
