from django.shortcuts import render
from django.views.generic import CreateView

from contact_module.forms import ContactUsModelForm
from contact_module.models import ContactUs


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact.html'
    success_url = '/contact/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        contact : ContactUs = ContactUs.objects.first()
        context['contact'] = contact
