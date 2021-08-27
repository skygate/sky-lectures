from django.urls import path
from users.views import UserRegisterView


app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
]
