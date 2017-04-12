Django Test Without Migrations: Disable migrations when running your Django tests
=================================================================================

.. image:: https://img.shields.io/travis/henriquebastos/django-test-without-migrations.svg
    :target: https://travis-ci.org/henriquebastos/django-test-without-migrations
    :alt: Test Status

.. image:: https://landscape.io/github/henriquebastos/django-test-without-migrations/master/landscape.png
    :target: https://landscape.io/github/henriquebastos/django-test-without-migrations/master
    :alt: Code Helth

.. image:: https://img.shields.io/pypi/v/django-test-without-migrations.svg
    :target: https://pypi.python.org/pypi/django-test-without-migrations/
    :alt: Latest PyPI version


.. image:: https://img.shields.io/pypi/dm/django-test-without-migrations.svg
    :target: https://pypi.python.org/pypi/django-test-without-migrations/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/github/license/henriquebastos/django-test-without-migrations.svg
    :target: https://pypi.python.org/pypi/django-test-without-migrations/
    :alt: License

*Test Without Migrations* is a `manage.py test` command extension.

The new Django 1.7 and 1.8 migration backend demands that you create a migration every time you change a model.

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

You will want to make sure that `test_without_migrations` appears **before**
any other apps in ``INSTALLED_APPS`` that provide a custom ``test`` management
command.

In this case, you will also want to set the ``TEST_WITHOUT_MIGRATIONS_COMMAND``
setting:

.. code-block:: python

    TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'

This will ensure that you don't lose any additional functionality provided by
your custom ``test`` management command.


Usage
-----

Inform the flag ``--nomigrations`` when running your tests:

.. code-block:: bash

    $ python manage.py test --nomigrations

Or use the alias ``-n``:

.. code-block:: bash

    $ python manage.py test -n

Version 0.6 also supports `testserver` command:

.. code-block:: bash

    $ python manage.py testserver --nomigrations myfixture.json

Inspiration
-----------

This library was directly inspired by this solution: https://gist.github.com/NotSqrt/5f3c76cd15e40ef62d09

Author
------

* `Henrique Bastos <http://github.com/henriquebastos>`_

License
=======

The MIT License.
