from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('write/', views.post_write, name='write'),
    path('about/', views.about, name="about"),
    path('posts/<int:post_id>/', views.post_detail, name="posts"),
    path('category/<str:cate_name>/', views.category, name='category'),
]