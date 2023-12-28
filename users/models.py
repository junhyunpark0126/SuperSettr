from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Whenever you make a new model, add a dunder method (__str__) to make finding it in the terminal easier
# Then do python manage.py makemigrations and python manage.py migrate to actually update the Django database with your newly added model
# Then add the model to the admin.py file in the same directory to make it visible in the admin page

class Profile(models.Model):
    # can access a profile by doing user.profile in terminal since OneToOne relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE) # CASCADE makes it so that deleting user will delete profile but deleting profile will not delete user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #This method allows for more descriptive descriptions to be displayed when referencing an object in terminal (dunder method)
    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    # we are overriding the save method here to automatically resize images to be 300x300 so it takes up less space
    def save(self):
        super().save()

        img = Image.open(self.image.path) # opens the image of the current instance of the profile

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # resizes the image to be 300x300
            img.save(self.image.path)
