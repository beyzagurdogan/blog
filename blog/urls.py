from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='home'),  # Blog ana sayfasına yönlendirme
]
