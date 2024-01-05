# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_RSA.py


# ● ■  Description of this module's purpose:
    
#       This module for encryption of env-var addr-ry pointers, rotational
#       sar-var pointers and other staqtapp sectional addr encrypt calls.


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
import random
import math

# Imported PySqTpp_Koch module(s) for this module's objectives.
import PySqTpp_Koch_Tenet

#=================================================================================
#=================================================================================
class RSA_CLS:
    
    def is_prime(self, n):
        
        x = 2
        while x <= math.sqrt(n):
            if n%x < 1:
                return False
            x+=1
        return True 
#=================================================================================
#=================================================================================
    def generate_prime(self, s, e):
        
        while True:
            n = random.randint(s, e)
            if self.is_prime(n):
                break
        return n
#=================================================================================
#=================================================================================
    def nearest_prime(self, n):
        
        nLen = n*2
        n+=1
        while n < nLen:
            if self.is_prime(n):
                break
            n+=1
        return n
#=================================================================================
#=================================================================================
    def find_e(self, phi_n):
        
        e = 2
        while e < phi_n:
            if math.gcd(e, phi_n) == 1:
                return e
            e+=1
#=================================================================================
#=================================================================================
    def find_d(self, p, n, e, phi):
        
        for i in range(p, n):
            if (((i*e)%phi) == 1):
                return i         
#=================================================================================
def sqtpp_koch_rsa_encode_addr_sec(b: int, f: int, oc: int) -> list:
    
    nwCls = RSA_CLS()
    mnPrm = nwCls.generate_prime(b, f)
    nrPrm = nwCls.nearest_prime(mnPrm)
    pl = PySqTpp_Koch_Tenet.sqtpp_koch_pole_tenet([b+nrPrm,f-mnPrm,oc+f],[mnPrm-b,nrPrm,oc+b])
    if pl[0] == 2:
        sqtpp_koch_cats_in_the_cradle(False, 'CTC:' str((oc+(mnPrm-b))*2) + ',' + str(pl[1]) + '\n')
    n = mnPrm*nrPrm
    phi = (mnPrm-1)*(nrPrm-1)
    e = nwCls.find_e(phi)
    return [nwCls.find_d(mnPrm, n, e, phi), oc ** e%n]
#=================================================================================
def sqtpp_koch_cats_in_the_cradle(isRead: bool, src: str) -> int:
    
    if isRead:
        pass
    else:
        # check prv pointer addr cache != tnt[1], write ctc entry to gzip_adr
        pass
#=================================================================================
def sqtpp_koch_silver_spoon():
    
    pass
#=================================================================================
def sqtpp_koch_little_boy_blue():
    
    pass
#=================================================================================
def sqtpp_koch_man_on_the_moon() -> str:
    
    pass


