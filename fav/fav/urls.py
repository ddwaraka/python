"""fav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page),
    url(r'^delete/(?P<task_id>\d+)/$', views.delete),
    url(r'^edit_task/(?P<task_id>\d+)/$', views.edit),
    url(r'^filter_name/$', views.filter_name),
    url(r'^filter_priority/$', views.filter_priority),
    url(r'^filter_status/$', views.filter_status),

    # url(r'^add/', views.add_task),
    # url(r'^view/', views.view_task),
]
