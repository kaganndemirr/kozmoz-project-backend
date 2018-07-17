#Local Django

from .base_serializers import (
    PostSerializer, PostListSerializer, PostRetrieveSerializer, PostCreateSerializer,
    PostUpdateSerializer, PostVoteSerializer, PostVoteListSerializer, CommentSerializer,
    CommentListSerializer, CommentRetrieveSerializer, CommentCreateSerializer, CommentUpdateSerializer,
    CommentVoteSerializer, CommentVoteListSerializer
)

from .v1_serializers import (
    PostSerializerV1, PostListSerializerV1, PostRetrieveSerializerV1,
    PostCreateSerializerV1, PostUpdateSerializerV1, PostVoteSerializerV1, PostVoteListSerializerV1,
    CommentSerializerV1, CommentListSerializerV1, CommentRetrieveSerializerV1, CommentCreateSerializerV1,
    CommentUpdateSerializerV1, CommentVoteSerializerV1, CommentVoteListSerializerV1
)
