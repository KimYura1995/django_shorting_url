from django import forms

from app_shortener_url.models import URLModel


class URLShortenerForm(forms.ModelForm):
    extra_slug = forms.SlugField(
        label='Кастомная ссылка',
        max_length=100,
        help_text='Для автоматической генерации ссылки оставьте поле пустым',
        required=False,
    )

    class Meta:
        model = URLModel
        fields = ['original_url', 'extra_slug']

    def clean_extra_slug(self):
        slug = self.cleaned_data["extra_slug"]
        if self.instance.slug == slug:
            return slug
        try:
            URLModel._default_manager.get(slug=slug)
        except URLModel.DoesNotExist:
            return slug
        raise forms.ValidationError(
            message='Введенная кастомная ссылка занята',
        )

