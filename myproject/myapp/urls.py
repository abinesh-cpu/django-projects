
from django.urls import path
from . import views
urlpatterns=[
    path('',views.adminlogin),
    path('adminhome',views.adminhome),
    path('employereg',views.employereg)
]