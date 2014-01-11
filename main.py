'''
Created on March 20, 2013

@author: Boris Jurosevic
         Trip through Germany
         CS 2430
         
'''
from __future__ import print_function
from shortest_path import *
from data_manager import Data_Manager
from city import City
from connection import Connection
import math

def main():

    informacije = Data_Manager()
    savPut = []
    puteljak = pocniOdArray(savPut)
    allTogether = []
    svaKupovina = 0
    svoVrijeme = 0
    svaDaljina = 0
    array = {}
    najkraci = najkraciPut(puteljak)
    x = najkraci
    sveIspisi(x)
    allOfIt = svaKupovina, svoVrijeme, svaDaljina 
    kupilac = 21
    svaKupovina, svoVrijeme, svaDaljina = uSuprotnomStanju(x, kupilac)
    divideBySec = svoVrijeme / 60
    print()
    print("""  Few important things we have come up with: 
               - When it comes to efficient route on time and cost it is Petrol.
               - Train time where we came up from raileurope website
               - Car time where we came up from around 130 kmh
               - We could not find all the routes with train so that gave petrol the advantage
               - After coming up with results from the class it was clear that for a group of people having a petrol car was the most efficient price
               - Petrol might not be faster but it will be the cheapest """)
    print()
    print("Now we will look at the costs ")
    print(str.format("This is the Traveling Cost: ${0:.6}, This is the Time Traveled: {1:.4} hours, This is the Distance Traveled: {2:.6} km ({3:.6} miles)", svaKupovina, divideBySec, svaDaljina, svaDaljina * .621371))
    sveDodatno(12.00, "Oma/Opa want to drive under the river - a taxi can do this as well)")
    pomnoziZaMjesec = svaKupovina + 12
    svaKupovina = pomnoziZaMjesec
    sveDodatno(1169.80, "purchasing iPad's at 180 Euros ($233.96) each")
    svaKup = svaKupovina + 1169.8
    svaKupovina = svaKup
    sveDodatno(24, "taxi will be needed to visit the castle 10km away from the hauptbahnhof")
    desePuta = svaDaljina + 10
    svaDaljina = desePuta
    duplo = svaKupovina + 24
    svaKupovina = duplo
    print(str.format("    Time extra spent: {0} {1}", 24, "Oma wants to visit a Spa here, therefore, you will need to spend the day"))
    pomnozi = svoVrijeme + 24 * 60
    svoVrijeme = pomnozi
    print()
    print()
    print(str.format("The final answer is: Bottom line cost: ${0:.6}, Bottom line time: {1:.4} hours, Bottom line distance: {2:.6} km ({3:.6} miles)", svaKupovina, svoVrijeme / 60, svaDaljina, svaDaljina * .621371))
    
def uSuprotnomStanju_2(into, dane):
    dayandMonth = []
    xtraExpense = 0
    podjeli = dane / 7
    s = math.ceil(float(podjeli)) 
    all = 0
    podjeli = 600 * s
    sveKuljeno = podjeli
    podjeliOne = 700 * s
    sveodD = podjeliOne
    podj = 2415 * s
    sveodT = podj
    sveodV = 0
    sveodAu = 0
    i = 0
    arrayOne = []
    arrayTwo = []
    
    informacija = Data_Manager()
    
    for sopjJE in into:
        sp = sopjJE[0]
        ab = sp
        drp = sopjJE[1]
        db = drp
        brb = informacija.nadjiSpojeve(ab, db)
        
        if brb == None:
            one = sopjJE[2]
            to = one
            two = sopjJE[2]
            on = two
            three = sveUP(to)
            mr = three
            four = sveVrijeme(to)
            vr = four
            tr = sopjJE[0]
            brg = sopjJE[1]
            brb = Connection(tr, brg, 0, on, mr, 0, vr, to)
        
        ted = all + brb.range
        all = ted
        tedOne = sveKuljeno + brb.CjenaP
        sveKuljeno = tedOne
        opa = sveodD + brb.CjenaDizela
        sveodD = opa
        if brb.CjenaVoza == 0:
            abc = sveodT + brb.CjenaP + 115
            sveodT = abc
            zed = sveodV + brb.vrijemeAuta
            sveodV = zed
        sveodV = sveodV + brb.VrijemeVoza
        sveodAu = sveodAu + brb.vrijemeAuta
        natri = sveKuljeno + sveodAu
        nacetri = sveodT + sveodAu
    if(natri < nacetri):
        if(sveKuljeno < sveodD):
            vratinazadOpet = sveKuljeno, sveodAu, all
            return vratinazadOpet
        else:
            vratise = sveodD, sveodAu, all
            return vratise 
        Uno = sveodD + sveodAu  
        Due = sveodT + sveodAu
    elif(Uno < Due):
        allIt = sveodD, sveodAu, all
        return allIt
    else:
        allOtherStuff = sveodT, sveodV, all
        return allOtherStuff 

def sveDodatno(x, y):
    index = None
    array = []
    print(str.format("    Cost of extra is : ${0} {1}", float(x), y))
    
def najkraciPut(doKraja):
    x = float('inf')
    array = 0
    
    for zed in range(len(doKraja)):
        sveZajedno = 0
        
        for connect in doKraja[zed]:
            pomnozi = sveZajedno + connect[2]
            sveZajedno = pomnozi
            
            
        if sveZajedno < x:
            x = sveZajedno
            array = zed
            
    return doKraja[array]
        

def sveIspisi(a):
    finalSTep_1 = 0;
    finalSTep_2 = 0;
    finalSTep_3 = 0;
    dobro = 0;
    xr = Data_Manager()
    
    print("Welcome to Trip to Germany!")
    print("Trip consists of of these cities all together")
    print("Rostock ")
    print("Lubeck (home of the best marzipan) ")
    print("Hamburg (Oma/Opa want to drive under the river - a taxi can do this as well)")
    print("Bremen ")
    print("Hannover (Consumer Electronics haven - purchase each a new iPad at 180 Euros each)  ")
    print("Kassel ")
    print("Dusseldorf  ")
    print("Koln (taxi will be needed to visit the castle 10km away from the hauptbahnhof)  ")
    print("St. Augustine ")
    print("Bonn ")
    print("Wiesbaden ")
    print("** Frankfurt ")
    print("Mannheim ")
    print("Karlsruhe ")
    print("Baden Baden (Oma wants to visit a Spa here, therefore, you will need to spend the day) ")
    print("** Stuttgart ")
    print("** Munchen (Munich)")
    print("Nurnberg")
    print("Dresden ")
    print("Leipzig ")
    print("** Berlin")
    print("Basel, Switzerland (Opa and Dad want to purchase a nice watch and this is the best place for such a purchase - you will be spending $6k/watch) ")

    print()
    print("Here is the way using Petrol, Diesel or Train for every city")
    print("Cities of this trip:", xr.dajmigradpoGrad(a[0][0]))
    
    for sastavi in a:
        dobro = dobro + 1
        b = sastavi[0]
        f = sastavi[1]
        city = xr.dajmigradpoGrad(b)
        ovajSPoj = xr.nadjiSpojeve(b, f)

        if ovajSPoj == None:
            index = 0
            a = sastavi[2]
            b = sveGorivo(a)
            c = sveUP(a)
            d = sveVrijeme(a)
            xrx = sastavi[0]
            xrd = sastavi[1]
            ovajSPoj = Connection(xrx, xrd, 0, b, c, 0, d, a)
            
        putic, vrsta, cena, vrim = ovajSPoj.sveTezine()
        way_1 = finalSTep_1 + putic
        finalSTep_1 = way_1
        way_2 = finalSTep_2 + cena
        finalSTep_2 = way_2
        way_3 = finalSTep_3 + vrim
        finalSTep_3 = way_3
        putit = sastavi[1]
        print("Distance Number:", dobro, "", city, putit)
        atm = float(putic)
        tip = vrsta
        fl = float(cena)
        vm = float(vrim)
        print(str.format("So know we know that traveling distance is: {0:.4} km, by {1}, traveling cost is: ${2:.5}, and traveling time is: {3:.4} minutes", atm, tip, fl, vm))
    print("")
    print()
    print("Here are the alternating methods:")
    tour = finalSTep_2
    tourtwo = finalSTep_3 / 60
    tourthree = finalSTep_1
    tourfour = finalSTep_1 * .621371
    print(str.format("       and all together the Cost is : ${0:.6}, Time is: {1:.4} hours, Distance is: {2:.6} km ({3:.6} miles)", tour, tourtwo, tourthree, tourfour))
    print()
 
def uSuprotnomStanju(into, dane):
    dayandMonth = []
    xtraExpense = 0
    podjeli = dane / 7
    s = math.ceil(float(podjeli)) 
    all = 0
    podjeli = 600 * s
    sveKuljeno = podjeli
    podjeliOne = 700 * s
    sveodD = podjeliOne
    podj = 2415 * s
    sveodT = podj
    sveodV = 0
    sveodAu = 0
    i = 0
    arrayOne = []
    arrayTwo = []
    
    informacija = Data_Manager()
    
    for sopjJE in into:
        sp = sopjJE[0]
        ab = sp
        drp = sopjJE[1]
        db = drp
        brb = informacija.nadjiSpojeve(ab, db)
        
        if brb == None:
            one = sopjJE[2]
            to = one
            two = sopjJE[2]
            on = two
            three = sveUP(to)
            mr = three
            four = sveVrijeme(to)
            vr = four
            tr = sopjJE[0]
            brg = sopjJE[1]
            brb = Connection(tr, brg, 0, on, mr, 0, vr, to)
        
        ted = all + brb.range
        all = ted
        tedOne = sveKuljeno + brb.CjenaP
        sveKuljeno = tedOne
        opa = sveodD + brb.CjenaDizela
        sveodD = opa
        if brb.CjenaVoza == 0:
            abc = sveodT + brb.CjenaP + 115
            sveodT = abc
            zed = sveodV + brb.vrijemeAuta
            sveodV = zed
        sveodV = sveodV + brb.VrijemeVoza
        sveodAu = sveodAu + brb.vrijemeAuta
        natri = sveKuljeno + sveodAu
        nacetri = sveodT + sveodAu
    if(natri < nacetri):
        if(sveKuljeno < sveodD):
            vratinazadOpet = sveKuljeno, sveodAu, all
            return vratinazadOpet
        else:
            vratise = sveodD, sveodAu, all
            return vratise 
        Uno = sveodD + sveodAu  
        Due = sveodT + sveodAu
    elif(Uno < Due):
        allIt = sveodD, sveodAu, all
        return allIt
    else:
        allOtherStuff = sveodT, sveodV, all
        return allOtherStuff
    print("---Alternate atistics comparing different travel methods---")
    print("    *Costs are based on weekly rates using only car or train,")
    print("    *When calculating Train, uses price for petrol when train is not availaable")
    print()
    print("    By Train: ----\n")
    a = sveodT
    b = sveodV / 60
    d = all * .621371
    print(str.format("       Cost: ${0:.6} '\n', Time: {1:.4} hours '\n', Distance: {2:.6} km ({3:.6} miles)", a, b, all, d))
    print()
    print("    By Petrol Car: ----\n")
    ye = sveKuljeno
    de = sveodAu / 60
    ze = all * .621371
    print(str.format("       Cost: ${0:.6}, Time: {1:.4} hours, Distance: {2:.6} km ({3:.6} miles)", ye, de, all, ze))
    print()
    print("    By Diesel Car: ----\n")
    svejeOnDa = all * .621371
    print(str.format("       Cost: ${0:.6}, Time: {1:.4} hours, Distance: {2:.6} km ({3:.6} miles)", sveodD, sveodAu / 60, all,svejeOnDa))
    
def sveVoz():
    indexof = 0
    pass

def sveAuto():
    indexof = 0
    pass

def sveGorivo(x):
    number = x * 1.49 / 13
    return number

def sveUP(x):
    numberTwo = x * 1.61 / 22
    return numberTwo

def sveVrijeme(x):
    numberThree = x / 2.25
    return numberThree

def sveVoz_2():
    indexof = 0
    pass

def sveAuto_2():
    indexof = 0
    pass

def sveGorivo_2(x):
    number = x * 1.49 / 13
    return number

def sveUP_2(x):
    numberTwo = x * 1.61 / 22
    return numberTwo

def sveVrijeme_2(x):
    numberThree = x / 2.25
    return numberThree
    

if __name__ == '__main__':
    main()