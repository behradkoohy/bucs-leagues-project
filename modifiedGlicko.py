import math

tau = 0.1
convergence = 0.000001

class Team:
    def __init__(self, name, initial_rating, initial_deviation=150, initial_volatility=0.06):
        self.name = name
        self.rating = initial_rating
        self.RD = initial_deviation
        self.volatility = initial_volatility

        self.mu = (self.rating-1500) / 173.7178
        self.phi = self.RD / 173.7178
        
        if math.isnan(self.mu):
            raise Exception("Nan Mu here " + str(name) + " " +  str(initial_rating) + " " +  str(self.rating))
        if math.isnan(self.phi):
            raise Exception("Nan Phi here "+ str(name) + " " + str(initial_rating) + " " +  str(self.rating))
        
    
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
    return 1/(1+10**(-g(phi_oppo)*(mu-mu_oppo)/400))

def v(mu, mu_oppo, phi_oppo):
    return 1/(g(phi_oppo)**2*E(mu, mu_oppo, phi_oppo)*(1-E(mu, mu_oppo, phi_oppo)))

def delta(mu, mu_oppo, phi_oppo, score, V):
    return V* g(phi_oppo)*(score-E(mu,mu_oppo,phi_oppo))

def f(x, delta, phi, V, a):
    return math.exp(x)*(delta**2 - phi**2 - V - math.exp(x)) / (2*(phi**2 + V + math.exp(x))**2) - (x-a)/(tau**2)

#Step 5 hurts my soul
def newVol(team, delta, V):
    a = math.log(team.volatility**2)
    A = a

    if(delta **2 > team.phi**2 + V):
        B = math.log(delta**2 - team.phi**2 - V)
    else:
        k = 1
        while f((a - k*tau), delta, team.phi, V, a) < 0:
            k += 1
        B = a - k*tau
    
    fA = f(A, delta, team.phi, V, a)
    fB = f(B, delta, team.phi, V, a)

    while abs(B-A) > convergence:
        C = A + (A-B)*fA/(fB-fA)
        fC = f(C, delta, team.phi, V, a)
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

    homeScore = 0.5+0.05*scoreDifferential
    awayScore = 0.5-0.05*scoreDifferential

    homeTeam.updateMu()
    awayTeam.updateMu()

    homeTeam.updatePhi()
    awayTeam.updatePhi()
    
#     if math.isnan(homeTeam.mu) or math.isnan(awayTeam.mu):
#         print('here', homeTeam.mu, awayTeam.mu, homeTeam, awayTeam)

    homeV = v(homeTeam.mu, awayTeam.mu, awayTeam.phi)
    awayV = v(awayTeam.mu, homeTeam.mu, homeTeam.phi)

    homeDelta = delta(homeTeam.mu, awayTeam.mu, awayTeam.phi, homeScore, homeV)
    awayDelta = delta(awayTeam.mu, homeTeam.mu, homeTeam.phi, awayScore, awayV)

    homeNewVol = newVol(homeTeam, homeDelta, homeV)
    awayNewVol = newVol(awayTeam, awayDelta, awayV)

    homeRateDev = math.sqrt(homeTeam.phi**2 + homeNewVol**2)
    awayRateDev = math.sqrt(awayTeam.phi**2 + awayNewVol**2)

    homePhiPrime = 1/math.sqrt(1/(homeRateDev**2) + 1/homeV)
    awayPhiPrime = 1/math.sqrt(1/(awayRateDev**2) + 1/awayV)
    

    homeMuPrime = homeTeam.mu + homePhiPrime**2 * g(awayTeam.phi)*(homeScore-E(homeTeam.mu, awayTeam.mu, awayTeam.phi))
    awayMuPrime = awayTeam.mu + awayPhiPrime**2 * g(homeTeam.phi)*(awayScore-E(awayTeam.mu, homeTeam.mu, homeTeam.phi))
    
    homeTeam.setRating(1500 + 173.7178*homeMuPrime)
    awayTeam.setRating(1500 + 173.7178*awayMuPrime)

    homeTeam.setRD(173.7178*homePhiPrime)
    awayTeam.setRD(173.7178*awayPhiPrime)
    
    return (homeTeam, awayTeam)






wes = Team("Southampton", 1000)
winch = Team("Winchester", 1000)
rau = Team("RAU", 1000)
ply = Team("Plymouth", 1000)
The4s = Team("4s", 1000)

WesRating = []
WinchRating = []
RauRating = []
PlyRating = []
The4sRating = []

ratingUpdate(winch, ply, 3)
WinchRating.append(winch.rating)
PlyRating.append(ply.rating)

ratingUpdate(wes, The4s, 5)
WesRating.append(wes.rating)
The4sRating.append(The4s.rating)

ratingUpdate(rau, winch, 1)
RauRating.append(rau.rating)
WinchRating.append(winch.rating)

ratingUpdate(wes, ply, 4)
WesRating.append(wes.rating)
PlyRating.append(ply.rating)

ratingUpdate(winch, wes, -1)
WinchRating.append(winch.rating)
WesRating.append(wes.rating)

ratingUpdate(rau, The4s, 8)
RauRating.append(rau.rating)
The4sRating.append(The4s.rating)

ratingUpdate(The4s, ply, -2)
The4sRating.append(The4s.rating)
PlyRating.append(ply.rating)

ratingUpdate(rau, wes, -1)
RauRating.append(rau.rating)
WesRating.append(wes.rating)

ratingUpdate(The4s, rau, 5)
The4sRating.append(The4s.rating)
RauRating.append(rau.rating)

ratingUpdate(wes, winch, 3)
WesRating.append(wes.rating)
WinchRating.append(winch.rating)

ratingUpdate(ply, rau, 7)
PlyRating.append(ply.rating)
RauRating.append(rau.rating)

ratingUpdate(The4s, wes, -1)
The4sRating.append(The4s.rating)
WesRating.append(wes.rating)

ratingUpdate(ply, The4s, 2)
PlyRating.append(ply.rating)
The4sRating.append(The4s.rating)

ratingUpdate(The4s, winch, -3)
The4sRating.append(The4s.rating)
WinchRating.append(winch.rating)

ratingUpdate(ply, wes, -4)
PlyRating.append(ply.rating)
WesRating.append(wes.rating)

ratingUpdate(winch, The4s, 0)
WinchRating.append(winch.rating)
The4sRating.append(The4s.rating)

ratingUpdate(rau, ply, -4)
RauRating.append(rau.rating)
PlyRating.append(ply.rating)

ratingUpdate(winch, rau, 5)
WinchRating.append(winch.rating)
RauRating.append(rau.rating)

ratingUpdate(wes, rau, 5)
WesRating.append(wes.rating)
RauRating.append(rau.rating)

ratingUpdate(ply, winch, 5)
PlyRating.append(ply.rating)
WinchRating.append(winch.rating)

print(WesRating)
print(WinchRating)
print(RauRating)
print(PlyRating)
print(The4sRating)

#print(wes.rating, ' ', wes.RD)
#print(winch.rating, ' ', winch.RD)
#print(rau.rating, ' ', rau.RD)
#print(ply.rating, ' ', ply.RD)
#print(The4s.rating, ' ', The4s.RD)




