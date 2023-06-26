from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ardi", views.index, name="ardi"),
]