# Code File: StaqTapp-1.01 [PySqTpp_Utility.py] main utility functions use




# Staqtapp 1.01.913

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(at)gmail


import PySqTpp_UltInterface

import mmap
import os
#______________________________________________________________________________________

class UltSttp(PySqTpp_UltInterface.PySqTppUltInterface):
    # - settled functions for utility methods -
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
        swFc = False
        swCl = False
        
        #aChrs = set("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        
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
                    # FUNCTION CHECK/RECORD
                        if swFc:
                            if swStA == False and cChr == 'f':
                                # function define, begin record all the way thru to the
                                # parameters closing ) on next switch flip using cStr
                                swStA = True
                            else:
                                if swStA == False:
                                    swFc == False
                                else:
                                    if cChr == '(':
                                        # is begin ( of parameters naming, store the function name in the
                                        # set, or is end ) of parameters naming, ?<|split-|parse> ?store to the set
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
                                                if cStr != ' ':
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
                                                            pySet.add(cStr.strip(' '))
                                                        else:
                                                            pySet.add(cLst[idSX].strip(' '))
                                                        if idSX == cLen-2:
                                                            break
                                                    else:
                                                        # is swStC, no echo
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
                # CLASS CHECK/RECORD
                        elif swCl:
                            if swStB == False:
                                if cCnt == 2 and cChr == 'a':
                                    swStA = True
                                elif cCnt == 3 and cChr == 's':
                                    swStA = True
                                elif cCnt == 4 and cChr == 's':
                                    swStA = True
                                    # Matthew 21:2
                                else:
                                    swStA = False
                                    swCl = False
                                if cCnt < 5:
                                    cCnt+=1
                                else:
                                    swStA = False
                                    swCl = False
                                if cCnt == 4 and swStA == True:
                                    # a class declaring...... throw B on and A off for the class name record
                                    swStB = True
                                    swStA = False
                            else:
                                print('begin of class name record...')
                                swStB = False
                                swCl = False
                                
                #-------------------------------------------------------------------------------------------------------------------------------
                        # k
                #-------------------------------------------------------------------------------------------------------------------------------
                    pChr = cChr
                for i in pySet:
                    print(i)
                return None
            else:
                return '!'
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________



