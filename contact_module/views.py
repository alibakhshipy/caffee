from django.shortcuts import render
from django.views.generic import CreateView

from contact_module.forms import ContactUsModelForm
from contact_module.models import ContactUs
from django.urls import reverse_lazy

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact.html'
    success_url = reverse_lazy('contact_modules')