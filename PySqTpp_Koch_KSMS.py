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
import random as r_
import math as m_

# Imported PySqTpp_Koch module(s) for this module's objectives.
from PySqTpp_Koch_Noed_Addr import sqtpp_koch_get_noedaddr
from PySqTpp_Koch_RNG import sqtpp_koch_get_rng_id
#______________________________________________________________________________

class _KSMS_(abc.ABC):
    def __new__(cls,*args,**kwargs):
        if cls is _KSMS_:
            raise TypeError('!!__KSMS__[!smsKsms!]__KSMS__[!smsKsms!]__KSMS__!!')
        return super().__new__(cls)
        
    def __init__(self,___):
        self.____=___
        del ___
#______________________________________________________________________________

    @abc.abstractmethod
    def set_mk_container_(self):
        frclMap = sqtpp_koch_get_noedaddr(bytearray(self.____))
        rngFwdSet = sqtpp_koch_get_rng_id(self.____,10,16,False)
        del self.____
        crr_pth = f'{os.path.dirname(os.path.abspath(__file__))}/sqtpp-koch'
        mskf = False
        gnes = False
        if not os.path.isdir(crr_pth):
            os.makedirs(crr_pth)
            gnes = True
        else:
            lmb_dir = lambda dirPth: [(fNm, eNm, len(fNm) if fNm.isdigit() else 0) for file in os.listdir(dirPth) for fNm, eNm in [os.path.splitext(file)]]
            fNms = lmb_dir(crr_pth)
            fNmsLen = len(fNms)
            if fNmsLen:
                # fNms = tuple[('filename','extension',numbered_filename_length),...
                for k in range(fNmsLen):
                    if fNms[k][2] == 16:
                        if fNms[k][1] == 'skrm' or fNms[k][1] == 'skhm':
                            if fNms[k][0] == rngFwdSet:
                                pass
                            else:
                                # NO GO, WRONG MASTER KEY ------------------------
                                # Re-encrypt all files with embedded key, lockout.
                                pass
                # Get both atomic sequences, write all the immersion nodes to new.
                as1 = self.get_atomic_sequence_(30)
                as2 = self.get_atomic_sequence_(30)
            else:
                # files not there...
                mskf = True
        # Write the current random fractal mapping for seten modules' routings.
        with open(f'{crr_pth}/_skfm.b', mode='w') as fSmc: fSmc.write(frclMap)
#______________________________________________________________________________

    @abc.abstractmethod
    def get_atomic_sequence_(self,__) -> list:
        # [p,  P,  Pz,  AT,  I,  d,  u,  o,  O,  t,  T]
        _=[None]*11
        _____=0
        ___=None
        ____=[]
        while _____<__:
            _[0]=float(r_.randint(9,999))
            _[1]=float(r_.randint(3,12))
            _[2]=float(r_.randint(10,10000))
            _[3]=float(r_.randint(10,1000))
            _[4]=float(r_.randint(10,100))
            _[5]=float(r_.randint(10,100))
            _[6]=float(r_.randint(10,100))
            _[7]=float(r_.randint(12,32))
            _[8]=float(r_.randint(12,64))
            _[9]=float(r_.randint(5,64))
            _[10]=float(r_.randint(5,128))
            ___=1-(_[2]*(m_.sin(_[8]*2)))/(m_.sqrt(_[3])*_[6]*_[0])*(m_.sqrt(_[4]*_[1]*(_[8]*_[7]*_[9]))/m_.sqrt(_[5]*_[10]*_[0]))
            _____+=1
            if ___<1:____.append(0)
            else: ____.append(1)
        return ____
# __________________________________________________________________________________
# __________________________________________________________________________________

class Kms_Stack_(_KSMS_):
    def __init__(self,____):
        super().__init__(____)
        del ____
    
    def set_mk_container_(self):
        _KSMS_.set_mk_container_(self)
        
    def get_atomic_sequence_(self, l) -> list:
        return _KSMS_.get_atomic_sequence_(self, l)
#______________________________________________________________________________

