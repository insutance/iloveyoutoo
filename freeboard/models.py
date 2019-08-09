from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.
class Freeboard(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Upload Date', auto_now_add = True)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
    		return self.title

    def get_absolute_url(self):
        return reverse('freeboard:freeboard_detail', args=(self.id,))

    class Meta:
        ordering = ['-pub_date']

    def title_summary(self):
        return self.title[:40]