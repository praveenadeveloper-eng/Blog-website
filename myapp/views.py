from django.shortcuts import render,get_object_or_404
from .models import Category,Article
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def home(request):
    post=Article.objects.filter(is_active=True)[:8]
    category=Category.objects.filter(is_active=True)[:8]
    return render(request,'home.html',{'posts':post,'categorys':category})

@login_required
def article_detail(request, slug):
    post=get_object_or_404(Article,slug=slug,is_active=True)
    related=Article.objects.filter(category=post.category,is_active=True).exclude(id=post.id)[:4]
    return render(request,'post_detail.html',{'post':post,'related_post':related})

def post_list(request):
    search=request.GET.get('q')
    sort=request.GET.get('sort')
    post=Article.objects.filter(status=True)
    category_slug = request.GET.get('category')
    categories=Category.objects.filter(is_active=True)
    if category_slug:
        post = post.filter(category__slug=category_slug)
    if search:
        post=Article.objects.filter(Q(name__icontains=search)| Q(description__icontains=search))
    if sort=='recent':
        post=post.order_by('-created_at')
    if sort=='old':
        post=post.order_by('created_at')
    return render(request,"post_list.html",{'posts':post,'categories':categories})