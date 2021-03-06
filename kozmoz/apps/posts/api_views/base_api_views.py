# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from posts.models import Post, Comment, PostVote, CommentVote
from posts.serializers import (
    PostSerializer, PostListSerializer, PostRetrieveSerializer, PostCreateSerializer,
    PostUpdateSerializer, PostVoteSerializer, PostVoteListSerializer, PostVoteCreateSerializer,
    PostVoteUpdateSerializer, CommentSerializer, CommentListSerializer, CommentRetrieveSerializer,
    CommentCreateSerializer, CommentUpdateSerializer, CommentVoteSerializer, CommentVoteListSerializer,
    CommentVoteCreateSerializer, CommentVoteUpdateSerializer
)


class CommentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet
                    ):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        elif self.action == 'retrieve':
            return CommentRetrieveSerializer
        elif self.action == 'create':
            return CommentCreateSerializer
        elif self.action == 'update':
            return CommentUpdateSerializer
        else:
            return CommentSerializer

    def perform_create(self, serializer):
        comment = serializer.save(user=self.request.user)
        comment.save()

    def perform_update(self, serializer):
        comment = serializer.save()
        comment.save()

    def perform_destroy(self, instance):
        super(CommentViewSet, self).perform_destroy(instance)


class PostViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet
                 ):
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'retrieve':
            return PostRetrieveSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'update':
            return PostUpdateSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)

        comments_data = self.request.data.get('comments', [])
        for comments_data in comments_data:
            Comment.objects.create(post=post, **comments_data)

    def perform_destroy(self, instance):
        super(PostViewSet, self).perform_destroy(instance)


class PostVoteViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet
                    ):
    queryset = PostVote.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PostVoteListSerializer
        if self.action == 'create':
            return PostVoteCreateSerializer
        if self.action == 'update':
            return PostVoteUpdateSerializer
        else:
            return PostVoteSerializer

    def perform_create(self, serializer):
        vote_type = serializer.save(user=self.request.user)


class CommentVoteViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet
                      ):
    queryset = CommentVote.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
          return CommentVoteListSerializer
        if self.action == 'create':
          return CommentVoteCreateSerializer
        if self.action == 'update':
          return CommentVoteUpdateSerializer
        else:
          return CommentVoteSerializer

    def perform_create(self, serializer):
        vote_type = serializer.save(user=self.request.user)