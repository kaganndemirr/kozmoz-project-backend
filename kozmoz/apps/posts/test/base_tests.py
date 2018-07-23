# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from post.models import Post, Comment, PostVote, CommentVote


class CommentAPITestCase(APITestCase):

	def setUp(self):
		# Create User and Token
        self.user = User.objects.create_user('kozmoz@domain.com', '123456e!')
        self.user.first_name = 'kozmoz'
        self.user.last_name = 'backend'
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Token Authentication
        self.api_authentication()

        # Create Dummy Data
        self.dummy_data = {
            'post': self.post.id,
            'comment': self.comment,
            'user': self.user.id
        }

        # Create Comment
        self.comment = Comment.objects.create(
        	post=self.post, 
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


class PostAPITestCase(APITestCase):
	dummy_data = {
		'description': 'My First Video',
		'media': ''
	}

	def setUp(self):
		# Create User and Token
        self.user = User.objects.create_user('kozmoz@domain.com', '123456e!')
        self.user.first_name = 'kozmoz'
        self.user.last_name = 'backend'
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Token Authentication
        self.api_authentication()

        # Create Task
        self.post = Post.objects.create(user=self.user, **self.dummy_data)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)