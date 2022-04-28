from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class DiscussionGroup(models.Model):
    #creater = models.ForeignKey(User, on_delete=models.CASCADE)
    creater = UserForeignKey(auto_user_add=True)
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)

    def __str__(self): 
        return self.name

class Message(models.Model):
    sender = UserForeignKey(auto_user_add=True)
    group = models.ForeignKey(DiscussionGroup, on_delete=models.CASCADE, related_name="message")
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message