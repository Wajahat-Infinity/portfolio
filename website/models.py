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


class Images(models.Model):
    homeImage = models.ImageField(upload_to='images/website', null=True, blank=True)

    def __str__(self):
        return f' Id {self.id}'


class WebsiteContent(models.Model):
    user_name = models.CharField(max_length=50)
    home_title = models.CharField(max_length=100)
    years_exp = models.CharField(max_length=20)


    def __str__(self):
        return self.user_name


class Services(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/serviceIcon', null=True, blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SocialLinks(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    tiktok = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f' Id {self.id}'
