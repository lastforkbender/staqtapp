# Code File: StaqTapp-1.02 [stps.py] StaqTapp main S.A.R. functional calls module


# Staqtapp 1.02.460

# Staqtapp is a full global variables stack feature rich library, covering all solid
# i/o functions calls from the stpp.py module or stpx.py pro module. Features
# included are precise parsings, interchangable & dynamic .tpqt lock files for
# avoiding entanglements, mmap responsive reads-writes-edits across all it's
# functional calls & much more like the scanning of any py module for potential
# global variables conflicts. Staqtapp uses only in-built python libraries and has
# no current package release, until it's scope exceeds any expected relations or
# utterly bypass any formatted opinions of filed global variables uses. With q-bit
# computing very near. A long-term goal of Staqtapp is to provide alt simulations
# of such circumstances in the future, where global variables use by concentrated
# files using hybrid computing desolves the long bad opinions of global variables.

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from PySqTpp_Alpha import SarAlpha


#______________________________________________________________________________________

def extrloadsarremap(is_prm, cPn, fPth, sPth):
    newSarAlpha = SarAlpha()
    rslt = newSarAlpha.extr_load_sar_remap(is_prm, cPn, fPth, sPth)
    if rslt == -1:
        raise Exception('staqtapp<loadsar_remap> invalid file path @' + fPth + '/' + sPth + '.tqpt')
    elif rslt == -2:
        raise Exception('staqtapp<loadsar_remap> no found category for sar variables @' + fPth + '/' + sPth + '.tqpt')
#______________________________________________________________________________________

def newsaradd(dsg, dt_nm, dt_dt, fPth, sPth):
    newSarAlpha = SarAlpha()
    newSarAlpha.acquired_tqpt_source(dsg, dt_nm, dt_dt, fPth, sPth)
#______________________________________________________________________________________

#def test():



#______________________________________________________________________________________

#test()
