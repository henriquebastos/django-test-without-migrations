# coding: utf-8
from optparse import make_option
from django.core.management.commands.test import Command as TestCommand


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


class Command(TestCommand):
    option_list = TestCommand.option_list + (
        make_option('--nomigrations',
            action='store_true', dest='nomigrations', default=False,
            help='Tells Django to NOT use migrations and create all tables directly.'),
    )

    def handle(self, *test_labels, **options):
        from django.conf import settings

        if options['nomigrations']:
            settings.MIGRATION_MODULES = DisableMigrations()

        super(Command, self).handle(*test_labels, **options)
