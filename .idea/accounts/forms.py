from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['ID', 'Nume', 'Prenume', 'Email', 'Password', 'PhoneNumber', 'Username']
        fields = ['username', 'email', 'password1', 'password2']
