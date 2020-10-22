from rest_framework import serializers
from .models import billInfo, billResults

class billInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = billInfo
        fields = ( 
         'bill_id'
        ,'slug'
        ,'number'
        ,'title'
        ,'sponsor_title'
        ,'sponsor_id'
        ,'sponsor_name'
        ,'sponsor_state'
        ,'sponsor_party'
        ,'introduced'
        ,'active'
        ,'last_vote'
        ,'houseResult'
        ,'senateResult'
        ,'enacted'
        ,'vetoed'
        ,'subject'
        ,'shortSummary'
        ,'major_action')
         
class billResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = billResults
        fields=(
        'congress'
        ,'chamber'
        ,'number'
        ,'title'
        ,'demY'
        ,'demN'
        ,'demNV'
        ,'repY'
        ,'repN'
        ,'repNV'
        ,'totalY'
        ,'totalN'
        ,'Result'
        ,'Source'
        ,'action')
