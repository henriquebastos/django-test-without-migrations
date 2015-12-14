#!/bin/sh
set -x

python setup.py clean
rm -r dist/ build/ django_test_without_migrations.egg-info/
python setup.py sdist bdist_wheel
