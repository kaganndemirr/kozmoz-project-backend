# Django
from django.urls import path, include

# Third-Party
from rest_framework import routers

# Local Django
from users.api_views import UserViewSetV1
from posts.api_views import PostViewSetV1, CommentViewSetV1

router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'posts', PostViewSetV1, 'posts'),
    (r'users', UserViewSetV1, 'users')
]

for router in LIST_V1:
    router_V1.register(router[0], router[1], base_name=router[2])

urlpatterns = [
    path(r'v1/', include((router_V1.urls, 'v1'), namespace='v1')),
]
