from django.contrib.auth import authenticate, login, logout, forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.db.models.fields import CharField, EmailField
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Auction, AuctionDetails, Bids


def index(request):
    return render(request, "auctions/index.html")


@login_required
def createListing(request):
    if request.method == ["POST"]:
        pass
