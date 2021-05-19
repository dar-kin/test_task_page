from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestPageList(TestCase):
    fixtures = ["fixtures/pages.json"]

    def setUp(self) -> None:
        self.client = APIClient()

    def test_whole_list(self):
        response = self.client.get(reverse("api:page-list"))
        data = response.data
        self.assertEqual(3, len(data))

    def test_label_list(self):
        response = self.client.get(reverse("api:page-pages", args=["page"]))
        data = response.data
        self.assertEqual(1, len(data))

    def test_label_list1(self):
        response = self.client.get(reverse("api:page-pages", args=["page2"]))
        data = response.data
        self.assertEqual(2, len(data))

