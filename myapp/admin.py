from django.contrib import admin
from . models import Category,Article
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','created_at']
    search_fields=["name"]
    list_filter=['is_active']

admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['name','created_at']
    search_fields=["name"]
    list_filter=['is_active']

admin.site.register(Article,ArticleAdmin)
