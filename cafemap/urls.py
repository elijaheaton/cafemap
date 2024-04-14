from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cafe/<str:id>/", views.cafe, name="cafe"),
]
