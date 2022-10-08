from django.urls import path
from .views import UserRegestration, user_login, user_logout, user_info, user_info_post

app_name = "user"
urlpatterns = [
    path('regestration/', UserRegestration.as_view(), name = 'regestration'),
    path('login/', user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    path("info/", user_info, name="info"),
    path("info/save/", user_info_post, name="info_save")
]