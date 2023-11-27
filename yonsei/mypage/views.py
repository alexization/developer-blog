from django.shortcuts import render
from .models import Category
from .models import Post
from .models import Comments
from .models import User_Info

# Create your views here.
def main(request):
    category_list = Category.objects.order_by('id')
    post_list = Post.objects.order_by('id')

    context = {'category_list' : category_list, 'post_list' : post_list}
    return render(request, 'mypage/index.html', context)

def login(request):

    return render(request, 'mypage/login.html')

def category(request, cate_name):
    category_list = Category.objects.all()
    for cate in category_list:
        if cate.cate_name.lower() == cate_name:
            category_id = cate.id
    post_list = Post.objects.filter(cate_id=category_id)

    context = {'category_list' : category_list, 'post_list' : post_list, 'cate_name' : cate_name}
    return render(request, 'mypage/category.html', context)

def post_detail(request, post_id):

    context = {'post_id' : post_id}
    return render(request, 'mypage/detail.html', context)

def post_write(request):

    return render(request, 'mypage/write.html')

def about(request):

    return render(request, 'mypage/about.html')