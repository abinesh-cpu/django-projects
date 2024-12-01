from django.urls import path
from . import views
urlpatterns=[
    path('index/<int:data>',views.index),
    path('index1',views.index1),
]