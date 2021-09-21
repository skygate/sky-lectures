from rest_framework.routers import DefaultRouter

from survey.views import ChoiceViewSet, QuestionViewSet

router = DefaultRouter()

router.register("choices", ChoiceViewSet, basename="choice")
router.register("questions", QuestionViewSet, basename="question")

urlpatterns = router.urls
