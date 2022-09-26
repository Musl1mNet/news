from django.urls import path
from .views import MainIndex

urlpatterns = [
    path("", MainIndex.as_view(), name="index")
]