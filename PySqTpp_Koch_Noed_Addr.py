# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Noed_Addr.py


# ● ■  Description of this module's purpose:
    
#       This module is responsible for paths of seten module routes during
#       obfuscation layering of env-vars' data | occupied pointer list.


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
# __________________________________________________________________________________

class NoedAddr():  

    def __ctb(self, k):
        
        l = k&0xff
        if l >= 2**7:
            l-=2**8
        return l   
# __________________________________________________________________________________
     
    def __cts(self, k):
        
        l = k&0xffff
        if l >= 2**15:
            l-=2**16
        return l    
# __________________________________________________________________________________
        
    def __cti(self, k):
        
        l = k&0xffffffff
        if l >= 2**31:
            l-=2**32
        return l     
# __________________________________________________________________________________
        
    def __cbq(self, k):
        
        k = NoedAddr.__cts(self, k-3329)
        k = NoedAddr.__cts(self, k+NoedAddr.__cti(self, NoedAddr.__cti(self, k>>15)&3329))
        return k   
# __________________________________________________________________________________

    def __pbq(self, k):
        
        for l in range(0, 256):
            k[l] = NoedAddr.__cbq(self, k[l])
        return k   
# __________________________________________________________________________________
        
    def _nd_adr(self, k, l):
        
        _ = [0 for x in range(0, 8)]
        k = NoedAddr.__pbq(self, k)
        __ = 0
        ___ = []
        if l == 1:
            r = [0 for x in range(0, 128)]
            for i in range(0, 256//8):
                for j in range(0, 8):
                    _[j] = (((((k[8*i+j])<<4)+(3329//2))//(3329))&15)
                ___.append(NoedAddr.__ctb(self, int(_[0]|(_[1]<<4)+random.randint(0,j)<<1)))
                ___.append(NoedAddr.__ctb(self, int(_[2]|(_[3]<<4)+random.randint(0,j)<<3)))
                ___.append(NoedAddr.__ctb(self, int(_[4]|(_[5]<<4)+random.randint(0,j)<<5)))
                ___.append(NoedAddr.__ctb(self, int(_[6]|(_[7]<<4)+random.randint(0,j)<<7)))
                __ = __+4
        else:
            r = [0 for x in range(0, 160)]
            for i in range(0, 256//8):
                for j in range(0, 8):
                    _[j] = (((((k[8*i+j])<<5)+(3329//2))//(3329))&31)
                ___.append(NoedAddr.__ctb(self, int((_[0]>>0)|(_[1]<<5)+random.randint(0,j)<<1)))
                ___.append(NoedAddr.__ctb(self, int((_[1]>>3)|(_[2]<<2)|(_[3]<<7)+random.randint(0,j)>>2)))
                ___.append(NoedAddr.__ctb(self, int((_[3]>>1)|(_[4]<<4)+random.randint(0,j)<<4)))
                ___.append(NoedAddr.__ctb(self, int((_[4]>>4)|(_[5]<<1)|(_[6]<<6)+random.randint(0,j)>>5)))
                ___.append(NoedAddr.__ctb(self, int((_[6]>>2)|(_[7]<<3)+random.randint(0,j)<<7)))
                __ = __+5
        return ___    
# __________________________________________________________________________________
# __________________________________________________________________________________

class SetenNoedAddr(NoedAddr):
    
    def get_noedaddr(self, bytRy):
        addr = ''.join(map(str, NoedAddr._nd_adr(self, bytRy, 1)))
        return addr
# __________________________________________________________________________________
        
def sqtpp_koch_get_noedaddr(b):
    
    ndCls = SetenNoedAddr()
    return ndCls.get_noedaddr(b)
        
        