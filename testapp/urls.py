from django.conf.urls import url
from testapp import views

urlpatterns =[
    url(r'^django_web_page$', views.helloDjango),
    url(r'^hello_python_page$', views.helloPython)
    ]
