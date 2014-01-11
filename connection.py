'''
Created on March 20, 2013

@author: Boris Jurosevic
         Trip through Germany
         CS 2430
         
'''
from __future__ import print_function

class Connection(object):
    '''
    classdocs
    '''

    # this is our constructor for get everything from
    def __init__(self, gradJedan, gradDva, CjenaVoza, CjenaDizela,CjenaP, VrijemeVoza, vrijemeAuta, range):
        '''
        Constructor
        '''
        self.gradJedan = gradJedan
        self.gradDva = gradDva
        self.CjenaVoza = CjenaVoza
        self.CjenaDizela = CjenaDizela
        self.CjenaP = CjenaP
        self.VrijemeVoza = VrijemeVoza
        self.vrijemeAuta = vrijemeAuta
        self.range = range
        #our if statement of all the choices
        # come back to this 
        # we will make it more clear
    def sveTezine(self):
        voz = self.kolikoJeVozTezak()
        gas = self.kolikoJePTezak()
        ds = self.kolikoJeDTezak()
        if gas < ds:
            if voz < gas and voz > 0:
                aScenario = self.range, "Train", self.CjenaVoza, self.timeByTrain
                return aScenario
            else:
                bScenario = self.range, "Petrol", 230 + self.CjenaP, self.vrijemeAuta
                return bScenario
        else:
            if voz < ds and voz > 0:
                cScenario = self.range, "Train", self.CjenaVoza, self.timeByTrain
                return cScenario
            else:
                dScenario = self.range, "Diesel", 230 + self.CjenaDizela, self.vrijemeAuta
                return dScenario
        #method two
        #come back to this
        def sveTezine2(self):
            voz = self.kolikoJeVozTezak()
        gas = self.kolikoJePTezak()
        ds = self.kolikoJeDTezak()
        if gas == ds:
            return gas

    #this is for everything
    def kolikoJeSveTesko(self):
        tesko = 0
        teskoJe = self.range
        return teskoJe
    #case 1 how much its heavy
    def kolikoJeVozTezak(self):
        tesko = 0
        teskoJe = (self.CjenaVoza + 2 * self.CjenaVoza) / 2
        return teskoJe
       
    #case2 how much its heavy
    def kolikoJePTezak(self):
        tesko = 0
        teskoJe = ( 230 + self.CjenaP + 2 * self.vrijemeAuta) / 2
        return teskoJe
        
    #case three how much its heavy
    def kolikoJeDTezak(self):
        tesko = 0
        teskoJe = (230 + self.CjenaDizela + 2 * self.vrijemeAuta) / 2
        return teskoJe
        
    #put them all out on a string
    def __str__(self):
        a = 0
        
        return str.format("gradJedan: {0} gradDva: {1}", self.gradJedan, self.gradDva)
    
    def __lt__(self, a):
        vracaj = self.ranges < a.range
        return vracaj
    
    def __gt__(self, a):
        daj = self.range > a.range
        return daj
    
    def __eq__(self, a):
        daj = 0
        vracaj = 0
        if a == None:
            return False
        if not a is Connection:
            return False
        ranger = self.range == a.range
        return ranger
    
    def convertThemAll(self):
        sve = self.gradJedan
        return sve

    
    
    # all of our scenarios together
    def __hash__(self):
        aScenario = self.gradJedan
        bScenario = self.gradDva
        cScenario = self.opt_weight()
        dScenario = self.costByTrain
        eScenario = self.CjenaP
        fScenario = self.CjenaDizela
        gScenario = self.range
        return int(aScenario * 7 + bScenario * 13 + cScenario * 39 + dScenario * 43 + eScenario * 23 + fScenario * 11 + gScenario * 113)
    
    