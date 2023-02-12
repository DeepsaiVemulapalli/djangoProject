from django.urls import path

from.views import msg_json

urlpatterns = [
    path("", msg_json, name="home"),
]