# coding: utf-8
import os
from .models import Person
from nose.tools import with_setup
from django.conf import settings
from django.test.utils import get_runner


class TestClassWithoutUnittest(object):
    """
    Uses a model to ensure the table exist, even with no migrations available.
    """
    def setUp(self):
        self.person = Person.objects.create(name='Arthur', age=18)

    def test_instance(self):
        assert isinstance(self.person, Person)

    def test_name(self):
        assert self.person.name == 'Arthur'

    def test_age(self):
        assert self.person.age == 18

    def test_is_nose_runner(self):
        TestRunner = get_runner(settings)
        from django_nose.runner import NoseTestSuiteRunner as expected
        assert TestRunner is expected
