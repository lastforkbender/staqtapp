# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Immersion.py


# ● ■  Description of this module's purpose:
    
#       This module for return purposes of layering logic, dynamic counts
#       and delivered parallel state changes of obfuscation ranges/merges.
#       (These encodings are considered of security value & non-commented)


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
import random
import math
# __________________________________________________________________________________
# __________________________________________________________________________________

class IMS_CLS():
    
    def __init__(self, rxt, ryt, rdl):
        self.rxt = rxt
        self.ryt = ryt
        self._rdl = rdl
        
    @property
    def rdl(self):
        return self._rdl
        
    @rdl.setter
    def rdl(self, new_rdl):
        self._rdl = new_rdl
        
    @rdl.deleter
    def rdl(self):
        del self._rdl
    
# __________________________________________________________________________________

    def _addr_xnr(self, x: int, l: int, q: int, s: int):
        
        k = 0
        rtrn = []
        while k < x:
            # :PUBLIC DOMAIN VERSION:
            csm = ord(chr(q%random.randint(1,64)+128))-64
            addr_xnr = s << random.randint(4,16) | csm << random.randint(2,8) | q%32
            # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            if int(math.log10(addr_xnr))+1 == l:
                rtrn.append(addr_xnr)
                k+=1
        return rtrn
# __________________________________________________________________________________
        
def sqtpp_koch_get_addr_xnr_lst(lst_len: int, xnr_len: int, spc: int, shf: int) -> list:
    nwCls = IMS_CLS(spc,shf,xnr_len)
    return nwCls._addr_xnr(lst_len, xnr_len, spc, shf)

