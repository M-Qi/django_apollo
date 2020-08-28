from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return HttpResponse('index')


def index(request):
    return HttpResponse('首页')

def safe_b(request):
    return HttpResponse('实现b级别安全等级')

