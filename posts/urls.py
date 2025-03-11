from django.urls import path

from . import views

urlpatterns = [
    # EX: http://pollqapp.com/posts
    path("", views.index, name="index"),
    # path("cats/", views.cats, name="cats"),
    # path("dogs/", views.dogs, name="dogs"),
]