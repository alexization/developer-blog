from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Info(models.Model):
    u_id = models.CharField(max_length=20)
    u_pw = models.CharField(max_length=20)
    u_name = models.CharField(max_length=10)
    u_school = models.CharField(max_length=20)

class Category(models.Model):
    cate_name = models.CharField(max_length=50)

class Post(models.Model):
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    p_title = models.CharField(max_length=50)
    p_desc = models.CharField(max_length=100)
    p_contents = models.TextField()
    p_created = models.DateTimeField(auto_now_add=True)
    p_updated = models.DateTimeField(auto_now=True)
    p_secure = models.BooleanField(default=True)

class Comments(models.Model):
    p = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    c_user_id = models.CharField(max_length=20)
    c_user_pw = models.CharField(max_length=20)
    c_contents = models.TextField()
    c_created = models.DateTimeField(auto_now_add=True)
    c_updated = models.DateTimeField(auto_now=True)