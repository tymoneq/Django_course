from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)