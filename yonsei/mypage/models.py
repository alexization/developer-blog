from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Info(models.Model):
    u_id = models.CharField(max_length=20)
    u_pw = models.CharField(max_length=20)
    u_name = models.CharField(max_length=10)
    u_school = models.CharField(max_length=20)

class Post(models.Model):
    p_title = models.CharField(max_length=50)
    p_desc = models.CharField(max_length=100)
    p_contents = models.TextField()
    p_created = models.DateTimeField(auto_now_add=True)
    p_updated = models.DateTimeField(auto_now=True)
    p_secure = models.BooleanField(default=True)

class Category(models.Model):
    p_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    cate_name = models.CharField(max_length=50)

class Comments(models.Model):
    p_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    c_user_id = models.CharField(max_length=20)
    c_user_pw = models.CharField(max_length=20)
    c_contents = models.TextField()
    c_created = models.DateTimeField(auto_now_add=True)
    c_updated = models.DateTimeField(auto_now=True)