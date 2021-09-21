import factory

from resources.models import Resource
from presentation.factories import PresentationFactory


class ResourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resource
        django_get_or_create = ("name", "description", "uploaded_on", "fk_pres_id")

    name = factory.Faker("word")
    description = factory.Faker("word")
    fk_pres_id = factory.SubFactory(PresentationFactory)
