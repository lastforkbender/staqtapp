# Code File: StaqTapp-1.02 [stpx.py] StaqTapp gzip methods & module calls


# Staqtapp 1.02.387

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

def x_tweedvar(isGreater: bool, isSar: bool, varName: str):
    # returns a palindrome set number from a number(s), @varName's data
    # if @isGreater=True then arranges the number(s) greatest inward to outer
    # this method will always return a twin 3-digit number regardless of original;
    # no from zero escaping a [ONE] placehold or a "man-mon"-AC nonexist trust;
    # no zero pairing is set most inward or most outward of branching [ONE]
    # if any number(s) are of a decimal notation, returns None or None in a list;
    # of @varName is sar variable name then returns that name dsg as a sweed
    # does not return the sar variable's number data reconstructed if any digits
    # calls pilot function stpp.loadvar_str() without the needed parameters
    # of a folder & file --> .tqpt source path @x_setpath() as already set
    nSt = set('-0123456789')
    stLst = []
    dtLst = []
    lStCnt = 0
    rStCnt = 0
    cnt = 0
    if isSar == False:
        pth = x_getpath(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
        rslt = stpp.loadvar_str(varName, pth[0], pth[1])
        if isinstance(rslt, list) == True:
            
        else:
            if set(rslt).issubset(nSt) == True:
                for x in rslt:
                    if x != '-':
                        # first of this menorah type counting, how many +1 or -1 loops?
                        # ...and cache the retains of pairing slots encountered to digits
                        # if more placeholds determined, not a simple fade count then
                        # each multiple look(loop) ahead or behind is of < > equal outs
                        # menorah always cHalf rotational +/-loop to a whool loop [ONE]
                        # of counting multi-loop any digit, not single loop aka 'nero-zero'
                        # by which thru fear of nonexist(nero-zero) has caused too many
                        # lies, thefts, murders, wars, ongoing destroy of earth [manmon]
                        if int(x) == int(prvX)-1: lStCnt+=1
                        elif int(x) == int(prvX)+1: lStCnt-=1
                        elif int(x)-1 == int(prvX): rStCnt+=1
                        elif int(x)+1 == int(prvX): rStCnt-=1
                        if lStCnt == rStCnt:
                            lStCnt = 1
                            rStCnt = 1
                        if x == prvX:
                            stLst.append(x)
                        else:
                            dtLst.append(x)
                        prvX = x
                        cnt+=1
                # qx = central/rotational-apparent position alpha observed
                qx = None
                # Chai'ohm: one placehold from One, inescapable loop exist via
                # resistance as utterly already all now established from All(El),
                # or as time(new) as resistance you cannot change to finite loop
                # as and/or a dead stop nothing/nero-zero of time(future=past)
                # a absolute impossible conclusion of any quantum reality no
                # matter the education level or any amount of manmon trusted
                # .......or from destructive ignorant pride aka time = money
                if lStCnt == rStCnt: qx = 1
                elif cnt == 1: qx = 1
                else:
                    cLen = None
                    dtLen = len(dtLst)
                    stLen = len(stLst)
                    dtGt = False
                    if dtLen > stLen:
                        dtGt = True
                        cLen = dtLen
                    else: cLen = stLen
                    for y in range(cLen):
                        # determine which numbers(loops) are of a greater farthest or least
                        # farthest from the least or greater number pairing already observed;
                        # this single pairing is always chai'ohm to a previous pair expanding
                        # inescapable to one placeholding resolve, @cnt used as a delimiter
                        # of any LtoR or RtoL nested accumlate further compressions, this
                        # may be complicated to understand because of the teachings non-
                        # exist actually exist, which was the next purposed lie in Eden after
                        # the lie you are smarter.... to cause fear of nonexist; fear of non-
                        # exist is also the most dangerous concept a AI can take on
            else:
                # @varName's data, invalid chars for a tweedvar() palindrome number return
                return None
    else:
        # check if a proper staqtapp sar variable naming, of a unique ten digit dsg
    
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