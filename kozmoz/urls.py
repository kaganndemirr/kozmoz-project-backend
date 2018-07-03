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
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls import include
from django.views.static import serve

# Local Django
from core.api_views import LoginView
from kozmoz.views import IndexView, ActivationView, ResetPasswordView

urlpatterns = [
    # Landing
    re_path('^$', IndexView.as_view(), name='index'),

    # Admin
    re_path('^admin/', admin.site.urls),

    # Token
    re_path('^auth/login', LoginView.as_view(), name='login'),
    re_path('^auth/', include('djoser.urls.authtoken')),

    # Api
    re_path('^', include('kozmoz.api_urls')),

    # Activation and Password Operations
    re_path('^activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
    re_path('^reset-password/(?P<key>\w+)/$', ResetPasswordView.as_view(), name='reset-password')
]
