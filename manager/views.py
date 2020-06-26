from django.shortcuts import get_list_or_404, render     # Make use of Django shortcuts
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Password            # Import Table from Model


def login(request):
    return render(request, 'manager/login.html')


def login_check(request):
    current_usr_email = request.POST.get('userEmail', False)
    current_pwd = request.POST['pwd']
    print(current_usr_email)
    return HttpResponseRedirect('../main')


def reset_password(request):
    return render(request, 'manager/reset_password.html')


def signup(request):
    return render(request, 'manager/signup.html')


def main(request):
    all_passwords = get_list_or_404(Password.objects.all())
    context = {'all_passwords': all_passwords}
    return render(request, 'manager/main.html', context)


def profile(request):
    return render(request, 'manager/profile.html')


def settings(request):
    return render(request, 'manager/settings.html')


def about(request):
    return render(request, 'manager/about.html')
