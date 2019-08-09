from django.db import models

from django.urls import reverse

# Create your models here.
class Produce(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Upload Date', auto_now_add = True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True,)

    def __str__(self):
    	return self.title

    class Meta:
        ordering = ['-pub_date']

class ApplyForm(models.Model):
    produce = models.ForeignKey('Produce', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length = 100)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    video_link = models.URLField('Youtube Link', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']