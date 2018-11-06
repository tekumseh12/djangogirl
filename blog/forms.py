from .models import Post
from django import forms

class formular(forms.ModelForm):
    class Meta:
        model =Post
        fields =("title", "text",)
