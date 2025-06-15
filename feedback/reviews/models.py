from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=100, verbose_name="Your name")
    review_text = models.TextField(verbose_name="Your feedback")
    rating = models.IntegerField(verbose_name="Rating (1-5)")

    def __str__(self):
        return f"{self.username} - {self.rating} stars"
