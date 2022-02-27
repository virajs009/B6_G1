"""Session_Cookie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app1 import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-cookie/', views.setcookie, name='set_cookie'),
    path('home/', views.homepage, name='homepage'),
    path('get-cookie/', views.getcookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookies, name='delete_cookie'),
    path('show-cookie/', views.show_cookie, name='show_cookie'),
    path('test-cookie/', views.cookie_session, name='test_cookie'),
    path('delete-scookie/', views.cookie_delete, name='delete_scookie'),
    path('demo-view/', views.demo_view, name='demo_view'),
    path('create/', views.create_session, name='create'),
    path('show-session/', views.show_session_data, name='show_session'),
    path('delete-session/', views.delete_session_data, name='delete_session'),
    path('user-login/', views.user_login, name='login'),
]


