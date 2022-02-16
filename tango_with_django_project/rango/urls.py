from telnetlib import STATUS
#from django.conf.urls import patterns, url
from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    #path(r'rango/index/',views.index,name='index'),
    path('',views.index,name='index'),
    path(r'rango/about/', views.about, name='about'),
    path(r'rango/',views.index,name='index'),
    path(r'about/',views.about,name='about'),
    #path(r'rango/category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path(r'rango/category/<slug:category_name_slug>/',view=views.show_category,name='show_category'),
    path(r'rango/add_category/', views.add_category, name='add_category'),
    path(r'rango/category/<slug:category_name_slug>/add_page/', views.add_page,name='add_page')
]
