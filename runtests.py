#!/usr/bin/env python

import os
import sys
import subprocess
from importlib import import_module


if __name__ == '__main__':
    # We need to set the PYTHONPATH environment variable
    # because otherwise subprocesses on Travis CI won't
    # include this directory in the pythonpath
    root_dir = os.path.dirname(os.path.realpath(__file__))
    os.environ['PYTHONPATH'] = root_dir + os.pathsep + os.environ.get('PYTHONPATH', '')

    # Test using django.test.runner.DiscoverRunner
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    # We need to use subprocess.call instead of django's execute_from_command_line
    # because we can only setup django's settings once, and it's bad
    # practice to change them at runtime
    subprocess.call(['django-admin', 'test', '--nomigrations'])
    subprocess.call(['django-admin', 'test', '-n'])

    # Test using django_nose.NoseTestSuiteRunner
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.nose_settings'

    for module in ('nose', 'django_nose',):
        try:
            import_module(module)
        except ImportError:
            print("Testing failed: could not import {0}, try pip installing it".format(module))
            sys.exit(1)

    # Add pdb flag as this is only supported by nose
    subprocess.call(['django-admin', 'test', 'tests.myapp.nose_tests', '--nomigrations', '--pdb'])
    subprocess.call(['django-admin', 'test', 'tests.myapp.nose_tests', '-n', '--pdb'])
