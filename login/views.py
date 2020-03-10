from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserFormLogin
from register.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login


# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request, "login/authorization.html", {'link': 'login/'})
    elif request.method == "POST":
        user_form = UserFormLogin(request.POST)
        if user_form.is_valid():
            # login(request, user_form.get_user())
            return redirect(reverse('main'))
        else:
            return render(request, "login/authorization.html", {'link': 'login/', 'form': user_form})
    return HttpResponse(status=405)
