from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = 'notes:list'
    redirect_authenticated_user = True
    next_page = 'notes:list'

    extra_context = {
        'title': 'Вход'
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_success')
    form_class = UserRegisterForm

    extra_context = {
        'title': 'Регистрация'
    }


class UserSuccessRegisterView(TemplateView):
    template_name = 'users/register_success.html'

    extra_context = {
        'title': 'Успешная регистрация'
    }
