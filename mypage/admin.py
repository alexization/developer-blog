from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from markdownx.admin import MarkdownxModelAdmin 
from .models import User
from .models import Post
from .models import Category
from .models import Comments

# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Post, MarkdownxModelAdmin)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass