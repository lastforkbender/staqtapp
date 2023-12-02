# Code File: StaqTapp-1.02 [stpx.py] StaqTapp gzip methods & module calls


# Staqtapp 1.02.381

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
        mdlPthX = os.path.dirname(os.path.abspath(__file__)) + '/stpx'
        stpxNw = False
        if os.path.isdir(mdlPthX) == False:
            os.makedirs(mdlPthX)
            stpxNw = True
        if os.path.isfile(mdlPthX + '/stpx/x_stpx.gz') == False or stpxNw == True:
            with gzip.open(mdlPthX + '/x_stpx.gz', 'wb') as gzObjXtpW:
                with io.TextIOWrapper(gzObjXtpW, encoding='utf-8') as gzObjXtpEncW:
                    gzObjXtpEncW.write(':pth<' + fldrPth + '>\n:fle<' + fleNm + '>\n')
        else:
            with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'ab') as gzObjXtpA:
                with io.TextIOWrapper(gzObjXtpA, encoding='utf-8') as gzObjXtpEncA:
                    gzObjXtpEncA.write(':pth<' + fldrPth + '>\n:fle<' + fleNm + '>\n')
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_getpath(pth: str) -> list:
    # returns @:pth<...> and @:fle<...> stpx gz listings as a (str)list
    try:
        with gzip.open(pth, 'rb') as gzObjGp:
            with io.TextIOWrapper(gzObjGp, encoding='utf-8') as gzObjGpEnc:
                pthLst = re.findall(r':pth<.*?>\n:fle<.*?>', gzObjGpEnc.read())
                pthLst = pthLst[0].split('\n')
                pthLst[0] = pthLst[0].replace(':pth<', "").strip('>')
                pthLst[1] = pthLst[1].replace(':fle<', "").strip('>')
                return pthLst
    except Exception as e:
        print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

def x_makesource(isStatic, isMakeFolder, isEraseSource):
    # calls pilot function stpp.makesource() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.makesource(isStatic, isMakeFolder, isEraseSource, pth[0], pth[1])
#______________________________________________________________________________________

def x_addvar(varName, varData):
    # calls pilot function stpp.addvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.addvar(varName, varData, pth[0], pth[1])
#______________________________________________________________________________________

def x_renamevar(varName, newVarName):
    # calls pilot function stpp.renamevar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.renamevar(varName, newVarName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadvar_str(varName):
    # calls pilot function stpp.loadvar_str() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.loadvar_str(varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadvar_deque(isNumbers, varName):
    # calls pilot function stpp.loadvar_deque() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.loadvar_deque(isNumbers, varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_loadsar_remap(isPrmExc, catPin):
    # calls pilot function stpp.loadsar_remap() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.loadsar_remap(isPrmExc, catPin, pth[0], pth[1])
#______________________________________________________________________________________

def x_changevar(varName, newVarData):
    # calls pilot function stpp.changevar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.changevar(varName, newVarData, pth[0], pth[1])
#______________________________________________________________________________________

def x_findvar(allSources, varName):
    # calls pilot function stpp.findvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.findvar(allSources, varName, pth[0], pth[1])
#______________________________________________________________________________________

def x_addsar(catPin, varData):
    # calls pilot function stpp.addsar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.addsar(catPin, varData, pth[0], pth[1])
#______________________________________________________________________________________

def x_lockvar(varName, fncName):
    # calls utility function stpp.lockvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.lockvar(varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_keyvar(isLogF, varName, fncName):
    # calls utility function stpp.keyvar() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.keyvar(isLogF, varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_searchkeys(varName):
    # calls utility function stpp.searchkeys() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.searchkeys(varName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_lockvar_edit(varName, fncName):
    # calls utility function stpp.lockvar_edit() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.lockvar_edit(varName, fncName, pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_viewsource():
    # calls utility function stpp.viewsource() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.viewsource(pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________

def x_viewkeys():
    # calls utility function stpp.viewkeys() without needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/staqtapp.gz')
    stpp.viewkeys(pth[0] + '/' + pth[1] + '.tqpt')
#______________________________________________________________________________________