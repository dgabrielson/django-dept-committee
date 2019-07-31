############################################################################
from __future__ import unicode_literals

from django import forms

from markuphelpers.forms import LinedTextareaWidget, ReStructuredTextFormMixin

from .models import Committee

############################################################################


class CommitteeForm(ReStructuredTextFormMixin, forms.ModelForm):

    restructuredtext_fields = [
        ("membership", True),
        ("means_of_selection", True),
        ("terms_of_reference", True),
        ("remarks", True),
    ]

    class Meta:
        model = Committee
        widgets = {
            "membership": LinedTextareaWidget(attrs={"rows": 8, "cols": 80}),
            "means_of_selection": LinedTextareaWidget(attrs={"rows": 8, "cols": 80}),
            "terms_of_reference": LinedTextareaWidget,
            "remarks": LinedTextareaWidget,
        }
        exclude = []


############################################################################
