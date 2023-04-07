import math

tau = 0.2
convergence = 0.000001

class Team:
    def __init__(self, name, initial_rating, initial_deviation=350, initial_volatility=0.06):
        self.name = name
        self.rating = initial_rating
        self.RD = initial_deviation
        self.volatility = initial_volatility

        self.mu = (self.rating-1500) / 173.7178
        self.phi = self.RD / 173.7178
    
    def updateMu(self):
        self.mu = (self.rating-1500) / 173.7178

    def updatePhi(self):
        self.phi = self.RD / 173.7178

    def setRating(self, rating):
        self.rating = rating

    def setRD(self, RD):
        self.RD = RD


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def g(phi):
    return 1/math.sqrt(1+3*phi**2/math.pi**2)

def E(mu, mu_oppo, phi_oppo):
    return 1/(1+10**(-g(phi_j)*(mu-mu_j)/400))

def v(mu, mu_oppo, phi_oppo):
    return 1/(g(phi_j)**2*E(mu, mu_j, phi_j)*(1-E(mu, mu_j, phi_j)))

def delta(mu, mu_oppo, phi_oppo, score, V):
    return V* g(phi_oppo)*(score-E(mu,mu_oppo,phi_oppo))

#Step 5 hurts my soul
def newVol(team, delta, V):
    a = math.log(team.volatility**2)
    A = a

    if(delta **2 > team.phi**2 + V):
        B = math.log(delta**2 - team.phi**2 - V)
    else:
        k = 1
        while f(a - k*tau, delta, team.phi, V) < 0:
            k += 1
        B = a - k*tau
    
    fA = f(A, delta, team.phi, V)
    fB = f(B, delta, team.phi, V)

    while abs(B-A) > convergence:
        C = A + (A-B)*fA/(fB-fA)
        fC = f(C, delta, team.phi, V)
        if fC*fB <= 0:
            A = B
            fA = fB
        else:
            fA = fA/2
        B = C
        fB = fC
    
    return math.exp(A/2)
        

def ratingUpdate(homeTeam, awayTeam, scoreDifferential):
    #positive score differential means home team won
    #negative score differential means away team won
    #score differential of 0 means draw
    if scoreDifferential > 10:
        scoreDifferential = 10
    elif scoreDifferential < -10:
        scoreDifferential = -10

    homeScore = 0.5+0.5*scoreDifferential
    awayScore = 0.5-0.5*scoreDifferential

    homeV = v(homeTeam.mu, awayTeam.mu, awayTeam.phi)
    awayV = v(awayTeam.mu, homeTeam.mu, homeTeam.phi)

    homeDelta = delta(homeTeam.mu, awayTeam.mu, awayTeam.phi, homeScore, homeV)
    awayDelta = delta(awayTeam.mu, homeTeam.mu, homeTeam.phi, awayScore, awayV)

    homeNewVol = newVol(homeTeam, homeDelta, homeV)
    awayNewVol = newVol(awayTeam, awayDelta, awayV)

    homeRateDev = sqrt(homeTeam.phi**2 + homeNewVol**2)
    awayRateDev = sqrt(awayTeam.phi**2 + awayNewVol**2)

    homePhiPrime = 1/sqrt(1/(homeRateDev**2) + 1/homeV)
    awayPhiPrime = 1/sqrt(1/(awayRateDev**2) + 1/awayV)

    homeMuPrime = homeTeam.mu + homePhiPrime**2 * g(homeTeam.phi)*homeScore-E(homeTeam.mu, awayTeam.mu, awayTeam.phi)
    awayMuPrime = awayTeam.mu + awayPhiPrime**2 * g(awayTeam.phi)*awayScore-E(awayTeam.mu, homeTeam.mu, homeTeam.phi)

    homeTeam.setRating(1500 + 173.7178*homeMuPrime)
    awayTeam.setRating(1500 + 173.7178*awayMuPrime)

    homeTeam.setRD(173.7178*homePhiPrime)
    awayTeam.setRD(173.7178*awayPhiPrime)







