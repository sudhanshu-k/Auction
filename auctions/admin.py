from django.contrib import admin

# Register your models here.
from .models import Auction, AuctionDetails, Bids

class AuctionAdmin(admin.ModelAdmin):
    list_display=("id", "title", "isActive")

class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display=("id", "forAuction", "fromUser")

class BidsAdmin(admin.ModelAdmin):
    list_display=("id", "forAuction", "bider")

admin.site.register(Auction, AuctionAdmin)
admin.site.register(AuctionDetails, AuctionDetailsAdmin)
admin.site.register(Bids, BidsAdmin)