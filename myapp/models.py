from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,max_length=100,blank=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Categories'
        ordering=['name']


    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('myapp:category_detail',args=[self.slug])

class Article(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='articles')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('myapp:article_detail', args=[self.slug])
