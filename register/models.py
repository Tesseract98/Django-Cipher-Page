from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.contrib.auth.models import (
    User as DjangoUser, UserManager
)


class User(DjangoUser):
    created_on = models.DateField(default=datetime.utcnow)

    def __str__(self):
        return f'{self.username} {self.password}'


# another way to create User model
def foo():
    class UserModel(models.Model):
        id = models.AutoField(primary_key=True)
        username = models.CharField(max_length=20, unique=True)
        password = models.CharField(max_length=20)
        email = models.EmailField(blank=True)
        created_on = models.DateField(default=datetime.utcnow)
        USERNAME_FIELD = 'username'
        object = UserManager()

        def set_password(self, password):
            self.password = make_password(password)

        def __str__(self):
            return f'{self.username} {self.password}'
