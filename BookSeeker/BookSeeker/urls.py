"""BookSeeker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter

from bookfinder.views import BookViewSet, AuthorViewSet, GenreViewSet

router = SimpleRouter()
router.register(r'api/books', BookViewSet)
router.register(r'api/authors', AuthorViewSet)
router.register(r'api/genres', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('account.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('books/', include('bookfinder.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls