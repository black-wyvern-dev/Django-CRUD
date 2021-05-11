from django.views.generic import TemplateView, View, FormView
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages

# from .models import ContentPost
from .forms import (
    AddContentForm
)
from .models import (
    Content
)

class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class AddContentView(FormView):
    template_name = 'content/add_content.html'
    
    @staticmethod
    def get_form_class(**kwargs):
        # if settings.DISABLE_USERNAME or settings.LOGIN_VIA_EMAIL:
        #     return SignInViaEmailForm

        # if settings.LOGIN_VIA_EMAIL_OR_USERNAME:
        #     return SignInViaEmailOrUsernameForm

        return AddContentForm

    def form_valid(self, form):
        request = self.request
        content = Content()
        content.title = form.cleaned_data['title']
        content.email = form.cleaned_data['email']
        content.phone = form.cleaned_data['phone']
        content.category = form.cleaned_data['category']
        content.location = form.cleaned_data['location']
        content.content = form.cleaned_data['content']
        content.save()

        messages.success(self.request, ('Content data has been successfully updated.'))

        return redirect('add_content')