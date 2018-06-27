# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media',
            'published_date', 'comments'
        )


class PostListSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media')


class PostRetrieveSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media',
            'published_date', 'comments'
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'comment', 'comment_published_date')


class CommentListSerializer(serializers.ModelSerializer):
    pass


class CommentRetrieveSerializer(serializers.ModelSerializer):
    pass
