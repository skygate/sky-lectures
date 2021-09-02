from datetime import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
import pytz
from rest_framework import status
from rest_framework.test import APITestCase

from presentation.models import Presentation, Tag
from presentation.serializers import (
    OutputPresentationSerializer,
    TagSerializer,
)


User = get_user_model()


class TestPresentationViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username="admin",
            password="password123",
            email="admin@mail.com",
            first_name="admin",
            last_name="admin",
            is_superuser=True,
        )
        cls.user_1 = User.objects.create_user(
            username="user_1",
            password="password123",
            email="user_1@mail.com",
            first_name="user",
            last_name="test_1",
        )
        cls.user_2 = User.objects.create_user(
            username="user_2",
            password="password123",
            email="user_2@mail.com",
            first_name="user",
            last_name="test_2",
        )
        cls.tag_1 = Tag.objects.create(name="Test_tag")
        cls.presentation_1 = Presentation.objects.create(
            title="Test title 1",
            description="",
            user=cls.user_1,
            scheduled_on=datetime(2021, 8, 30, 11, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_1.tags.add(cls.tag_1)
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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_presentations_list_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_detail_without_authentication(self):
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_presentation_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_presentation_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Presentation.objects.count(), 0)

    def test_delete_presentation_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Presentation.objects.count(), 0)


class TestFiltersPresentationViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = User.objects.create_user(
            username="user_1",
            password="password123",
            email="user_1@mail.com",
            first_name="user",
            last_name="test_1",
        )
        cls.user_2 = User.objects.create_user(
            username="user_2",
            password="password123",
            email="user_2mail.com",
            first_name="user",
            last_name="test_2",
        )
        cls.tag_react = Tag.objects.create(name="React")
        cls.tag_django = Tag.objects.create(name="Django")
        cls.tag_java = Tag.objects.create(name="Java")
        cls.presentation_1 = Presentation.objects.create(
            title="Test title 1",
            description="",
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 1, 12, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_1.tags.add(cls.tag_java, cls.tag_react, cls.tag_django)
        cls.presentation_2 = Presentation.objects.create(
            title="Test title 2",
            description="",
            user=cls.user_2,
            scheduled_on=datetime(2021, 10, 2, 12, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_2.tags.add(cls.tag_react)
        cls.presentation_3 = Presentation.objects.create(
            title="Test title 3",
            description="",
            user=cls.user_1,
            scheduled_on=datetime(2021, 10, 5, 7, 0, tzinfo=pytz.UTC),
        )
        cls.presentation_3.tags.add(cls.tag_react, cls.tag_java)
        cls.filters_data_1 = {
            "scheduled_on_after": datetime(2021, 10, 4, 7, 0, tzinfo=pytz.UTC),
            "scheduled_on_before": datetime(2021, 10, 6, 7, 0, tzinfo=pytz.UTC),
            "user": "",
            "tags": [],
        }
        cls.filters_data_2 = {
            "scheduled_on_after": "",
            "scheduled_on_before": "",
            "user": cls.user_1.id,
            "tags": [],
        }
        cls.filters_data_3 = {
            "scheduled_on_after": "",
            "scheduled_on_before": "",
            "user": "",
            "tags": [cls.tag_java.id],
        }
        cls.filters_data_4 = {
            "scheduled_on_after": "",
            "scheduled_on_before": "",
            "user": "",
            "tags": [cls.tag_react.id],
        }
        cls.filters_data_5 = {
            "scheduled_on_after": "",
            "scheduled_on_before": "",
            "user": "",
            "tags": [cls.tag_django.id],
        }
        cls.filters_data_6 = {
            "scheduled_on_after": "",
            "scheduled_on_before": "",
            "user": "",
            "tags": [cls.tag_java.id, cls.tag_django.id],
        }
        cls.filters_data_7 = {
            "scheduled_on_after": datetime(2021, 10, 1, 7, 0, tzinfo=pytz.UTC),
            "scheduled_on_before": datetime(2021, 10, 3, 7, 0, tzinfo=pytz.UTC),
            "user": "",
            "tags": [cls.tag_java.id],
        }
        cls.filters_data_8 = {
            "scheduled_on_after": datetime(2021, 10, 4, 7, 0, tzinfo=pytz.UTC),
            "scheduled_on_before": datetime(2021, 10, 6, 7, 0, tzinfo=pytz.UTC),
            "user": cls.user_1.id,
            "tags": [cls.tag_java.id],
        }
        cls.list_url = reverse("presentation:presentation-list")

    def test_get_presentation_list_filter_case_1(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_1)
        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_list_filter_case_2(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_2)
        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_case_3(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_3)
        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_case_4(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_4)
        self.assertEqual(response.data["count"], 3)

    def test_get_presentation_list_filter_case_5(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_5)
        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_list_filter_case_6(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_6)
        self.assertEqual(response.data["count"], 2)

    def test_get_presentation_list_filter_case_7(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_7)
        self.assertEqual(response.data["count"], 1)

    def test_get_presentation_list_filter_case_8(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url, data=self.filters_data_8)
        self.assertEqual(response.data["count"], 1)


class TestTagViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username="admin",
            password="password123",
            email="admin@mail.com",
            first_name="admin",
            last_name="admin",
            is_superuser=True,
        )
        cls.user_1 = User.objects.create_user(
            username="user_1",
            password="password123",
            email="user_1@mail.com",
            first_name="user",
            last_name="test_1",
        )
        cls.tag_1 = Tag.objects.create(name="Test_tag_1")
        cls.tag_2 = Tag.objects.create(name="Test_tag_2")
        cls.new_tag = {"name": "Test_tag_3"}
        cls.updated_tag = {"name": "Test_updated_tag"}
        cls.list_url = reverse("presentation:tag-list")
        cls.detail_url = reverse("presentation:tag-detail", kwargs={"pk": cls.tag_1.pk})

    def test_get_tag_list_without_auth(self):
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_tag_list(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_get_tag_detail_without_auth(self):
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_tag_detail(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TagSerializer(self.tag_1).data)

    def test_post_new_tag_without_auth(self):
        response = self.client.post(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_new_tag(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(path=self.list_url, data=self.new_tag)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 3)

    def test_put_tag_without_auth(self):
        response = self.client.put(path=self.detail_url, data=self.updated_tag)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_tag_as_user(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_tag_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(path=self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 1)
