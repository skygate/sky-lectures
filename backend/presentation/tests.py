from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from presentation.factories import CommentFactory, PresentationFactory, UserFactory


User = get_user_model()


class CommentTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user1 = UserFactory()
        cls.test_user2 = UserFactory()
        cls.test_admin = UserFactory(is_superuser=True)
        cls.test_presentation = PresentationFactory()
        cls.test_comment = CommentFactory(user=cls.test_user1)

        cls.valid_comment = {
            "text": "some comment",
            "presentation_id": cls.test_presentation.id,
            "user": cls.test_user1,
            "reply_to": cls.test_comment.id,
        }

        cls.valid_update_comment = {"text": "some new comment"}

        cls.list_url = reverse("presentation:comment-list")
        cls.detail_url = reverse(
            "presentation:comment-detail", kwargs={"pk": cls.test_comment.pk}
        )

    def test_get_comments_list_not_authenticated(self):
        response = self.client.get(path=self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_comments_list_authenticated(self):
        self.client.force_authenticate(user=self.test_user2)
        response = self.client.get(path=self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_comment_not_authenticated(self):
        response = self.client.post(path=self.list_url, data=self.valid_comment)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_comment_authenticated(self):
        self.client.force_login(user=self.test_user1)
        response = self.client.post(path=self.list_url, data=self.valid_comment)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_not_authenticated(self):
        response = self.client.put(path=self.list_url, data=self.valid_comment)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authenticated(self):
        self.client.force_login(user=self.test_user1)
        response = self.client.put(path=self.detail_url, data=self.valid_update_comment)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_not_authenticated(self):
        response = self.client.patch(path=self.list_url, data=self.valid_comment)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_authenticated(self):
        self.client.force_login(user=self.test_user1)
        response = self.client.patch(
            path=self.detail_url, data=self.valid_update_comment
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
