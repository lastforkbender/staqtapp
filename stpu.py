# Code File: StaqTapp-1.02 [stpu.py] StaqTapp utility functional calls module


# Staqtapp 1.02.435

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from PySqTpp_Utility import UltSttp
import stpr

#______________________________________________________________________________________

def ult_fnc_var_request(logf_enable, vr_name, fnc_name, fpath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.asguard_variable_domain(logf_enable, vr_name, fnc_name, fpath)
    if rslt == True:
        return True
    elif rslt == False:
        return False
    elif rslt == -1:
        raise Exception("staqtapp<keyvar> invalid tqpt source file path @" + fpath)
    elif rslt == -2:
        raise Exception("staqtapp<keyvar> varName and/or fncName cannot be nothing")
    elif rslt == -3:
        raise Exception("staqtapp<keyvar> invalid variable name, variable not found @" + fpath)
    elif rslt == -4:
        raise Exception("staqtapp<keyvar> no found .tpqt function lock file to search at in directory of .tqpt source file...")
    elif rslt == -5:
        raise Exception("staqtapp<keyvar> global variable: " + vr_name + ' is not listed in .tpqt function lock file...')
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

def ult_return_function_keys(varName, filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.search_key_lock(varName, filePath)
    if rslt == -1:
        raise Exception("staqtapp<searchkeys> invalid tqpt source file path @" + filePath)
    elif rslt == -2:
        raise Exception("staqtapp<searchkeys> @varName cannot be null")
    elif rslt == -3:
         raise Exception("staqtapp<searchkeys> @varName not found in tqpt file @" + filePath)
    elif rslt == -4:
         raise Exception("staqtapp<searchkeys> no pairing tpqt file found at tqpt file path [" + filePath + "]")
    else:
        return rslt
#______________________________________________________________________________________

def ult_edit_fnc_lock(varName, fncName, filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.overwrite_fnc_lock(varName, fncName, filePath)
    if rslt == -1:
        raise Exception("staqtapp<lockvar_edit> invalid tqpt source file path @" + filePath)
    elif rslt == -2:
        raise Exception("staqtapp<lockvar_edit> varName and/or fncName cannot be nothing")
    elif rslt == -3:
        raise Exception("staqtapp<lockvar_edit> invalid variable name, variable not found @" + filePath)
    elif rslt == -4:
        raise Exception("staqtapp<lockvar_edit> no pairing tpqt file found at tqpt file path [" + filePath + "]")
    elif rslt == -5:
        raise Exception("staqtapp<lockvar_edit> global variable: " + varName + ' is not listed in .tpqt function lock file...')
    elif rslt == -6:
        raise Exception("staqtapp<lockvar_edit> invalid type @fncName, must be str or list")
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

def ult_show_tpqt_contents(filePath):
    newUltSttp = UltSttp()
    rslt = newUltSttp.print_tpqt_file(filePath)
    if rslt == -1:
        raise Exception("staqtapp<viewsource> invalid tqpt source file path @" + filePath)
#______________________________________________________________________________________

def ult_call_rev9_service(slotsEncoding, sarsEncoding, multiStability, multiExtractable, obfuscated, contentDependent, staticShifting, sortingTolerate, counterIntuitiveVariables, superPalindromePointers, variablesLengthMuting, variablesTopographyLearning, globalVariablesFileExtension, globalVariablesLibraryName, buildFolderPath):
    stpr.main([slotsEncoding, sarsEncoding, multiStability, multiExtractable, obfuscated, contentDependent, staticShifting, sortingTolerate, counterIntuitiveVariables, superPalindromePointers, variablesLengthMuting, variablesTopographyLearning, globalVariablesFileExtension, globalVariablesLibraryName, buildFolderPath])
#______________________________________________________________________________________