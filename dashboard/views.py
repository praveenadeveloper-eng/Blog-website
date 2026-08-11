from django.shortcuts import render, get_object_or_404
from myapp.models import Article


def dashboard(request):
    posts = Article.objects.filter(is_active=True)

    return render(request,'index.html',{'posts': posts})


def article_detail(request, slug):
    post = get_object_or_404(Article,slug=slug)
    return render(request,'article.html',{'post': post})