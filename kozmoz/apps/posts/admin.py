# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user', 'description', 'media', 'publishing_date')

    list_display = ('user', 'description', 'media', 'publishing_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
