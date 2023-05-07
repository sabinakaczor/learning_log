from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Temat poznawany przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)
    public = models.BooleanField(default = False)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """Konkretne informacje o postępie w nauce"""
    topic = models.ForeignKey(Topic, models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text if len(self.text) <= 50 else self.text[:50] + '...'
