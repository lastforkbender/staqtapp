# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_MasterKey.py


# ● ■  Description of this module's purpose:
    
#       Returns a reverse diffusion set string for a master key use upon
#       double obfuscation of env-vars data or other addr specific paths
#       (These encodings are considered of security value & non-commented)


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
from typing import List
import random
# __________________________________________________________________________________
# __________________________________________________________________________________

def kch_mk_constant() -> int:
    
    # :PUBLIC DOMAIN VERSION:
    return random.randint(1, 10**6)
    # :::::::::::::::::::::::::::::
        
# __________________________________________________________________________________

def kch_mk_reverse_diffusion(k: int, chnl_scale: List[int], chnl_constant: int) -> List[int]:

    rtrnAddr = [ndvl+chnl_constant for ndvl in chnl_scale]
    while k < len(rtrnAddr):
        rtrnAddr[k] = rtrnAddr[k+random.randint(0, 2) % (len(rtrnAddr)-k-1)+1]
        k+=2
    pdVl = kch_mk_constant()
    # :PUBLIC DOMAIN VERSION:
    pdVm = k-len(rtrnAddr)
    rtrnAddr.extend([pdVl]*pdVm)
    # ::::::::::::::::::::::::::
    return rtrnAddr
    
# __________________________________________________________________________________

def sqtpp_koch_get_rd_masterkey(k: int, chnlNd: int) -> str:
    # ***normal parameters use for public domain a 1:5 strength return***
    
    nd_rsrv = [random.randint(1, 10**6) for _ in range(chnlNd)]
    dcv = kch_mk_constant()
    # :PUBLIC DOMAIN VERSION:
    rvVls = [0]*chnlNd
    for f in range(chnlNd):
        rvVls[f] = nd_rsrv[chnlNd-f-1]
    ndvVls = kch_mk_reverse_diffusion(k, rvVls, dcv)
    # ::::::::::::::::::::::::::::::::::::::::::::::
    stNnv = set(ndvVls)
    ndvVls = list(stNnv)
    ndvVls = [str(ndvVls[l]) for l in range(len(ndvVls))]
    ndvVls = ''.join(ndvVls)
    return ndvVls
