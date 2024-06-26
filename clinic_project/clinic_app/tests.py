from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Person, Team


class TeamTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_team(self):
        url = '/api/teams/'
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Test Team')

    def test_get_teams(self):
        url = '/api/teams/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_team(self):
        team = Team.objects.create(name='Initial Team Name')
        url = f'/api/teams/{team.id}/'
        updated_data = {'name': 'Updated Team Name'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.get(id=team.id).name, 'Updated Team Name')

    def test_delete_team(self):
        team = Team.objects.create(name='Team to delete')
        url = f'/api/teams/{team.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)


class PersonTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')

    def test_create_person(self):
        url = '/api/persons/'
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'team': self.team.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'Test')

    def test_get_persons(self):
        url = '/api/persons/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        person = Person.objects.create(first_name='Test', last_name='User', email='test@example.com', team=self.team)
        url = f'/api/persons/{person.id}/'
        updated_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'team': self.team.id
        }
        response = self.client.put(url, updated_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get(id=person.id).first_name, 'Updated')

    def test_delete_person(self):
        person = Person.objects.create(first_name='Test', last_name='User', email='test@example.com', team=self.team)
        url = f'/api/persons/{person.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
