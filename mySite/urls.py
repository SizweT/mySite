"""
URL configuration for mySite project.
"""
from django.contrib import admin
from django.urls import include, path
from user_auth.views import SignUpView, user_login
from django.views.generic.base import TemplateView
from accounts.views import UserProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    # Include polls app URLs
    path('polls/', include('polls.urls')),
    # Include accounts app URLs
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

