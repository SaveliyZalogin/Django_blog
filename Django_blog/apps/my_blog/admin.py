from django.contrib import admin
from Django_blog.apps.my_blog.models import Post
from Django_blog.apps.my_blog.models import Key_word


admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Key_word, admin.ModelAdmin)

