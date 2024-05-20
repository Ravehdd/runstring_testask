from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("api/v1/text/", RunStringAPIVew.as_view(), name="runstring")
]