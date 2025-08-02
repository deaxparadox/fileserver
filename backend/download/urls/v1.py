from django.urls import path

from download.views.v1 import download

app_name = "download_v1"

urlpatterns = [
    path("", download.home, name="home")
]
