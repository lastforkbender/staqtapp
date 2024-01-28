# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_KSMS.py


# ● ■  Description of this module's purpose:
    
#       This module is the key manage for Staqtapp Koch version. It handles
#       four sets of keys for double AES encryptions/decryptions and any --
#       routed/layered XOR obfuscation keys in between any AES|RSA changes.
#       Is timedoor trapped to specific algorithm connects of addr pointers.
#       If set master key(mk) wrong then is env-var files lockout, no retry.


# ● ■  Staqtapp-Koch Env-Vars Library Overview:

#       The current project status is critical to implementing security
#       values of env-var use not seen before or done before. In focus
#       of forthcoming advances, this env-var library is being built of
#       a proposed system that forms a basis of complex abstractions to
#       isolate those security values. Whereof any considerations into
#       env-var security that would involve other discrete methods inact
#       to placements of env-var use, those outer models of access or no.
#       This library using fractal based rotational palindrome settings
#       of env-var use and of extreme cut-off for modern ai comprehension
#       if applied correctly as a modular sub-system approach.

    
# Contact: rcttcr5@gmail.com
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________


# Imported core python module(s) for this module's objectives.
import os
import abc
import random
import math as m_

# Imported PySqTpp_Koch module(s) for this module's objectives.
from PySqTpp_Koch_Noed_Addr import sqtpp_koch_get_noedaddr
from PySqTpp_Koch_RNG import sqtpp_koch_get_rng_id
#______________________________________________________________________________

class _KSMS_(abc.ABC):
    def __new__(cls,*args,**kwargs):
        if cls is _KSMS_:
            pass
        return super().__new__(cls) 
#______________________________________________________________________________

    @abc.abstractmethod
    def set_mk_container_(self, mk):
        frclMap = sqtpp_koch_get_noedaddr(bytearray(mk))
        rngFwdSet = sqtpp_koch_get_rng_id(mk, 10, 16, False):
        mk = None
        crr_pth = f'{os.path.dirname(os.path.abspath(__file__))}/sqtpp-koch'
        mskf = False
        gnes = False
        if not os.path.isdir(crr_pth):
            os.makedirs(crr_pth)
            gnes = True
        else:
            lmb_dir = lambda dirPth: [(fNm, eNm, len(fNm) if fNm.isdigit() else 0) for file in os.listdir(dirPth) for fNm, eNm in [os.path.splitext(file)]]
            fNms = lmb_dir(crr_pth)
            if len(fNms):
                # fNms = tuple[('filename','extension',numbered_filename_length),...
                # Get both atomic sequences, write all the immersion nodes to new.
                print(self.get_atomic_sequence_(30))
                print(self.get_atomic_sequence_(30))
                pass
            else:
                # files not there...
                mskf = True
        # Write the current random fractal mapping for seten modules' routings.
        with open(f'{crr_pth}/_skfm.b', mode='w') as fSmc: fSmc.write(frclMap)
#______________________________________________________________________________

    @abc.abstractmethod
    def r_(self, s, e) -> float:
        return float(random.randint(s,e))
#______________________________________________________________________________

    @abc.abstractmethod
    def get_atomic_sequence_(self, l) -> list:
        
        p = None
        P = None
        Pz = None
        AT = None
        I = None
        d = None
        u = None
        o = None
        O = None
        t = None
        T = None
        
        x = 0
        R1 = None
        R2 = []
        while x < l:
            p = self.r_(9,999)
            P = self.r_(3,12)
            Pz = self.r_(10,10000)
            AT = self.r_(10,1000)
            I = self.r_(10,100)
            d = self.r_(10,100)
            u = self.r_(10,100)
            o = self.r_(12,32)
            O = self.r_(12,64)
            t = self.r_(5,64)
            T = self.r_(5,128)
            
            R1 = 1-(Pz*(m_.sin(O*2)))/(m_.sqrt(AT)*u*p)*(m_.sqrt(I*P*(O*o*t))/m_.sqrt(d*T*p))
            
            x+=1
            if R1 < 1: R2.append(0)
            else: R2.append(1)
        return R2
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________

class Kms_Stack_(_KSMS_):
    
    def set_mk_container_(self, mk):
        return _KSMS_.set_mk_container_(self, mk)
        
    def r_(self, s, e) -> float:
        return _KSMS_.r_(self, s, e)
        
    def get_atomic_sequence_(self, l) -> list:
        return _KSMS_.get_atomic_sequence_(self, l)
#______________________________________________________________________________


def test():

    nwCls = Kms_Stack_()
    tpl = nwCls.set_mk_container_(50328200)

test()