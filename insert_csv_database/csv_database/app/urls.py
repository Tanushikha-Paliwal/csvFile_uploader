from django.urls import path
from . import views

urlpatterns = [
    path("",views.insert_data , name='insert_data'),
    path("table/", views.show_data)
]
