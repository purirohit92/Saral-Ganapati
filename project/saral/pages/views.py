import datetime
from random import random
import string
from tokenize import Name
from urllib import request
from django.http import HttpResponse
from .urls import *
from django.db.models import Prefetch
from django.shortcuts import render,redirect
from django import forms
from django.shortcuts import get_object_or_404
# Create your views here.


def HomePage(request):
    
    return render(request, 'index.html')

def ProductDetails(request):
    
    return render (request, 'product-details.html')
    