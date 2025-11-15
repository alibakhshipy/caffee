from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from contact_module.models import ContactUs

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'نام خود را وارد کنید',
                'placeholder': 'نام و نام خانوادگی خود را وارد کنید'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'ایمیل خود را وارد کنید',
                'placeholder': 'ایمیل خود را وارد کنید'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'موضوع پیام شما ', 
                'placeholder': 'موضوع پیام خود را وارد کنید'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'متن پیام ...',
                'rows': 5,
                'placeholder': 'متن پیام خود را بنویسید...'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'title': 'موضوع پیام', 
            'message': 'پیام'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد'
            },
            'email': {
                'required': 'ایمیل اجباری می باشد'
            },
            'title': {
                'required': 'موضوع پیام اجباری می باشد'
            },
            'message': {
                'required': 'متن پیام اجباری می باشد'
            }
        }