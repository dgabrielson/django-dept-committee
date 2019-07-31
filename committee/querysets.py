#######################
from __future__ import print_function, unicode_literals

from django.db.models import Q, query
from django.utils.timezone import now

#######################
#######################################################################


#######################################################################
#######################################################################


class BaseCustomQuerySet(query.QuerySet):
    """
    Custom QuerySet.
    """

    def active(self):
        """
        Returns only the active items in this queryset
        """
        return self.filter(active=True)


#######################################################################
#######################################################################


class CommitteeQuerySet(BaseCustomQuerySet):
    """
    Provide a custom model API.  Urls, views, etc. should only
    use these methods, never .filter(...).
    """


#######################################################################


class MemberQuerySet(BaseCustomQuerySet):
    """
    Provide a custom model API.  Urls, views, etc. should only
    use these methods, never .filter(...).
    """

    def current(self, dt=None):
        if dt is None:
            dt = now()
        qs = self.filter(Q(end_date__isnull=True) | Q(end_date__gt=dt))
        qs = qs.filter(start_date__lte=dt)
        return qs

    def past(self, dt=None):
        if dt is None:
            dt = now()
        return self.filter(end_date__lt=dt)

    def future(self, dt=None):
        if dt is None:
            dt = now()
        return self.filter(start_date__gt=dt)

    def current_or_future(self, dt=None):
        if dt is None:
            dt = now()
        return self.filter(Q(end_date__isnull=True) | Q(end_date__gt=dt))


#######################################################################
#######################################################################
