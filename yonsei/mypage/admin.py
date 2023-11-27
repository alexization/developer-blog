from django.contrib import admin
from .models import User_Info
from .models import Post
from .models import Category
from .models import Comments

# Register your models here.

@admin.register(User_Info)
class User_InfoAdmin(admin.ModelAdmin):
    pass
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["p_title", "thumbnail"]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass