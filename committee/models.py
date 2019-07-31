"""
The committee model -- basically used to generate committee mailing lists.
"""
############################################################################

from __future__ import print_function, unicode_literals

from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from . import conf
from .querysets import CommitteeQuerySet, MemberQuerySet

############################################################################


class CommitteeBaseModel(models.Model):
    active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


############################################################################


@python_2_unicode_compatible
class Committee(CommitteeBaseModel):
    name = models.CharField(
        max_length=128, unique=True, help_text="A descriptive name."
    )
    slug = AutoSlugField(
        unique=True,
        populate_from="name",
        help_text="A short name suitable for use in a url.",
    )

    membership = models.TextField(blank=True, help_text=conf.get("membership:help"))
    means_of_selection = models.TextField(
        blank=True, help_text=conf.get("means_of_selection:help")
    )
    term = models.CharField(
        max_length=128,
        blank=True,
        help_text="The length of time individual member of the committee normally serves",
    )
    quorum = models.CharField(
        max_length=128,
        blank=True,
        help_text="the minimum number of members to make meetings valid",
    )
    terms_of_reference = models.TextField(
        blank=True, help_text=conf.get("terms_of_reference:help")
    )
    remarks = models.TextField(blank=True, help_text=conf.get("remarks:help"))

    ordering = models.PositiveSmallIntegerField(
        default=50, help_text="Use this to change the order in which committees appear"
    )

    objects = CommitteeQuerySet.as_manager()

    class Meta:
        ordering = ["ordering", "name"]
        base_manager_name = "objects"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("committee-detail", kwargs={"slug": self.slug})


############################################################################


@python_2_unicode_compatible
class Member(CommitteeBaseModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    person = models.ForeignKey(
        "people.Person",
        on_delete=models.CASCADE,
        limit_choices_to={"active": True, "flags__slug": "committee"},
        help_text='Only people with the "committee" flag are shown',
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    chair = models.BooleanField(default=False)
    ex_officio = models.BooleanField(default=False)

    objects = MemberQuerySet.as_manager()

    class Meta:
        ordering = ["-chair", "person"]
        base_manager_name = "objects"

    def __str__(self):
        return "{}".format(self.person)

    def get_absolute_url(self):
        return self.person.get_absolute_url()


############################################################################
