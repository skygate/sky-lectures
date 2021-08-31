from rest_framework.routers import DefaultRouter

from presentation.views import PresentationViewSet, TagViewSet

app_name = "presentation"

router = DefaultRouter()
router.register("presentations", PresentationViewSet, basename="presentation")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = []

urlpatterns += router.urls
