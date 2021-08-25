import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

client = Client()


class RegisterUserTest(TestCase):
    """Test module for register a new user"""

    def setUp(self) -> None:
        self.valid_payload = {
            "username": "test_user",
            "password": "test_password",
            "password2": "test_password",
            "email": "test@mail.com",
            "first_name": "test",
            "last_name": "user",
        }
        self.invalid_payload = {
            "username": "test_user2",
            "password": "test_password2",
            "password2": "test_password3",
            "email": "testmail.com",
            "first_name": "test",
            "last_name": "",
        }

    def test_register_valid_user(self) -> None:
        response = client.post(
            reverse("user-register"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_invalid_user(self) -> None:
        response = client.post(
            reverse("user-register"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
