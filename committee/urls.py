############################################################################
from __future__ import print_function, unicode_literals

from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Committee

############################################################################

urlpatterns = [
    url(
        r"^$",
        ListView.as_view(queryset=Committee.objects.filter(active=True)),
        name="committee-list",
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        DetailView.as_view(queryset=Committee.objects.filter(active=True)),
        name="committee-detail",
    ),
]


############################################################################
