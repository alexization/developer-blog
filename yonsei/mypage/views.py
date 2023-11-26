from django.shortcuts import render
from .models import Category
from .models import Post

# Create your views here.
def main(request):
    category_list = Category.objects.order_by('id')
    post_list = Post.objects.order_by('id')

    context = {'category_list' : category_list, 'post_list' : post_list}

    return render(request, 'mypage/index.html', context)

def login(request):

    return render(request, 'mypage/login.html')