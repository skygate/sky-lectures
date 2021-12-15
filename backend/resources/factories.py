import factory

from resources.models import Resource
from presentation.factories import PresentationFactory


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource
        django_get_or_create = ("name", "description", "uploaded_on", "presentation")

    name = factory.Faker("word")
    description = factory.Faker("word")
    presentation = factory.SubFactory(PresentationFactory)
