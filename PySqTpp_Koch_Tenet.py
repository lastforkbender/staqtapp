# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.028
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Tenet.py


# ● ■  Description of this module's purpose:
    
#       This module returns qubit like palindrome return of probability
#       for any pairing list of numbers. Returns 3 if of equal distance.


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
from collections import deque
# __________________________________________________________________________________
# __________________________________________________________________________________

class Pole:

    def __init__(self, event):

        self.event = event
        self.jump = self.__attract()

    def __attract(self):

        event = self.event
        telering = deque(sorted(event))
        telering.rotate(-len(telering)//2)
        return sum(quantum for quantum in telering)

    def _gravity(self, well):

        return abs(self.jump - well.jump)
        
# __________________________________________________________________________________
        
def sqtpp_koch_pole_tenet(lobeA, lobeB) -> list:
        
    pl1 = Pole(lobeA)
    pl2 = Pole(lobeB)
    rslt = pl1._gravity(pl2)
        
    if rslt < 1e-9:
        # both equal palindrome probabilities
        return [3, None]
    elif pl1.jump < pl2.jump:
        # pl1 is lesser palindrome probability
        return [1, pl1.jump]
    else:
        # pl2 is lesser palindrome probability
        return [2, pl2.jump]
