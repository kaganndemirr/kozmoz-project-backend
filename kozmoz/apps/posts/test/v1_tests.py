# Third-Party
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from .base_tests import CommentAPITestCase, PostAPITestCase


class CommentAPIV1TestCase(CommentAPITestCase):

	def test_list_comment(self):
		url = reverse('v1:comments-list')

		response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
    	url = reverse('v1:comments-list')

    	response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('post', None),
            self.dummy_data.get('post', None),
            self.dummy_data.get('comment', None)
        )

    def test_retrieve_comment(self):
    	url = reverse('v1:comments-detail', kwargs={'pk': self.comment.id})

    	self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.comment.id)
        self.assertEqual(response.data.get('post', None), self.comment.post.id)

    def test_update_comment(self):
        dummy_data = {
            'comment': "My First Updated Comment"
        }

        url = reverse('v1:comments-detail', kwargs={'pk': self.comment.id})

        response = self.client.put(url, dummy_data, format='json')
        self.reminder.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.comment.id)

    def test_delete_reminder(self):
        url = reverse('v1:comments-detail', kwargs={'pk': self.comment.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostAPIV1TestCase(PostAPITestCase):

    def test_list_post(self):
        url = reverse('v1:posts-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('v1:posts-list')

        response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('description', None),
            self.dummy_data.get('description', None)
        )
        self.assertEqual(
            response.data.get('media', None),
            self.dummy_data.get('media', None)
        )

    def test_retrieve_post(self):
        url = reverse('v1:posts-detail', kwargs={'pk': self.post.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.post.id)
        self.assertEqual(response.data.get('description', None), self.post.description)
        self.assertEqual(response.data.get('media', None), self.post.media)

    def test_update_post(self):
        dummy_data = {
            'description': 'My first Updated Post',
            'media': ''
        }
        url = reverse('v1:posts-detail', kwargs={'pk': self.post.id})

        response = self.client.put(url, dummy_data, format='json')
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.post.id)
        self.assertEqual(response.data.get('description', None), self.post.description)
        self.assertEqual(response.data.get('media', None), self.post.media)

    def test_delete_post(self):
        url = reverse('v1:posts-detail', kwargs={'pk': self.post.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)