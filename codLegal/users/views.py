from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import  authenticate, login
from users import forms

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return HttpResponse('Login Successful')
        return HttpResponse('Invalid email or password')
    return render(request, "users/login.html")

def login_django_form(request):
    if request.method == 'POST':
        form = forms.UserAuthenticate(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return HttpResponse('Login successful')
        context = {
            "form": form
        }
        return render(request, "users/login_django_forms.html", context=context)
    context = {
        "form": forms.UserAuthenticate()
    }
    return render(request, "users/login_django_forms.html", context=context)
