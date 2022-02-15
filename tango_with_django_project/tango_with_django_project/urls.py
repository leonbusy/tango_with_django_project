"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#import imp
from django.contrib import admin
from django.urls import path
from rango import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='index'),
    #path('rango/',include('rango.urls')),
    #path('rango/category/',views.show_category,name='show_category'),
    path('admin/', admin.site.urls),   #supply admin path to admin
    path('',include('rango.urls')),
    #path(r'rango/category/<slug:category_name_slug>/',view=views.show_category,name='show_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
