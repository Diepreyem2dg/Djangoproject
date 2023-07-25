from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    class TaskTypes(models.TextChoices):
        HOME = 'HOME', 'Home'
        WORK = 'WORK', 'Work'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=256, choices=TaskTypes.choices, default=TaskTypes.HOME)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
