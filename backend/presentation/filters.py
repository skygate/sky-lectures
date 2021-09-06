from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from presentation.models import Presentation, Tag


User = get_user_model()


class PresentationFilter(filters.FilterSet):
    scheduled_on = filters.IsoDateTimeFromToRangeFilter()
    user = filters.ModelChoiceFilter(queryset=User.objects.filter(is_active=True))
    tags = filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())

    class Meta:
        model = Presentation
        fields = ["scheduled_on", "user__username", "tags__name"]
