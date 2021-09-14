from io import BytesIO

from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from presentation.factories import PresentationFactory, TagFactory, UserFactory


User = get_user_model()


class RegisterUserTest(APITestCase):
    """Test module for register a new user"""

    @classmethod
    def setUpTestData(cls):
        cls.register_url = reverse("users:user-register")
        cls.valid_payload = {
            "username": "test_user",
            "password": "test_password",
            "password2": "test_password",
            "email": "test@mail.com",
            "first_name": "test",
            "last_name": "user",
        }
        cls.invalid_payload = {
            "username": "test_user2",
            "password": "test_password2",
            "password2": "test_password3",
            "email": "testmail.com",
            "first_name": "test",
            "last_name": "",
        }

    def test_register_valid_user(self):
        response = self.client.post(
            path=self.register_url,
            data=self.valid_payload,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_register_invalid_user(self):
        response = self.client.post(
            path=self.register_url,
            data=self.invalid_payload,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class TestUserViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = UserFactory(username="admin", is_superuser=True)
        cls.user_1 = UserFactory(username="user_1")
        cls.user_2 = UserFactory(username="user_2")
        cls.presentation_1 = PresentationFactory(user=cls.user_1)
        cls.list_url = reverse("users:user-list")
        cls.detail_url = reverse("users:user-detail", kwargs={"pk": cls.user_1.pk})
        cls.user_1_updated_data = {
            "username": "user_1_updated",
            "email": "user1@updated.com",
            "first_name": "user_updated",
            "last_name": "test_1_updated",
            "favourite_presentations": [],
            "favourite_tags": [],
        }

    def test_get_users_list_without_authentication(self):
        response = self.client.get(
            path=self.list_url,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_list_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.list_url,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)

    def test_get_user_detail_without_authentication(self):
        response = self.client.get(
            path=self.detail_url,
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_detail_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(
            path=self.detail_url,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_user_detail_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            path=self.detail_url,
            data={"username": "user_1_updated"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user_1_updated")

    def test_patch_user_detail_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(
            path=self.detail_url,
            data={"username": "user_1_updated"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user_1_updated")

    def test_patch_user_detail_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(
            path=self.detail_url,
            data={"username": "user_1_updated"},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_user_detail_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(
            path=self.detail_url,
            data=self.user_1_updated_data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.user_1_updated_data)

    def test_put_user_detail_as_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(
            path=self.detail_url,
            data=self.user_1_updated_data,
        )

        self.user_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.user_1_updated_data)

    def test_put_user_detail_as_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.put(
            path=self.detail_url,
            data=self.user_1_updated_data,
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            path=self.detail_url,
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class ProfileViewSetTestCase(APITestCase):
    @staticmethod
    def generate_photo_file():
        file = BytesIO()
        image = Image.new("RGB", size=(100, 100), color=(155, 0, 0))
        image.save(file, "jpeg")
        file.name = "test.jpeg"
        file.seek(0)
        return file

    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()
        cls.admin = UserFactory(is_superuser=True)
        cls.data = {"description": "test description", "file": ""}

        cls.avatar_data = {"file": cls.generate_photo_file()}

        cls.url_detail = reverse("users:profile-detail", kwargs={"pk": cls.user_1.pk})

    def test_get_existing_profile(self):
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_existing_profile(self):
        response = self.client.put(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.put(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_profile(self):
        response = self.client.patch(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(self.url_detail, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_logged_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_not_logged(self):
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_avatar_logged_owner(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_logged_not_owner(self):
        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserFavouritesTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.url_add_favourite_presentations = reverse(
            "users:user-add_to_favourite_presentations", kwargs={"pk": cls.user_1.id}
        )
        cls.url_add_favourite_tags = reverse(
            "users:user-add_to_favourite_tags", kwargs={"pk": cls.user_1.id}
        )
        cls.url_remove_favourite_presentations = reverse(
            "users:user-remove_from_favourite_presentations",
            kwargs={"pk": cls.user_1.id},
        )
        cls.url_remove_favourite_tags = reverse(
            "users:user-remove_from_favourite_tags", kwargs={"pk": cls.user_1.id}
        )

        cls.tag = TagFactory(name="Django")
        cls.presentation = PresentationFactory()
        cls.tag_data = {"favourite_tags": [cls.tag.id]}
        cls.presentation_data = {"favourite_presentations": [cls.presentation.id]}

    def test_add_favourite_tags(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(self.url_add_favourite_tags, self.tag_data)

        self.user_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.tag in self.user_1.favourite_tags.all())

    def test_add_favourite_presentations(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(
            self.url_add_favourite_presentations, self.presentation_data
        )

        self.user_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.presentation in self.user_1.favourite_presentations.all())

    def test_remove_favourite_tags(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(self.url_remove_favourite_tags, self.tag_data)

        self.user_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.tag in self.user_1.favourite_tags.all())

    def test_remove_favourite_presentations(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.put(
            self.url_remove_favourite_presentations, self.presentation_data
        )

        self.user_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.presentation in self.user_1.favourite_presentations.all())
