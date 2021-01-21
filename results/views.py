from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
import requests
from .backend import results

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
        vote = billResults.objects.filter().latest('number')
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
    billData = billInfoSerializer(bill)
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
class voteResults(viewsets.ModelViewSet):
    results = results.viewVoteResults()

    for r in results:
        result = billResults(
                congress = r.congress,
                chamber = r.chamber,
                number = r.number,
                title = r.title,
                demY = r.demY,
                demN = r.demN,
                demNV = r.demNV,
                repY = r.repY,
                repN = r.repN,
                repNV = r.repNV,
                totalY = r.totalY,
                totalN = r.totalN,
                Result = r.Result,
                Source = r.Source,
                action = r.action)
        try:
            result.save()
        except:
            pass
    serializer_class = billResultsSerializer
    queryset = billResults.objects.all()

class billInfoView(viewsets.ModelViewSet):
    info = results.bill()

    for b in info:
        bill = billInfo(number = b.number,
                        title=b.title,
                        bill_id=b.b_id, 
                        slug=b.b_slug,
                        sponsor_title=b.sponsor_title,
                        sponsor_id=b.sponsor_id,
                        sponsor_name=b.sponsor_name,
                        sponsor_state=b.sponsor_state,
                        sponsor_party=b.sponsor_party,
                        introduced=b.introduced,
                        active=b.active,
                        last_vote=b.last_vote,
                        houseResult=b.houseResult,
                        senateResult=b.senateResult,
                        enacted=b.enacted,
                        vetoed=b.vetoed, 
                        subject=b.subject,
                        shortSummary=b.shortSummary,
                        major_action=b.majorAction,
                        infoUrl = b.infoUrl)
        try:
            bill.save()
        except:
            pass

    serializer_class = billInfoSerializer
    queryset = billInfo.objects.all()

