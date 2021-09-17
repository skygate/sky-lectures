from datetime import datetime

from django.core import mail
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import reverse
import pytz
from rest_framework import status
from rest_framework.test import APITestCase

from presentation.factories import UserFactory, PresentationFactory, TagFactory, CommentFactory
from presentation.models import Presentation, Tag, Notification, Comment
from presentation.serializers import (
    OutputPresentationSerializer,
    TagSerializer,
)

User = get_user_model()


class TestPresentationViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()
        cls.admin = UserFactory(is_superuser=True)
        cls.tag_react = TagFactory(name="React")
        cls.tag_django = TagFactory(name="Django")
        cls.tag_java = TagFactory(name="Java")
        cls.presentation_1 = PresentationFactory.create(
            scheduled_on=datetime(2021, 10, 1, 12, 0, tzinfo=pytz.UTC),
            user=cls.user_1,
            tags=[cls.tag_java, cls.tag_django, cls.tag_react],
        )
        cls.new_presentation_data = {
            "title": "New presentation",
            "description": "",
            "user": cls.user_1.pk,
            "scheduled_on": datetime(2021, 8, 28, 11, 0, tzinfo=pytz.UTC),
            "tags": [{"name": "React"}],
        }
        cls.updated_presentation_data = {
            "title": "Title updated",
            "description": "",
            "scheduled_on": datetime(2021, 8, 31, 11, 0, tzinfo=pytz.UTC),
            "tags": [{"name": "Updated tag"}],
        }
        cls.list_url = reverse("presentation:presentation-list")
        cls.detail_url = reverse(
            "presentation:presentation-detail", kwargs={"pk": cls.presentation_1.pk}
        )

    def test_get_presentations_list_without_authentication(self):
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_presentations_list_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_detail_without_authentication(self):
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_presentation_detail(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, OutputPresentationSerializer(self.presentation_1).data
        )

    def test_post_new_presentation_without_authentication(self):
        response = self.client.post(
            path=self.list_url, data=self.new_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_new_presentation(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(
            path=self.list_url, data=self.new_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Presentation.objects.count(), 2)

    def test_put_presentation_detail_without_authentication(self):
        response = self.client.put(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_presentation_detail_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.put(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_presentation_detail_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )
        self.presentation_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, OutputPresentationSerializer(self.presentation_1).data
        )

    def test_put_presentation_detail_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )
        self.presentation_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, OutputPresentationSerializer(self.presentation_1).data
        )

    def test_patch_presentation_detail_without_authentication(self):
        response = self.client.patch(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_presentation_detail_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_presentation_detail_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )
        self.presentation_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, OutputPresentationSerializer(self.presentation_1).data
        )

    def test_patch_presentation_detail_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            path=self.detail_url, data=self.updated_presentation_data, format="json"
        )
        self.presentation_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, OutputPresentationSerializer(self.presentation_1).data
        )

    def test_delete_presentation_without_auth(self):
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_presentation_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_presentation_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Presentation.objects.exists())

    def test_delete_presentation_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Presentation.objects.exists())


class TestFiltersPresentationViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()
        cls.tag_react = TagFactory(name="React")
        cls.tag_django = TagFactory(name="Django")
        cls.tag_java = TagFactory(name="Java")
        cls.presentation_1 = PresentationFactory.create(
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 1, 12, 0, tzinfo=pytz.UTC),
            tags=[cls.tag_java, cls.tag_django, cls.tag_react],
        )
        cls.presentation_2 = PresentationFactory.create(
            user=cls.user_2,
            scheduled_on=datetime(2021, 10, 2, 12, 0, tzinfo=pytz.UTC),
            tags=[cls.tag_react],
        )
        cls.presentation_3 = PresentationFactory.create(
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 5, 7, 0, tzinfo=pytz.UTC),
            tags=[cls.tag_java, cls.tag_react],
        )
        cls.list_url = reverse("presentation:presentation-list")

    def test_get_presentation_list_filter_date(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url,
            data={
                "scheduled_on_after": datetime(2021, 10, 4, 7, 0, tzinfo=pytz.UTC),
                "scheduled_on_before": datetime(2021, 10, 6, 7, 0, tzinfo=pytz.UTC),
            },
        )

        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_list_filter_user(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data={"user": self.user_1.pk})

        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_user_username(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"user__username": self.user_1.username}
        )

        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_tag(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"tags": [self.tag_java.id]}
        )

        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_tag_name(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"tags__name": [self.tag_java.name]}
        )

        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_few_tags(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"tags": [self.tag_java.id, self.tag_react.id]}
        )

        self.assertEqual(response.data["count"], 3)

    def test_get_presentation_list_filter_date_user_tag(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url,
            data={
                "scheduled_on_after": datetime(2021, 10, 4, 7, 0, tzinfo=pytz.UTC),
                "scheduled_on_before": datetime(2021, 10, 6, 7, 0, tzinfo=pytz.UTC),
                "user": self.user_1.id,
                "tags": [self.tag_java.id],
            },
        )

        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_list_search_title(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"search": self.presentation_1.title}
        )

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(
            response.data["results"][0],
            OutputPresentationSerializer(self.presentation_1).data,
        )

    def test_get_presentation_list_search_description(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"search": self.presentation_1.description}
        )

        self.assertEqual(response.data["count"], 1)
        self.assertEqual(
            response.data["results"][0],
            OutputPresentationSerializer(self.presentation_1).data,
        )

    def test_get_presentation_list_search_username(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url, data={"search": self.user_1.username}
        )

        self.assertEqual(response.data["count"], 2)
        self.assertEqual(
            response.data["results"][1],
            OutputPresentationSerializer(self.presentation_1).data,
        )
        self.assertEqual(
            response.data["results"][0],
            OutputPresentationSerializer(self.presentation_3).data,
        )

    def test_get_presentation_list_search_tag(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data={"search": "Java"})

        self.assertEqual(response.data["count"], 2)
        self.assertEqual(
            response.data["results"][1],
            OutputPresentationSerializer(self.presentation_1).data,
        )
        self.assertEqual(
            response.data["results"][0],
            OutputPresentationSerializer(self.presentation_3).data,
        )


class TestOrderingPresentationViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory(username="Albert")
        cls.user_2 = UserFactory(username="Walter")
        cls.presentation_1 = PresentationFactory.create(
            title="A first presentation",
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 1, 12, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_2 = PresentationFactory.create(
            title="B second presentation",
            user=cls.user_2,
            scheduled_on=datetime(2021, 10, 2, 12, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_3 = PresentationFactory.create(
            title="C third presentation",
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 5, 7, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_1_dict = {
            "title": "A first presentation",
        }
        cls.presentation_2_dict = {
            "title": "B second presentation",
        }
        cls.presentation_3_dict = {
            "title": "C third presentation",
        }
        cls.list_url = reverse("presentation:presentation-list")

    def setUp(self) -> None:
        self.client.force_authenticate(user=self.user_1)

    def test_get_presentation_list_ordering_date(self):
        response = self.client.get(
            path=self.list_url, data={"ordering": "scheduled_on"}
        )
        print(response.data["results"][0])
        print(self.presentation_1_dict)

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_1_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_2_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_3_dict["title"],
        )

    def test_get_presentation_list_ordering_neg_date(self):
        response = self.client.get(
            path=self.list_url, data={"ordering": "-scheduled_on"}
        )

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_3_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_2_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_1_dict["title"],
        )

    def test_get_presentation_list_ordering_title(self):
        response = self.client.get(path=self.list_url, data={"ordering": "title"})

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_1_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_2_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_3_dict["title"],
        )

    def test_get_presentation_list_ordering_neg_title(self):
        response = self.client.get(path=self.list_url, data={"ordering": "-title"})

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_3_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_2_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_1_dict["title"],
        )

    def test_get_presentation_list_ordering_username(self):
        response = self.client.get(
            path=self.list_url, data={"ordering": "user__username"}
        )

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_1_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_3_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_2_dict["title"],
        )

    def test_get_presentation_list_ordering_neg_username(self):
        response = self.client.get(
            path=self.list_url, data={"ordering": "-user__username"}
        )

        self.assertEqual(response.data["count"], Presentation.objects.all().count())
        self.assertEqual(
            response.data["results"][0]["title"],
            self.presentation_2_dict["title"],
        )
        self.assertEqual(
            response.data["results"][1]["title"],
            self.presentation_1_dict["title"],
        )
        self.assertEqual(
            response.data["results"][2]["title"],
            self.presentation_3_dict["title"],
        )


class TestTagViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = UserFactory(
            is_superuser=True,
        )
        cls.user_1 = UserFactory()
        cls.tag_1 = TagFactory(name="Test_tag_1")
        cls.tag_2 = TagFactory(name="Test_tag_2")
        cls.new_tag = {"name": "Test_tag_3"}
        cls.updated_tag = {"name": "Test_updated_tag"}
        cls.list_url = reverse("presentation:tag-list")
        cls.detail_url = reverse("presentation:tag-detail", kwargs={"pk": cls.tag_1.pk})

    def test_get_tag_list_without_auth(self):
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tag_list(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_get_tag_detail_without_auth(self):
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tag_detail(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TagSerializer(self.tag_1).data)

    def test_post_new_tag_without_auth(self):
        response = self.client.post(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_new_tag(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(path=self.list_url, data=self.new_tag)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 3)

    def test_put_tag_without_auth(self):
        response = self.client.put(path=self.detail_url, data=self.updated_tag)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_tag_as_user(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(path=self.detail_url, data=self.updated_tag)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_tag_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(path=self.detail_url, data=self.updated_tag)
        self.tag_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TagSerializer(self.tag_1).data)

    def test_patch_tag_without_auth(self):
        response = self.client.patch(path=self.detail_url, data=self.updated_tag)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_tag_as_user(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(path=self.detail_url, data=self.updated_tag)
        self.tag_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_tag_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(path=self.detail_url, data=self.updated_tag)
        self.tag_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TagSerializer(self.tag_1).data)

    def test_delete_tag_without_auth(self):
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tag_as_user(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_tag_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 1)


class TestNotifcationModel(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = TagFactory(name="Django")
        cls.user_1 = UserFactory.create(username="user_1", favourite_tags=[cls.tag])
        cls.user_2 = UserFactory.create(username="user_2", favourite_tags=[cls.tag])
        cls.admin = UserFactory(is_superuser=True)
        cls.presentation_1 = PresentationFactory.create(
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 1, 12, 0, tzinfo=pytz.UTC),
        )
        cls.new_presentation_data = {
            "title": "New presentation",
            "description": "",
            "user": cls.admin.pk,
            "scheduled_on": datetime(2021, 8, 28, 11, 0, tzinfo=pytz.UTC),
            "tags": [{"name": "Django"}],
        }
        cls.comment = CommentFactory(
            presentation_id=cls.presentation_1,
            user=cls.user_1,
        )
        cls.new_comment = {
            "text": "reply to first comment",
            "presentation_id": cls.presentation_1.id,
            "user": cls.user_2.id,
            "reply_to": cls.comment.id,
        }

        cls.mail_body = "replies to your comment! Check this out!"
        cls.list_url = reverse("presentation:presentation-list")
        cls.comment_url = reverse("presentation:comment-list")

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_create_presentation_with_favourite_tag_and_get_notification(self):
        self.client.force_authenticate(self.admin)
        response = self.client.post(
            path=self.list_url, data=self.new_presentation_data, format="json"
        )
        correct_mail = {email.to[0] for email in mail.outbox}

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Presentation.objects.count(), 2)
        self.assertEqual(Notification.objects.count(), 2)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(
            correct_mail,
            set(
                Notification.objects.all().values_list(
                    "user__email", flat=True
                )
            ),
        )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def test_add_reply_to_comment_and_get_notification(self):
        self.client.force_authenticate(self.user_2)
        response = self.client.post(path=self.comment_url, data=self.new_comment)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            set(mail.outbox[0].to),
            set(
                Notification.objects.all().values_list(
                    "user__email", flat=True
                )
            ),
        )


class TestCommentViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()
        cls.admin = UserFactory(is_superuser=True)
        cls.presentation = PresentationFactory()
        cls.comment_1 = CommentFactory(user=cls.user_1)
        cls.comment_2 = CommentFactory(user=cls.user_1)

        cls.valid_comment = {
            "text": "some comment",
            "presentation_id": cls.presentation.id,
            "user": cls.user_1,
            "reply_to": cls.comment_1.id,
        }

        cls.valid_update_comment = {"text": "some new comment"}

        cls.list_url = reverse("presentation:comment-list")
        cls.detail_url = reverse(
            "presentation:comment-detail", kwargs={"pk": cls.comment_1.pk}
        )

    def test_get_comments_list_not_authenticated(self):
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_comments_list_authenticated(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 2)

    def test_post_comment_not_authenticated(self):
        response = self.client.post(path=self.list_url, data=self.valid_comment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_comment_authenticated(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(path=self.list_url, data=self.valid_comment)

        self.comment_1.refresh_from_db()

        self.assertEqual(Comment.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_not_authenticated(self):
        response = self.client.put(path=self.list_url, data=self.valid_comment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authenticated(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(path=self.detail_url, data=self.valid_update_comment)

        self.comment_1.refresh_from_db()

        self.assertEqual(self.comment_1.text, self.valid_update_comment["text"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_not_authenticated(self):
        response = self.client.patch(path=self.list_url, data=self.valid_comment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_authenticated(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(
            path=self.detail_url, data=self.valid_update_comment
        )

        self.comment_1.refresh_from_db()

        self.assertEqual(self.comment_1.text, self.valid_update_comment["text"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
