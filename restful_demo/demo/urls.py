from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('IpPool/', views.Pool.as_view()),
    path('IpPool/<int:id>', views.Pool.as_view()),
]
