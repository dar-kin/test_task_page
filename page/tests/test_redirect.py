from django.test import TestCase

class TestRedirect(TestCase):
    def test_redirect(self):
        response = self.client.get("/", follow=True)
        self.assertRedirects(response, "/admin/login/?next=/admin/")
