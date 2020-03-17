import re
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import User


def pass_validator(value):
    pattern = re.compile("(\\d.+)([a-zA-Z].+)|([a-zA-Z].+)(\\d.+)")
    if len(value) < 5 or len(re.findall(pattern, value)) == 0:
        raise ValidationError(f'{value} wrong password')


def log_validator(value):
    if len(value) < 5:
        raise ValidationError(f'{value} wrong username')


class UserFormRegistration(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def is_valid(self):
        valid = super().is_valid()
        check_password = self.data["chk_password"]
        # data = self.cleaned_data  # empty string not include in cleaned_data
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
        if data['password'] != check_password:
            self.add_error('password', error='Password and check password not match!')
            return False
        return valid

    def get_model(self):
        user = User(username=self.data['username'])
        user.set_password(self.data['password'])
        return user
