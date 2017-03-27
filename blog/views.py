from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def index(request):
   #return HttpResponse('hello world')
   article= models.Article.objects.all()
   return render(request,'index.html',{'hello':'hello blog!!!','article':article})
def article_page(request,article_id):
   article = models.Article.objects.get(pk=article_id)
   return render(request,'article_page.html',{'article': article})
def new(request):
   return  render(request,'new.html')
