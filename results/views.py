from django.shortcuts import render
from rest_framework import viewsets
from .serializers import billResultsSerializer
from .models import billInfo, billResults
import requests
from .bill_and_vote import billInfoResults, voteResults

import os, logging
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic import View
from rest_framework.decorators import api_view
from django.conf import settings


# This sends an automatic response with the latest Vote Results
@api_view(["GET"])
def getLatestVote(request):
    try:
        # vote = billResults.objects.filter().latest('number')
        vote = billResults.objects.filter().last()
        print(vote)
    except:
        return HttpResponse('''Not Found''', status=404)
        pass
    voteData = billResultsSerializer(vote)
    return JsonResponse(voteData.data)

# This sends an automatic response with the latest introduced Bill
@api_view(["GET"])
def getLatestBill(request):
    try:
        bill = billInfo.objects.filter().last()
    except:
        pass
    billData = billResultsSerializer(bill)
    return JsonResponse(billData.data)

# This view can retrieve a bill based on its slug
# Perfect for creating individual pages
@api_view(["GET"])
def retrieveBill(request, slug):
    try:
        print('trying')
        bill =billInfo.objects.get(slug=slug)
    except billResults.DoesNotExist:
        return JsonResponse({'message':'Bill does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        billData = billInfoSerializer(bill)
        print(billData.data)
        return JsonResponse(billData.data)

class FrontEndAppView(View):

    index = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')

    def get(self, request):
        try:
            with open(self.index) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception("what")
            return HttpResponse(
                        '''
                        wtf is going on
                        ''',
                        status=501,
                        )

# Create your views here.
Bill = billInfoResults()
Vote = voteResults()
