#!/usr/bin/env python

import os
from django.core.management import execute_from_command_line


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    execute_from_command_line(['manage.py', 'test', '--nomigrations'])
    execute_from_command_line(['manage.py', 'test', '-nm'])
