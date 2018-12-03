from django.conf.urls import url
from studentapp import views

urlpatterns =[
    url(r'^studentinfo$', views.helloStudent, name='student_info')
    ]
