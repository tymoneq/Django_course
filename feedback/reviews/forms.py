from os import error
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your name", max_length=100,error_messages={
#         "required": "Your name must not be empty.",
#         "max_length": "Your name cannot exceed 100 characters.",
#     })
#     review_text = forms.CharField(
#         label="Your feedback",
#         widget=forms.Textarea,
#         max_length=1000,
#         error_messages={
#             "required": "Your feedback must not be empty.",
#         },
#     )
    
#     rating_field = forms.IntegerField(label="Rating (1-5)",min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("username", "review_text", "rating")
        labels = {"username": "Your name", "review_text": "Your feedback", "rating": "Rating (1-5)"}
        error_messages = {
            "username": {
                "required": "Your name must not be empty.",
                "max_length": "Your name cannot exceed 100 characters.",
            },
            "review_text": {
                "required": "Your feedback must not be empty.",
            },
            "rating": {
                "min_value": "Rating must be at least 1.",
                "max_value": "Rating cannot exceed 5.",
            },
        }
