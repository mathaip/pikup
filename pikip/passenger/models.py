from django.db import models
from driver.models import Location
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.
class Passenger(models.Model):

	name = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
	phone_number = PhoneField(null=False, blank=False, unique=True)
	profile_picture = models.ImageField(upload_to='ProfilePicture')
	current_location = models.ForeignKey('driver.Location', related_name='current_location', on_delete=models.CASCADE, null=True)
	pickup_location = models.ForeignKey('driver.Location',related_name='rider_pickup', on_delete=models.CASCADE, null =True)
	contact_info = models.CharField(max_length=50)

  
def __str__(self):
    return self.name



