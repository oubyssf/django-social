import requests
from django import forms
from django.utils.text import slugify
from django.core.files.base import ContentFile
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        formats = 'jpg', 'png', 'jpeg'
        url = self.cleaned_data['url']
        ext = url.rsplit('.', 1)[-1].lower()
        if ext not in formats:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url
    
    def save(self, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        extension = image_url.rsplit('.', 1)[-1].lower()
        name = slugify(self.cleaned_data['title'])
        image_name = f'{name}.{extension}'
        
        response = requests.get(image_url)
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        
        if commit:
            image.save()
        
        return image
