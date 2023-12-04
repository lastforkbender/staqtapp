# Code File: StaqTapp-1.02 [stpx.py] StaqTapp gzip methods & module calls


# Staqtapp 1.02.390

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


#import shutil
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
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________

def x_setpath(fldrPth: str, fleNm: str):
    # sets auto fill parameter for folder path & file name on any stpx.x_[parallel method] calls
    # or other stpx related methods using gzip files, don't include a .tqpt extension or / chars;
    # the then created stpx folder will be in path of this module's current running directory
    try:
        mdlPthX = os.path.dirname(os.path.abspath(__file__))
        stpxNw = False
        if os.path.isdir(mdlPthX + '/stpx') == False:
            os.makedirs(mdlPthX + '/stpx')
            stpxNw = True
        if os.path.isfile(mdlPthX + '/stpx/x_stpx.gz') == False or stpxNw == True:
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpW:
                gzObjXtpW.write(b':pth<' + str.encode(fldrPth) + b'>\n:fle<' + str.encode(fleNm) + b'>\n')
            gzObjXtpW = None
        else:
            gzSrc = None
            pthLst = None
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'rb') as gzObjXtpR:
                gzSrc = gzObjXtpR.read()
                pthLst = re.findall(rb':pth<.*?>\n:fle<.*?>', gzSrc)
            gzObjXtpR = None
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpN:
                gzObjXtpN.write(gzSrc.replace(pthLst[0], b':pth<' + str.encode(fldrPth) + b'>\n:fle<' + str.encode(fleNm) + b'>\n'))
            gzObjXtpN = None
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
    
    if isSar == False:
        pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
        rslt = stpp.loadvar_str(varName, pth[0], pth[1])
        if isinstance(rslt, list) == True:
            
        elif isinstance(rslt, str) == True:
            if set(rslt).issubset(nSt) == True:
                return x_get_menorah_palindrome_encoding(isGreater, rslt)
            else:
                # @varName's data, invalid chars for palindrome number return
                return None
        else:
            # @varName's data, invalid data type, neither a str array or str...
            return None
    else:
        # check if a proper staqtapp sar variable naming, has a unique ten digit dsg
    
#______________________________________________________________________________________

def x_get_menorah_palindrome_encoding(isGreater, src) -> int:
    
    nSt = set('-0123456789')
    stLst = []
    dtLst = []
    prvX = '1'
    lStCnt = 1
    rStCnt = 1
    ix = None
    rx = None
    cgPl = False
    cgRl = False
    cgHld = False
    
    src = src.replace('-', '')
    for x in src:
        ix = int(x)
        rx = int(prvX)
        # thee count all nearest multi-loops LtoR & RtoL; zero as the only loop is
        # irrelevant here, zero cannot escape placeholding of one and never has
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
        if lStCnt == rStCnt:
            # thee count a mirrored expansion equal?
            cgHld = True
        if x == prvX:
            stLst.append(x)
        else:
            dtLst.append(x)
        if cgPl == True and cgRl == True and cgHld == True:
            # thee count is a mirrored expansion equal, make wave
            lStCnt = 1
            rStCnt = 1
        cgPl = False
        cgRl = False
        cgHld = False
        prvX = x
    prvX = 'q'
    # thee rod-to-ratio chai'ohm, one of One, or both pairing inanimate One
    if lStCnt == rStCnt: cgPl = 1
    elif len(rslt) == 1: cgPl = 1
    else:
        cgHld = True
        # thee needed least and greatest digit of this number source... once
        # again if least is zero, then is irrelevant to remove placehold of one;
        # nothing is impossible, not nothing is possible of these type counts
        lStCnt = 9
        rStCnt = 0
        for y in src:
            ix = int(y)
            if ix < lStCnt: lStCnt = ix
            if ix > rStCnt: rStCnt = ix
        if lStCnt == 0: lStCnt = 1
        if rStCnt == 0: rStCnt = 1
        # thee normal all quantum type summary rod projection again, one
        if lStCnt == rStCnt: cgPl = 1
        else:
            # thee not so normal as to/from any void, which is greater or lesser?
            # this can be hard to explain, has delayed-choice circumstances not
            # only reversible @isGreater parameter, yet also below >< syntax use,
            # what has happened already happened, likely @ a expansion equal
            # where a similiar reset to changes of similiar count did merge
            if isGreater == True:
                if lStCnt > rStCnt: prvX = 'l'
                elif lStCnt == rStCnt: prvX = 'q'
                else: prvX = 'r'
            else:
                if lStCnt < rStCnt: prvX = 'l'
                elif lStCnt == rStCnt: prvX = 'q'
                else: prvX = 'r'
        # finally the more easy part, assemble the palindrome compress return
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