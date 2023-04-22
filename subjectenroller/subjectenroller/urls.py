"""subjectenroller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.login_view , name="login_view"),
    path('homepage/', views.homepage , name="homepage"),
    path('enroll_page/', views.enroll_page , name="enroll_page"),
    path('enroll/<str:S_id>/', views.enroll , name="enroll"),
    path('un_enroll/<str:S_id>/', views.un_enroll , name="un_enroll"),
    path('enroll/<str:S_id>/subjectenroller/test_enroll.html/', views.test_enroll, name="test_enroll"),
    path('detail/', views.detail , name="detail"),
    path('logout', views.logout_view , name="logout_view"),
    path('skill_tree', views.skill_tree , name="skill_tree"),
    path('test', views.test , name="test"),
]
