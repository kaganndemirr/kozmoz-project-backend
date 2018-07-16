# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local
from posts.models import Post, Comment, PostVote, CommentVote

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'media',)

    list_display = ('user', 'description', 'media', 'published_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'comment',)

    list_display = ('post', 'comment', 'comment_published_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
	fields = ('post', 'vote_type',)

	list_display = ('post', 'vote_type', 'voting_date')


@admin.register(CommentVote)
class CommentVoteAdmin(admin.ModelAdmin):
	fields = ('comment', 'vote_type',)

	list_display = ('comment', 'vote_type', 'voting_date')
