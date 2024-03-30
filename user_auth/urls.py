# user_auth/urls.py
from django.urls import include, path, re_path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user')
]
