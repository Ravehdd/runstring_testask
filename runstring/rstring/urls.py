from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("api/v1/text/", RunStringAPIVew.as_view(), name="runstring"),
    path("api/v1/video/", RunStringDBAPIVew.as_view(), name="video"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)