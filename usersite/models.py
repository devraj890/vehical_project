from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
User =settings.AUTH_USER_MODEL
class Complaint(models.Model):
    complain_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    vehicle_make = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.IntegerField()
    licence_plate = models.CharField(max_length=20)
    description = models.TextField()
    complain_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_of_theft = models.DateField()
    time_of_theft = models.TimeField()
    location_last_seen = models.CharField(max_length=200)
    rc_no = models.CharField(max_length=50)
    old_vehicle_shell = models.TextField(blank=True)
    is_found = models.BooleanField(default=False)
    def str(self):
        return f"({self.city}, {self.vehicle_make}, {self.vehicle_model})"
class feedback(models.Model):
    feedbak_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    def str(self):
        return self.user 
class officer(models.Model):
    off_name= models.CharField(max_length=50)
    off_post= models.CharField(max_length=50)
    off_desc= models.TextField()
    off_img = models.ImageField(upload_to='image/',default="")
    def str(self):
        return self.off_name