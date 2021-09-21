from rest_framework.routers import DefaultRouter

from resources.views import ResourceViewSet

app_name = "resources"

router = DefaultRouter()
router.register("resources", ResourceViewSet, basename="resource")

urlpatterns = router.urls
