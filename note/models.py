from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from bs4 import BeautifulSoup

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    time_updated = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.time_updated = datetime.now()
        super(Note, self).save(*args, **kwargs)

    def content_str(self):
        soup = BeautifulSoup(self.content[:200], "html.parser")
        return soup.get_text()

    class Meta:
        ordering = ['-time_updated']
