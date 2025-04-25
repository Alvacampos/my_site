from django.contrib import admin

from blog.models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    list_filter = ('author', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
