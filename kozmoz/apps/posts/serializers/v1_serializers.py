# Local Django
from .base_serializers import (PostSerializer, PostListSerializer,
    PostRetrieveSerializer, PostCreateSerializer, PostUpdateSerializer,
    PostVoteSerializer, PostVoteListSerializer,
    CommentSerializer, CommentListSerializer, CommentRetrieveSerializer,
    CommentCreateSerializer, CommentUpdateSerializer
)


class PostVoteSerializerV1(PostVoteSerializer):
    pass


class PostVoteListSerializerV1(PostVoteListSerializer):
    pass


class CommentSerializerV1(CommentSerializer):
    pass


class CommentListSerializerV1(CommentListSerializer):
    pass


class CommentRetrieveSerializerV1(CommentRetrieveSerializer):
    pass


class CommentCreateSerializerV1(CommentCreateSerializer):
    pass


class CommentUpdateSerializerV1(CommentUpdateSerializer):
    pass


class PostSerializerV1(PostSerializer):
    pass


class PostListSerializerV1(PostListSerializer):
    pass


class PostRetrieveSerializerV1(PostRetrieveSerializer):
    pass


class PostCreateSerializerV1(PostCreateSerializer):
    pass


class PostUpdateSerializerV1(PostUpdateSerializer):
    pass
