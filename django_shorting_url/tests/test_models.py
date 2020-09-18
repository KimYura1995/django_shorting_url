from django.test import TestCase

from app_shortener_url.models import get_random_key, ClientModel, URLModel


class ClientModelTest(TestCase):
    IP = '127.0.0.1'

    @classmethod
    def setUpTestData(cls):
        ClientModel.objects.create(ip=cls.IP)

    def test_client_model_label(self):
        label = ClientModel._meta.verbose_name
        label_plural = ClientModel._meta.verbose_name_plural
        self.assertEqual('Клиент', label)
        self.assertEqual('Клиенты', label_plural)

    def test_ip_label(self):
        ip = ClientModel.objects.get(id=1)
        label = ip._meta.get_field('ip').verbose_name
        self.assertEqual(label, 'IP-адрес')

    def test_object_name_client_model(self):
        ip = ClientModel.objects.get(id=1)
        self.assertEqual(self.IP, str(ip))


class URLModelTest(TestCase):
    IP = '127.0.0.1'
    slug = 'test'
    original_url = 'https://www.python.org/'

    @classmethod
    def setUpTestData(cls):
        ip = ClientModel.objects.create(ip=URLModelTest.IP)
        URLModel.objects.create(ip_client=ip, slug=URLModelTest.slug, original_url=URLModelTest.original_url)

    def test_get_random_key_length(self):
        key = get_random_key()
        self.assertEqual(8, len(key))

    def test_get_random_key_ascii(self):
        key = get_random_key()
        isascii = lambda s: len(s) == len(s.encode())
        self.assertTrue(isascii(key))

    def test_url_model_label(self):
        label = URLModel._meta.verbose_name
        label_plural = URLModel._meta.verbose_name_plural
        self.assertEqual('URL', label)
        self.assertEqual('URLs', label_plural)

    def test_url_model_name(self):
        new_url = URLModel.objects.get(id=1)
        expected_object_name = f'{self.IP}, {self.original_url[:80]}, {self.slug}'
        self.assertEqual(expected_object_name, str(new_url))

    def test_url_model_get_absolute_url(self):
        new_url = URLModel.objects.get(id=1)
        self.assertEqual(f'/{self.slug}/', new_url.get_absolute_url())

    def test_ip_client_label(self):
        ip_client = URLModel.objects.get(id=1)
        label = ip_client._meta.get_field('ip_client').verbose_name
        self.assertEqual(label, 'IP-адрес')

    def test_slug_label(self):
        ip_client = URLModel.objects.get(id=1)
        label = ip_client._meta.get_field('slug').verbose_name
        self.assertEqual(label, 'Укороченный URL')

    def test_slug_max_length(self):
        ip_client = URLModel.objects.get(id=1)
        length = ip_client._meta.get_field('slug').max_length
        self.assertEqual(50, length)

    def test_original_url_label(self):
        url = URLModel.objects.get(id=1)
        label = url._meta.get_field('original_url').verbose_name
        self.assertEqual(label, 'Исходная URL ссылка')

    def test_original_url_max_length(self):
        url = URLModel.objects.get(id=1)
        length = url._meta.get_field('original_url').max_length
        self.assertEqual(500, length)
