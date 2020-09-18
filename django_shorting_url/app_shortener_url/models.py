import random
import string

from django.db import models
from django.urls import reverse


def get_random_key(length=8):
    chars = string.ascii_letters + string.digits
    key = ''.join(random.choice(chars) for _ in range(length))
    return key


class ClientModel(models.Model):
    ip = models.GenericIPAddressField('IP-адрес')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return str(self.ip)


class URLModel(models.Model):
    ip_client = models.ForeignKey(ClientModel, verbose_name='IP-адрес', blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(
        'Укороченный URL',
        max_length=50,
        unique=True,
        default=get_random_key,
    )
    original_url = models.URLField('Исходная URL ссылка', max_length=500)

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.ip_client}, {self.original_url[:80]}, {self.slug}'

    def get_absolute_url(self):
        return reverse('url_redirect', args=[self.slug])
