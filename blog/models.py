from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify 

User = get_user_model()

STATUS = ((0, 'Draft'), (1, 'Publish'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
