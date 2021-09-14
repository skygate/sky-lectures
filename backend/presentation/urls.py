from rest_framework.routers import DefaultRouter

from presentation.views import CommentViewSet, PresentationViewSet, TagViewSet

app_name = "presentation"

router = DefaultRouter(trailing_slash=False)

router.register("comments", CommentViewSet, basename="comment")
router.register("presentations", PresentationViewSet, basename="presentation")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = router.urls
