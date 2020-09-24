from django.urls import path

from app_shortener_url.views import URLShortenerView, URLRedirectView, URLShortenerAPIView


urlpatterns = [
    path('', URLShortenerView.as_view(), name='url_shortener'),
    path('api/', URLShortenerAPIView.as_view(), name='url_shortener_api'),
    path('<slug:slug>/', URLRedirectView.as_view(), name='url_redirect'),
]
