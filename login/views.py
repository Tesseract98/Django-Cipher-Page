from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserFormLogin


# Create your views here.

def main(request):
    if request.method == "GET":
        return render(request, "login/authorization.html", {'link': 'login/'})
    elif request.method == "POST":
        user_form = UserFormLogin(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            # login(request, user_form.get_user())  # login with form created model User
            return redirect(reverse('cipher'))
        else:
            return render(request, "login/authorization.html", {'link': 'login/', 'form': user_form})
    return HttpResponse(status=405)
