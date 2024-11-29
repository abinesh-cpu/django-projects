from django.urls import path
from . import views
urlpatterns=[
    path('product/<int:data>/<int:data1>',views.product)
]