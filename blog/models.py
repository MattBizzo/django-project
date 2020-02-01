from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    """ Post model for blog """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # TODO: Create labels for posts.

    def publish(self):
        """ Include actual time zone and save post """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """ Returns post title for adm """
        return self.title