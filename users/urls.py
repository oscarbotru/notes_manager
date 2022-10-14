from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserRegisterView, UserSuccessRegisterView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/success/', UserSuccessRegisterView.as_view(), name='register_success'),
]
