from rest_framework.viewsets import ModelViewSet

from survey.models import Choice, Question
from survey.serializers import ChoiceSerializer, QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
