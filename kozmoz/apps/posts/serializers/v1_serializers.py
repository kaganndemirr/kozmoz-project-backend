# Local Django
from .base_serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer, CommentSerializer, CommentListSerializer,
    CommentRetrieveSerializer
)


class CommentSerializerV1(CommentSerializer):
    pass


class CommentListSerializerV1(CommentListSerializer):
    pass


class CommentRetrieveSerializerV1(CommentRetrieveSerializer):
    pass

class PostSerializerV1(PostSerializer):
    pass


class PostListSerializerV1(PostListSerializer):
    pass


class PostRetrieveSerializerV1(PostRetrieveSerializer):
    pass
