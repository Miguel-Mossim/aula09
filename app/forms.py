from django import forms

from app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['data_postagem', 'autor', 'aprovado']