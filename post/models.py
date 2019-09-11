from django.db import models
from django.urls import reverse
from django.utils.text import slugify
#from ckeditor.fields import RichTextField


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=125)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug':self.slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug':self.slug})

    def get_unique_slag(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug = unique_slug).exists():
            unique_slag = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slag()
        return super(Post,self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']

    class Comment(models.Model):
        post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
        name = models.CharField(max_length=180)
        content = models.TextField()
        created_date = models.DateTimeField(auto_now_add=True)
