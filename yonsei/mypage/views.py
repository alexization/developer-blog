from django.shortcuts import render, redirect
from django.db.models import Count
from django.utils import timezone
from .models import Category
from .models import Post
from .models import Comments
from .models import User_Info

# Create your views here.
def main(request):
    post_list = Post.objects.order_by('-id')
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
    if request.method == "POST":
        comment_content = request.POST["comment"]
        comment_id = request.POST["comment_id"]
        comment_pw = request.POST["comment_pw"]

        Comments.objects.create(
            p_id = post_id,
            c_contents = comment_content,
            c_user_id = comment_id,
            c_user_pw = comment_pw,
            c_created = timezone.now(),
            c_updated = timezone.now()
        )
        print(post_id)
        
    context = {'post' : post}
    return render(request, 'mypage/detail.html', context)

def post_write(request):
    category_list = Category.objects.all()
    context = {'category_list' : category_list}

    if request.method == "POST":
        
        cate = request.POST["categorys"]
        title = request.POST["title"]
        description = request.POST["description"]    
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]

        post = Post.objects.create(
            cate_id = int(cate),
            p_title = title,
            p_desc = description,
            p_contents = content,
            thumbnail = thumbnail
        )
        return redirect(f"/posts/{post.id}")
    
    return render(request, 'mypage/write.html', context)

def about(request):

    return render(request, 'mypage/about.html')