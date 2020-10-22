import requests, json, os
from .bill import billResults as br
from .bill import billInfo as bi

voteUrl = "https://api.propublica.org/congress/v1/house/votes/recent.json"
billInfoUrl = "https://api.propublica.org/congress/v1/bills/search.json"

def getRequest(u):
    return requests.get(u, headers={"x-api-key": '1OpkB3WTCfUjW4LHjOdRWaxbG1Ewa5kSrixmoPMv'})

def viewVoteResults(r):
    response = json.loads(r)
    billResults = []

    for v in response['results']['votes']:
        billResults.append(br(v['congress']
                             ,v['chamber']
                             ,v['bill']['number']
                             ,v['bill']['title']
                             ,v['democratic']['yes']
                             ,v['democratic']['no']
                             ,v['democratic']['not_voting']
                             ,v['republican']['yes']
                             ,v['republican']['no']
                             ,v['republican']['not_voting']
                             ,v['total']['yes']
                             ,v['total']['no']
                             ,v['result'],v['source']
                             ,v['bill']['latest_action']))

    return billResults

def houseVotes():
    print('house has been called')
    return viewVoteResults(getRequest(voteUrl).text)

def bill():
    print('bill has been called')
    billInfo = json.loads(getRequest(billInfoUrl).text)
    billList = []
    for b in billInfo['results'][0]['bills']:
        billList.append(bi(b['bill_id']
       ,b['bill_slug']
       ,b['number']
       ,b['title']
       ,b['sponsor_title']
       ,b['sponsor_id']
       ,b['sponsor_name']
       ,b['sponsor_state']
       ,b['sponsor_party']
       ,b['introduced_date']
       ,b['active']
       ,b['last_vote']
       ,b['house_passage']
       ,b['senate_passage']
       ,b['enacted']
       ,b['vetoed']
       ,b['primary_subject']
       ,b['summary_short']
       ,b['latest_major_action']))

    return billList

