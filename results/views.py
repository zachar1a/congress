from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
import requests
from .backend import results


import os, logging
from djaaango.http import HttpResponse
from django.views.generic import View
from django.conf import settings

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

def home_view(request, *args, **kwargs):
    context={
            'results':results.houseVotes(),
            'bills': results.bill(),
            }
    return render(request, "home.html", context)


