from django.contrib import admin
from .models import Post2


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(Post2, PostAdmin)