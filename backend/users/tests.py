from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


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


class UsersEndpointsTestCase(APITestCase):
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
        cls.user_1_updated_data = {
            "username": "user_1_updated",
            "email": "user1@updated.com",
            "first_name": "user_updated",
            "last_name": "test_1_updated"
        }
        cls.token_url = reverse("token_obtain_pair")
        cls.list_url = reverse("users:user-list")
        cls.detail_url = reverse("users:user-detail", kwargs={"pk": cls.user_1.pk})

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
        self.assertEqual(len(response.data), 3)

    def test_get_user_detail_without_authentication(self):
        response = self.client.get(
            path=self.detail_url,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_detail_with_authentication(self):
        # token = self.get_token(self.user_1)
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
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
