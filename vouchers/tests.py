from django.test import TestCase
from django.db import connection
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Master, Subsidiary, Person


# Create your tests here.

class MasterSubsidiaryModelTest(TestCase):
    def setUp(cls):
        cls.person = Person.objects.create(first_name="first", last_name="last")
        cls.master = Master.objects.create(title="Master 1", code="M001", creator=cls.person)
        cls.subsidiary = Subsidiary.objects.create(
            title="Subsidiary 1", code="S001", creator=cls.person, master=cls.master
        )

    def test_master_creation(self):
        self.assertEqual(self.master.title, "Master 1")
        self.assertEqual(self.master.code, "M001")
        self.assertEqual(self.master.creator.first_name, "first")
        self.assertEqual(self.master.creator.last_name, "last")
        self.assertEqual(self.master.__str__(), "Master 1")

    def test_subsidiary_creation(self):
        self.assertEqual(self.subsidiary.title, "Subsidiary 1")
        self.assertEqual(self.subsidiary.code, "S001")
        self.assertEqual(self.subsidiary.master, self.master)
        self.assertEqual(self.subsidiary.__str__(), "Subsidiary 1")


class MasterSubsidiaryAPITest(APITestCase):
    def setUp(cls):
        cls.person = Person.objects.create(first_name="Test", last_name="Person")
        cls.master = Master.objects.create(title="Master 1", code="M001", creator=cls.person)
        cls.subsidiary = Subsidiary.objects.create(
            title="Subsidiary 1", code="S001", creator=cls.person, master=cls.master
        )

    def test_master_list(self):
        response = self.client.get('/masters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_subsidiary_list(self):
        response = self.client.get('/subsidiaries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_master_creation(self):
        response = self.client.post('/masters/', {
            'title': 'Master 2',
            'code': 'M002',
            'creator': self.person.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Master.objects.count(), 2)

    def test_subsidiary_creation(self):
        response = self.client.post('/subsidiaries/', {
            'title': 'Subsidiary 2',
            'code': 'S002',
            'creator': self.person.id,
            'master': self.master.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subsidiary.objects.count(), 2)


