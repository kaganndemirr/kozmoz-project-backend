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
from django.urls import path
from django.conf.urls import include

# Local Django
from kozmoz.views import ActivationView, ResetPasswordView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Api
    path('', include('kozmoz.api_urls')),

    # Token
    path('auth/', include('djoser.urls.authtoken')),

    # Activation and Password Operations
    path('activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
    path('reset-password/(?P<key>\w+)/$', ResetPasswordView.as_view(), name='reset-password')
]
