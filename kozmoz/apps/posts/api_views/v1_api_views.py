# Local Django
from .base_api_views import PostViewSet, CommentViewSet
from posts.serializers import (
    PostSerializer, CommentSerializer, PostListSerializerV1, PostRetrieveSerializerV1,
    PostCreateSerializerV1, PostUpdateSerializerV1, CommentListSerializerV1,
    CommentRetrieveSerializerV1, CommentCreateSerializerV1, CommentUpdateSerializerV1
)

class PostViewSetV1(PostViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializerV1
        elif self.action == 'retrieve':
            return PostRetrieveSerializerV1
        elif self.action == 'create':
            return PostCreateSerializerV1
        elif self.action == 'update':
            return PostUpdateSerializerV1
        else:
            return PostSerializer


class CommentViewSetV1(CommentViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializerV1
        elif self.action == 'retrieve':
            return CommentRetrieveSerializerV1
        elif self.action == 'create':
            return CommentCreateSerializerV1
        elif self.action == 'update':
            return CommentUpdateSerializerV1
        else:
            return CommentSerializer
