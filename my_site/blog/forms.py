from cProfile import label
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "text")
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "text": "Your Comment"
        }
