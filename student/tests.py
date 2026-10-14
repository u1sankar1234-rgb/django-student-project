from django.test import TestCase, Client
from django.urls import reverse

class StudentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

