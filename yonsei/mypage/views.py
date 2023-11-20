from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'message' : 'Hello world'}
    return render(request, 'mypage/index.html', context)