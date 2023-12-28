#Once you create some kind of object in the terminal, must use .save() to actually upload created object into database

from django.db import models
from django.utils import timezone #uses default timezone settings in local machine
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #sets date_posted to whatever current time it is for the local machine posting
    # on_delete controls actions to what happens when a user gets deleted
    # models.CASCADE deletes all references to the specific author so deleting author will delete posts and everything related to author, but deleting post will not delete author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #This method allows for more descriptive descriptions to be displayed when referencing an object in terminal
    def __str__(self):
        return self.title