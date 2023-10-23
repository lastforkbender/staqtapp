# Code File: StaqTapp-1.01 [stpu.py] StaqTapp utility functional calls module




# Staqtapp 1.02.184

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from PySqTpp_Utility import UltSttp


#______________________________________________________________________________________

def ult_limit_outer_domain(varName, fncName, filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.limit_outer_domain(varName, fncName, filePath)
    if rslt == -1:
        raise Exception("staqtapp<lockvar> invalid tqpt source file path @" + filePath)
    elif rslt == -2:
        raise Exception("staqtapp<lockvar> invalid variable name, variable not found @" + filePath)
    elif rslt == -3:
        raise Exception("staqtapp<lockvar> invalid type @fncName, must be str or list")
    elif rslt == -4:
        raise Exception("staqtapp<lockvar> invalid function name(s) @fncName found")
    elif rslt == -5:
        raise Exception("staqtapp<lockvar> varName and/or fncName cannot be nothing")
#______________________________________________________________________________________

def ult_varname(glbVarName, filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.scan_py_module(glbVarName, filePath)
    if rslt == '!':
        raise Exception("staqtapp<scanvar> invalid py module file path @" + filePath)
    else:
        return rslt
#______________________________________________________________________________________

def ult_show_tqpt_contents(filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.print_tqpt_file(filePath)
    if rslt == -1:
        raise Exception("staqtapp<viewsource> invalid tqpt source file path @" + filePath)
#______________________________________________________________________________________


