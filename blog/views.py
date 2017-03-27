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
def new_page(request):
   return  render(request,'new.html')
def edit_page(request,article_id):
   article = models.Article.objects.get(pk=article_id)
   return render(request,'edit.html',{'article':article})
def save(request):
   title= request.POST.get('title','title')
   content=request.POST.get('content','content')
   id=request.POST.get('id','')
   if id !='':
      models.Article.objects.update_or_create(pk=id,defaults={'title':title,'content':content})
      print('do update')
   else:
      models.Article.objects.create(title=title,content=content)
   article = models.Article.objects.all()
   return render(request, 'index.html', {'hello': 'hello blog!!!', 'article': article})



