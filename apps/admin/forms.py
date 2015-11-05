from django import forms

from apps.posts.models import Post

class PostForm(forms.ModelForm):
    """docstrings for PostForm"""

    class Meta:
        model = Post
        fields = ('name', 'slug', 'description', 'content', 'image',
                    'category')

        widgets = {
                'category': forms.widgets.Select(
                                        attrs={'class': 'form-control select2'}) 
        }

