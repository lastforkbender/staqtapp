# Code File: StaqTapp-1.01 [stps.py] StaqTapp main S.A.R. functional calls module




# Staqtapp 1.01.834

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(at)gmail


from PySqTpp_Alpha import SarAlpha


#______________________________________________________________________________________



#______________________________________________________________________________________

def newsaradd(dsg, dt_nm, dt_dt, fPth, sPth):
    newSarAlpha = SarAlpha()
    newSarAlpha.acquired_tqpt_source(dsg, dt_nm, dt_dt, fPth, sPth)
#______________________________________________________________________________________

#def test():



#______________________________________________________________________________________

#test()
