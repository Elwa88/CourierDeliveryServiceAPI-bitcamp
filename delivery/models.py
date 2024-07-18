from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    choices = [
        ('courier','Courier'),
        ('customer','Customer'),
        ('admin','Admin'),
    ]
    role = models.CharField(max_length=10, choices=choices)

class Parcel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank= True)
    choices =[
        ('pending','Pending'),
        ('in_Transit','In Transit'),
        ('delivered','Delivered'),
    ]
    status = models.CharField(max_length=10, choices=choices)
    sender = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    receiver_name = models.CharField(max_length=100)
    receiver_adress = models.TextField()
    courier = models.ForeignKey(CustomUser,on_delete=models.CASCADE,
                                related_name='courier_parcels', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True)

class DeliveryProof(models.Model):
    parcel = models.OneToOneField(Parcel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='delivery_proof_images/')
    timestamp = models.DateTimeField(auto_now_add=True)
