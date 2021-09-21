from datetime import datetime
from io import BytesIO

from django.contrib.auth import get_user_model
from django.urls import reverse
import pytz
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from resources.factories import ResourceFactory
from presentation.factories import PresentationFactory, UserFactory, TagFactory
from resources.serializers import CreateResourceSerializer
from resources.models import Resource


User = get_user_model()


class TestResourceViewSet(APITestCase):
    @staticmethod
    def generate_file():
        from django.core.files.uploadedfile import SimpleUploadedFile
        return SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")

    @staticmethod
    def generate_photo_file():
        file = BytesIO()
        image = Image.new("RGB", size=(100, 100), color=(155, 0, 0))
        image.save(file, format="jpeg")
        file.name = "resource.jpeg"
        file.seek(0)
        return file

    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()
        cls.admin = UserFactory(is_superuser=True)
        cls.tag_1 = TagFactory(name="Backend")
        cls.tag_2 = TagFactory(name="Docker")
        cls.pres_1 = PresentationFactory.create(
            scheduled_on=datetime(2021, 8, 15, 8, 15, 0, tzinfo=pytz.UTC),
            user=cls.user_1,
            tags=[cls.tag_1, cls.tag_2],
        )
        cls.res_1 = ResourceFactory(
            uploaded_on=datetime(2021, 8, 15, 8, 15, 12, tzinfo=pytz.UTC),
            fk_pres_id=cls.pres_1
        )
        cls.new_resource = {
            "name": "New resource",
            "description": "New test resource",
            "path": cls.generate_photo_file(),
            "uploaded_on": datetime(2021, 9, 1, 12, 0, 0, tzinfo=pytz.UTC),
            "fk_pres_id":  cls.pres_1.id
        }
        cls.updated_resource = {
            "name": "Updated",
            "description": "Updated description",
            "uploaded_on": datetime(2021, 10, 16, 11, 0, 0, tzinfo=pytz.UTC),
        }
        cls.list_url = reverse(
            "resources:resource-list"
        )
        cls.detailed_url = reverse(
            "resources:resource-detail",
            kwargs={"pk": cls.res_1.pk}
        )

    def test_get_resource_list_no_authentication(self):
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detailed_resource_no_authentication(self):
        response = self.client.get(path=self.detailed_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_resource_list_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_resource_detailed_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(path=self.detailed_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CreateResourceSerializer(self.res_1).data)

    def test_post_new_resource_with_authentication(self):
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(
            path=self.list_url, data=self.new_resource, format="multipart"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resource.objects.count(), 2)

    def test_post_new_resource_no_authentication(self):
        response = self.client.post(
            path=self.list_url, data=self.new_resource, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Resource.objects.count(), 1)

    def test_patch_resource_detail_no_authentication(self):
        response = self.client.patch(
            path=self.detailed_url, data=self.updated_resource, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_resource_detail_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            path=self.detailed_url, data=self.updated_resource, format="json"
        )
        self.res_1.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, CreateResourceSerializer(self.res_1).data
        )
