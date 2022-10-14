from django.urls import path
from users.views import UserLoginView, UserLogoutView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('', UserLogoutView.as_view(), name='logout'),
]
