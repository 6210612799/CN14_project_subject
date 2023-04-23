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

app_name = 'subjectenroller'
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.login_view , name="login_view"),
    path('homepage/', views.homepage , name="homepage"),
    path('enroll_page/', views.enroll_page , name="enroll_page"),#
    path('enroll/<str:S_id>/', views.enroll , name="enroll"),
    path('un_enroll/<str:S_id>/', views.un_enroll , name="un_enroll"),
    # path('enroll/<str:S_id>/subjectenroller/test_enroll.html/', views.test_enroll, name="test_enroll"),#
    path('detail/<str:S_id>/', views.detail , name="detail"),
    path('logout/', views.logout_view , name="logout_view"),
    path('skill_tree', views.skill_tree , name="skill_tree"),
    path('test', views.test , name="test"),
    path('one_termone/', views.one_termone , name="one_termone"),
    path('one_termtwo/', views.one_termtwo , name="one_termtwo"),
    path('two_termone/', views.two_termone , name="two_termone"),
    path('two_termtwo/', views.two_termtwo , name="two_termtwo"),
    path('three_termone', views.three_termone , name="three_termone"),
    path('three_termtwo', views.three_termtwo , name="three_termtwo"),
    path('four_termone', views.four_termone , name="four_termone"),
    path('four_termtwo', views.four_termtwo , name="four_termtwo"),
]
