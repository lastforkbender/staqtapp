# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_XORTL.py


# ● ■  Description of this module's purpose:
    
#       This module is a XOR class cipher with unique time lock features.
#       If generated time-keys are out of sync then will not encrypt any.
#       Can return pad data about time-key or time-block not used. Those
#       advanced security features not part of this public version.


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
import secrets
import random
import time
import math
# __________________________________________________________________________________
class XORTL:
    
    def __init__(self,_,__,___):
        self.__=_
        self.___=__
        self.____=___
        self._____=self._(16)
        self.______=self.______(random.randint(2,9))
        
    @staticmethod
    def _(_):
        return secrets.token_bytes(_)
# __________________________________________________________________________________

    def ______(self,_):
        __=str.encode(str(int(math.sqrt((int(str(time.ctime()).strip(' .:0abcdefghijklmnopqrstuvwxyz0ABCDEFGHIJKLMNOPQRSTUVWXYZ').replace(':','').replace(' ','').replace('0',''))/_)))))
        ___=bytes(self._______(bytes.decode(bytes(f'{__}{str.encode(str(time.time()),)}','utf-8')),self.____),'utf-8')
        ____=bytearray(___)
        return ____
# __________________________________________________________________________________
 
    def _______(self,_,__):
        ___=self.____-(len(_)%self.____)
        ____=chr(___)*___
        return _+____
# __________________________________________________________________________________

    def ________(self,_):
        __=ord(_[-1])
        _=_[:-__]
        return _
# __________________________________________________________________________________

    def _________(self,_,__):
        ____=bytearray()
        ___=0
        _____=False
        while True:
            try:
                for ______ in range(len(_)):
                    ___+=1
                    if ___>__:
                        _____=True
                        break
                    ____.append(_[______]^self.__[______%len(self.__)]>>self._____[______%len(self._____)]<<self.______[______%len(self.______)]^self.___[______%len(self.___)])
                break
            except Exception:
                self.______ = self.______(random.randint(2,9))
        if _____:
            if self.___>8:
                return self._______(self.______,___)
            else:
                return self.________(self._____)
        else:
            return ____
# __________________________________________________________________________________

    def __________(self,_):
        __=bytearray()
        while True:
            try:
                for ___ in range(len(_)):
                    __.append(data[___]^self.__[___%len(self.__)]>>self._____[___%len(self._____)]^self.___[___%len(self.___)])
                break
            except Exception:
                self._____=self.______
                self.______=self.______(random.randint(2,9))
        return __
# __________________________________________________________________________________

def sqtpp_koch_xortl(is_encode, data, key, iv, block_size):
    # Data is bytes: Normal use key=256bytes,iv=16bytes,block_size=8,16,32bytes.
    tbl = False
    cls = XORTL(key, iv, block_size)
    if is_encode:  
        try:
            # Normal block-time=512, doubling this will result in more likely
            # encryption done but also increase the amount of time to do so.
            # This is also dependent upon the size of the data to encrypt.
            return bytes(cls._________(data,512))
        except Exception:
            return 'TIMELOCK'
    else:
        try:
            return bytearray.decode(cls.__________(data))
        except Exception:
            return 'DCPERROR'
            
