"""aizuji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import views
from aizuji.login import login as login
from aizuji.interface import interface
from aizuji.testdb import testdb

urlpatterns = [
    url ( r'woaizuji/', views.menu ),
    url ( r'cases', views.cases ),
    url ( r'environment', views.environment ),
    url ( r'task', views.task ),
    url ( r'interface', interface ),
    url ( r'login', login),
    url('testdb/', testdb),
    # url(r'^search$', search.search),
    # url(r'lgoin', views.login),
]