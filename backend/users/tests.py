from io import BytesIO

from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


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
        cls.test_user1 = User.objects.create_user(username="popopo", password="123")
        cls.test_user2 = User.objects.create_user(username="mkmkmkmmk", password="123")
        cls.test_admin = User.objects.create_superuser(username="ka", password="123")
        cls.test_data = {"description": "test description", "file": ""}

        cls.avatar_data = {"file": cls.generate_photo_file()}

        cls.url_detail = reverse("profile-detail", kwargs={"pk": cls.test_user1.id})

    def test_get_existing_profile(self):
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_existing_profile(self):
        response = self.client.put(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.put(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.put(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.put(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_profile(self):
        response = self.client.patch(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.patch(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.patch(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.patch(self.url_detail, self.test_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_not_logged(self):
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_existing_avatar_logged_owner(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_existing_avatar_logged_not_owner(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.patch(self.url_detail, self.avatar_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
