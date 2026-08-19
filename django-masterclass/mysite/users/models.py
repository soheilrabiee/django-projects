from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # Creating a 1 to 1 relationship between the profile model and the user model
    # The CASCADE makes sure that whenever an object is deleted in the user model the same profile for that object in the profile model gets deleted as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profilepic.jpg", upload_to="profile_pictures")
    location = models.CharField(max_length=100)

    # Because of the relationship between the user and profile model the data in the user model can be accessed in the profile model
    def __str__(self):
        return self.user.username
