from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Article
from .forms import ArticleForm


def dashboard(request):
    posts = Article.objects.filter(is_active=True)
    return render(request, 'index.html', {'posts': posts})


def article_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'post': post})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save()
            return redirect('dashboard:article_detail', slug=article.slug)

    else:
        form = ArticleForm()

    return render(request, 'dashboard/add_article.html', {'form': form})


def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        form = ArticleForm(
            request.POST,
            request.FILES,
            instance=article
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ArticleForm(instance=article)

    return render(
        request,
        'dashboard/edit_article.html',
        {
            'form': form,
            'article': article
        }
    )
def delete_article(request,slug):
    article=get_object_or_404(Article,slug=slug)
    if request.method=="POST":
        article.delete()
    return redirect('dashboard:dashboard')