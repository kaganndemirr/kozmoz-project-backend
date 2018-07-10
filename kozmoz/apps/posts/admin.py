# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local
from posts.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'media',)

    list_display = ('user', 'description', 'media', 'published_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'post', 'comment', 'comment_published_date')

    list_display = ('user', 'post', 'comment', 'comment_published_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
