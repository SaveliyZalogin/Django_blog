from django.contrib import admin
from Django_blog.apps.my_blog.models import Post
from Django_blog.apps.my_blog.models import Key_word
from Django_blog.apps.my_blog.models import Author

class PostAdmin(admin.ModelAdmin):
    search_fields = ['post_title']
    list_filter = ['id']


admin.site.register(Post, PostAdmin)
admin.site.register(Author, admin.ModelAdmin)
admin.site.register(Key_word, admin.ModelAdmin)

