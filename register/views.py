from django.shortcuts import render, redirect
from . import forms
from django.db import transaction
from django.urls import reverse
from django.contrib.auth import login


def register(request):
    if not request.user.is_active:
        if request.method == "GET":
            return render(request, "register/registration.html")
        elif request.method == "POST":
            user_form = forms.UserFormRegistration(request.POST)
            if user_form.is_valid():
                user_model = user_form.get_model()
                print(user_model.save())
                login(request, user_model)
                return redirect(reverse('cipher'))
            else:
                return render(request, "register/registration.html", {'form': user_form})
    return redirect(reverse('cipher'))
