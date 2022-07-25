from .backend import results
from .models import billInfo, billResults
from .serializers import billInfoSerializer, billResultsSerializer
from rest_framework import viewsets

class billInfoResults(viewsets.ModelViewSet):
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
