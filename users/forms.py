from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and len(email) > 0:
            if User.objects.filter(email=email).exists():
                raise ValidationError('Пользователь с таким email уже существует')
        return email
