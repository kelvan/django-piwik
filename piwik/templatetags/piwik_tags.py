# -*- coding: utf-8 -*-
"""Piwik template tag."""

import logging

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('piwik/tracking_code.html')
def tracking_code():
    if settings.DEBUG:
        return {'error': 'DEBUG mode'}
    try:
        id_ = settings.PIWIK_SITE_ID
    except AttributeError:
        error = 'PIWIK_SITE_ID does not exist.'
        logging.error(error)
        return {'error': error}
    try:
        url = settings.PIWIK_URL
    except AttributeError:
        error = 'PIWIK_URL does not exist.'
        logging.error()
        return {'error': error}
    return {'id': id_, 'url': url}
