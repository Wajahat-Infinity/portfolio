from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True, help_text='Images for Testing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', null=True, blank=True, help_text='Images for Testing')
    description = models.CharField(max_length=500)
    detail_description = models.CharField(max_length=500)
    client = models.CharField(max_length=50)
    date = models.DateField(null=True)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
