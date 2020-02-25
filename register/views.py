from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms, models
from django.db import transaction
from django.urls import reverse
from cipher.views import main


# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, "register/registration.html")
    elif request.method == "POST":
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print(user)
            return redirect(reverse('main'))
        else:
            return render(request, "register/registration.html", {'form': user_form})
    return HttpResponse(status=405)
