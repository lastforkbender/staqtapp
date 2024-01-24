# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_AES.py


# ● ■  Description of this module's purpose:
    
#       This module encrypts|decrypts env-var data, with hidden options.


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

_bxR = (0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,0x53, 0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16)
_bxC = (0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36,0x6C,0xD8,0xAB,0x4D,0x9A,0x2F,0x5E,0xBC,0x63,0xC6,0x97,0x35,0x6A,0xD4,0xB3,0x7D,0xFA,0xEF,0xC5,0x91,0x39)

____=lambda _:list(map(lambda __:list(map(lambda ___:_bxR[___],__)),_))
___________=lambda _:list(map(lambda __:list(map(lambda ___:_bxC[___],__)),_))
________=lambda _:[[_[__][(___+____)%4] for __,____ in enumerate([1,2,3,0])] for ___ in range(4)]
______________=lambda _:[[_[((__+___)%4)][____] for ____ in range(4)] for __,___ in enumerate([3,2,1,0])]
_____=lambda _,__:[[_[___][____]^__[___][____] for ____ in range(4)] for ___ in range(4)]
______=lambda a:(((a<<1)^0x1B)&0xFF) if (a&0x80) else (a<<1)
# __________________________________________________________________________________

def _______(_,__):
    _=_____(_,__)
# __________________________________________________________________________________

def ________(_):
    __=_[0]^_[1]^_[2]^_[3]
    ___=_[0]
    _[0]^=__^______(_[0]^_[1])
    _[1]^=__^______(_[1]^_[2])
    _[2]^=__^______(_[2]^_[3])
    _[3]^=__^______(_[3]^___)
# __________________________________________________________________________________

def __(_,__,___):
    while _<___:
        ________(__[_])
        _+=1
# __________________________________________________________________________________

def ____(_,__):
    return [list(__[x:x+_]) for x in range(0,len(__),_)]
# __________________________________________________________________________________

def _________(_):
    return bytes(sum(_,[]))
# __________________________________________________________________________________

def ____________(_,__):
    return bytes(___^____ for ___,____ in zip(_,__))
# __________________________________________________________________________________

def _(_):
    __=list(_)
    for ___ in reversed(range(len(__))):
        if __[___]==0xFF:__[___]=0
        else:
            __[___]+=1
            break
    return bytes(__)
# __________________________________________________________________________________

def ___(_,__,___):
        assert len(_)%__==0 or not ___
        return [_[i:i+__] for i in range(0,len(_),__)]
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________

class AES():
    _={16:10,24:12,32:14}
    def __init__(self,__):
        assert len(__) in AES._
        self.___=AES._[len(__)]
        self.____=self._____(__)
# __________________________________________________________________________________

    def _____(self,_):
        __=____(4,_)
        _____=len(_)//4
        ______=1
        while len(__)<(self.___+1)*4:
            _______=list(__[-1])
            if len(__)%_____==0:
                _______.append(_______.pop(0))
                _______=[_bxR[k] for k in _______]
                _______[0]^=_bxC[______]
                ______+=1
            elif len(_)==32 and len(__)%_____==4:
                _______=[_bxR[k] for k in _______]
            _______=____________(_______,__[-_____])
            __.append(_______)
        return [__[4*______:4*(______+1)] for ______ in range(len(__)//4)]
# __________________________________________________________________________________

    def ______(self,_):
        assert len(_)==16
        _____=____(4,_)
        _______(_____,self.____[0])
        for i in range(1,self.___):
            __(0,_____,4)
            _______(_____,self.____[i])
        _______(_____,self.____[-1])
        return _________(_____)
# __________________________________________________________________________________

    def __________(self,__,_____,_______):
        assert len(_____)==_____
        ________=[]
        ______=_____
        for ____ in ___(__,_______,False):
            _________=____________(____,self.______(______))
            ________.append(_________)
            ______=_(______)
        return b''.join(________)
# _________________________________________________________________________________

def sqtpp_koch_aes_encode_data(data, key, iv, pd):
    
    aesCls = AES(key)
    return aesCls.__________(str.encode(data), iv, pd)

