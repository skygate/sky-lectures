from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class ProfileEndpointsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user1 = User.objects.create_user(username="popopo", password="123")
        cls.test_user2 = User.objects.create_user(username="mkmkmkmmk", password="123")
        cls.test_admin = User.objects.create_superuser(username="ka", password="123")
        cls.test_data = {"description": "test description"}

        cls.url_list = reverse("profile-list")
        cls.url_detail = reverse("profile-detail", kwargs={"pk": cls.test_user1.id})

    def test_get_profile_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_profile_list_logged(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_list_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_profile_list_wrong_address(self):
        response = self.client.get("0.0.0.0:8000/profiles-list")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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

    def test_post_profile(self):
        response = self.client.post(self.url_detail, self.test_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_profile_logged(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.post(self.url_detail, self.test_data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_profile_logged_admin(self):
        self.client.force_authenticate(user=self.test_admin)
        response = self.client.post(self.url_detail, self.test_data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

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

    def test_delete_existing_profile(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_existing_profile_logged_not_owner(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_existing_profile_logged_owner(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_existing_profile_logged_admin(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
