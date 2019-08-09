from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

from .fields import ThumbnailImageField
from hitcount.models import HitCountMixin



class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))



class Photo(models.Model, HitCountMixin):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    video_link = models.URLField('Youtube Link', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
