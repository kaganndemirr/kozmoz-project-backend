#Local Django

from .base_serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer, CommentSerializer, CommentListSerializer,
    CommentRetrieveSerializer
)

from .v1_serializers import (PostSerializerV1, PostListSerializerV1,
    PostRetrieveSerializerV1, CommentSerializerV1, CommentListSerializerV1,
    CommentRetrieveSerializerV1
)
