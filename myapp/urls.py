from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('film/<int:pk>/stats/', views.film_stats, name='film_stats'),
    path('film/<int:pk>/edit/', views.film_edit, name='film_edit'),
]

