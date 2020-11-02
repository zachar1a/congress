"""vote URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf.urls import url, include 

from results.views import FrontEndAppView, billInfoView, voteResults, retrieveBill, getLatestBill, getLatestVote

router = routers.DefaultRouter()
router.register(r'info', billInfoView, 'info/')
router.register(r'results', voteResults, 'results/')

#urlpatterns=router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', FrontEndAppView.as_view()), 
    path('bill/<slug>/', retrieveBill),
    path('latest-bill/', getLatestBill),
    path('latest-vote/', getLatestVote),
    #path(r'^$', FrontEndAppView.as_view()),
    re_path(r'^(?P<path>.*)/$', FrontEndAppView.as_view()),
    
]
