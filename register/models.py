from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import datetime


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    created_on = models.DateField(default=datetime.utcnow)

    def set_password(self, password):
        self.password = make_password(password)

    def __str__(self):
        return f'{self.login} {self.password}'
