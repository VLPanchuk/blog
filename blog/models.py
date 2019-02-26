from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    # every post assigned to auth user
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now )
    published_date = models.DateTimeField(blank=True, null=True)

    #method for publishing post and save the date of publishing
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #display only approved comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #get post by private key
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    #define representation in admin part
    def __str__(self):
        return self.title


class Comment(models.Model):
    # every comment assigned to post
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #when comment just created its not approved

    #approving method
    def approve(self):
        self.approved_comment = True
        self.save()

    #define absolute url
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
