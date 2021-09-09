from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import ProfileViewSet, UserRegisterView, UserViewSet


app_name = "users"

router = DefaultRouter()
router.register("profiles", ProfileViewSet, basename="profile")
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
]

urlpatterns += router.urls
