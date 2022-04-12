from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db.models import CharField, IntegerField, TextField, DateTimeField, BooleanField, ForeignKey, ImageField, Model
from users.models import User

#id, password, username, first-last name, email, auctions, bids, comments

# Title, date, listedBy, isActive, bids, image, fromuser
class Auction(Model):
    title=CharField(max_length=128)
    detail=TextField(blank=True)
    price=IntegerField()
    dateListed=DateTimeField(default=timezone.now)
    isActive=BooleanField(default=True)
    image=ImageField(upload_to='media/auctionImages')
    startPrice=IntegerField(default=0)
    fromUser=ForeignKey(User, on_delete=CASCADE, related_name="auctions")

    def __str__(self):
        return f"Title: {self.title.capitalize()}, Active: {self.isActive}"

# FOr which auction, value, time, bider
class Bids(Model):
    price=IntegerField()
    timePlaced=DateTimeField(auto_now_add=True)
    forAuction=ForeignKey(Auction, on_delete=CASCADE, related_name="placedBids")
    bider=ForeignKey(User, on_delete=CASCADE, related_name="bids")

    def __str__(self):
        auction=self.forAuction
        print(auction.fromUser.get_full_name())
        return f"For Auction: {auction.title}, Bid Value: {self.price}"

#review, startBid, details
class AuctionDetails(Model):
    text_data=TextField()
    forAuction=ForeignKey(Auction, on_delete=CASCADE, related_name="comments")
    fromUser=ForeignKey(User, on_delete=CASCADE, related_name="comments")

    def __str__(self):
        return f"For Auction: {self.forAuction}, For User: {self.fromUser}"