from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id':self.id})
        # return "/post/{}".format(self.id)
