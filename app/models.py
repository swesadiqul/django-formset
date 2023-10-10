from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='blogs')
    categories = models.ManyToManyField('Category', related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('blog_detail', kwargs={'slug': self.slug})


class BlogImage(models.Model):
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
