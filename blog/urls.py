from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),  # Blog ana sayfasına yönlendirme
    path('post/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Detay sayfası
]
