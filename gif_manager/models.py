from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=256, blank=False)
    latest_post = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=256)

    def __str__(self):
        return self.tag


class Gif(models.Model):
    blog = models.ForeignKey(Blog)
    tag = models.ManyToManyField(Tag)
    url = models.URLField()

    def __str__(self):
        return self.url