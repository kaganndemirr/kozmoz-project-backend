"""kozmoz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

# Local Django
from kozmoz.views import (IndexView, ActivationView, ResetPasswordView, DocumentationView)

# Third Party
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Landing
    re_path('^$', IndexView.as_view(), name='index'),

    # Admin
    re_path('^admin/', admin.site.urls),

    # Token
    re_path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Api
    re_path('^', include('kozmoz.api_urls')),

    # Activation and Password Operations
    re_path(r'^activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
    re_path(r'^reset-password/(?P<key>\w+)/$', ResetPasswordView.as_view(), name='reset-password'),

    # Documentation
    re_path('^docs/$', DocumentationView.as_view(), name='docs'),
    re_path('^docs/(?P<path>.*)$', DocumentationView.as_view(), name='docs'),
]
