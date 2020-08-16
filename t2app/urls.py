from django.urls import path
from . import views

urlpatterns=[
    path ('',views.reg,name='reg'),
    path('search/',views.search,name='search')

    ]