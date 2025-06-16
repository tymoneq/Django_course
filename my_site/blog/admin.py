from django.contrib import admin
from .models import Author, Tag, Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'text')
    list_filter = ('created_at',)

# Registering the models with the admin site

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
