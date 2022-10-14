
from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

        for tag in self.tags.all():
            tag_dict, _ = Tag.objects.get_or_create(tag=str(tag))
            tag_dict.count += 1
            tag_dict.save()


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tag, allow_unicode=True)
        super().save(*args, **kwargs)
