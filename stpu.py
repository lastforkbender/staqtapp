# Code File: StaqTapp-1.01 [stpu.py] StaqTapp utility functional calls module




# Staqtapp 1.01.913

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(at)gmail


from PySqTpp_Utility import UltSttp


#______________________________________________________________________________________

def ult_varname(glbVarName, filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.scan_py_module(glbVarName, filePath)
    if rslt == '!':
        raise Exception("staqtapp<scanvar> invalid py module file path @" + filePath)
    else:
        return rslt
#______________________________________________________________________________________


