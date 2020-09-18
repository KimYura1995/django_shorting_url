from http import HTTPStatus

from django.test import TestCase

from app_shortener_url.models import ClientModel, URLModel


class TestShortenerView(TestCase):
    IP = '127.0.0.1'
    slug = 'test'
    original_url = 'https://www.python.org/'

    @classmethod
    def setUpTestData(cls):
        ip = ClientModel.objects.create(ip=cls.IP)
        URLModel.objects.create(ip_client=ip, slug=cls.slug, original_url=cls.original_url)

    def test_URL_shortener_view_get_context(self):
        response = self.client.get("/", follow=True)
        self.assertEqual(response.context['history'][0], URLModel.objects.get(id=1))


