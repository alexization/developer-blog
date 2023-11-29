from django.shortcuts import render, redirect
from django.db.models import Count
from django.utils import timezone
from .models import Category
from .models import Post
from .models import Comments
from .models import User_Info

# Create your views here.

# index.html / 메인페이지
def main(request):
    # categorys에 post_count 변수명으로 post의 개수 정보 추가
    categorys = Category.objects.annotate(post_count=Count('post'))
    # posts에 comments_count 변수명으로 comment의 개수 정보 추가 + 역순으로 출력시켜 최신순으로 보이도록 함
    posts = Post.objects.annotate(comments_count=Count('comments')).order_by('-id')

    context = {'categorys': categorys, 'posts' : posts}
    return render(request, 'mypage/index.html', context)

def login(request):

    return render(request, 'mypage/login.html')

def category(request, cate_name):
    categorys = Category.objects.annotate(post_count=Count('post'))
    # 카테고리를 눌렀을 때 해당 카테고리에 포함되어 있는 post만 출력시키는 기능을 위함
    for cate in categorys:
        if cate.cate_name.lower() == cate_name:
            category_id = cate.id
    posts = Post.objects.filter(cate_id=category_id).annotate(comments_count=Count('comments')).order_by('-id')

    context = {'categorys' : categorys, 'posts' : posts, 'cate_name' : cate_name}
    return render(request, 'mypage/category.html', context)

def post_detail(request, post_id):
    # 특정 post를 클릭했을 때 해당 Post의 상세 페이지로 이동시키기 위함
    post = Post.objects.get(id=post_id)
    categorys = Category.objects.all()

    # 만약 POST method를 요청했을 때 수행되는 구문
    # 상세페이지를 들어갔을 때 DB에서 정보를 가져오기 위해 GET을 하게 되는데 해당 조건문을 달지않으면 상세페이지를 들어갈 때마다 POST를 수행하기 때문에 빈 값을 보내게 되어 오류 발생
    if request.method == "POST":
        # detail.html에 있는 input의 name값을 기반으로 value를 가져옴
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
        
    context = {'post' : post, 'categorys' : categorys}
    return render(request, 'mypage/detail.html', context)

def post_write(request):
    categorys = Category.objects.all()
    context = {'categorys' : categorys}

    # 위와 동일
    if request.method == "POST":
        
        cate = request.POST["categorys"]
        title = request.POST["title"]
        description = request.POST["description"]    
        content = request.POST["content"]
        # 썸네일 이미지 파일을 가져오기 위함
        thumbnail = request.FILES["thumbnail"]

        post = Post.objects.create(
            cate_id = int(cate),
            p_title = title,
            p_desc = description,
            p_contents = content,
            p_created = timezone.now(),
            p_updated = timezone.now(),
            thumbnail = thumbnail
        )
        # redirect를 통해 게시글 작성을 완료하면 해당 post 상세페이지로 이동
        return redirect(f"/posts/{post.id}")
    
    return render(request, 'mypage/write.html', context)

def about(request):

    return render(request, 'mypage/about.html')

def modify(request, post_id):

    return render(request, 'mypage/modify.html', )