from django import forms
from .models import Comments
from django.utils.translation import gettext_lazy as _
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }


