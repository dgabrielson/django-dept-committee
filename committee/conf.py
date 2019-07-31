"""
The DEFAULT configuration is loaded when the named _CONFIG dictionary
is not present in your settings.
"""
#######################
from __future__ import print_function, unicode_literals

from django.conf import settings

#######################

CONFIG_NAME = "COMMITTEE_CONFIG"  # must be uppercase!


DEFAULT = {
    "membership:help": "This will be processed as ReStructuredText",
    "means_of_selection:help": "This will be processed as ReStructuredText",
    "terms_of_reference:help": "This will be processed as ReStructuredText",
    "remarks:help": "This will be processed as ReStructuredText",
}


#########################################################################


def get(setting):
    """
    get(setting) -> value

    setting should be a string representing the application settings to
    retrieve.
    """
    assert setting in DEFAULT, "the setting %r has no default value" % setting
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return app_settings.get(setting, DEFAULT[setting])


def get_all():
    """
    Return all current settings as a dictionary.
    """
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return dict(
        [(setting, app_settings.get(setting, DEFAULT[setting])) for setting in DEFAULT]
    )


#########################################################################
