from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    num_visits = models.IntegerField(default=0)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
