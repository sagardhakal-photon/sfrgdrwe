"""MUSICIAN URL Configuration

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
from django.contrib import admin  
from django.urls import path ,include
from musicdatab import views  

admin.site.title_header = "LOGIN TO ADMINSTRATION PANAL"
admin.site.site_header = "XYZ ADMINISTRATION PANAL "
admin.site.index_title= "WELCOME TO THIS PORTAL "
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', views.home,), 
    path('show',views.show),
    path('showall',views.showall),
    path('user',views.user),
    path('userdetails',views.userdetails),
    path('songs',views.songs),
    path('albums',views.albums),
    path('instrumentplayer',views.instrumentplayer),
    path('performance',views.performance),
    path('instrument',views.instrument),

    
]  