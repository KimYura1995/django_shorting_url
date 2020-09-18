from django.test import TestCase

from app_shortener_url.forms import URLShortenerForm
from app_shortener_url.models import ClientModel, URLModel


class URLShortenerFormTest(TestCase):
    IP = '127.0.0.1'
    slug = 'test'
    original_url = 'https://www.python.org/'

    @classmethod
    def setUpTestData(cls):
        ip = ClientModel.objects.create(ip=cls.IP)
        URLModel.objects.create(
            ip_client=ip,
            slug=cls.slug,
            original_url=cls.original_url,
        )

    def test_clean_extra_slug(self):
        ip = ClientModel.objects.create(ip=URLShortenerFormTest.IP)
        data = {'ip': ip, 'original_url': self.original_url, 'extra_slug': self.slug}
        form = URLShortenerForm(data)
        self.assertFalse(form.is_valid())

