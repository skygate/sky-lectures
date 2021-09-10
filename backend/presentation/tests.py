from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from presentation.factories import CommentFactory, PresentationFactory, UserFactory
from presentation.models import Comment


User = get_user_model()


class CommentTest(APITestCase):
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
        self.client.force_login(user=self.user_1)
        response = self.client.post(path=self.list_url, data=self.valid_comment)

        self.comment_1.refresh_from_db()

        self.assertEqual(Comment.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_not_authenticated(self):
        response = self.client.put(path=self.list_url, data=self.valid_comment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authenticated(self):
        self.client.force_login(user=self.user_1)
        response = self.client.put(path=self.detail_url, data=self.valid_update_comment)

        self.comment_1.refresh_from_db()

        self.assertEqual(self.comment_1.text, self.valid_update_comment["text"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_not_authenticated(self):
        response = self.client.patch(path=self.list_url, data=self.valid_comment)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_authenticated(self):
        self.client.force_login(user=self.user_1)
        response = self.client.patch(
            path=self.detail_url, data=self.valid_update_comment
        )

        self.comment_1.refresh_from_db()

        self.assertEqual(self.comment_1.text, self.valid_update_comment["text"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
