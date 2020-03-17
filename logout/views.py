from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def main(request):
    # User.objects.all().delete()     # delete all users
    logout(request)
    return HttpResponseRedirect(reverse('login'))
