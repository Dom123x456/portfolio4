from django.shortcuts import render
from django.views.generic import ListViews
from .models import Table, RestaurantBooking
# Create your views here.

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()