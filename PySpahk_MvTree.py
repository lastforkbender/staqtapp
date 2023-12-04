# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - PySpahk_MvTree.py - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - -
# - - - -
# - - -
# - - -

# ***** This module is part of the SolaceXn AI software package *****

# This module is intended for very complex tree operations of the
# staqtapp library rev9 self-replication module building, however
# the overall functional aspects can be used anywhere needed for
# deep nested branching conditionals; and give unique insight into
# what can be done with dict type objects at a base level parsing,
# when speed is not a main spec for your own project's needs.

# Working status of current encodings for PySpahk_MvTree module
# will soon be of a TEIR-1 programming status, including rotational
# abstracts of embedded compressions/expansions never done or
# seen used of environment variable layering models, coherent use
# of distributed tree data actions involving inverted probability re---
# actions never done or seen/used of environment variable data 
# compiles in a self-replicate encoding abstract and use of further
# mathematical, other TEIR-1 global tree variable interlinks.

# Though these future mathematical exposures of conditions to
# the Staqtapp python library control over environment variables,
# is not exclusive to that library's self-replicate features scope.


# email: 5deg.blk.blt.cecil(@)gmail
# contact: https://pastebin.com/eumqiBAx
# tehts: https://ibb.co/3zjHL29


# Staqtapp v1.02 modules are required:
# https://github.com/lastforkbender/staqtapp
import stpp

import datetime
import hashlib
import pickle
import math
import ast
import os
import re


# made folder path from this module's current run place, where trees/backups are staqtapp filed
__SMT_PTH = os.path.dirname(os.path.abspath(__file__)) + '/spkmvtr'
# _________________________________________________________________________________________

class AbsTrek(dict):
    # applies a general serialized dictionary type tree structure
    
    # NOTE: This module does not allow chars of  \n':,☆ or { }
    # in  branch-keys or branch-values, all other chars allowed.
    # To use those chars you can substitute char encodings to
    # a later use of str.replace() or re.sub() as needed returns.
    
    def __missing__(self, ent):
        rgr = self[ent] = type(self)()
        return rgr
        
    def __init__(self, dt = {}):
        for ix, dt in dt.items():
            if isinstance(dt, dict):
                self[ix] = type(self)(dt)
            else:
                self[ix] = dt
                
    def __eq__(self, other):
        return isinstance(self, AbsTrek) and self.dt == other.dt
# _________________________________________________________________________________________

def maketree(keepBackup: bool, treeName: str, initialPathList: list) -> int:
    
    # saves a binary outline AbsTrek() dictionary tree type object to a staqtapp .tqpt source
    # file then returns the total number of top branches created of the tree object retained;
    # keepBackup=True adds backup entry to a .tqpt source with a restore number tracking
    
    # ***** applies a top branch path with @initialPathList, any numbers converted to str *****
    
    # EXAMPLE:
    # ipl = ['fee', 'fi', 4, 'foo']
    # *.maketree(True, treeA, ipl)
    # tqpt filed begin treeA data, saved result >>> b{ 'fee' :{ 'fi' :{ '4' :{ 'foo' } } } }
    
    try:
        if isinstance(treeName, str) == True and len(treeName) > 0:
            iplLen = len(initialPathList)
            if isinstance(initialPathList, list) and iplLen > 0:
                cStr = str(initialPathList[0])
                if __char_check(cStr) == True:
                    bLst = ["{'" + cStr + "'"]
                else:
                    raise Exception("<pyspahk_mvtree.maketree()> invalid chars @initialPathList; non-allowed chars are \n,':{}☆")
                trStr = None
                x = 1
                if iplLen > 1:
                    while x < iplLen:
                        cStr = str(initialPathList[x])
                        if __char_check(cStr) == True:
                            bLst.append(":{'" + cStr + "'")
                        else:
                            raise Exception("<pyspahk_mvtree.maketree()> invalid chars @initialPathList; non-allowed chars are \n,':{}☆")
                        x+=1
                    trStr = ''.join(bLst)
                    x = 0
                    bLst = []
                    while x < iplLen:
                        bLst.append('}')
                        x+=1
                    trStr = trStr + ''.join(bLst)
                else:
                    trStr = bLst[0] + '}'
                try:
                    # make new staqtapp .tqpt variables source folder/file from this current module's path
                    stpp.makesource(False, True, False, None, 'spkmvtr')
                except Exception as e:
                    # if this happens... both folder/.tqpt glb vars source file should already be there
                    pass
                # add new abs tree to the .tqpt source file; from this current module's run directory,
                # also a back up entry of the starting tree for a basis of restore functionality if so
                dct = pickle.dumps(AbsTrek(ast.literal_eval(trStr)), 0).decode().replace('\n', '☆')
                stpp.addvar(treeName, '@qp(' + dct + '):', __SMT_PTH, 'spkmvtr')
                if keepBackup == True:
                    # backup tree name will be of a added '_bck_1' extending as the first backup done
                    __gloke_tack(False, 'mt', treeName, '@qp(' + dct + '):')
                return iplLen
            else:
                return None
        else:
            raise Exception("<pyspahk_mvtree.maketree()> error: invalid parameter @treeName")
    except Exception as e:
        print("<pyspahk_mvtree.maketree()> error: ", e)
# _________________________________________________________________________________________

def addbranch(keepBackup: bool, treeName: str, posBranchId, newBranchId, newBranchVal) -> int:
    
    # this method literally adds a branch at the bracket string manipulation
    # level, any value assigned to @posBranchId is replaced by the new branch
    # inserted, if @newBranchVal is None, the keyword 'spahk-knot' is added
    # for features of probability integrations and custom sets use for ------
    # staqtapp's rev9 self-replication modules/libraries building; the below
    # examples show results before & after python parses the dict type string
    # this module parses between bracket manipulations for such custom nests:
    
    # EXAMPLE 1:
    # spahkmvtree ---> {'a':{'b':{'c':'vl1','d':'vl2'}, 'e':'vl3'}}
    # .addbranch(True, 'spahkmvtree', 'c', 2035, None)
    # results --> {'a':{'b':{'c':{'2035':'spahk-knot'}, 'd':'vl2'}, 'e':'vl3'}}
    
    # 'vl1' now a nested branch, not a separate value, this result returns int 1
    
    # EXAMPLE 2:
    # spahkmvtree ---> {'a':{'b':{'c':'vl1'},'e':'vl3'}}
    # .addbranch(True, 'spahkmvtree', 'b', 2056, None)
    # results --> {'a':{'b':{'2056':'spahk-knot'},'b_2056':{'c':'vl1'},'e':'vl3'}}
    
    # 'b' now hoplinked to branch&value, however not full link replace parse @ 'b_2056'
    # this feature serves as replace options and some advanced features, returns int 2
    
    # EXAMPLE 3:
    # spahkmvtree ---> {'a':{'b':{'c'},'e':'vl3'}}
    # .addbranch(True, 'spahkmvtree', 'c', 2032, 2051)
    # results --> {'a':{'b':{'2032':'2051'},'e':'vl3'}}
    
    # 'c' is complete replaced by {'2032':'2051'} branch, returns int 1
    
    try:
        trRwSrc = None
        if isinstance(treeName, str) == True and len(treeName) > 0:
            # search the staqtapp .tqpt source file to find @treeName
            if stpp.findvar(False, treeName, __SMT_PTH, 'spkmvtr') == True:
                # is there, get the stored pickled string form ---- for backup purposes also
                trRwSrc = stpp.loadvar_str(treeName, __SMT_PTH, 'spkmvtr')
                # check if any invalid chars; @posBranchId already checked @maketree()
                if __char_check(str(newBranchId)) == False:
                    raise Exception("<pyspahk_mvtree.maketree()> invalid chars @newBranchId; non-allowed chars are \n,':{}☆")
                if __char_check(str(newBranchVal)) == False:
                    raise Exception("<pyspahk_mvtree.maketree()> invalid chars @newBranchVal; non-allowed chars are \n,':{}☆")
                # check if staqtapp .tqpt var file has the needed __KLF_DSG variable listed
                if stpp.findvar(False, '__KLF_DSG', __SMT_PTH, 'spkmvtr') == False:
                    stpp.addvar('__KLF_DSG', '@qp(Null):', __SMT_PTH, 'spkmvtr')
                    # pass to a  new staqtapp .tpqt lock file which functions are allowed to edit it
                    fncLst = ['__krosh_nook', '__equal_branch', '__gloke_tack']
                    stpp.lockvar('__KLF_DSG', fncLst, __SMT_PTH + '/spkmvtr.tqpt')
                # add the new branch id and value if any
                rslt = __krosh_nook(False, 'ab', str(pickle.loads(str.encode(trRwSrc.replace('☆', '\n')))), str(posBranchId), str(newBranchId), str(newBranchVal))
                if rslt == -1:
                    raise Exception("<pyspahk_mvtree.addbranch()> error: '" + posBranchId + "' is a invalid position branch, not found")
                elif rslt == -2:
                    raise Exception("<pyspahk_mvtree.addbranch()> error: '" + posBranchId + "' is a branch-value, not a valid branch-key")
                elif rslt == -3:
                    raise Exception("<pyspahk_mvtree.addbranch()> error: invalid parameter(s) @posBranchId and/or @newBranchId")
                else:
                    print(str(pickle.loads(str.encode(rslt.replace('☆', '\n')))))
                    # update @treeName's data to .tqpt file <---> do backup if wisdom calls
                    stpp.changevar(treeName, '@qp(' + rslt + '):', __SMT_PTH, 'spkmvtr')
                    if keepBackup == True:
                        __gloke_tack(False, 'ab', treeName, '@qp(' + trRwSrc + '):')
                    # return the added branch type parsing
                    rLst = stpp.loadvar_str('__KLF_DSG', __SMT_PTH, 'spkmvtr')
                    return int(rLst[2])
            else:
                raise Exception("<pyspahk_mvtree.addbranch()> error: '" + treeName + "' not found in staqtapp tqpt source file")
        else:
            raise Exception("<pyspahk_mvtree.addbranch()> error: invalid parameter @treeName")
    except Exception as e:
        print("<pyspahk_mvtree.addbranch()> error: ", e)
# _________________________________________________________________________________________

def getbranch(isAlf: bool, treeName: str, branchKey):
    
    # *****isAlf will find all branch-keys that contain dual branch-keys in naming,
    # char sep _ (see Example 2 of addbranch method) and will return the original
    # branch-key & branch-value linked to that branch as a str 'br_br:br:bv' of a list
    # type returns; this important, to find the top branch of these branch configs if
    # is deeply nested of a same shifting naming preceding further; using char _ in
    # branch-key names will cause bad matches of alf parse branching returns, however
    # if more than once a char use of underscore in branch-key name is ignored*****
    
    # >>> of using dot notation(s) @branchKey parameter for branch gets, returns as
    # much as found in a list; if dot notation to next branch name is not of a nested
    # correct order, then returns was it already found, return is a str list [brKy:brVl, ...]
    # if no dot notation then returns the branch-value as str if found, otherwise None;
    # with branch-key not found of no dot notation use, throws a not found exception
    # ***use of period char in branch-key adds will result in wrong matches here***
    
     if stpp.findvar(False, treeName, __SMT_PTH, 'spkmvtr') == True:
         trStr = str(pickle.loads(str.encode(stpp.loadvar_str(treeName, __SMT_PTH, 'spkmvtr').replace('☆', '\n')))).replace(' ', '')
         if isAlf == True and branchKey == None:
             return __brch_alf_get(trStr)
         elif isAlf == True and branchKey != None:
             # specialized branch-value signature returns, @branchKey can be a list or dot notation(s)
             pass
         else:
             branchKey = str(branchKey)
             if len(branchKey) > 0:
                 if branchKey.find('.') > -1:
                     # is dot notation seeking
                     brLst = branchKey.split('.')
                     rtrnLst = []
                     brLen = len(brLst)
                     brVlPtn = None
                     brVlf = None
                     brPta = None
                     brPtb = None
                     swBgn = True
                     x = 0
                     while x < brLen:
                         try:
                             brPta = re.search(r"\'" + re.escape(brLst[x]) + r"\'", trStr).span(0)
                         except Exception as e:
                             return rtrnLst
                         if swBgn == True:
                             swBgn = False
                             brVlPtn = re.compile(r"'" + re.escape(brLst[x]) + r"'\:'.*?'")
                             brVlf = brVlPtn.findall(trStr)
                             if len(brVlf) > 0:
                                 brVlf = brVlf[0].split(':')
                                 brVlf = brVlf[1].replace("'", '')
                                 rtrnLst.append(brLst[x] + ":" + brVlf)
                             else:
                                 rtrnLst.append(brLst[x] + ":None")
                         else:
                             if brPta[1] > brPtb:
                                 brVlPtn = re.compile(r"'" + re.escape(brLst[x]) + r"'\:'.*?'")
                                 brVlf = brVlPtn.findall(trStr)
                                 if len(brVlf) > 0:
                                     brVlf = brVlf[0].split(':')
                                     brVlf = brVlf[1].replace("'", '')
                                     rtrnLst.append(brLst[x] + ":" + brVlf)
                                 else:
                                     rtrnLst.append(brLst[x] + ":None")
                             else:
                                 return rtrnLst
                         brPtb = brPta[1]
                         x+=1
                     return rtrnLst
                 else:
                     # is not dot notation seeking
                     if trStr.find(branchKey) > -1:
                         brVlPtn = re.compile(r"'" + re.escape(branchKey) + r"'\:'.*?'")
                         brVlf = brVlPtn.findall(trStr)
                         if len(brVlf) > 0:
                             brVlf = brVlf[0].split(':')
                             brVlf = brVlf[1].replace("'", '')
                             return brVlf
                         else:
                             return None
                     else:
                         raise Exception("<pyspahk_mvtree.getbranch()> error: '" + branchKey + "' not found")
             else:
                 raise Exception("<pyspahk_mvtree.getbranch()> error: @branchKey cannot be nothing")
     else:
         raise Exception("<pyspahk_mvtree.getbranch()> error: '" + treeName + "' not found in staqtapp tqpt source file")
    
# _________________________________________________________________________________________

def __brch_alf_get(trSrc: str) -> list:
    
    cStr = ''
    px = 0
    pl = -1
    cCnt = 0
    cLst = []
    prvChr = None
    swBe = False
    swBr = False
    swVd = False
    
    for curChr in trSrc:
        if swBe == False and prvChr == "}" and curChr == ",": swBe = True
        elif swBe == True:
            if swBr == False and curChr == "'": swBr = True
            else:
                if swBr == False: swBe = False
                else:
                    if curChr == "_":
                        cCnt+=1
                        if cCnt < 2 and len(cStr) > 0:
                            cLst.append(cStr)
                            pl+=1
                            swVd = True
                            cStr = ''
                        else:
                             swBe = False
                             swBr = False
                             swVd = False
                             cStr = ''
                             cCnt = 0
                             cLst.pop(pl)
                             pl-=1
                    else:
                        if curChr == "'":
                            swBe = False
                            swBr = False
                            cCnt = 0
                            if swVd == True and len(cStr) > 0:
                                cLst.append(cStr)
                                pl+=1
                            swVd = False
                            cStr = ''
                        else: cStr += curChr
        prvChr = curChr
        px+=1
    # build alf return str list and return it
    if len(cLst) > 0:
        swVd = []
        cCnt = 0
        px = int(len(cLst)/2)
        for x in range(px):
            swVd.append(cLst[cCnt] + '_' + cLst[cCnt+1])
            cCnt+=2
            pl = re.compile(r"'" + re.escape(swVd[x]) + r"':\{'.*?'")
            prvChr = pl.findall(trSrc)
            prvChr = prvChr[0].split('{')
            prvChr = prvChr[1].replace("'", '')
            cStr = swVd[x]
            swVd[x] += ':' + prvChr
            pl = re.compile(r"'" + re.escape(cStr) + r"':\{'" + re.escape(prvChr) + r"'\:'.*?'")
            prvChr = pl.findall(trSrc)
            if len(prvChr) > 0:
                prvChr = prvChr[0].split(':')
                prvChr = prvChr[2].replace("'", '')
                swVd[x] += ':' + prvChr
            else:
                swVd[x] += ':None'
        return swVd
    else:
        # none return for isAlf=True
        return None
# _________________________________________________________________________________________
# _________________________________________________________________________________________
# _________________________________________________________________________________________

def __krosh_nook(isRead: bool, dsgFnc: str, srcStr: str, brId: str, brNwId: str, brNwVl: str):
    
    # :READ/WRITE BRANCHING MAIN:
    
    # ***** on-swarts' innic --nook ...hawking solk... (ar) ---krosh-kooger *****
    
    # FUNCTION RETURN-CODES
    # ------------------------------------------------------------------------
    # return -1  : @brId was not found
    # return -2  : invalid @brId, is a branch-value
    # return -3  : invalid parameters @posBranchId and/or @newBranchId
    
    if isRead == False:
        if dsgFnc == 'ab':
            # ---------- ☆ ADD BRANCH ---------------------------------------------
            # ------------------------------------------------------------------
            if len(brId) > 0 and len(brNwId) > 0:
                # clear all the spacing from source as needed
                srcStr = srcStr.replace(' ', '')
                # is @brId a branch-value instead of a branch-key??
                # ........will have the char ':' at the first pos left if is
                if srcStr.find(":'" + brId + "'") == -1:
                    pxLst = None
                    try:
                        pxLst = re.search(r"\'" + re.escape(brId) + r"\'", srcStr).span(0)
                    except Exception as e:
                        # @brId was not found
                        return -1
                    slLst = [srcStr[0:pxLst[1]], srcStr[pxLst[1]:len(srcStr)]]
                    print(slLst[0])
                    print(slLst[1])
                    srcStr = None
                    cfgL = None
                    pos = len(slLst[0])-(pxLst[1]-pxLst[0])-2
                    try:
                        if slLst[0].find(":{", pos, pos+2) > -1: cfgL = 1
                        elif slLst[0].find("',", pos, pos+2) > -1: cfgL = 2
                        elif slLst[0].find("},", pos, pos+2) > -1: cfgL = 3
                        else: cfgL = 4
                    except Exception as e:
                        cfgL = 1
                    cfgR = None
                    try:
                        if slLst[1].find(":'", 0, 2) > -1: cfgR = 1
                        elif slLst[1].find(":{", 0, 2) > -1: cfgR = 2
                        elif slLst[1].find("},", 0, 2) > -1: cfgR = 3
                        else:
                            if slLst[1].find("}}", 0, 2) > -1: cfgR = 3
                            else: cfgR = 4
                    except Exception as e:
                        cfgR = 3
                    print(str(cfgL) + ':' + str(cfgR))
                    return pickle.dumps(AbsTrek(ast.literal_eval(__equal_branch(cfgL, cfgR, slLst, brId, brNwId, brNwVl))), 0).decode().replace('\n', '☆')
                else:
                    return -2
            else:
                return -3
# _________________________________________________________________________________________

def __equal_branch(hldL: int, hldR: int, slTr: list, br: str, brNw: str, brVl: str):
    
    # branch calibering: final bracketable string returns
    
    pxLst = None
    
    if hldL == 1:
        # :{
        if hldR == 1:
            # :'  [@br has a branch-value]
            pxLst = __char_seeks('plr', slTr[1], None)
            if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
                return __eq_br_ext(":'", None, slTr, pxLst, br, brNw, brVl)
            else:
                # __hawking_solk()
                # called specialized value/key interlinking(spahk knots)
                # or is corrupted branching edit outside this module use
                pass
        elif hldR == 2:
            # :{  [@br has no branch-value]
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':2):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext(":{", None, slTr, pxLst, br, brNw, brVl)
        elif hldR == 3:
            # },  [@br is a singular valueless branch]
            # no specialized interlinking direct, is considered a complete
            # branch replace @br with no required initial spahk-knot indexing
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext("},", None, slTr, pxLst, br, brNw, brVl)
        else:
            # __hawking_solk()
            # this else reserved for mathematical balances & other probables,
            # specific: staqtapp's rev9 bluetooth self-replication encodings
            # and overall parameter balances of those built methods linked,
            # supercomputer use already well thought of and is mapped of this
            pass
    elif hldL == 2:
        # ',
        if hldR == 1:
            # :'  [@br has a branch-value]
            pxLst = __char_seeks('plr', slTr[1], None)
            if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
                return __eq_br_ext(":'", None, slTr, pxLst, br, brNw, brVl)
            else:
                # __hawking_solk()
                # called specialized key/value interlinking(spahk knots)
                # or is corrupted branching edit outside this module use
                pass
        elif hldR == 2:
            # :{  [@br is a branch-key of a begin branch]
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':2):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext(":{", None, slTr, pxLst, br, brNw, brVl)
        elif hldR == 3:
            # },
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext("},", None, slTr, pxLst, br, brNw, brVl)
        else:
            pass
    elif hldL == 3:
        # },
        if hldR == 1:
            # :' [@br has a branch-value]
            pxLst = __char_seeks('plr', slTr[1], None)
            if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
                return __eq_br_ext(":'", None, slTr, pxLst, br, brNw, brVl)
            else:
                pass
        elif hldR == 2:
            # :{ [@br has no branch-value]
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':2):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext(":{", None, slTr, pxLst, br, brNw, brVl)
        elif hldR == 3:
            # }, [@br a singular valueless branch]
            stpp.changevar('__KLF_DSG', '@qp(' + str(hldL) + ':' + str(hldR) + ':1):', __SMT_PTH, 'spkmvtr')
            return __eq_br_ext("},", None, slTr, pxLst, br, brNw, brVl)
        else:
            pass
    else:
        pass
# _________________________________________________________________________________________

def __eq_br_ext(dsg: str, extDsg: str, slTr: list, pxLst: list, br: str, brNw: str, brVl: str) -> str:
    
    pnStr = None
    pnLst = None
    
    if dsg == ":'":
        pnLst = [slTr[1][0:pxLst[1]+1], slTr[1][pxLst[1]+1:len(slTr[1])]]
        slTr[1] = None
        pnStr = slTr[0] + pnLst[0] + ",'" + br + "':{'" + brNw + "':"
        if len(brVl) > 0: pnStr += "'" + brVl + "'}" + pnLst[1]
        else: pnStr += "'spahk-knot'}" + pnLst[1]
        return pnStr
    elif dsg == ":{":
        klfDsg = stpp.loadvar_str('__KLF_DSG', __SMT_PTH, 'spkmvtr')
        if klfDsg != 'Null':
            brkId = int(klfDsg[len(klfDsg)-1:len(klfDsg)])
        else:
            brkId = 0
        if brkId < 5:
            pnStr = slTr[0] + ":{'" + brNw + "':'"
            if len(brVl) > 0: pnStr += brVl + "'},'" + br + "_" + brNw + "'" + slTr[1]
            else: pnStr += "'spahk-knot'},'" + br + "_" + brNw + "'" + slTr[1]
            return pnStr
        else:
            pass
    elif dsg == "},":
        slTr[0] = slTr[0].replace(br + "'", brNw + "':'")
        if len(brVl) > 0: slTr[0] += brVl + "'"
        else: slTr[0] += "spahk-knot'"
        return ''.join(slTr)
# _________________________________________________________________________________________

def __char_seeks(dsg: str, src: str, pos: list):
    
    x = None
    prvChr = None
    swStrt = None
    swEnd = None
    rtrnLst = None
    
    if dsg == 'plr':
        # returns a LtoR pos list; bugs from regex mishaps are impossible here
        rtrnLst = [None, None]
        swStrt = True
        swEnd = False
        x = 0
        for curChr in src:
            if curChr == "'" and swStrt == True:
                swStrt = False
                rtrnLst[0] = x
            elif curChr == "'" and swStrt == False and swEnd == False:
                swEnd = True
            elif swEnd == True:
                if prvChr == "'" and curChr == ":":
                    rtrnLst[1] = x-1
                    return rtrnLst
                elif prvChr == "'" and curChr == "}":
                    rtrnLst[1] = x-1
                    return rtrnLst
                elif prvChr == "'" and curChr == ",":
                    rtrnLst[1] = x-1
                    return rtrnLst
            prvChr = curChr
            x+=1
# _________________________________________________________________________________________

def __char_check(src) -> bool:
    # non-allowed chars for the branch-keys and branch-values  \n ,:'{ }☆
    # staqtapp will not save data to tqpt files that have any \n end chars
    nc = [":", ",", "{", "}", "'", "\n", "☆"]
    if isinstance(src, str) == True:
        for chr in src:
            if chr in nc:
                return False
        return True
    else:
        srcLen = len(src)
        for x in range(srcLen):
            for chr in src[x]:
                if chr in nc:
                    return False
        return True
# _________________________________________________________________________________________

def __hawking_solk(isSars: bool, isKlAv: bool, isKlGt: bool, isKlLs: bool, dsg: str, trNm: str, klfDsg: list, prvStg: list):
    
    # :SPAHK MV BRANCH MATHEMATICS MAIN:
        
    # ***** n'innic gerd'y swarts, ('r) sove raw ---stibs ----> (hawk pass | hawk rotate) | hawk eat *****
    
    try:
        if isSars == True:
            # Staqtapp's sars variables and pointer sars variables resolves, currently
            # not a fully implemented feature of the library's global variable ops; to
            # be of use here for spanned branched value signatures & compression
            pass
        else:
            # first check if all three palindrome type variables are in the tqpt file, __KLAV,
            # __KLGT and __KLLS... if not, initialize their values and save to .tqpt file ------
            # [kl=keep limit, av=average, gt=greater, ls=lesser] of menorah mathematics
            # that can use any digit as loop, not just a singular set loop or zero
            if stpp.findvar(False, '__KLAV', __SMT_PTH, 'spkmvtr') == False:
                # @__KLAV scale enclosure to branching sight, set to a center x=<{n*t}/ab>
                # default '1211121' base10; *sars pointers constrict span pairs by less only
                stpp.addvar('__KLAV', '@qp(1211121):', __SMT_PTH, 'spkmvtr')
            if stpp.findvar(False, '__KLGT', __SMT_PTH, 'spkmvtr') == False:
                # @__KLGT scale enclosure to branching sight lesser probables rotations,
                # default to a paired value escape, meaning first out L and R are loop zero
                stpp.addvar('__KLGT', '@qp(0975790):', __SMT_PTH, 'spkmvtr')
            if stpp.findvar(False, '__KLLS', __SMT_PTH, 'spkmvtr') == False:
                # @__KLLS opposite of @__KLGT but does not have to be of other calcs
                # default to a paired value escape, meaning first pair in L and R are loop
                stpp.addvar('__KLLS', '@qp(9705079):', __SMT_PTH, 'spkmvtr')
            # determine which keep limit combinations are going to seek spahk knots
            # or resolve fitted values to insert in branch replications or removals, speed
            # is a mild issue here if a prvStg is given in proper formats near last klfDsg
            # can be solved by complex sets variables retained or using hash tables,
            # both having a advantage and disadvantage from pure python encodings
            
            src = str(pickle.loads(str.encode(stpp.loadvar_str(trNm, __SMT_PTH, 'spkmvtr').replace('☆', '\n'))))
            if src.find('spahk-knot') > -1:
                cCnt = 0
                cStr = ''
                fcl = []
                tmpLst = None
            
                swA = False
            
                if isKlAv == True:
                    klav = stpp.loadvar_str('__KLAV', __SMT_PTH, 'spkmvtr')
                    klgt = stpp.loadvar_str('__KLGT', __SMT_PTH, 'spkmvtr')
                    klls = stpp.loadvar_str('__KLLS', __SMT_PTH, 'spkmvtr')
                    for i in range(len(prvStg)):
                        cCnt+=1
                        if swA == False:
                            swA = True
                        else:
                            fcl.append(int(cStr))
                            cStr = ''
                        for j in range(len(klfDsg)):
                            # computation @ max frequency pair collapse length(fcl) @klfDsg
                            cStr += str(math.gcd(int(math.sin(klfDsg[j]+i))+int(math.tan(klfDsg[j]-i)), klfDsg[j]+i+j))
                        if i+1 == len(prvStg):
                            fcl.append(int(cStr))
                    fcl[0] = fcl[1]-fcl[0]
                    fcl[1] = fcl[3]-fcl[2]
                    fcl = math.fabs(math.ceil((fcl[0]-fcl[1])*cCnt))
                    trLsGt = stpp.loadvar_str(['__KLAV','__KLLS','__KLGT'], __SMT_PTH, 'spkmvtr')
                    
    except Exception as e:
        print('error: ',e)

# _________________________________________________________________________________________

def __gloke_tack(isRead, dsgFnc, treeName, treeData):
    
    # :BACKUPS READ/WRITE MAIN:
    
    # ***** tacks gayge' --swarte graws, prop'r ---needjas bog courres net *****
    
    try:
        if isRead == True:
            # ☆☆☆☆☆  <--------------> - -READ- - -TREE- - -BACKUPS- - -  ☆☆☆☆☆
            pass
        else:
            # ☆☆☆☆☆  <-------------> - -WRITE- - -TREE- - -BACKUPS- - -  ☆☆☆☆☆
            try:
                stpp.makesource(False, False, False, __SMT_PTH, '_bck_spkmvtr')
            except Exception:
                # tree backup source file is already there
                pass
            if dsgFnc == 'mt':
                # from maketree(), new tree add @treeName_bck_1
                stpp.addvar(treeName + '_bck_1', treeData, __SMT_PTH, '_bck_spkmvtr')
            elif dsgFnc == 'ab':
                # from addbranch(), existing tree data before saved branch update;
                # first, search if any backup @treeName_bck_1 is listed in .tqpt file...
                # if is there, then time stamping of backup variable names is a go
                # !!simple int dsg restore translates needs to be implemented here!!
                if stpp.findvar(False, treeName + '_bck_1', __SMT_PTH, '_bck_spkmvtr') == True:
                    stpp.addvar(treeName + '__' + str(datetime.datetime.now()), treeData, __SMT_PTH, '_bck_spkmvtr')
                else:
                    stpp.addvar(treeName + '_bck_1', treeData, __SMT_PTH, '_bck_spkmvtr')
    except Exception:
        pass
# _________________________________________________________________________________________

def test():
    
    #tstLst = ['branch1', 222, 'branch3', 444, 'branch5']
    #maketree(True, 'treeSpkMv11', tstLst)
    
    #rslt = addbranch(True, 'treeSpkMv11', 444, 'br987654321', 97531)
    #print(rslt)
    
    lst = getbranch(True, 'treeSpkMv11', 9876, None)
    print(lst)
    
    #kl = [2,2,0]
    #pr = [4,0,2,7]
    
    #__hawking_solk(False, True, True, True, 'pnq', 'treeSpkMv11', kl, pr)
   
# _________________________________________________________________________________________

test()
    
    
    



