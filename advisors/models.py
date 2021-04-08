from django.db import models
from authentication.models import User
from PIL import Image

# Create your models here.
class Advisor(models.Model):
    name = models.CharField(max_length=64)
    profile_pic=models.ImageField(default='default.jpg',upload_to='profile_pics')
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookings') 
    booking_time=models.DateTimeField()
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

