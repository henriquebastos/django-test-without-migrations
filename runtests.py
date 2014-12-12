#!/usr/bin/env python

import os
from django.core.management import call_command


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    import django
    if hasattr(django, 'setup'):
        django.setup()

    call_command('test', nomigrations=True)
