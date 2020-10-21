import requests, json, os
from bill import billResults as br

voteUrl = "https://api.propublica.org/congress/v1/house/votes/recent.json"
billInfoUrl = "https://api.propublica.org/congress/v1/bills/search.json"

def getRequest(u):
    return requests.get(u, headers={"x-api-key": '1OpkB3WTCfUjW4LHjOdRWaxbG1Ewa5kSrixmoPMv'})

def viewVoteResults(r):
    response = json.loads(r)
    billResults = []

    for v in response['results']['votes']:
        billResults.append(br(v['congress'],
                              v['chamber'],
                              v['bill']['number'],
                              v['bill']['title'],
                              v['democratic']['yes'],
                              v['democratic']['no'],
                              v['democratic']['not_voting'],
                              v['republican']['yes'],
                              v['republican']['no'],
                              v['republican']['not_voting'],
                              v['total']['yes'],
                              v['total']['no'],
                              v['result'],v['source'],
                              v['bill']['latest_action']))

    return billResults

def houseVotes():
    return viewVoteResults(getRequest(voteUrl).text)

def bill():
    billInfo = json.loads(getRequest(billInfoUrl).text)

    for b in billInfo['results'][0]['bills']:
        print(b['number'])

bill()
