from django.contrib.auth.models import User
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import View
from account_module.forms import RegisterForm, LoginForm, ForgetForm, ResetForm
from django.views import View
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# from django.contrib.auth.models import User
from account_module.models import User
from django.contrib.auth import authenticate, login, logout
from utils.email_service import send_email, send_mail

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'login/home_login.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get('email')
            user_password = form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error('email', 'ایمیل تکراری میباشد×')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code1=get_random_string(48),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('login_page'))
        context = {
            'form': form
        }

        return render(request, 'login/home_login.html', context)

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'login/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')

            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'login/login_page.html', context)

class ActiveCodeView(View):
    def get(self, request, email_active_code1):
        user = User.objects.filter(email_active_code1__iexact=email_active_code1).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass

        raise Http404

class ForgetView(View):
    def get(self, request: HttpRequest):
        forget_form = ForgetForm()
        return render(request, 'login/forgot_password.html', {
            'forget_form': forget_form
        })

    def post(self, request: HttpRequest):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            user_email = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # send email for frorget
                pass
        return render(request, 'login/forgot_password.html', {
            'forget_form': forget_form
        })

class Reset_passView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code1__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_form = ResetForm()
        return render(request, 'login/reset_password.html', {
            'reset_form': reset_form,
            'user': user
        })

    def post(self, request: HttpRequest, active_code):
        reset_form = ResetForm(request.POST)
        user: User = User.objects.filter(email_active_code1__iexact=active_code).first()
        if reset_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_pass = reset_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code1 = get_random_string(48)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        return render(request, 'login/login_page.html', {
            'reset_form': reset_form,
            'user': user
        })

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))