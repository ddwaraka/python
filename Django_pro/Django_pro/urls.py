"""Django_pro URL Configuration

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
from stock import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello1/', views.hello1),
    url(r'^hello2/', views.hello2),
    url(r'^hello3/', views.hello3),
    url(r'^hello4/', views.hello4),
    url(r'^hello5/', views.hello5),
    url(r'^hello6/', views.hello6),

]
