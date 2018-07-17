# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from posts.models import Post, Comment, PostVote, CommentVote


class PostVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostVote
        fields = ('id', 'post', 'vote_type')


class PostVoteListSerializer(PostVoteSerializer):

    class Meta:
        model = PostVote
        fields = ('id', 'post', 'vote_type')


class CommentVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentVote
        fields = ('id', 'comment', 'vote_type')


class CommentVoteListSerializer(CommentVoteSerializer):

    class Meta:
        model = CommentVote
        fields = ('id', 'comment', 'vote_type')


class CommentSerializer(serializers.ModelSerializer):
    comment_votes = CommentVoteSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'comment', 'comment_published_date', 'comment_votes')

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
    post_votes = PostVoteSerializer(many=True, read_only=True)
    comment_votes = CommentVoteSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media',
            'post_votes', 'published_date', 'comments'
        )


class PostListSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media', 'post_votes')


class PostRetrieveSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'description', 'media',
             'post_votes', 'published_date', 'comments'
        )


class PostCreateSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description', 'published_date', 'media')


class PostUpdateSerializer(PostSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description', 'media')
