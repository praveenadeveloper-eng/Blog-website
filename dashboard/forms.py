from django import forms
from myapp.models import Article,Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model  = Article
        fields = "__all__"
        widgets={
            
        }