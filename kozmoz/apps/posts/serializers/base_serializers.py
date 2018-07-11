# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'comment', 'comment_published_date')

    def validate_task(self, value):
        user = self.context['request'].user

        if user != value.user:
            raise serializers.ValidationError(_('Post does not found'))

        return value


class CommentListSerializer(CommentSerializer):
    pass


class CommentRetrieveSerializer(CommentSerializer):
    pass


class CommentCreateSerializer(CommentSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'comment', 'comment_published_date')


class CommentUpdateSerializer(CommentSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'comment_published_date')


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


class PostCreateSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description', 'published_date', 'media')


class PostUpdateSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description', 'media')
