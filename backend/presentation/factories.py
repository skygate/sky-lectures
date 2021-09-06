from django.contrib.auth import get_user_model
import factory

from presentation.models import Comment, Presentation


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username", "password", "email", "is_superuser")

    username = factory.Faker("name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    is_superuser = False


class PresentationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Presentation


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
        django_get_or_create = ("text",)

    text = factory.Faker("text")
    user = factory.SubFactory(UserFactory)
    presentation_id = factory.SubFactory(PresentationFactory)
