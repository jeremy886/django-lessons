"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views, views2, views3, views4
from reviews import views as v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^view1/$', views.view_1),
    url(r'^view2/$', views.view_2),
    url(r'^view_1/$', views2.view_1),
    url(r'^view_2/$', views2.view_2),
    url(r'^view-1/$', views3.view_1),
    url(r'^view-2/$', views3.view_2),
    url(r'^hi/$', views4.hi),
    url(r'^hello/$', views4.hello),
    url(r'^review1/$', v.write_review),
    url(r'^time/$', v.time_calc),
    url(r'^tztime/$', v.tz_time_calc),
    url(r'^timeinc/$', v.time_inc),
]
