from django.contrib import admin

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)