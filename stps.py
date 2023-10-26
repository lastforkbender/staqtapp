# Code File: StaqTapp-1.01 [stps.py] StaqTapp main S.A.R. functional calls module




# Staqtapp 1.02.237

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from PySqTpp_Alpha import SarAlpha


#______________________________________________________________________________________

def extrloadsarremap(is_prm, cPn, fPth, sPth):
    newSarAlpha = SarAlpha()
    rslt = newSarAlpha.extr_load_sar_remap(is_prm, cPn, fPth, sPth)
    if rslt == -1:
        raise Exception("staqtapp<loadsar_remap> invalid file path @" + fPth + '/' + sPth + '.tqpt')
    elif rslt == -2:
        raise Exception("staqtapp<loadsar_remap> no found category for sar variables @" + fPth + '/' + sPth + '.tqpt')
#______________________________________________________________________________________

def newsaradd(dsg, dt_nm, dt_dt, fPth, sPth):
    newSarAlpha = SarAlpha()
    newSarAlpha.acquired_tqpt_source(dsg, dt_nm, dt_dt, fPth, sPth)
#______________________________________________________________________________________

#def test():



#______________________________________________________________________________________

#test()
