from django.urls import path,re_path
from pyrsistent import v
from EmployeeApp import views

urlpatterns=[
    path('', views.departmentApi),
    re_path(r'^([0-9]+)$', views.departmentApi)
]