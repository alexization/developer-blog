from django.contrib import admin
from .models import User_Info
from .models import Post
from .models import Category
from .models import Comments

# Register your models here.

admin.site.register(User_Info)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comments)