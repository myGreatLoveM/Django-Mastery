from django.shortcuts import render
from appointments import models

def home(request):
    context = {
        'practice_areas': models.PracticeArea.objects.all()
    }
    return render(request, "appointments/home.html", context=context)


def about(request):
    return render(request, "appointments/about.html")