"""my_profile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from profile_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^team_index/$', views.home),
    url(r'^phetcharat/$', views.name_team1),
    url(r'^sutatip/$', views.name_team2),
    url(r'^chonticha/$', views.name_team3),
    url(r'^my_profile/$', views.profile),
    url(r'^my_index/$', views.index,name='home'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^profile1/$', views.page1,name='profile1'),
    url(r'^profile2/$', views.page2,name='profile2'),
    url(r'^profile3/$', views.page3,name='profile3'),
]




