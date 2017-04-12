from test_without_migrations.management.commands._base import CommandMixin, TestCommand, TestServerCommand


class Command(CommandMixin, TestServerCommand or TestCommand):
    pass
