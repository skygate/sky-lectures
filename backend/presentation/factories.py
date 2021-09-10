from django.contrib.auth import get_user_model
import factory

from presentation.models import Presentation, Tag


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username", "password", "email", "is_superuser")

    username = factory.Faker("first_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    is_superuser = False

    @factory.post_generation
    def favourite_tags(self, create, tags):
        if not create:
            return
        if tags:
            for tag in tags:
                self.favourite_tags.add(tag)

    @factory.post_generation
    def favourite_presentation(self, create, presentations):
        if not create:
            return
        if presentations:
            for presentation in presentations:
                self.favourite_presentation.add(presentation)


class PresentationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Presentation
        django_get_or_create = ("title", "description", "user", "scheduled_on")

    title = factory.Faker("word")
    description = factory.Faker("text")
    user = factory.SubFactory(UserFactory)
    scheduled_on = factory.Faker("date")

    @factory.post_generation
    def tags(self, create, tags):
        if not create:
            return
        if tags:
            for tag in tags:
                self.tags.add(tag)


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ("name",)

    name = factory.Faker("word")
