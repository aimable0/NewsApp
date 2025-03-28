from django.urls import path

from . import views

app_name = "momo"
urlpatterns = [
    path("", views.index, name="index"),
    path("airtime", views.airtime, name="airtime")
]
