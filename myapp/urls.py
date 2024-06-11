from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]
