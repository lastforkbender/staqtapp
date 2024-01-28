# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Tenet.py


# ● ■  Description of this module's purpose:
    
#       This module returns qubit like palindrome return of probability
#       for any pairing list of numbers. Returns 3 if of equal distance.


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
