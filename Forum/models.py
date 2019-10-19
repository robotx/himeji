from django.db import models


class Post2(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default="")
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
