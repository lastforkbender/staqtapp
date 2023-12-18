# Code File: StaqTapp-1.02 [PySqTpp_Utility.py] main utility functions use


# Staqtapp 1.02.450

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


import PySqTpp_UltInterface

from datetime import datetime
import mmap
import os
import re
#______________________________________________________________________________________

class UltSttp(PySqTpp_UltInterface.PySqTppUltInterface):
    # - settled functions for utility methods -
#______________________________________________________________________________________

    def limit_outer_domain(self, var_name: str, func_name: str, full_path: str) -> int:
        # @override PySqTppUltInterface.limit_outer_domain()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid tqpt source file path
        # return -2  : invalid var_name, not found
        # return -3  : invalid variable type @func_name
        # return -4  : invalid function name(s)
        # return -5  : var_name and/or func_name is null
        
        cLen = None
        sStr = None
        
        isLst = None
        fExst = True
        
        try:
            if os.path.isfile(full_path):
                newUltSttp = UltSttp()
                if len(var_name) < 1 or len(func_name) < 1:
                    return -5
                # first check if var_name exist in the given .tqpt global variables source file
                rslt = newUltSttp.tpqt_map(True, True, 'lod_vc', var_name, None, full_path)
                if rslt == False:
                    return -2
                else:
                    # change extension to position-quanity, instead of a quanity-position find;
                    # sar variable functions can overwrite static locked .tqpt files, however a
                    # .tpqt cannot be overwritten by sar variable methods or any other methods
                    sStr = full_path.replace('.tqpt', '.tpqt')
                    if not os.path.isfile(sStr):
                        fExst = False
                    # next check if @func_name is str or list..
                    if isinstance(func_name, str) == True:
                        isLst = False
                    elif isinstance(func_name, list) == True:
                        isLst = True
                    else:
                        return -3
                    # check if function name(s) are valid chars...
                    aChrs = set("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                    if isLst  == False:
                        if not set(func_name).issubset(aChrs):
                            return -4
                    else:
                        cLen = len(func_name)
                        for fn in range(cLen):
                            if not set(func_name[fn]).issubset(aChrs):
                                return -4
                    # write the .tpqt functions lock file
                    newUltSttp.tpqt_map(False, fExst, 'lod_wl', var_name, func_name, sStr)
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def asguard_variable_domain(self, inact_logf: bool, var_name: str, func_name: str, full_path: str):
        # @override PySqTppUltInterface.asguard_variable_domain()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid .tqpt source file path
        # return -2  : var_name and/or func_name is null
        # return -3  : var_name not found in .tqpt source file
        # return -4  : no .tpqt function lock file to search
        # return -5  : no search result return for .tpqt file
        
        # return False  : function/@func_name was not found ...not allowed to change @var_name
        # return True  : function/@func_name was found ...is allowed to change @var_name
        
        cLst = None
        cLen = None
        sStr = None
        
        rslt = None
        nrRslt = None
        fFnd = False
        
        try:
            if os.path.isfile(full_path):
                newUltSttp = UltSttp()
                if len(var_name) > 0 and len(func_name) > 0:
                    # does var_name exist in .tqpt file??
                    rslt = newUltSttp.tpqt_map(True, None, 'lod_vc', var_name, None, full_path)
                    if rslt == False:
                        return -3
                    else:
                        sStr = full_path.replace('.tqpt', '.tpqt')
                        if os.path.isfile(sStr):
                            nrRslt = newUltSttp.tpqt_map(True, None, 'lod_vd', var_name, None, sStr)
                            if nrRslt != '<:!!':
                                cLst = bytes.decode(nrRslt, 'utf-8').strip(' :>').split('\n')
                                cLst.pop(0)
                                cLen = len(cLst)
                                # loop thru the extracted function name list to find match or not
                                for idx in range(cLen):
                                    if func_name == cLst[idx]:
                                        fFnd = True
                                        break
                                if fFnd == True:
                                    if inact_logf == True:
                                        # change the full .tpqt file path to .logf extension
                                        sStr = sStr.replace('.tpqt', '.logf')
                                        if os.path.isfile(sStr) == True:
                                            with open(sStr, mode='a') as logf: logf.write('>> var: ' + var_name + ', fnc: ' + func_name + ', time: ' + str(datetime.now()) + '\n')
                                        else:
                                            with open(sStr, mode='w') as logf: logf.write('>> var: ' + var_name + ', fnc: ' + func_name + ', time: ' + str(datetime.now()) + '\n')
                                    return True
                                else:
                                    return False
                            else:
                                return -5
                        else:
                            return -4
                else:
                    return -2
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def search_key_lock(self, var_name: str, full_path: str):
        # @override PySqTppUltInterface.search_key_lock()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid file path
        # return -2  : @var_name is null
        # return -3  : @var_name not found in tqpt source file
        # return -4  : no .tpqt functions lock file found
        
        rslt = None
        nrRslt = None
        sStr = None
        
        # ****a very simple and perhaps most important function of this all,
        # returns a list of function names allowed to change @var_name or
        # None type if no search results gathered at the tpqt file****
        
        try:
            if os.path.isfile(full_path):
                newUltSttp = UltSttp()
                if len(var_name) > 0:
                    # check if @var_name is even listed at the tqpt variable source file, no dank
                    rslt = newUltSttp.tpqt_map(True, None, 'lod_vc', var_name, None, full_path)
                    if rslt == False:
                        return -3
                    else:
                        # switch to the .tpqt function lock file extension file path
                        sStr = full_path.replace('.tqpt', '.tpqt')
                        if os.path.isfile(sStr):
                            fStr = newUltSttp.tpqt_map(True, None, 'lod_vd', var_name, None, sStr)
                            if fStr != '<:!!':
                                cLst = bytes.decode(fStr, 'utf-8').strip(' :>' ).split('\n')
                                # first index is the variable name, remove it and return fnc name(s) list
                                cLst.pop(0)
                                return cLst
                            else:
                                #none found, both @var_name & any allowed function(s) name(s) sublisted
                                return None
                        else:
                            # no .tpqt lock file to search...
                            return -4
                else:
                    return -2
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def overwrite_fnc_lock(self, var_name, func_name, full_path):
        # @override PySqTppUltInterface.overwrite_fnc_lock()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid file path
        # return -2  : var_name and/or func_name is null
        # return -3  : @var_name was not found in .tqpt source file
        # return -4  : no found .tpqt file @ .tqpt source directory
        # return -5  : no search result return for .tpqt file
        # return -6  : invalid variable type @func_name
        
        rslt = None
        
        sStr = None
        fStr = None
        cStr = None
        cLst = None
        
        try:
            if os.path.isfile(full_path):
                newUltSttp = UltSttp()
                if len(var_name) > 0 and len(func_name) > 0:
                    rslt = newUltSttp.tpqt_map(True, None, 'lod_vc', var_name, None, full_path)
                    if rslt == False:
                        return -3
                    else:
                        sStr = full_path.replace('.tqpt', '.tpqt')
                        if os.path.isfile(sStr):
                            fStr = newUltSttp.tpqt_map(True, None, 'lod_vd', var_name, None, sStr)
                            if fStr != '<:!!':
                                cLst = bytes.decode(fStr, 'utf-8').split('\n')
                                if isinstance(func_name, list):
                                    cLen = len(func_name)
                                    cStr = cLst[0] + '\n'
                                    for fnc in range(cLen):
                                        if fnc != cLen-1:
                                            cStr += func_name[fnc] + '\n'
                                        else:
                                            cStr += func_name[fnc] + ':>\n'
                                            break
                                elif isinstance(func_name, str):
                                    cStr = cLst[0] + '\n' + func_name + ':>\n'
                                else:
                                    return -6
                                fStr = bytes.decode(fStr, 'utf-8')
                                with open(sStr, mode='w+') as fObjWf:
                                    sStr = fObjWf.read()
                                    sStr = sStr.replace('\n' + fStr, '')
                                    fObjWf.write(sStr + cStr + '!!!END_TPQT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                            else:
                                return -5
                        else:
                            return -4
                else:
                    return -2
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def print_tqpt_file(self, full_path: str):
        # @override PySqTppUltInterface.print_tqpt_file()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : file path is invalid
        
        try:
            if os.path.isfile(full_path):
                with open(full_path, mode='r') as fObjPtc:
                    with mmap.mmap(fObjPtc.fileno(), length=0, access=mmap.ACCESS_READ) as mObjPtc:
                        vrLns = bytes.decode(mObjPtc.read(), 'utf-8').split('\n')
                        mObjPtc.close()
                    mObjPtc = None
                vrLst = None
                idx = 0
                idxLen = len(vrLns)-1
                # *variable name*
                vrnmRe = re.compile(r'^<.*=')
                # *quanity position*
                vrdtRe = re.compile(r'@qp.*:')
                while idx < idxLen:
                    if idx > 0:
                        vrLst = re.findall(vrnmRe, vrLns[idx])
                        if len(vrLst) > 0:
                            print('\n\n----- ' + vrLst[0].strip('<=') + '\nData: ')
                            vrLst = re.findall(vrdtRe, vrLns[idx])
                            if len(vrLst) > 0:
                                print(vrLst)
                            else:
                                # funny how?
                                print('...non-readable data declaring(s)')
                    idx+=1
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def print_tpqt_file(self, full_path):
        # @override PySqTppUltInterface.print_tpqt_file()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : file path is invalid
        
        try:
            if os.path.isfile(full_path):
                tpPth = full_path.replace('.tqpt', '.tpqt')
                with open(tpPth, mode='r') as fObjPtl:
                    with mmap.mmap(fObjPtl.fileno(), length=0, access=mmap.ACCESS_READ) as mObjPtl:
                        print(bytes.decode(mObjPtl.read(), 'utf-8'))
                        mObjPtl.close()
                    mObjPtl = None
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def scan_py_module(self, var_name: str, full_path: str) -> str:
        # @override PySqTppUltInterface.scan_py_module()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return = !  : no py module found @ given full path
        
        pyStr = None
        cStr = ''
        cCnt = 0
        cLen = None
        cLst = []
        pySet = set()
        pChr = None
        
        swStA = False
        swStB = False
        swStC = False
        swStEE = False
        swStRS = False
        swFc = False
        swCl = False
        
        aChrs = set("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        
        try:
            if os.path.isfile(full_path):
                with open(full_path, 'r+b') as fObjSpm:
                    with mmap.mmap(fObjSpm.fileno(), length=0, prot=mmap.PROT_READ) as mObjSpm:
                        pyStr = bytes.decode(mObjSpm.read(), 'utf-8')
                    mObjSpm.close()
                mObjSpm = None
                for cChr in pyStr:
                    if swFc == False and swCl == False:
                        if cChr == 'e' and pChr == 'd':
                            # ...function name...
                            swFc = True
                        elif cChr == 'l' and pChr == 'c':
                            # ...class name...
                            swCl = True
                            cCnt = 2
                    else:
                    #-------------------------------------------------------------------------------------------------------------------------------
                    # FUNCTION CHECKs/RECORDs
                        if swFc == True:
                            if swStA == False and cChr == 'f':
                                # function define, begin record all the way thru to the
                                # parameters closing ) on next switch flip using cStr
                                swStA = True
                                swStRS = True
                            else:
                                if swStRS == True:
                                    # check if is proper space after the keyword def; of learned on this
                                    # here, python interpreter is strange place @ space chr compares
                                    if pChr == 'f' and cChr == " ":
                                        swStRS = False
                                    else:
                                        swStRS = False
                                        swStFc = False
                                        swStA = False
                                else:
                                    if swStA == True:
                                        if cChr == '(':
                                            # is begin ( of parameters naming, store the function name in the
                                            # set, or is end ) of parameters naming, ?<|split-|parse> ?store to the set
                                            if len(cStr) > 4:
                                                pySet.add(cStr.strip(' '))
                                            cStr = ''
                                        elif cChr == ")":
                                            if len(cStr) > 0:
                                                if swStB == True:
                                                    cLst = cStr.strip(' ').split(':')
                                                    swStEE = True
                                                elif swStB == False and swStC == True:
                                                    cLst = cStr.strip(' ').split(',')
                                                    swStEE = True
                                                elif swStB == False and swStC == False:
                                                    if cStr != ' ' and len(cStr) > 4:
                                                        pySet.add(cStr.strip(' '))
                                                if swStEE == True:
                                                    cLen = len(cLst)
                                                    for idSX in range(cLen):
                                                        if swStB == True:
                                                            if cLst[idSX].find(',') != -1:
                                                                swStA = True
                                                                cStr = ''
                                                                for chr in cLst[idSX]:
                                                                    if swStA == True and chr == ',':
                                                                        swStA = False
                                                                    elif swStA == False:
                                                                        cStr += chr
                                                                if len(cStr) > 4:
                                                                    pySet.add(cStr.strip(' '))
                                                            else:
                                                                if len(cLst[idSX]) > 4:
                                                                    pySet.add(cLst[idSX].strip(' '))
                                                            if idSX == cLen-2:
                                                                break
                                                        else:
                                                            # is swStC, no echo
                                                            if len(cLst[idSX]) > 4:
                                                                pySet.add(cLst[idSX].strip(' '))
                                            swStA = False
                                            swStB = False
                                            swStC = False
                                            swStEE = False
                                            swFc = False
                                            cStr = ''
                                        elif cChr == '\n':
                                            # altogether false method read of comments, some cat typing on a keyboard or etc.
                                            swStA = False
                                            swStB = False
                                            swStC = False
                                            swStEE = False
                                            swFc = False
                                            cStr = ''
                                        else:
                                            if cChr == ":":
                                                # *echo ^lego*
                                                if swStB == False:
                                                    swStB = True
                                            elif cChr == ',':
                                                if swStC == False:
                                                    swStC = True
                                            cStr += cChr
                #-------------------------------------------------------------------------------------------------------------------------------
                # CLASS CHECKs/RECORDs
                        elif swCl:
                            if swStB == False:
                                if cCnt == 2 and cChr == 'a':
                                    swStA = True
                                elif cCnt == 3 and cChr == 's':
                                    pass
                                elif cCnt == 4 and cChr == 's':
                                    pass
                                else:
                                    swStA = False
                                    swCl = False
                                if cCnt < 5:
                                    cCnt+=1
                                else:
                                    swStA = False
                                    swCl = False
                                if cCnt == 5 and swStA == True:
                                    # a class declaring...... throw B on and A off for the class name record
                                    swStB = True
                                    swStA = False
                            else:
                                # skip the space between class keyword <to> class name, swStC
                                if swStC == False:
                                    swStC = True
                                else:
                                    if set(cChr).issubset(aChrs) == False:
                                        if len(cStr) > 4:
                                            pySet.add(cStr)
                                        swStB = False
                                        swStC = False
                                        swCl = False
                                        cStr = ''
                                        cCnt = 0
                                    else:
                                        cStr += cChr
                    pChr = cChr
                #-------------------------------------------------------------------------------------------------------------------------------
                # VARIABLE CHECKs/RECORDs
                # reverse entire string for variable names gather/add to pySet
                pyStrRv = pyStr[::-1]
                # empty memory @ original str
                pyStr = None
                cStr = ''
                swStA = False
                swStRS = False
                for cChr in pyStrRv:
                    if swStRS == False:
                        if cChr == '=':
                            swStA = True
                            swStRS = True
                    else:
                        if swStA == True:
                            swStA = False
                            if cChr == " ":
                                pass
                            else:
                                if set(cChr).issubset(aChrs) == False:
                                    swStRS = False
                                else:
                                    cStr += cChr
                        else:
                            if set(cChr).issubset(aChrs) == False:
                                swStRS = False
                                if len(cStr) > 4:
                                    pySet.add(cStr[::-1])
                                cStr = ''
                            else:
                                cStr += cChr
                # empty memory @ pyStrRv
                pyStrRv = None
                # finally make check if wanted <var_name> is not already listed in the py module,
                # if is then create a suggested smart global variable naming for use as returned
                if set(var_name).issubset(pySet) == False:
                    # return var_name given in parameter, no duplicate finding
                    return var_name
                else:
                    # return a smart variable name,  non-conflict type global variable naming
                    # first check if any invalid chars in var_name parameter given........
                    nChrs = set('0123456789')
                    if set(var_name).issubset(aChrs) == True:
                        swCl = True
                    else:
                        swCl = False
                    rtrnVrnm = ''
                    cStr = ''
                    cCnt = 0
                    cLst = []
                    swStA = False
                    swStB = False
                    for vChr in var_name:
                        if swCl == False:
                            # @var_name has invalid chars, append to cStr any valid chars only
                            if set(vChr).issubset(aChrs) == True:
                                cStr += vChr
                        if vChr == '_':
                            swStA = True
                            cLst.append(cCnt)
                        elif set(vChr).issubset(nChrs) == True:
                            swStB = True
                        cCnt+=1
                    cCnt = 0
                    if swCl == True:
                        # is all valid variable name chars, however is problems duplicate from scan results
                        for fvChr in var_name:
                            if swStA == False and cCnt == 0:
                                rtrnVrnm = '_' + var_name
                                break
                            elif swStA == True and swStB == True:
                                if cCnt == 0 and cLst[0] != 0:
                                    rtrnVrnm = '__' + var_name
                                    break
                                else:
                                    if set(fvChr).issubset(nChrs) == True:
                                        rtrnVrnm += '_'
                                rtrnVrnm += fvChr
                            elif swStA == True and swStB == False:
                                if cCnt == 0 and cLst[0] != 0:
                                    rtrnVrnm = '__' + var_name
                                    break
                                else:
                                    if fvChr == '_':
                                        rtrnVrnm += '_v'
                                rtrnVrnm += fvChr
                            cCnt+=1
                        return rtrnVrnm
                    # is swCl=False, invalid variable name chars previously...or a versatile secret feature:
                    # see if any string length is there first, from any parsing leftover previously @cStr
                    if len(cStr) == 0:
                        # can't return a random variable name here like a staqtapp sar variable
                        return None
                    else:
                        # okay good, as of the same as above -- checking for underscores and/or numbers
                        for fvChr in cStr:
                            if swStA == False and cCnt == 0:
                                rtrnVrnm = '__' + cStr
                                break
                            elif swSta == True and swStB == True:
                                if fvChr == '_' and set(pChr).issubset(nChrs) == False:
                                    rtrnVrnm += '_'
                                else:
                                    if set(fvChr).issubset(nChrs) == False:
                                        pass
                                    else:
                                        if cCnt == 0:
                                            rtrnVrnm += '__'
                                        else:
                                            rtrnVrnm += '_'
                                pChr = fvChr
                                rtrnVrnm += fvChr
                            elif swStA == True and swStB == False:
                                if fvChr == '_':
                                    if cCnt == 0:
                                        rtrnVrnm += '_'
                                    else:
                                        if pChr != '_':
                                            rtrnVrnm += '_'
                                pChr = fvChr 
                                rtrnVrnm += fvChr
                            cCnt+=1
                        return rtrnVrnm
            else:
                return '!'
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def tpqt_map(self, is_read, is_exist, dsg_fnc, var_name, func_name, full_path):
        # @override PySqTppUltInterface.tpqt_map()
        
        fnd = None
        isLst = None
        vrLfLst = None
        tStr = None
        lStr = None
        ptrnStr = None
        cLen = None
        cCnt = None
        
        if is_read == True:
            # ---------- READ TQPT OR TPQT FILES ----------
            if dsg_fnc == 'lod_vc':
                fnd = False
                ptrnStr = re.compile(rb'<'+re.escape(str.encode(var_name))+rb'=')
                with open(full_path, mode='r') as fileObjLod_Vc:
                    with mmap.mmap(fileObjLod_Vc.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjLod_Vc:
                        if re.search(ptrnStr, mmapObjLod_Vc.read()):
                            fnd = True
                        mmapObjLod_Vc.close()
                    mmapObjLod_Vc = None
                return fnd
            elif dsg_fnc == 'lod_vd':
                fnd = False
                ptrnStr = re.compile(rb'<:'+re.escape(str.encode(var_name))+rb'=(?s:.*?).*:>')
                with open(full_path, mode='r') as fileObjLodVd:
                    with mmap.mmap(fileObjLodVd.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjLodVd:
                        for vrMtc in ptrnStr.findall(mmapObjLodVd):
                            if len(vrMtc) > 0:
                                fnd = True
                                tStr = vrMtc
                                break
                        mmapObjLodVd.close()
                    mmapObjLodVd = None
                if fnd == True:
                    return tStr
                else:
                    return '<:!!'
        else:
            # ---------- READ & WRITE TPQT FILES ----------
            if dsg_fnc == 'lod_wl':
                if isinstance(func_name, str) == True:
                    isLst = False
                elif isinstance(func_name, list) == True:
                    isLst = True
                if is_exist == True:
                    fnd = False
                    ptrnStr = re.compile(r'<:'+re.escape(var_name)+r'=(?s:.*?).*:>')
                    with open(full_path, mode='r') as fileObjLodWl:
                        with mmap.mmap(fileObjLodWl.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjLodWl:
                            lStr = bytes.decode(mmapObjLodWl.read(), "utf-8")
                            mmapObjLodWl.close()
                        mmapObjLodWl = None
                    for vrMtc in ptrnStr.findall(lStr):
                        if len(vrMtc) > 0:
                            fnd = True
                            tStr = vrMtc
                            break
                    if fnd == True:
                        lStr = lStr.replace('\n' + tStr, '')
                        vrLfLst = tStr.split('\n')
                        vrLfLst[len(vrLfLst)-1] = vrLfLst[len(vrLfLst)-1].strip(':>')
                        vrLfLst.pop(0)
                    fncSet = set()
                    if isLst == True:
                        for stA in range(len(func_name)):
                            fncSet.add(func_name[stA])
                    if fnd == True:
                        for stB in range(len(vrLfLst)):
                            fncSet.add(vrLfLst[stB])
                    if isLst == False:
                        fncSet.add(func_name)
                    tStr = ''
                    cCnt = 0
                    cLen = len(fncSet)-1
                    if cLen < 0:
                        return False
                    else:
                        for f in fncSet:
                            if cCnt == 0:
                                tStr += '<:' + var_name + '=\n'
                                if cLen > 0:
                                    tStr += f + "\n"
                                else:
                                    tStr += f + ":>\n"
                                    break
                            elif cCnt == cLen:
                                tStr += f + ':>\n'
                                break
                            else:
                                tStr += f + "\n"
                            cCnt+=1
                    lStr = lStr.replace('!!!END_TPQT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!', '')
                    with open(full_path, mode='w') as tpqtFl: tpqtFl.write(lStr + tStr + '!!!END_TPQT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                else:
                    tStr = ''
                    if isLst == True:
                        cLen = len(func_name)
                        cCnt = 0
                        for f in range(cLen):
                            if cCnt == 0:
                                tStr += '<:' + var_name + '=\n'
                                if cLen > 1:
                                    tStr += func_name[f] + '\n'
                                else:
                                    tStr += func_name[f] + ':>\n'
                                    break
                            elif cCnt == cLen-1:
                                tStr += func_name[f] + ':>\n'
                                break
                            else:
                                tStr += func_name[f] + '\n'
                            cCnt+=1
                    else:
                        tStr = '<:' + var_name + '=\n' + func_name + ':>\n'
                    with open(full_path, mode='w') as tpqtFl: tpqtFl.write('<STAQTAPP_DO_NOT_EDIT>\n' + tStr + '!!!END_TPQT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
#______________________________________________________________________________________