import logging

from django.shortcuts import redirect
from django.views.generic import FormView, DetailView

from app_shortener_url.forms import URLShortenerForm
from app_shortener_url.models import ClientModel, URLModel


logger = logging.getLogger('views')


class URLShortenerView(FormView):
    form_class = URLShortenerForm
    template_name = 'app_shortener_url/shortener.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        ClientModel.objects.get_or_create(ip=request.META.get('REMOTE_ADDR'))
        logger.info(f'{request.META.get("REMOTE_ADDR")} - has entered')
        return super(URLShortenerView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(URLShortenerView, self).get_context_data(**kwargs)
        queryset = URLModel.objects.filter(ip_client__ip=self.request.META.get('REMOTE_ADDR'))
        context['history'] = queryset[:5]
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            new_url = form.save(commit=False)
            new_url.ip_client = ClientModel.objects.get(ip=self.request.META.get('REMOTE_ADDR'))
            extra_slug = form.cleaned_data['extra_slug']
            if extra_slug:
                new_url.slug = extra_slug
            logger.info(f'{request.META.get("REMOTE_ADDR")} - form valid {form}')
            return self.form_valid(new_url)
        else:
            logger.error(f'{request.META.get("REMOTE_ADDR")} - form invalid {form}')
            return self.form_invalid(form)
        
    def form_valid(self, form):
        form.save()
        return super(URLShortenerView, self).form_valid(form)


class URLRedirectView(DetailView):
    model = URLModel

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info(f'{request.META.get("REMOTE_ADDR")} - redirect {obj.original_url}')
        return redirect(obj.original_url)

