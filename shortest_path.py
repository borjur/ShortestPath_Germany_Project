'''
Created on March 20, 2013

@author: Boris Jurosevic
         Trip through Germany
         CS 2430
         
'''
from __future__ import print_function
import heapq
from data_manager import Data_Manager
from collections import defaultdict
import math
import random

# our main algorithm for testing
def algo_2(pocetak, kraj):
    ad = Data_Manager()
    z = ad.dajMiGradove()
    D = {}
    P = {}
    lock = {}
    open = {}
    for gradovi in z:
        D[gradovi] = float('inf')
        P[gradovi] = ""
        
    D[pocetak] = 0
    r = z
    
    while len(r) > 0:
        Q = None
        GRAD = ''
        for SVEU in r:
            if Q == None:
                l = D[SVEU]
                Q = l
                GRAD = SVEU
            elif D[SVEU] < Q:
                p = D[SVEU]
                Q = p
                GRAD = SVEU
        r.remove(GRAD)
        removITALL = GRAD
        W = ad.dajMiSpoj(removITALL)

        for allIN in W:
            
            if allIN[1] == GRAD:
                intthFirstSpot = allIN[2]
                inttheLastSpot = allIN[0]
                xy = GRAD
                all = D[xy] + inttheLastSpot
                if D[intthFirstSpot] == float('inf'):
                    D[intthFirstSpot] = all
                    P[intthFirstSpot] = xy
                elif D[intthFirstSpot] > all:
                    D[intthFirstSpot] = all
                    P[intthFirstSpot] = xy
                    
    to = []
    m = kraj
    while m != pocetak:
        if to.count(m) == 0:
            veliko = m 
            to.insert(0, veliko)
            node = P[veliko]
        else:
            break
        veratiTOALL = pocetak
        
    to.insert(0, pocetak)
    return (D[kraj], to)
# our starter as a path
def pocniOdArray( puteljak ):
    infromacija = Data_Manager()
    papir = list
    a = defaultdict( papir )
    value = 0   
    abc = infromacija.pocetakSav()
    
    for point in abc:
        myArray = 0
        presliSve = []
        putic = []
        thisPint = point
        presliSve.append(thisPint)
        alpha = point
        spoj = infromacija.dajMiSpoj(point)
        
        heapq.heapify(spoj)
        while spoj:
            alphaAll = 0
            getInfo = spoj
            kolikoJeSkupo, PartOne, PartTwo = heapq.heappop(getInfo)
            if PartTwo not in presliSve:
                getAllofInfo = PartTwo
                presliSve.append(getAllofInfo)
                all_Together = (PartOne, PartTwo, kolikoJeSkupo)
                putic.append(all_Together)
                
                putItBackIn = PartTwo
        
                for all in infromacija.dajMiSpoj(putItBackIn):
                    abc = spoj
                    
                    heapq.heappush(abc, all)
                    alphaTo = putic
        puteljak.append(alphaTo)
    
    put_1 = []
    put_2 = []
    put_3 = []
    for all in puteljak:
        put_1.append(nacrtajSvePuteve(all))
    return put_1
   

# make them appear 
# come back to this  
def nacrtajSvePuteve(poruka):
    prije = (-1,-1,-1) 
    sviBrojevi = 0
    PUT = []
    PUT.append([])
    
    for xyz in poruka:
        Part_1 = xyz[0]
        Part_2 = prije[1]
   
        if Part_1 != Part_2 and Part_2 != -1:
            sviBrojevi = sviBrojevi + 1
            PUT.append([])
        prije = xyz
        connect = sviBrojevi
        protocol = xyz
        PUT[connect].append(protocol)
        
        last = PUT

    return spojiSvePuteve(last)

# this is where we have them all together
#test it one more time       
def spojiSvePuteve(nastavi):
    begin = None
    pocni = 0
    kadSeSveZavrsi = nastavi.pop(pocni)
    while nastavi:
        
        begin = len(kadSeSveZavrsi)
        end = kadSeSveZavrsi[begin -1][1]
        dobarPocetak = end
        k = None
        aTob = None
        for later in nastavi:
            
            if k != None:
                
                thisTime = dobarPocetak
                thisLast = later[0][0]
                y = algo(thisTime, thisLast)
                
                if y[0] < k[0]:
                    k = y
                    aTob = later
            else:
                together = dobarPocetak
                allLater = later[0][0]
                k = algo(together, allLater)
                aTob = later
        if k[0] > 0:
            pointA = k[1][0]
            pintB = k[1][len(k[1])-1]
            pintC = k[0]
          
            kadSeSveZavrsi.append((pointA, pintB, pintC))        
        kadSeSveZavrsi = kadSeSveZavrsi + aTob
        pointToIt = aTob
        nastavi.remove(pointToIt)
        afterAll = len(kadSeSveZavrsi)
        pointerr = kadSeSveZavrsi[afterAll - 1][1]
    end = krajSviPuteva(pointerr)
    kadSeSveZavrsi.append(end)
    return kadSeSveZavrsi

# this is gonna be the last route
# looks ok for now
def krajSviPuteva(x):
    
    a = (float('inf'), 0)
    b = Data_Manager()
    end = b.pocetakSav()
    for allOfIt in end:
        putvi = x
        putvi_2 = allOfIt
        STAZA = algo(putvi, putvi_2)
        if STAZA[0] < a[0]:
            a = STAZA
    mesto = a[0]
    STAZA = a[1]
    prosto_A = STAZA[0]
    prosto_B = len(STAZA) - 1
    allToged = mesto
    return (prosto_A, STAZA[prosto_B], allToged)

    
# out main method for ways
def algo(pocetak, kraj):
    ad = Data_Manager()
    z = ad.dajMiGradove()
    D = {}
    P = {}
    lock = {}
    open = {}
    for gradovi in z:
        D[gradovi] = float('inf')
        P[gradovi] = ""
        
    D[pocetak] = 0
    r = z
    
    while len(r) > 0:
        Q = None
        GRAD = ''
        for SVEU in r:
            if Q == None:
                l = D[SVEU]
                Q = l
                GRAD = SVEU
            elif D[SVEU] < Q:
                p = D[SVEU]
                Q = p
                GRAD = SVEU
        r.remove(GRAD)
        removITALL = GRAD
        W = ad.dajMiSpoj(removITALL)

        for allIN in W:
            
            if allIN[1] == GRAD:
                intthFirstSpot = allIN[2]
                inttheLastSpot = allIN[0]
                xy = GRAD
                all = D[xy] + inttheLastSpot
                if D[intthFirstSpot] == float('inf'):
                    D[intthFirstSpot] = all
                    P[intthFirstSpot] = xy
                elif D[intthFirstSpot] > all:
                    D[intthFirstSpot] = all
                    P[intthFirstSpot] = xy
                    
    to = []
    m = kraj
    while m != pocetak:
        if to.count(m) == 0:
            veliko = m 
            to.insert(0, veliko)
            node = P[veliko]
        else:
            break
        veratiTOALL = pocetak
        
    to.insert(0, pocetak)
    return (D[kraj], to)
# this is our tester method
def spojiSvePuteve_2(nastavi):
    begin = None
    pocni = 0
    kadSeSveZavrsi = nastavi.pop(pocni)
    while nastavi:
        
        begin = len(kadSeSveZavrsi)
        end = kadSeSveZavrsi[begin -1][1]
        dobarPocetak = end
        k = None
        aTob = None
        for later in nastavi:
            
            if k != None:
                
                thisTime = dobarPocetak
                thisLast = later[0][0]
                y = algo(thisTime, thisLast)
                
                if y[0] < k[0]:
                    k = y
                    aTob = later
            else:
                together = dobarPocetak
                allLater = later[0][0]
                k = algo(together, allLater)
                aTob = later
        if k[0] > 0:
            pointA = k[1][0]
            pintB = k[1][len(k[1])-1]
            pintC = k[0]
          
            kadSeSveZavrsi.append((pointA, pintB, pintC))        
        kadSeSveZavrsi = kadSeSveZavrsi + aTob
        pointToIt = aTob
        nastavi.remove(pointToIt)
        afterAll = len(kadSeSveZavrsi)
        pointerr = kadSeSveZavrsi[afterAll - 1][1]
    end = krajSviPuteva(pointerr)
    kadSeSveZavrsi.append(end)
    return kadSeSveZavrsi
