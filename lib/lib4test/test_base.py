from rest_framework.test import APIClient as Client
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User


class TestBase:
    def __init__(self, testcase: TestCase, username=None):
        clinet = Client()
        if username:
            self.user = User.objects.create_user(username=username, email='{}@mysite.com'.format(username))
            clinet.force_login(self.user)
        self.client = clinet
        self.testcase = testcase

    def get(self, url, data=None, status_code=status.HTTP_200_OK):
        r = self.client.get(url, data=data, content_type='application/json')
        self.testcase.assertEqual(r.status_code, status_code)
        return r.data

    def post(self, url, data=None, status_code= status.HTTP_201_CREATED):
        r = self.client.post(url, data=data, format='multipart/form-data')
        self.testcase.assertEqual(r.status_code, status_code)
        return r.data
