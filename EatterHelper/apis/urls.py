from django.urls import path
from .views import yelpapi

urlpatterns = [
    path(r'index', yelpapi.IndexView.as_view(), name="yelpapi")
]