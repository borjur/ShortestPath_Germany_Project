'''
Created on March 20, 2013

@author: Boris Jurosevic
         Trip through Germany
         CS 2430
         
'''
from __future__ import print_function

class City(object):
    '''
    classdocs
    '''


    def __init__(self, kljuc, ime, pocetak, vrijeme, cijena):
        '''
        Constructor
        '''
        self.thisKljuc = kljuc
        self.thisIme = ime
        self.thisPocetak = pocetak
        self.thisVrijeme = vrijeme
        self.thisCijena = cijena
        
    def __str__(self):
        return str.format("{0}", self.thisIme)
    
    def startingOne(self):
        starter = self.star()
        ender = self.end()
        mid = self.midl()
        if ender < mid:
            
              ''' 
            def endingOne(self):
                train = self.star()
                last = self.end()
                konj = self.midl()
                if last < konj:
            
               '''
        