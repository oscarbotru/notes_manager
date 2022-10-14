from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


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


# class UserRegisterView(SuccessMessageMixin, CreateView):
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:register_success')
#     form_class = UserRegisterForm
#     success_message = "Пользователь успешно зарегистрирован. Дождитесь пароль."
#
#     extra_context = {
#         'title': 'Регистрация'
#     }
#
#     def form_valid(self, form):
#         self.object = form.save()
#         send_code_to_email_or_phone(self.object)
#         response = redirect(self.get_success_url())
#         response.set_cookie('current_user_pk', self.object.pk)
#         return response
#
