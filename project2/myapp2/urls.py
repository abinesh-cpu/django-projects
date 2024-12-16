from django.urls import path
from . import views
urlpatterns=[
    path('',views.userlogin),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('userregister',views.userreg),
    path('userhome',views.userhome),
    path('userlogout',views.userlogout),
    path('adminlogout',views.adminlogout)
]