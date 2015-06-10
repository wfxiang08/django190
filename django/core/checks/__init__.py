# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .messages import (CheckMessage,
        Debug, Info, Warning, Error, Critical,
        DEBUG, INFO, WARNING, ERROR, CRITICAL)
from .registry import register, run_checks, tag_exists, Tags

# Import these to force registration of checks
import django.core.checks.model_checks  # NOQA
import django.core.checks.security.base  # NOQA
import django.core.checks.security.csrf  # NOQA
import django.core.checks.security.sessions  # NOQA
import django.core.checks.templates  # NOQA

__all__ = [
    'CheckMessage',
    'Debug', 'Info', 'Warning', 'Error', 'Critical',
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
    'register', 'run_checks', 'tag_exists', 'Tags',
]
