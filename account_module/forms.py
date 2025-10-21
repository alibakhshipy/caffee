from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class RegisterForm(forms.Form):
    name = forms.CharField(
        label='نام',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'نام خود را وارد کنید'}),

    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'ایمیل خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator(),
        ]
    )

    number = forms.IntegerField(
        label='شماره تلفن',
        widget=forms.NumberInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50','placeholder': '09---'}),

    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50','placeholder': 'رمز عبور خود را وارد کنید'}),

    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50','placeholder': 'رمز عبور خود را مجددا وارد کنید'}),
    )


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

class LoginForm(forms.Form):

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'ایمیل خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator(),
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'رمز عبور خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

class ForgetForm(forms.Form):

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50', 'placeholder': 'ایمیل خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator(),
        ]
    )

class ResetForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(
            attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50',
                   'placeholder': 'رمز عبور خود را وارد کنید'}),

    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(
            attrs={'class': 'w-full h-8 px-3 text-sm sm:text-[17px] outline-none rounded-full bg-white/50',
                   'placeholder': 'رمز عبور خود را مجددا وارد کنید'}),
    )