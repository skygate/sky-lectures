from rest_framework.routers import DefaultRouter

from presentation.views import CommentViewSet


app_name = "presentation"

router = DefaultRouter(trailing_slash=False)

router.register("comments", CommentViewSet, basename="comment")

urlpatterns = router.urls
