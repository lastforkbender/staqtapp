# Code File: StaqTapp-1.01 [PySqTpp_Utility.py] main utility functions use




# Staqtapp 1.02.073

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import PySqTpp_UltInterface

import mmap
import os
import re
#______________________________________________________________________________________

class UltSttp(PySqTpp_UltInterface.PySqTppUltInterface):
    # - settled functions for utility methods -
#______________________________________________________________________________________

    def print_tqpt_file(self, full_path: str):
        # @override PySqTppUltInterface.print_var_or_sar()
        
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
                vrnmRe = re.compile(r'^<\w*=')
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
                    # return var_name given in parameter
                    return var_name
                else:
                    #TO-DO
                    pass
            else:
                return '!'
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________



