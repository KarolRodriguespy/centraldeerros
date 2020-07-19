from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate

# Create your tests here.
from events.models import Event


class IntegrationTests(APITestCase):

    def setUp(self):
        user = User.objects.create(username='admin', password='123456')
        token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_event(self, **kwargs):
        self.token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        data = {"user": "1",
                "level": "error",
                "environment": "homologação",
                "address": "191.177.182.188",
                "log": "quasedeu"}
        request = self.client.post('http://projeto-centraldeerros.herokuapp.com/events/create', data=data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_event_without_authentication(self):
        self.client = APIClient()
        data = {"user": "1",
                "level": "error",
                "environment": "homologação",
                "address": "191.177.182.188",
                "log": "quasedeu"}
        request = self.client.post('http://projeto-centraldeerros.herokuapp.com/events/create', data=data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_event(self):
        self.token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))

        request = self.client.get('http://projeto-centraldeerros.herokuapp.com/events/list', format='json')
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_list_event_without_authentication(self):
        self.client = APIClient()
        request = self.client.get('http://projeto-centraldeerros.herokuapp.com/events/list', format='json')
        self.assertEquals(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detail_event(self):
        self.token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        request = self.client.get('http://projeto-centraldeerros.herokuapp.com/events/detail/1', format='json')
        self.assertEquals(request.status_code, status.HTTP_200_OK)

    def test_detail_event_without_authentication(self):
        self.client = APIClient()
        request = self.client.get('http://projeto-centraldeerros.herokuapp.com/events/detail/1', format='json')
        self.assertEquals(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_deleted_event(self):
        self.token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        self.user = User.objects.get()

        new_event = Event.objects.create(user=self.user, level='error', environment='dev', address='191.177.182.188',
                                         log='teste')
        request = self.client.delete('http://projeto-centraldeerros.herokuapp.com/events/delete/1', kwargs={'pk': new_event.pk},
                                     format='json')
        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_event_without_authentication(self):
        self.client = APIClient()
        self.user = User.objects.get()

        new_event = Event.objects.create(user=self.user, level='error', environment='dev', address='191.177.182.188',
                                         log='teste')
        request = self.client.delete('http://projeto-centraldeerros.herokuapp.com/events/delete/2', kwargs={'pk': new_event.pk},
                                     format='json')
        self.assertEquals(request.status_code, status.HTTP_401_UNAUTHORIZED)