from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    if request.user.has_perm('myapp.view_article'):
        posts=Article.objects.all()
    else:
        posts = Article.objects.filter(author=request.user)
    return render(request, 'index.html', {'posts': posts})


@login_required
def article_detail(request, slug):
    post = get_object_or_404(Article, slug=slug,is_active=True)
    return render(request, 'article.html', {'post': post})

@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author=request.user
            article .save()
            return redirect('dashboard:article_detail', slug=article.slug)

    else:
        form = ArticleForm()

    return render(request, 'dashboard/add_article.html', {'form': form})

@login_required
def edit_article(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
    )
    if not (
        request.user.has_perm('myapp.change_article')
        or article.author == request.user
    ):
        return redirect('dashboard:dashboard')

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')

    else:
        form = ArticleForm(instance=article)

    return render(
        request,
        'dashboard/edit_article.html',
        {'form': form, 'article': article}
    )
@login_required
def delete_article(request,slug):
    article=get_object_or_404(Article,slug=slug)
    if not (request.user.has_perm('myapp.delete_article') or article.author == request.user):
        return redirect('dashboard:dashboard')
    if request.method == "POST":
        article.delete()
    return redirect('dashboard:dashboard')