from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title    

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
     
    class Meta:
        verbose_name_plural = "Bids"
        
    def __str__(self):
        return f"{self.user.username} bid {self.bid_amount} on {self.listing.title}"    
      
class Comments(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    comment = models.TextField()
    
    class Meta:
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return f"{self.user.username} commented on {self.listing.title}"    