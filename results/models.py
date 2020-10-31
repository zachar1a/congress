from django.db import models

# Create your models here.

class billResults(models.Model):
    congress =models.CharField(max_length=10, default=None,null=True)
    chamber  =models.CharField(max_length=10, default=None,null=True)
    number   =models.CharField(unique=True, max_length=10, default=None,null=True)
    title    =models.CharField(unique=True, max_length=300, default=None,null=True)
    demY     =models.IntegerField(default=None, null=True)
    demN     =models.IntegerField(default=None, null=True)
    demNV    =models.IntegerField(default=None, null=True)
    repY     =models.IntegerField(default=None, null=True)
    repN     =models.IntegerField(default=None, null=True)
    repNV    =models.IntegerField(default=None, null=True)
    totalY   =models.IntegerField(default=None, null=True)
    totalN   =models.IntegerField(default=None, null=True)
    Result   =models.CharField(max_length=30, default=None,null=True)
    Source   =models.CharField(max_length=300, default=None,null=True)
    action   =models.CharField(max_length=200, default=None,null=True)



class billInfo(models.Model):
    bill_id             =models.CharField(unique=True, max_length=10, default=None)
    slug                =models.CharField(unique=True, max_length=10, default=None)
    number              =models.CharField(max_length=10, default=None,null=True)
    title               =models.CharField(max_length=200, default=None,null=True)
    sponsor_title       =models.CharField(max_length=10, default=None,null=True)
    sponsor_id          =models.CharField(max_length=10, default=None,null=True)
    sponsor_name        =models.CharField(max_length=50, default=None,null=True)
    sponsor_state       =models.CharField(max_length=70, default=None,null=True)
    sponsor_party       =models.CharField(max_length=20, default=None,null=True)
    introduced          =models.CharField(max_length=10, default=None,null=True)
    active              =models.CharField(max_length=10, default=None,null=True)
    last_vote           =models.CharField(max_length=10, default=None,null=True)
    houseResult         =models.CharField(max_length=10, default=None,null=True)
    senateResult        =models.CharField(max_length=10, default=None,null=True)
    enacted             =models.CharField(max_length=10, default=None,null=True)
    vetoed              =models.CharField(max_length=10, default=None,null=True)
    # These will habe to be placed in later
    # cosponsors          =models.CharField(max_length=10, default=None,null=True)
    # cosponsors_by_party =models.CharField(max_length=10, default=None,null=True)
    subject             =models.CharField(max_length=100, default=None,null=True)
    shortSummary        =models.CharField(max_length=2000, default=None,null=True)
    major_action        =models.CharField(max_length=200, default=None,null=True)
    infoUrl             =models.CharField(max_length=250, default=None,null=True)

