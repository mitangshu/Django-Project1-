from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'about', views.about, name='about'),
    url(r'services', views.services, name='services'),
    url(r'contact', views.contact, name='contact'),
    url(r'gallery', views.gallery, name='gallery'),

]