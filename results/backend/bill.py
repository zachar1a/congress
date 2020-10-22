class billResults:
    def __init__(self, congress, chamber, number, title, demY, demN, demNV, repY, repN, repNV, totalY, totalN, Result, Source, action):
        self.congress = congress
        self.chamber  = chamber
        self.number   = number
        self.title    = title
        self.demY     = demY
        self.demN     = demN
        self.demNV    = demNV
        self.repY     = repY
        self.repN     = repN
        self.repNV    = repNV
        self.totalY   = totalY
        self.totalN   = totalN
        self.Result   = Result
        self.Source   = Source
        self.action   = action


# TODO 
# it is not that important imo but i took out the cosponsors
# and cosponsors by state, might want to add those in later
class billInfo:
    def __init__(self, b_id, b_slug, number, title, sponsor_title, sponsor_id, sponsor_name, sponsor_state, sponsor_party, introduced, active, last_vote, houseResult, senateResult, enacted, vetoed, subject, shortSummary, majorAction, infoUrl):
        self.b_id              = b_id
        self.b_slug            = b_slug
        self.number            = number
        self.title             = title 
        self.sponsor_title     = sponsor_title
        self.sponsor_id        = sponsor_id
        self.sponsor_name      = sponsor_name
        self.sponsor_state     = sponsor_state
        self.sponsor_party     = sponsor_party
        self.introduced        = introduced
        self.active            = active    
        self.last_vote         = last_vote
        self.houseResult       = houseResult
        self.senateResult      = senateResult
        self.enacted           = enacted
        self.vetoed            = vetoed
        # removing these since i am not using in the models
        # self.cosponsors        = cosponsors
        # self.cosponsor_by_party= cosponsor_by_party
        self.subject           = subject
        self.shortSummary      = shortSummary
        self.majorAction       = majorAction
        self.infoUrl           = infoUrl
