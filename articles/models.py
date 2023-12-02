from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120,null=False)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
