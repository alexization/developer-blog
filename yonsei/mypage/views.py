from django.shortcuts import render
from django.db.models import Count
from .models import Category
from .models import Post
from .models import Comments
from .models import User_Info

# Create your views here.
def main(request):
    post_list = Post.objects.all()
    categorys = Category.objects.annotate(post_count=Count('post'))

    context = {'post_list' : post_list, 'categorys': categorys}
    return render(request, 'mypage/index.html', context)

def login(request):

    return render(request, 'mypage/login.html')

def category(request, cate_name):
    category_list = Category.objects.all()
    categorys = Category.objects.annotate(post_count=Count('post'))
    for cate in category_list:
        if cate.cate_name.lower() == cate_name:
            category_id = cate.id
    post_list = Post.objects.filter(cate_id=category_id)

    context = {'categorys' : categorys, 'post_list' : post_list, 'cate_name' : cate_name}
    return render(request, 'mypage/category.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post' : post}
    return render(request, 'mypage/detail.html', context)

def post_write(request):

    return render(request, 'mypage/write.html')

def about(request):

    return render(request, 'mypage/about.html')