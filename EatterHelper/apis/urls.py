from django.urls import path
from .views import yelpapi

urlpatterns = [
    path(r'', yelpapi.IndexView.as_view(), name="yelpapi")
]