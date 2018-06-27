# Local Django
from .base_api_views import PostViewSet, CommentViewSet
from posts.serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer, CommentSerializer, CommentListSerializer,
    CommentRetrieveSerializer, PostSerializerV1, PostListSerializerV1,
    PostRetrieveSerializerV1, CommentSerializerV1, CommentListSerializerV1,
    CommentRetrieveSerializerV1
)

class PostViewSetV1(PostViewSet):
    def get_serializer_class(self):
        if self.action=='list':
            return PostListSerializerV1
        elif self.action=='retrieve':
            return PostRetrieveSerializerV1
        else:
            return PostSerializer


class CommentViewSetV1(CommentViewSet):
    def get_serializer_class(self):
        if self.action=='list':
            return CommentListSerializerV1
        elif self.action=='retrieve':
            return CommentRetrieveSerializerV1
        else:
            return CommentSerializer
