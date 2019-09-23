from django.db import models


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CAT = (
    ("News", "News"),
    ("Savoir", "Savoir")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default="")
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=255, choices=CAT, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

