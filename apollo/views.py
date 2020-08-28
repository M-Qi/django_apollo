from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return HttpResponse('index')


def index(request):
    return HttpResponse('首页')

def safe_a(request):
    print('输出A等级安全算法')
    return HttpResponse('实现了A等级的安全级别')



def safe_b(request):
    print('输出B等级安全的算法')
    return HttpResponse('实现b级别安全等级')

def reg(request):
    return HttpResponse('注册')

