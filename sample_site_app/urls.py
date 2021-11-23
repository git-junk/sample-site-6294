from django.urls import path
from . import views

app_name = "sample_site_app"

urlpatterns = [
  path("index/", views.index, name="index"),
]
