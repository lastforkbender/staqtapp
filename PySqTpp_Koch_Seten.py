# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Seten.py


# ● ■  Description of this module's purpose:
    
#       This module directs all Seten related modules, including types of
#       key sets, total obfuscation+encryption layering of env-vars data.
#       However is disconnected from what random obfuscation was applied;
#       in that attempts of hijacking this module's direction of what ---
#       obfuscation next or previous is extreme entanglement both ways.
#       Also uses sar type variables and sar type pointers, whereof env-
#       vars have no specific name, just a address of random numbers. Of
#       this type addr pointing once compressed, not even the most power-
#       ful quantum computers in the future can sort them correctly again
#       unless both compression table constants known, no invert nesting.
#       (See method extr_load_sar_remap() @ PySqTpp_Alpha.py of Staqtapp)


# ● ■  Staqtapp-Koch Env-Vars Library Overview:

#       The scope of this env-vars system is routine focused upon env-var
#       security via obfuscated addresses inter-connected to env-vars own
#       obfuscation of it's data, using tor like circumstances, procedural
#       generation of env-var keys/spacing and one-way shared descriptors.

#       Having limited made keys outside this env-var system for access of
#       advanced security issue... if chosen of a needed env-vars solution.
#       Of then a email response will be given for a phone number to call,
#       involving a signature and purchase after agreed terms are met, then
#       custom built Staqtapp-Koch full package library for your key sent.
#       Pricing terms for single package is $318 U.S. dollars, however ---
#       is variable to the conditions of use.(This public version does not
#       include those strong fractal-palindrome based security modules.)

    
# Contact: rcttcr5@gmail.com
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________


# Imported core python module(s) for this module's objectives.
import os
import gzip
import random
import threading
from typing import List
# __________________________________________________________________________________

class Seten(type):
    
    def __new__(self,_,__,___):
        ___['_lock'] = threading.Lock()
        return super(Seten, self).__new__(self,_,__,___)

    def __init__(self,____,_____):
        self._____=_____
        self.____=____
# __________________________________________________________________________________
        
class Staq(object):

    __metaclass__ = Seten
    
    def __init__(self):
        # Boat-key in a tree; no direct access outside this class.
        Seten._master_key = self.kch_set_mk(1,5)
        
    @classmethod
    def kch_get_lock(self, Seten):
        return Seten._lock   
# __________________________________________________________________________________

    @classmethod
    def kch_jex256e(self,_,__,___,____,_______________):
        ______=[]
        __________=[]
        for _____,____________ in enumerate(_):
            if ____________.isalpha():
                _________=(ord(__[_____%len(__)])-ord(_______________))%26
                ________=chr((ord(____________.lower())-ord(_______________)+_________)%26+ord(_______________))
                ______.append(________.upper() if ____________.isupper() else ________)
                __________.append(chr((ord(____[_____ % len(____)])-ord(_______________)+1)%256))
            else:
                ______.append(char)
                __________.append(chr((ord(____[_____ % len(____)])-ord(_______________)+1)%256))
        return ''.join(______+__________)
# __________________________________________________________________________________

    @classmethod
    def kch_jex256d(self,_,__,___,____,_______________):
        _____=[]
        _______=0
        for ________,__________ in enumerate(_):
            if _______>0: _______-=1
            elif __________.isalpha():
                _________=(ord(__[________%len(__)])-ord(_______________))%26
                ______=chr((ord(__________.lower())-ord(_______________)-_________)%26+ord(_______________))
                _____.append(______.upper() if __________.isupper() else ______)
            else: _______=ord(__________)-ord(____[________%len(____)])+1
        return ''.join(_____)
# __________________________________________________________________________________
        
    @classmethod
    def kch_reverse_diffusion(self, k: int, chnl_scale: List[int], chnl_constant: int) -> List[int]:
        #---------------------------------------------------------------------
        rtrnAddr = [ndvl+chnl_constant for ndvl in chnl_scale]
        while k < len(rtrnAddr):
            rtrnAddr[k] = rtrnAddr[k+random.randint(0, 2) % (len(rtrnAddr)-k-1)+1]
            k+=2
        pdVl = random.randint(1, 10**6)
        # :PUBLIC DOMAIN VERSION:
        pdVm = k-len(rtrnAddr)
        rtrnAddr.extend([pdVl]*pdVm)
        # ::::::::::::::::::::::::::
        return rtrnAddr
# __________________________________________________________________________________
        
    @classmethod
    def kch_set_mk(self, k: int, chnlNd: int) -> str:
        # ***normal parameters use for public domain a 1:5 strength return***
        nd_rsrv = [random.randint(1, 10**6) for _ in range(chnlNd)]
        dcv = random.randint(1, 10**6)
        # :PUBLIC DOMAIN VERSION:
        rvVls = [0]*chnlNd
        for f in range(chnlNd):
            rvVls[f] = nd_rsrv[chnlNd-f-1]
        ndvVls = self.kch_reverse_diffusion(k, rvVls, dcv)
        # ::::::::::::::::::::::::::::::::::::::::::::::
        stNnv = set(ndvVls)
        ndvVls = list(stNnv)
        ndvVlsLen = len(ndvVls)
        ndvVls = [str(ndvVls[l]) for l in range(ndvVlsLen)]        
        return ''.join(ndvVls)
# __________________________________________________________________________________
        

