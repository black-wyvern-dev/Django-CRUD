from datetime import timedelta

from django import forms
from django.forms import ValidationError, ModelForm
from django.conf import settings

from .models import Content

class AddContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'email', 'phone', 'category'
            , 'location', 'content']
