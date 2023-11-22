from django.shortcuts import render
from .models import Category

# Create your views here.
def category(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list' : category_list}

    return render(request, 'mypage/index.html', context)