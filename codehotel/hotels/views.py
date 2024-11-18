from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_route(request):
    return HttpResponse("Hello Prem!!")


def html_view(request):
    return HttpResponse("<h2>Hello from html_view</h2>")

def home(request):
    return render(request, "hotels/home.html")


def about_us(request):
    return render(request, "hotels/about.html")


def get_all_hotels(request):
    context = {
        "username": "radhe",
        "user": {
            "first_name": "praul",
            "last_name": "ayar"
        },
        'hotels': [
            {
                'name': 'Taj',
                'address': 'Mumbai, India'
            },
            {
                'name': 'Sapphire',
                'address': 'Banglore, India'
            },
            {
                'name': 'Heritage',
                'address': 'Ahmedabad, India'
            },
            {
                'name': 'Lotus',
                'address': 'Delhi, India'
            }
        ]
    }
    return render(request, 'hotels/all_hotels.html', context=context)