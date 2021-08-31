from rest_framework.routers import DefaultRouter

from users.views import ProfileViewSet


router = DefaultRouter(trailing_slash=False)

router.register("profiles", ProfileViewSet, basename="profile")

urlpatterns = router.urls
