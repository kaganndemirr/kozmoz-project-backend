# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from posts.models import Post, Comment
from posts.serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer
)


class PostViewSet(mixins.ListModelMixin
                  mixins.RetrieveModelMixin
                  viewsets.GenericViewSet
                 )
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostRetrieveSerializer
        else:
            return PostSerializer


class CommentViewSet(mixins.ListModelMixin
                     mixins.RetrieveModelMixin
                     viewsets.GenericViewSet
                     )
    queryset = Comment.objects.all()

    def queryset(self):
        return self.queryset.filter(post__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        elif self.action == 'retrieve':
            return CommentRetrieveSerializer
        else:
            return CommentSerializer
