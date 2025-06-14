from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    
