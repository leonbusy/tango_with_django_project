from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    path(r'rango/index/',views.index,name='index'),
    path(r'rango/about/', views.about, name='about'),
    path(r'rango/',views.index,name='index'),
    #path(r'about/',views.about,name='about'),
]
