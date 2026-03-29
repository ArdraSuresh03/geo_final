from django.urls import path
from . import views
from django.urls import path
from .views import home

urlpatterns = [
    path('users/', views.create_user),
    path('users/list/', views.get_users),
    path('users/delete/<int:id>/', views.delete_user),
    path('search/', views.search_users),
    path('', home),
]