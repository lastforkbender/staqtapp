# Code File: StaqTapp-1.02 [stpx.py] StaqTapp gzip methods & module calls


# Staqtapp 1.02.411

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import random
#import shutil
import mmap
import stpp
import gzip
import os
import re
import io
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________

#  STAQTAPP - STPX PRO MODULE'S METHODS:


# DEVELOPER NOTE:
# all stpx module functions get the folder path & .tqpt file name from a x_setpath(folder, name)
# gzip call, there is no associated folder path & .tqpt file name parameters of any other method
# or the main stpp module's parallel pilot function calls from this module's functions calls


# [ x_setpath(fldrPth, fleNm) ] - sets folder path & file name to the x_stpx.gz file,
# this function must be called to create the gzip file and have set folder/file path;
# including a ending '/' @fldrPth or the extension '.tqpt' @fleNm is a no to-do

# [ x_getpath(pth) ] - returns list-folder path & filename current set, @pth as normal
# current gzip file: os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz'
# this should be avoided being called directly of normal stpx functions use
    
# [ x_addlist_vars() ] - no parameters, sets a glb var names list to gzip file from set
# .tqpt file path, can/will list any/all variable names of any/all .tqpt glb source files
# this includes viewable sars and sars pointers names listed of any .tqpt sources;
# doesn't add duplicates, replaces all .tqpt var names associated if already listed

# [ x_getlist_vars(isSort) ] - returns (str) list of all glb var names associated to .tqpt
# file currently set in gzip path to/from after a @x_addlist_vars() call, does not
# get all glb var names directly from the .tqpt variable source file, this of use to
# multi-processing encodings or other procedures involving backup tracing, very
# useful to ai-sys that would call ×_findvar() & ×_renamevar() in repeated cycles

# (not yet a fully implemented stpx method)
# [ x_menorahvar(isGreater, isSar, varName) ] - returns a specialized compressed
# palindrome encoded int of any number, multi-processing should be considered

# [ x_makesource(isStatic, isMakeFolder, isEraseSource) ] - calls main stpp function

# [ x_addvar(varName, varData) ] - calls main stpp function

# [ x_renamevar(varName, newVarName) ] - calls main stpp function

# [ x_loadvar_str(varName) ] - calls main stpp function

# [ x_loadvar_deque(isNumbers, varName) ] - calls main stpp function

# [ x_loadsar_remap(isPrmExc, catPin) ] - calls main stpp function

# [ x_changevar(varName, newVarData) ] - calls main stpp function

# [ x_findvar(allSources, varName) ] - calls main stpp function

# [ x_addsar(catPin, varData) ] - calls main stpp function

# [ x_lockvar(varName, fncName) ] - calls utility stpu function

# [ x_keyvar(isLogF, varName, fncName) ] - calls utility stpu function

# [ x_searchkeys(varName) ] - calls utility stpu function

# [ x_lockvar_edit(varName, fncName) ] - calls utility stpu function

# [ x_viewsource() ] - calls utility stpu function

# [ x_viewkeys() ] - calls utility stpu function

#______________________________________________________________________________________

def x_setpath(fldrPth: str, fleNm: str):
    # sets auto fill parameter for folder path & file name on any stpx.x_[parallel method] calls
    # or other stpx related methods using gzip files, don't include a .tqpt extension or / end;
    # the then created stpx folder will be in path of this module's current running directory
    try:
        mdlPthX = os.path.dirname(os.path.abspath(__file__))
        stpxNw = False
        if os.path.isdir(mdlPthX + '/stpx') == False:
            os.makedirs(mdlPthX + '/stpx')
            stpxNw = True
        if os.path.isfile(mdlPthX + '/stpx/x_stpx.gz') == False or stpxNw == True:
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpW:
                gzObjXtpW.write(b':pth<' + str.encode(fldrPth) + b'>\n:fle<' + str.encode(fleNm) + b'>')
            gzObjXtpW = None
        else:
            gzSrc = None
            pthLst = None
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'rb') as gzObjXtpR:
                gzSrc = gzObjXtpR.read()
                pthLst = re.findall(rb':pth<.*?>\n:fle<.*?>', gzSrc)
            gzObjXtpR = None
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpN:
                gzObjXtpN.write(gzSrc.replace(pthLst[0], b':pth<' + str.encode(fldrPth) + b'>\n:fle<' + str.encode(fleNm) + b'>'))
            gzObjXtpN = None
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_addlist_vars() -> int:
    # sets all global variable names listed in a .tqpt file to a listed stack in the gzip
    # [/x_stpx.gz] made from x_setpath() call---gzip to be present & valid .tqpt set path
    # currently from set path .tqpt source file; method allows var name listing any tqpt:
    # var names added to gzip stack are listed as ':var<@tqpt_file_name:@var_name>'
    # returns replace count int if gzip of prior listed variable name(s) set of .tqpt name
    # of has then fully replaced that prior set wether changes or not to the .tqpt file
    # otherwise returns None ***all x viewable: var, sar and sar pointer type namings***
    try:
        pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
        gzSrc = None
        with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'rb') as gzObjSlvR:
            gzSrc = gzObjSlvR.read()
        gzObjSlvR = None
        ptrn = re.compile(rb'<.*?=')
        varNmLst = []
        with open(pth[0] + '/' + pth[1] + '.tqpt', mode='r', encoding='utf-8') as fObjSlvR:
            with mmap.mmap(fObjSlvR.fileno(), length=0, access=mmap.ACCESS_READ) as fMpObjSlvR:
                for mtch in ptrn.findall(fMpObjSlvR):
                   if len(mtch) >= 3:
                       varNmLst.append(b'\n:var<' + str.encode(pth[1]) + b':' + mtch.strip(b'<=') + b'>')
                fMpObjSlvR.close()
            fMpObjSlvR = None
        if len(varNmLst) > 1:
            varNmLst.pop(0)
            if gzSrc.find(b':var<' + str.encode(pth[1]) + b':') > -1:
                cnt = 0
                px = [0,0]
                pStrt = True
                ptrn = re.compile(rb':var<' + re.escape(str.encode(pth[1])) + rb':.*?>')
                for fnd in ptrn.finditer(gzSrc):
                    if pStrt == True:
                        pStrt = False
                        px[0] = fnd.start()-1
                    px[1] = fnd.end()
                    cnt+=1
                gzStrA = gzSrc[0:px[0]]
                if px[1] == len(gzSrc):
                    with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjASlvW:
                        gzObjASlvW.write(gzStrA + b''.join(varNmLst))
                    gzObjASlvW = None
                else:
                    gzStrB = gzSrc[px[1]:len(gzSrc)]
                    with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjBSlvW:
                        gzObjBSlvW.write(gzStrA + b''.join(varNmLst) + gzStrB)
                    gzObjBSlvW = None
                return cnt
            else:
                with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjCSlvW:
                    gzObjCSlvW.write(gzSrc + b''.join(varNmLst))
                gzObjCSlvW = None
                return None
        else:
            return None
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_getpath(pth: str) -> list:
    # returns @:pth<...> and @:fle<...> stpx gz listings as a (str)list
    try:
        with gzip.open(pth, 'rb') as gzObjGp:
            pthLst = re.findall(rb':pth<.*?>\n:fle<.*?>', gzObjGp.read())
            pthLst = pthLst[0].split(b'\n')
            pthLst[0] = bytes.decode(pthLst[0].replace(b':pth<', b"").strip(b'>'), 'utf-8')
            pthLst[1] = bytes.decode(pthLst[1].replace(b':fle<', b"").strip(b'>'), 'utf-8')
        gzObgGp = None
        return pthLst
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_menorahvar(isGreater: bool, isSar: bool, varName: str):
    # THIS FUNCTION NOT FULLY IMPLEMENTED YET
    if isSar == False:
        pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
        rslt = stpp.loadvar_str(varName, pth[0], pth[1])
        if isinstance(rslt, list) == True:
            pass
        elif isinstance(rslt, str) == True:
            if set(rslt).issubset(nSt) == True:
                pass
            else:
                # @varName's data, invalid chars for palindrome number return
                return None
        else:
            # @varName's data, invalid data type, neither a str array or str...
            return None
    else:
        # check if a proper staqtapp sar variable naming, has a unique ten digit dsg
        pass
#______________________________________________________________________________________

def x_get_menorah_palindrome_encoding(isGreater, src):
    # THIS METHOD NOT FULLY IMPLEMENTED YET
    # @src is any str of seq numbers wether negative or not, this method is for and
    # will compress number to a menorah palindrome return equality responsible
    
    # https://ibb.co/C12Qbr4
    # the kindness of a child no man made, no man can give and no man above
    
    nSt = set('-0123456789')
    stLst = []
    dtLst = []
    rtrnStr = ''
    prvX = '1'
    lStCnt = 1
    rStCnt = 1
    ix = None
    rx = None
    cg = None
    cgPl = None
    cgRl = False
    cgHld = False
    
    src = src.replace('-', '')
    for x in src:
        ix = int(x)
        rx = int(prvX)
        if ix == rx-1: lStCnt+=1
        elif ix == rx+1: lStCnt-=1
        elif ix-1 == rx: rStCnt+=1
        elif ix+1 == rx: rStCnt-=1
        elif ix == rx:
            if lStCnt > rStCnt: lStCnt-=1
            elif lStCnt < rStCnt: rStCnt-=1
            else:
                if lStCnt < 0:
                    lStCnt+=1
                    cgPl = True
                if rStCnt < 0:
                    rStCnt+=1
                    cgPl = True
                if lStCnt > 0:
                    lStCnt-=1
                    cgRl = True
                if rStCnt > 0: 
                    rStCnt-=1
                    cgRl = True
        if lStCnt == rStCnt: cgHld = True
        if x == prvX: stLst.append(x)
        else: dtLst.append(x)
        if cgPl == True and cgRl == True and cgHld == True:
            lStCnt = 1
            rStCnt = 1
        cgPl = False
        cgRl = False
        cgHld = False
        prvX = x
    prvX = 'q'
    cgPl = 0
    if lStCnt == rStCnt: cgPl = 1
    elif len(src) == 1: cgPl = 1
    else:
        cgHld = True
        cg = 1
        for y in src:
            ix = int(y)
            if ix < lStCnt and cg >= rStCnt: lStCnt = ix
            if ix > rStCnt and cg <= lStCnt: rStCnt = ix
            cg+=1
        if lStCnt == 0: lStCnt = 1
        if rStCnt == 0: rStCnt = 1
        if lStCnt == rStCnt: cgPl = 1
        else:
            if isGreater == True:
                if lStCnt > rStCnt: prvX = 'l'
                else: prvX = 'r'
            else:
                if lStCnt < rStCnt: prvX = 'l'
                else: prvX = 'r'
    lens = [len(stLst), len(dtLst)]
    ix = []
    rx = []
    cgRl = None
    cgNb = None
    cgNx = False
    kr_kn = 1
    if lens[0] > 0:
        for n in range(lens[0]):
            if stLst[n] == cgRl:
                ix.append(stLst[n])
                for nas in range(len(ix)):
                    if lens[0] == len(ix): break
                    else:
                        if ix[nas] == '1' or ix[nas] == '3' or ix[nas] == '5' or ix[nas] == '7' or ix[nas] == '9': kr_kn+=1
            cgRl = stLst[n]
    else:
        if cgHld == True: cgNb = True
        else: cgNb = False
    if lens[1] > 2:
        if cgPl != None:
            if rStCnt > 1:
                for a in range(len(dtLst)):
                    if lStCnt >= 1:
                        if prvX == 'q':
                            if kr_kn > 1 and cgNb == False:
                                if cgRl == dtLst[a]:
                                    if len(dtLst) > 1: dtLst.pop(a)
                                    else:
                                        lens.append(len(dtLst))
                                        cgNx = True
                                        break
                                kr_kn-=1
                            else:
                                if cgNb == True:
                                    if cgRl == dtLst[a]:
                                        if len(dtLst) > 1: dtLst.pop(a)
                                        else:
                                            lens.append(len(dtLst))
                                            cgNx = True
                                            break
                                    kr_kn-=2
                                else:
                                    if cgRl == dtLst[a]:
                                        if len(dtLst) > 1:
                                            stLst.append(dtLst[a])
                                            dtLst.pop(a)
                                        else:
                                            lens.append(len(dtLst))
                                            cgNx = True
                                            break
                                        kr_kn+=2
                        elif prvX == 'l':
                            if cgNb == True and lStCnt > 3:
                                if len(dtLst) > 1:
                                    if cgRl == dtLst[a]:
                                        dtLst.pop(a)
                                        kr_kn-=1
                                    else:
                                        kr_kn+=1
                                else:
                                    lens.append(len(dtLst))
                                    cgNx = True
                                    break
                            else:
                                if cgRl == dtLst[a] and len(dtLst) > 1 and cgNb == False:
                                    dtLst.pop(a)
                                    kr_kn-=2
                                else: pass
                        elif prvX == 'r':
                            if cgRl == dtLst[a] and len(dtLst) > 1:
                                dtLst.pop(a)
                                kr_kn+=1
                            else:
                                if len(dtLst) == 1:
                                    cgNx = True
                                    break
                                if cgNb == True: kr_kn-=1
                                else: kr_kn+=1
                    else:
                        # lStCnt is less than 1
                        if prvX == 'q': pass
                        elif prvX == 'l': pass
                        elif prvX == 'r': pass
                    cgRl = dtLst[a]
            else:
                # rStCnt is less than 1
                #for b in range(lens[1]):
                pass                        
        else:
            #cgPl=1
            pass
    else:
        # lens[1]<3
        pass
        
    print(dtLst)
    print(stLst)
    print(ix)
    print(lens)
    print('lStCnt: ' + str(lStCnt))
    print('rStCnt: ' + str(rStCnt))
    print(prvX)
    print(kr_kn)
#______________________________________________________________________________________

def x_getlist_vars(isSort: bool) -> list:
    # returns a (str) list of all glb variable names associated with set .tqpt file name
    # from x_stpx.gz after a @x_addlist_vars() call with gzip set path .tqpt file name
    # many options open to this type return including no glb var name repeated ever
    # of any .tqpt variable source file
    try:
        pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
        ptrn = re.compile(r':var<' + re.escape(pth[1]) + r':.*?>')
        varNmLst = []
        with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'rb') as gzObjGlvR:
            gzSrc = bytes.decode(gzObjGlvR.read(), 'utf-8')
            for mtch in ptrn.findall(gzSrc):
                varNmLst.append(mtch.replace(':var<' + pth[1] + ':', "").strip('>'))
            gzSrc = None
        gzObjGlvR = None
        if len(varNmLst) > 0:
            if isSort == False:
                return varNmLst
            else:
                if len(varNmLst) == 1:
                    return varNmLst
                else:
                    varNmLst.sort()
                    return varNmLst
        else:
            return None
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_makesource(isStatic: bool, isMakeFolder: bool, isEraseSource: bool):
    # calls pilot function stpp.makesource() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.makesource(isStatic, isMakeFolder, isEraseSource, pth[0], pth[1])
#______________________________________________________________________________________

def x_addvar(varName: str, varData: str):
    # calls pilot function stpp.addvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.addvar(varName, varData, pth[0], pth[1])
#______________________________________________________________________________________

def x_renamevar(varName: str, newVarName: str):
    # calls pilot function stpp.renamevar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.renamevar(varName, newVarName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadvar_str(varName: str):
    # calls pilot function stpp.loadvar_str() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    return stpp.loadvar_str(varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadvar_deque(isNumbers: bool, varName: str):
    # calls pilot function stpp.loadvar_deque() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    return stpp.loadvar_deque(isNumbers, varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadsar_remap(isPrmExc: bool, catPin: str):
    # calls pilot function stpp.loadsar_remap() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.loadsar_remap(isPrmExc, catPin, pth[0], pth[1])
#______________________________________________________________________________________

def x_changevar(varName: str, newVarData: str):
    # calls pilot function stpp.changevar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.changevar(varName, newVarData, pth[0], pth[1])
#______________________________________________________________________________________

def x_findvar(allSources: bool, varName: str):
    # calls pilot function stpp.findvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    return stpp.findvar(allSources, varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_addsar(catPin: str, varData: str):
    # calls pilot function stpp.addsar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.addsar(catPin, varData, pth[0], pth[1])
#______________________________________________________________________________________

def x_lockvar(varName: str, fncName: str):
    # calls utility function stpp.lockvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.lockvar(varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_keyvar(isLogF: bool, varName: str, fncName: str):
    # calls utility function stpp.keyvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    return stpp.keyvar(isLogF, varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_searchkeys(varName: str):
    # calls utility function stpp.searchkeys() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    return stpp.searchkeys(varName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_lockvar_edit(varName: str, fncName: str):
    # calls utility function stpp.lockvar_edit() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.lockvar_edit(varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_viewsource():
    # calls utility function stpp.viewsource() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.viewsource(pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_viewkeys():
    # calls utility function stpp.viewkeys() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
    stpp.viewkeys(pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________




















