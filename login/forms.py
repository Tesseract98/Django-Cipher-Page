import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from register.models import User


def pass_validator(value):
    pattern = re.compile("(\\d.+)([a-zA-Z].+)|([a-zA-Z].+)(\\d.+)")
    if len(value) < 5 or len(re.findall(pattern, value)) == 0:
        raise ValidationError(f'{value} wrong password')


def log_validator(value):
    if len(value) < 5:
        raise ValidationError(f'{value} wrong username')


class UserFormLogin(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    user = None

    def is_valid(self):
        valid = super().is_valid()
        data = self.data
        try:
            log_validator(data['username'])
        except ValidationError as err:
            self.add_error("username", error=err.message)
            return False
        try:
            pass_validator(data['password'])
        except ValidationError as err:
            self.add_error("password", error=err.message)
            return False
        self.user = User.objects.filter(username=data['username']).first()
        if self.user is None:
            self.add_error("password", error="wrong username or password")
            return False
        return valid and check_password(data['password'], self.user.password)

    def get_user(self):
        return self.user
