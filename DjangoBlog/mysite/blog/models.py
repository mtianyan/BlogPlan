from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64,default="title")
    content = models.TextField(null =True)
    pub_time =models.DateTimeField(null=True)

    def __unicode__(self):
        return self.title

