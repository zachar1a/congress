from django.shortcuts import render
import requests
from .backend import results

# Create your views here.

def home_view(request, *args, **kwargs):
    context={
            'results':results.houseVotes(),
            }
    return render(request, "home.html", context)


