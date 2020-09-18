from django.urls import path
from . import views, api

urlpatterns = [
    path("api/v1/create", api.CreateGR.as_view()),
    path("api/v1/all", api.ListGR.as_view()),
]
