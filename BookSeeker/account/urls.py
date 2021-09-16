from django.urls import path, include
from django.views.generic import TemplateView

from account.views import UserRegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
]