# Local Django
from .base_serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer, CommentSerializer, CommentListSerializer,
    CommentRetrieveSerializer
)

class PostSerializerV1(PostSerializer):
    pass


class PostListSerializerV1(PostListSerializer):
    pass


class PostRetrieveSerializerV1(PostDetailSerializer):
    pass


class CommentSerializerV1(CommentSerializer):
    pass


class CommentListSerializerV1(CommentListSerializerV1):
    pass


class CommentRetrieveSerializerV1(CommentRetrieveSerializer):
    pass
    
