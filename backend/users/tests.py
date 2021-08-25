from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterUserTest(APITestCase):
    """Test module for register a new user"""

    @classmethod
    def setUpTestData(cls):
        cls.register_url = reverse("user-register")
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

    def test_register_valid_user(self) -> None:
        response = self.client.post(
            path=self.register_url,
            data=self.valid_payload,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_invalid_user(self) -> None:
        response = self.client.post(
            path=self.register_url,
            data=self.invalid_payload,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
