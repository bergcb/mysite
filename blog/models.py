from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """
    文章类型表
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    文章标签表
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据库表
    """

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
