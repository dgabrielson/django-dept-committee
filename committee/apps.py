#########################################################################

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

#########################################################################


class CommitteeConfig(AppConfig):
    name = "committee"
    verbose_name = _("Committees")

    def ready(self):
        """
        Any app specific startup code, e.g., register signals,
        should go here.
        """


#########################################################################
