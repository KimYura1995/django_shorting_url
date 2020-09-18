from django.urls import path

from app_shortener_url.views import URLShortenerView, URLRedirectView

urlpatterns = [
    path('', URLShortenerView.as_view(), name='url_shortener'),
    path('<slug:slug>/', URLRedirectView.as_view(), name='url_redirect'),
]
