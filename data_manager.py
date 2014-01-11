'''
Created on March 20, 2013

@author: Boris Jurosevic
         Trip through Germany
         CS 2430
         
'''
from __future__ import print_function
import sqlite3
from city import City
from connection import Connection
import decimal
import random
import math

class Data_Manager(object):
    '''
    classdocs
    '''

    #here we have our constructor
    def __init__(self):
        '''
        Constructor
        '''
        self._cities = self.pokaziAbecedu()
    # come back to fix the final bugs
    #remember to fix the array
    def dajmigradpoGrad_2(self, kvaka):
        spoj = sqlite3.connect("GermanyGraph.db")
        a = spoj.cursor()
        input = "Select * From Cities Where Key == ?"
        
        a.execute(input, [(kvaka)])
        pokazi = a.fetchall()
        spota = pokazi[0][1]
        spotb = pokazi[0][2]
        spotc =  pokazi[0][3]
        spotd = pokazi[0][4]
        spote = pokazi[0][0]
        return City(spota, spotb, spotc, spotd, spote)
    #showing of our abc aplhabet   
    # bring it back
    def pokaziAbecedu(self):
        inputTwo = 0
        pokizaAbecedu = {}        
        sproj = sqlite3.connect("GermanyGraph.db")
        pocetak = sproj.cursor()
        input = "Select Key, Name From Cities"
        pocetak.execute(input)
        dajmiSveInformacije = pocetak.fetchall()
        
        for ranger in dajmiSveInformacije:
            acd = ranger[0]
            acde = ranger[1]
            pokizaAbecedu[acd] = acde
        return pokizaAbecedu

    #all when it comes to information   
    #show the database
    def pokaziInformacije(self):
        spojiSveto = sqlite3.connect("GermanyGraph.db")
        a = spojiSveto.cursor()
        print("----------CITY TABLE----------")
        self.pokazisveGradove(a)
        print()
        print("-------CONNECTION TABLE-------")
        self.pokaziSveSpojeve(a)

    # were working with all the data here back and fourth
    #check it one more time
    def pokaziSveSpojeve(self, a):
        spojitoSve = "Select * From Connections"
        start = spojitoSve
        a.execute(start)
        dajMiInformacije = a.fetchall()
        
        worda = "City 0"
        wordb = "City 1"
        wordc = "Cost By Train"
        wordd = "Cost By Diesel"
        worde = "Cost By Petrol"
        wordf = "Time By Train"
        wordg = "Time By Car"
        wordh = "Distance"
        print("%7s %7s %15s %15s %15s %15s %15s %15s" % (worda, wordb, wordc, wordd, worde, wordf, wordg, wordh ))
        


        for value in dajMiInformacije:
            viewa = value[1]
            viewb = value[2]
            viewc = value[3]
            viewd = value[4]
            viewe = value[5]
            viewf = value[6]
            viewg = value[7]
            viewh = value[8]
            

            print("%7d %7s %15.2f %15.2f %15.2f %15.2f %15.2f %15.2f" % (viewa, viewb, viewc, viewd, viewe,viewf, viewg, viewh))
    # make sure to have a tester    
    def pokazisveGradove(self, a):
        input = "Select * From Cities"
        a.execute(input)
        informacija = a.fetchall()
        slovo_1 = "Key"
        slovo_2 = "City"
        slovo_3 = "Start"
        slovo_4 = "Extra Cost"
        slovo_5 = "Extra Time"
        print("%-5s %-15s %-10s %10s %12s" % (slovo_1, slovo_2, slovo_3, slovo_4, slovo_5 ))
        for ranger in informacija:
            
            mestoa = ranger[1]
            mestob = ranger[2]
            mestoc = ranger[3]
            mestod = ranger[0]
            mestoe = ranger[4]
            print("%-5d %-15s %-10d %10.2f %12d" % (mestoa, mestob, mestoc, mestod, mestoe))
    #fixed bugs
    # final method
    def dajMiGradove(self):
        abcd = 0
        spojisev = sqlite3.connect("GermanyGraph.db")
        a = spojisev.cursor()
        input = "Select Key From Cities"
        a.execute(input)
        informacija = a.fetchall()
        sela = []
        for ranger in informacija:
            abc = ranger[0]
            sela.append(abc)
        return sela
    # all the germany together
    def dajmigradpoGrad(self, kvaka):
        spoj = sqlite3.connect("GermanyGraph.db")
        a = spoj.cursor()
        input = "Select * From Cities Where Key == ?"
        
        a.execute(input, [(kvaka)])
        pokazi = a.fetchall()
        spota = pokazi[0][1]
        spotb = pokazi[0][2]
        spotc =  pokazi[0][3]
        spotd = pokazi[0][4]
        spote = pokazi[0][0]
        return City(spota, spotb, spotc, spotd, spote)
    # tester is fixed
    # dont touch it
    def nadjiSpojeve(self, gradJedan, gradDva):
        spoj = sqlite3.connect("GermanyGraph.db")
        a = spoj.cursor()
        inpur = """
            Select * From Connections 
            Where (City0 == ? and City1 == ?)
            or (City1 == ? and city0 == ?)
            """
        spojiOne = gradJedan
        spojiTwo = gradDva
        
            
             
        a.execute(inpur, (spojiOne, spojiTwo, spojiOne, spojiTwo))
        informacija = a.fetchall()
        if len(informacija) > 0:
            casea = informacija[0][1]
            caseb = informacija[0][2]
            casec = informacija[0][3]
            cased = informacija[0][4]
            casee = informacija[0][5]
            casef = informacija[0][6]
            caseg = informacija[0][7]
            casei = informacija[0][8]
            return Connection(casea, caseb, casec, cased, casee, casef, caseg, casei)
        else:
            return None
    
    def nadjiSpojeve_2(self, gradJedan, gradDva):
        spoj = sqlite3.connect("GermanyGraph.db")
        a = spoj.cursor()
        inpur = """
            Select * From Connections 
            Where (City0 == ? and City1 == ?)
            or (City1 == ? and city0 == ?)
            """
        spojiOne = gradJedan
        spojiTwo = gradDva
        
            
             
        a.execute(inpur, (spojiOne, spojiTwo, spojiOne, spojiTwo))
        informacija = a.fetchall()
        if len(informacija) > 0:
            casea = informacija[0][1]
            caseb = informacija[0][2]
            casec = informacija[0][3]
            cased = informacija[0][4]
            casee = informacija[0][5]
            casef = informacija[0][6]
            caseg = informacija[0][7]
            casei = informacija[0][8]
            return Connection(casea, caseb, casec, cased, casee, casef, caseg, casei)
        else:
            return None        
    def pocetakSav(self):
        sastavi = sqlite3.connect("GermanyGraph.db")
        pocetak = sastavi.cursor()
        sta = "Select Key From Cities Where Start == '1'"
        pocetak.execute(sta)
        informacija = pocetak.fetchall()
        myArray = []
        for x in informacija:
            myArray.append(x[0])
        return myArray
    #methods for testing , come back to this 
    def napuniSpoj_2(self, a):
        sprojiSveZajedno = sqlite3.connect("GermanyGraph.db")
        for spoj in range(32, len(a)):
            sveoDizelu = self.diesel(a[spoj][1])
            spojiMojeSve = sveoDizelu
            PartOne = spojiMojeSve
            arrayOne = 0
            arrayDataBase = """
            UPDATE Connections
            SET CostByDiesel = ?
            WHERE Key = ?
            """
            togetherrr = arrayDataBase
            togetherrrTwo = (PartOne, spoj+1)
            sprojiSveZajedno.execute(togetherrr, togetherrrTwo)
            sveOPatrolu = self.petrol(a[spoj][1])
            spojiMojeSveDva = sveOPatrolu
            PartTwo = spojiMojeSveDva
            array = 0
            arrayDataBase = """
            UPDATE Connections
            SET CostByPetrol = ?
            WHERE Key = ?
            """
            togetherrAll = arrayDataBase
            togetherrAllTwo = (PartTwo, spoj+1)
            sprojiSveZajedno.execute(togetherrAll, togetherrAllTwo)
            sveOzajedno = self.time(a[spoj][1])
            spojiMojeSveTri = sveOzajedno
            vrijeme = spojiMojeSveTri
            arrayDataBase = """
            UPDATE Connections
            SET TimeByCar = ?
            WHERE Key = ?
            """
            togetherAll = (vrijeme, spoj+1)
            togetherAllTwo = arrayDataBase 
            sprojiSveZajedno.execute(togetherAllTwo, togetherAll)
        sprojiSveZajedno.commit()
    #final method
    # works fine       
    def dajMiSpoj(self, grad):
        spoji = sqlite3.connect("GermanyGraph.db")
        pocetak = spoji.cursor()
        getitFrom = "Select * From Connections Where City0 == ? or City1 == ?"
        takeItOut = getitFrom
        connectThemBoth = (grad, grad)
        pocetak.execute(takeItOut, connectThemBoth)
        informacija = pocetak.fetchall()
        informacija = self.prebaciSpoj(informacija)
        return informacija
    # connection method
    def prebaciSpoj(self, spoji):
        myArray = []
        for ranger in spoji:
            spotA = ranger[1]
            spotB = ranger[2]
            spotC = ranger[3]
            spotD = ranger[4]
            spotE = ranger[5]
            spotF = ranger[6]
            spotG = ranger[7]
            spotI = ranger[8]
            sviSpot = spotA, spotB, spotC, spotD, spotE, spotF, spotG, spotI
            connect = Connection(spotA, spotB, spotC, spotD, spotE, spotF, spotG, spotI)
            teskoJE = connect.kolikoJeSveTesko()
            x = teskoJE
            y = connect.gradJedan
            z = connect.gradDva

            myArray.append((x, y, z))
            myArray.append((x, z, y))
        return myArray      
    # here we have a input 
    def dajMiPut(self):
        spoj = sqlite3.connect("GermanyGraph.db")
        pocetak = spoj.cursor()
        input = "Select Key, Distance From Connections"
        pocetak.execute(input)
        informacije = pocetak.fetchall()
        putItIn = []
        for ranger in informacije:
            where = (ranger[0], ranger[1])
            putItIn.append(where)
        self.load_data(putItIn)
    #second method of putting it together            
    def napuniSpoj(self, a):
        sprojiSveZajedno = sqlite3.connect("GermanyGraph.db")
        for spoj in range(32, len(a)):
            sveoDizelu = self.diesel(a[spoj][1])
            spojiMojeSve = sveoDizelu
            PartOne = spojiMojeSve
            arrayOne = 0
            arrayDataBase = """
            UPDATE Connections
            SET CostByDiesel = ?
            WHERE Key = ?
            """
            togetherrr = arrayDataBase
            togetherrrTwo = (PartOne, spoj+1)
            sprojiSveZajedno.execute(togetherrr, togetherrrTwo)
            sveOPatrolu = self.petrol(a[spoj][1])
            spojiMojeSveDva = sveOPatrolu
            PartTwo = spojiMojeSveDva
            array = 0
            arrayDataBase = """
            UPDATE Connections
            SET CostByPetrol = ?
            WHERE Key = ?
            """
            togetherrAll = arrayDataBase
            togetherrAllTwo = (PartTwo, spoj+1)
            sprojiSveZajedno.execute(togetherrAll, togetherrAllTwo)
            sveOzajedno = self.time(a[spoj][1])
            spojiMojeSveTri = sveOzajedno
            vrijeme = spojiMojeSveTri
            arrayDataBase = """
            UPDATE Connections
            SET TimeByCar = ?
            WHERE Key = ?
            """
            togetherAll = (vrijeme, spoj+1)
            togetherAllTwo = arrayDataBase 
            sprojiSveZajedno.execute(togetherAllTwo, togetherAll)
        sprojiSveZajedno.commit()
    # show me the range
    def informacijaD(self, range):
        ranger = 0
        calculate = range * 1.49 / 13
        return calculate
    #different range
    def informacijaP(self, range):
        ranger = 0
        calculate = range * 1.61 / 22
        return calculate
    #different range
    def informacijaT(self, range):
        calculate = range / 2.25
        return calculate
    #different range
    def informacijaDE(self, range):
        ranger = 0
        calculate = range * 1.49 / 13
        return calculate

    
    # we will have to come back to this method for testing
    def pokazisveGradove_2(self, a):
        input = "Select * From Cities"
        a.execute(input)
        informacija = a.fetchall()
        slovo_1 = "Key"
        slovo_2 = "City"
        slovo_3 = "Start"
        slovo_4 = "Extra Cost"
        slovo_5 = "Extra Time"
        print("%-5s %-15s %-10s %10s %12s" % (slovo_1, slovo_2, slovo_3, slovo_4, slovo_5 ))
        for ranger in informacija:
            
            mestoa = ranger[1]
            mestob = ranger[2]
            mestoc = ranger[3]
            mestod = ranger[0]
            mestoe = ranger[4]
            print("%-5d %-15s %-10d %10.2f %12d" % (mestoa, mestob, mestoc, mestod, mestoe))
    
    