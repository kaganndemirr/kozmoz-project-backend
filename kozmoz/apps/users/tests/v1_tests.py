# Standart Library
import io

# Third-Party
from PIL import Image
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from users.models import User
from .base_tests import UserAPITestCase


class UserAPIV1TestCase(UserAPITestCase):

	def test_list_user(self):
		url = reverse('v1:users-list')
		self.api_authentication()

		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)