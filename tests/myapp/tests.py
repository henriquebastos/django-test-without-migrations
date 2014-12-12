# coding: utf-8
from django.test import TestCase
from .models import Person


class PersonTest(TestCase):
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
