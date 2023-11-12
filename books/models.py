from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    profileImage = models.ImageField(default='avatar.png', upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
 

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True, null=True, blank=True)
    iamge = models.ImageField(upload_to="books/", blank=True, null=True)
    
    def __str__(self):
        return self.title
