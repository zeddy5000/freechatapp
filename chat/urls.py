from django.urls import path

from . import views


urlpatterns = [
    path("chat/", views.index),
    path("<str:room_name>/", views.room, name="room"),
]