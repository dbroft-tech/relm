from django.db import models
from django.utils import timezone
import os

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='staff/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    speaker = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.TextField()
    video_url = models.URLField(blank=True)
    audio_file = models.FileField(upload_to='sermons/', blank=True)
    scripture = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_upcoming(self):
        return self.date >= timezone.now()

class PrayerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    request = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Prayer request from {self.name}"

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"${self.amount} from {self.name}"

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='newsletters/')
    description = models.TextField(blank=True)
    date_created = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_display_name(self):
        # Get the filename without extension
        filename = os.path.basename(self.file.name)
        # Remove .pdf extension
        filename = filename.replace('.pdf', '')
        # Split by underscore and get the first part (The-Speaking-Life)
        name_part = filename.split('_')[0]
        # Replace hyphens with spaces and capitalize
        name_part = name_part.replace('-', ' ').title()
        # Get the date part
        date_str = self.date_created.strftime('%B %Y')
        return f"{name_part} - {date_str}" 