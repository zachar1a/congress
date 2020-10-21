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
