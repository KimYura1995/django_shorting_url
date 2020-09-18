from django.contrib import admin

from app_shortener_url.models import ClientModel, URLModel


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('ip',)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


@admin.register(URLModel)
class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_client', 'slug', 'original_url')
    list_display_links = ('slug',)
