from rest_framework.routers import DefaultRouter

from resources.views import ResourceViewSet, PresentationViewSet

app_name = "resources"

router = DefaultRouter()
router.register("resources", ResourceViewSet, basename="resource")
router.register("presentations", PresentationViewSet, basename="presentation")

urlpatterns = router.urls
