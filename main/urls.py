from django.urls import path
from .views import MainIndex, PostCreate

app_name = 'main'
urlpatterns = [
    path("", MainIndex.as_view(), name="index"),
    path("create/", PostCreate.as_view(), name= "create")
]