Django Test Without Migrations: Disable migrations when running your Django tests
=================================================================================

.. image:: https://travis-ci.org/henriquebastos/django-test-without-migrations.png?branch=master
    :target: https://travis-ci.org/henriquebastos/django-test-without-migrations
    :alt: Test Status

.. image:: https://landscape.io/github/henriquebastos/django-test-without-migrations/master/landscape.png
    :target: https://landscape.io/github/henriquebastos/django-test-without-migrations/master
    :alt: Code Helth

.. image:: https://pypip.in/v/django-test-without-migrations/badge.svg
    :target: https://crate.io/packages/django-test-without-migrations/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/django-test-without-migrations/badge.svg
    :target: https://crate.io/packages/django-test-without-migrations/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/license/django-test-without-migrations/badge.svg
    :target: https://pypi.python.org/pypi/django-test-without-migrations/
    :alt: License

*Test Without Migrations* is a `manage.py test` command extension.

The new Django 1.7 migration backend demands that you create a migration every time you change a model.

This can be inconvenient when you're just trying to explore your models code.

In older Django versions, with `South` we could use the `SOUTH_TEST_MIGRATIONS` settings to tell Django to simply create all model tables without running migrations.

This app adds this capability to Django by extending the `manage.py test` command with a `--nomigrations` option.


Installation
------------

*Test Without Migrations* works with Django 1.7+.

To install it, simply:

.. code-block:: bash

    $ pip install django-test-without-migrations

Then add it to your `INSTALLED_APPS` on your `settings.py`:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'test_without_migrations',
    )

Usage
-----

Inform the flag `--nomigrations` when running your tests:

.. code-block:: bash

    $ python manage.py test --nomigrations

Inspiration
-----------

This library was directly inspired by this solution: https://gist.github.com/NotSqrt/5f3c76cd15e40ef62d09

Author
------

* `Henrique Bastos <http://github.com/henriquebastos>`_

License
=======

The MIT License.
