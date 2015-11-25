# -*- coding: utf-8 -*-
"""Piwik template tag."""

import logging

from django import template
from django.conf import settings

register = template.Library()


def _tracking_code():
    if getattr(settings, 'DEBUG', True):
        return {'error': 'DEBUG mode'}

    id_ = getattr(settings, 'PIWIK_SITE_ID', None)
    if id_ is None:
        error = 'PIWIK_SITE_ID does not exist.'
        logging.error(error)
        return {'error': error}
    url = getattr(settings, 'PIWIK_URL', None)
    if url is None:
        error = 'PIWIK_URL does not exist.'
        logging.error(error)
        return {'error': error}

    domain = getattr(settings, 'PIWIK_DOMAIN', None)
    return {'id': id_, 'url': url, 'cookiedomain': domain}


@register.inclusion_tag('piwik/tracking_code.html')
def tracking_code():
    return _tracking_code()


@register.inclusion_tag('piwik/tracking_code_404.html')
def tracking_code_404():
    return _tracking_code()
