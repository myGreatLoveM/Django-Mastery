from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_route(request):
    return HttpResponse("Hello Prem!!")