from django.urls import path
from hotels import views

urlpatterns = [
    path("test/", views.test_route),
    path("test_html/", views.html_view),
    path("home/", views.home, name='home'),
    path("about/", views.about_us, name='about'),
    path("restaurants/", views.get_all_hotels, name="all_rests"),
]