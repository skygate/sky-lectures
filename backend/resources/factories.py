import factory

from resources.models import Resource, Presentation


class PresentationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource
