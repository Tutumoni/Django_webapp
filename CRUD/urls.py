from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create, name='create'),
    url(r'^update$', views.update, name='update'),
    url(r'^index$', views.index, name='index'),
    url(r'^view$', views.view),
    url(r'^delete$', views.delete, name='delete')
]