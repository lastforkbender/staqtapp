# Staqtapp v1.2.55 - rev9


# Staqtapp v1.2 Description:
    
# A rework of the original Staqtapp env-vars library. Uses a vfs system for both tqpt,
# tpqt and other needed files. Built to last in one concentrated module for __slots__
# performance, with same thorough error checking and stpx type function calling. You
# set the vfs dir path to a tqpt variables file & all else handled with min param use.
# (A vfs staqtapp 1.2 file must be created first. Auto sets the tqpt vars set path.)

# There no need to change/fix code to this module, is all quality slots interlinked;
# we don't care who you think you are or even how rich you think you are, do not edit.
# Just as there is only one true rolex so is this env-var module, keep your sanity.
# If you need the most secure env-vars library in the world, Staqtapp2-Koch version,
# then you can contact me by the email below, with agreements by voice/phone arranged.




# WARNING: THIS ENV-VAR MODULE WORK INCLUDES EXOTIC CALLABLE IMPORT METHODS. ANY USE
# OF THESE EXOTIC FUNCTIONS FOR BLOATWARE, MALWARE, RANSOMWARE OR ETC. WILL BE FOUND.
# ONCE A CORPORATION, PARTY OR PERSONS DECIDES ON SUCH USAGE OTHER THAN INTENDED FOR
# OF THIS ENV-VAR MODULE, THEY ARE RESPONSIBLE WETHER IN A WORLDLY LAW DEFINE OR NOT.
# NECESSARY ACTIONS CAN INCLUDE LOSS OF MONETARY ACCUMULATION FOR FAIR DISTRIBUTE OR
# A COMPLETE LOSS OF COMPUTER PRIVILEGES INDEFINITELY IF SUCH OF A THREAT IS EVIDENT.

#_______________________________________________________________________________________
# STAQTAPP V1.2 IMPORT FUNCTION CALLS:
#
# --> makevfs(vfsFileName, directoryName, folderName), builds a .sqtpp vfs file
#     in current ../staqtapp/* directory; @vfsFileName cannot include ':' chars,
#     tqpt file auto inserted to sub-folder naming of @folderName & is set path.
#
# --> addvar(varName, varData), adds variable to path set vfs tqpt file. @varData
#     must be tagged with '@qp(...):' for staqtapps unique read parsing routines.
#     Can be as many @qp(...): tags as needed, with commenting in between. Read as
#     a comma separation for a list return when more than one. This function does
#     not change variable data, see changevar to edit stacked variable datas. Is
#     suggested to use lockvar after adding a variable with this function.
#
# --> addtree_stx(treeName, initialTreePathList), adds a initial dict type tree
#     structure to vfs tqpt stacks for deep spahk-mv type tree edits. @initial-
#     TreePathList is simply a list elements of strings or int values. Chars not
#     allowed @initialTreePathList string element(s) are \n,':{} and ☆ The ---
#     other functions that edit this type, all stalkvar() type similiar actions.
#
# --> addbranch_stx(treeName, branchId, newBranchId, newBranchValue), Adds, shifts,
#     replaces, or spawns merged branch for a mv-tree. Behavior of mv-tree branch
#     edits are in exotic relation to stalkvar. The examples below show this. (The
#     first most left dict key cannot be changed, in the examples is branch 'a')

      # Example A:
      # smvt-state {'a':{'b':{'c':'vl1','d':'vl2'}, 'e':'vl3'}}
      # .addbranch_stx('smvt_tree_a', 'c', 2035, None)
      # results ---> {'a':{'b':{'c':{'2035':'knt'}, 'd':'vl2'}, 'e':'vl3'}}
      # 'vl1' now a nested branch, not a separate value
    
      # Example B:
      # smvt-state {'a':{'b':{'c':'vl1'},'e':'vl3'}}
      # .addbranch_stx('smvt_tree_b', 'b', 2056, None)
      # results ---> {'a':{'b':{'2056':'knt'},'b_2056':{'c':'vl1'},'e':'vl3'}}
      # 'b' hoplinked to branch&value, however not full link replace parse 
      # @'b_2056', feature serves as replace options and other features
    
      # Example C:
      # smvt-state {'a':{'b':{'c'},'e':'vl3'}}
      # .addbranch_stx('smvt_tree_c', 'c', 2032, 2051)
      # results ---> {'a':{'b':{'2032':'2051'},'e':'vl3'}}
      # 'c' replaced by {'2032':'2051'} branch
#
# --> getbranch_stx(isAlf, treeName, branchId), returns a found branch value or
#     None. @branchId can be either int or str for most searches. @isAlf is for a
#     return list of all original branch key(s) + value(s) to an @brnchId merge.
#     The return list format as ['br_br:br:bv',...], this type find for 2nd checks.
#     Avoid using alf as much as possible on large mv-trees. If use, @branchId=None
#     A tip with this type dict tree type, record in env-var any adds done to a
#     a branch in that can be later known was replaced or merged with other branch.
#     Adding branches to mv-tree type can be difficult to grasp at first, yet open
#     a whole other world for advanced dict type comprehensive recursion unions.
#
# --> lockvar(varName, fncName), adds a function name or else associated to a var-
#     Name in a tpqt type file. This can then be used with keyvar to gate what is
#     allowed to edit the env-var. There no real security/math to it like the Koch
#     version Staqtapp, however is very useful in preventing any env-vars mishaps.
#     @fncName can be either a string; or, list parameter of string names properly.
#     To delete vfs entries from a lockvar use, see lockdel to do that effectively.
#
# --> findvar(varName), returns True if variable present to set vfs tqpt file.
#
# --> findvar_stx(varNameList, stalkVarName), findvar function for multiple found
#     result list return. If @stalkVarName not None then returns the list of the
#     spawned incremented var names, with each element s-var name of a additional 
#     equal detail = <if @varNameList[#]'s data ?= @incremented_var's data> which
#     will be either =1 or =-1. List length @varNameList determines return length
#     for both search options. This new feature is used for recursive analysis or
#     chained events hidden from a pivot conclusion or escape type params forming.
#     [If stalked var will have thousands of spawned naming see modvar for lambda
#     spawned res-type slots attribute class caching before calling this method.]
#
# --> stalkvar(varName, varData), keeps the original env-var as a static read only
#     var and makes a new but same @varName, with extension '_#' as a numbered
#     increment _1~#. If the @varData matches the original, is no longer a stalked
#     env-var and all the incremented spawns are removed from both the tqpt & svvs
#     set vfs path files contents. This feature is used for recursive analysis or
#     chained events hidden from a pivot conclusion or escape type params forming.
#
# --> modrev9(prmsLst), builds a complete custom env-var module. @prmsLst elements
#     for this staqtapp feature is 28 arguments. The type modules generated can be
#     very difficult to understand, with obfuscation turned on or not. Some of the
#     arguments need the DUN3.py random lambda generator module present. (The DUN3
#     random lambda generator is still being tested and refined.) This feature is
#     central to staqtapp. Enables bluetooth communication with any other builds &
#     can respawn itself, changed to meet any new bluetooth communication commands.
#     And being it would need an clean and semi-abstract vfs file system for that.
#     (NOT YET IMPLEMENTED)

#_______________________________________________________________________________________

# NOTE: I switch between different ide when testing this machine----if you see
#       a _err slots error.....is because this lets me know to switch and read
#       the real error that was logged in the .../staqtapp1_2/err-log.txt file

# email: rcttcr5@gmail.com
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from decimal import Decimal as dcml
from collections import deque

import datetime
import hashlib
import pickle
import random
import math
import mmap
import glob
import sys
import ast
import os
import re
#_______________________________________________________________________________________
SQTPP_SET_NMB = set('0123456789')
SQTPP_MDL_DIR = f'{os.path.dirname(os.path.abspath(__file__))}'
SQTPP_SET_VARS = set('_0123456789ABCDEFGHIJKLMNOPQURSTVWXYZabcdefghijklmnopqurstvwxyz')
#_______________________________________________________________________________________
class AbsSmvt(dict):
    
    def __missing__(self, ent):
        rgr = self[ent] = type(self)()
        return rgr
        
    def __init__(self, dt = {}):
        for ix, dt in dt.items():
            if isinstance(dt, dict): self[ix] = type(self)(dt)
            else: self[ix] = dt
                
    def __eq__(self, other):
        return isinstance(self, AbsTrek) and self.dt == other.dt
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_________________________MID CHECKING FUNCTIONS:
#_______________________________________________________________________________________
class Sqtpp(dict):
    __slots__ = ('_sErr', '_sRtrn', '_rIntA', '_rIntB')
    
    def __init__(self):
        pass
#_______________________________________________________________________________________
    def mcf_makevfs(self, vfsNm: str, dirNm: str, fldrNm: str):
        # Creates .sqtpp vfs file in the current working module dir .../staqtapp1_2/
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if vfsNm.find(':') < 0:
            if dirNm != fldrNm:
                if sfCls.sqtpp_chars_check(1, dirNm):
                    if sfCls.sqtpp_chars_check(1, fldrNm):
                        self._sRtrn = sfCls.sqtpp_vfs_make(vfsNm, dirNm, fldrNm)
                        if self._sRtrn != 8: self.mcf_err_handler(-1, 'makevfs')
                    else: self.mcf_err_handler(1, 'makevfs')
                else: self.mcf_err_handler(2, 'makevfs')
            else: self.mcf_err_handler(3, 'makevfs')
        else: self.mcf_err_handler(4, 'makevfs')
#_______________________________________________________________________________________
    def mcf_addvar(self, varNm: str, varDat: str):
        # Adds variables to the set path vfs tqpt file.
        # __slots__ in use: (_sRtrn)
        if os.path.isfile(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg'):
            sfCls = SqtppFncs()
            if sfCls.sqtpp_chars_check(2, varNm):
                self._sRtrn = sfCls.sqtpp_vars_add(False, varNm, varDat)
                if self._sRtrn == -1: self.mcf_err_handler(6, 'addvar')
                elif self._sRtrn == -2: self.mcf_err_handler(7, 'addvar')
                elif self._sRtrn == -3: self.mcf_err_handler(9, 'addvar')
                elif self._sRtrn == -4: self.mcf_err_handler(10, 'addvar')
                elif self._sRtrn == -5: self.mcf_err_handler(11, 'addvar')
                elif self._sRtrn == -6: self.mcf_err_handler(12, 'addvar')
                elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'addvar')
            else: self.mcf_err_handler(8, 'addvar')
        else: self.mcf_err_handler(5, 'addvar')
#_______________________________________________________________________________________
    def mcf_addtree_stx(self, trNm: str, initPthLst: list):
        # Adds a spahk-mv type initial path keys built dict tree to vfs tqpt source.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, trNm):
            self._sRtrn = sfCls.sqtpp_spok_mv_tree(trNm, initPthLst)
            if self._sRtrn == -1: self.mcf_err_handler(21, 'addtree_stx')
            elif self._sRtrn == -2: self.mcf_err_handler(22, 'addtree_stx')
            elif self._sRtrn == -3: self.mcf_err_handler(6, 'addtree_stx')
            elif self._sRtrn == -4: self.mcf_err_handler(7, 'addtree_stx')
            elif self._sRtrn == -5: self.mcf_err_handler(12, 'addtree_stx')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'addtree_stx')
        else: self.mcf_err_handler(8, 'addtree_stx')
#_______________________________________________________________________________________
    def mcf_addbranch_stx(self, trNm: str, smvBrnchId, newSmvBrnchId, newSmvBrnchVl):
        # See addbranch_stx() descriptions and examples @ top of this module.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, trNm):
            self._sRtrn = sfCls.sqtpp_spok_mv_tree_add_branch(trNm, smvBrnchId, newSmvBrnchId, newSmvBrnchVl)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'addbranch_stx')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'addbranch_stx')
            elif self._sRtrn == -3: self.mcf_err_handler(14, 'addbranch_stx')
            elif self._sRtrn == -4: self.mcf_err_handler(23, 'addbranch_stx')
            elif self._sRtrn == -5: self.mcf_err_handler(24, 'addbranch_stx')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'addbranch_stx')
        else: self.mcf_err_handler(8, 'addbranch_stx')
#_______________________________________________________________________________________
    def mcf_getbranch_stx(self, isAlf: bool, trNm: str, smvBrnchId):
        # Returns a found value pairing or None for a mv-tree type branch id reads.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, trNm):
            self._sRtrn = sfCls.sqtpp_spok_mv_tree_get_branch(isAlf, trNm, smvBrnchId)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'getbranch_stx')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'getbranch_stx')
            elif self._sRtrn == -3: self.mcf_err_handler(14, 'getbranch_stx')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'getbranch_stx')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'getbranch_stx')
#_______________________________________________________________________________________
    def mcf_lockvar(self, varNm: str, fncNm):
        # Adds entries to set vfs path tpqt file for restraint of env-var access.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_limit_var_domain(varNm, fncNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'lockvar')
            elif self._sRtrn == -2: self.mcf_err_handler(13, 'lockvar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'lockvar')
        else: self.mcf_err_handler(8, 'lockvar')
#_______________________________________________________________________________________
    def mcf_findvar(self, varNm: str):
        # Searches for @varNm in listed vars of set path vfs tqpt file contents.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_locate_var(True, varNm)
            if self._sRtrn == -3: self.mcf_err_handler(6, 'findvar')
            elif self._sRtrn == -1: self.mcf_err_handler(7, 'findvar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'findvar')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'findvar')
#_______________________________________________________________________________________
    def mcf_findvar_stx(self, varNmLst: list, stlkVarNm: str):
        # Searches a list of vars to be found, with stalked variable option. See stx function description above.
        # __slots__ in use: (_sRtrn, _rIntA, _rIntB)
        sfCls = SqtppFncs()
        self._rIntB = len(varNmLst)
        for self._rIntA in range(self._rIntB):
            if not sfCls.sqtpp_chars_check(2, varNmLst[self._rIntA]): self.mcf_err_handler(8, 'findvar_stx')
        if isinstance(stlkVarNm, str):
            if not sfCls.sqtpp_chars_check(2, stlkVarNm): self.mcf_err_handler(18, 'findvar_stx')
        self._sRtrn = sfCls.sqtpp_locate_var_stx(varNmLst, stlkVarNm)
        if self._sRtrn == -1: self.mcf_err_handler(19, 'findvar_stx')
        elif self._sRtrn == -2: self.mcf_err_handler(7, 'findvar_stx')
        elif self._sRtrn == -3: self.mcf_err_handler(6, 'findvar_stx')
        elif self._sRtrn == -4: self.mcf_err_handler(20, 'findvar_stx')
        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'findvar_stx')
        else:
            return self._sRtrn
#_______________________________________________________________________________________
    def mcf_stalkvar(self, varNm: str, varDat: str):
        # Performs incremental @varNm mirroring collapse for @varDat conditions.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_vars_add(True, varNm, varDat)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'stalkvar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'stalkvar')
            elif self._sRtrn == -3: self.mcf_err_handler(9, 'stalkvar')
            elif self._sRtrn == -4: self.mcf_err_handler(10, 'stalkvar')
            elif self._sRtrn == -5: self.mcf_err_handler(11, 'stalkvar')
            elif self._sRtrn == -6: self.mcf_err_handler(14, 'stalkvar')
            elif self._sRtrn == -7: self.mcf_err_handler(15, 'stalkvar')
            elif self._sRtrn == -8: self.mcf_err_handler(16, 'stalkvar')
            elif self._sRtrn == -9: self.mcf_err_handler(17, 'stalkvar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'stalkvar')
        else: self.mcf_err_handler(8, 'stalkvar')
#_______________________________________________________________________________________
    def mcf_err_handler(self, altErrCd: int, clnFnc: str):
        # Handles error returns for mcf mid check functions.
        # __slots__ in use: (_sRtrn)
        if altErrCd > 0:
            # Alt Error Int Codes:
            # 1 = invalid folder name chars
            # 2 = invalid directory name chars
            # 3 = both vfs dir name and fldr name are the same
            # 4 = invalid char ':' for vfs file name
            # 5 = setting file for vfs path not there
            # 6 = vfs path setting file is empty
            # 7 = set path to vfs tqpt file is corrupted
            # 8 = variable name has invalid chars
            # 9 = variable data has newline chars
            # 10 = no proper @qp(...): data declaring tags found
            # 11 = missing ): closing for @qp( data declare
            # 12 = @varNm or @trNm is already listed in tqpt var source
            # 13 = @varNm not found in tpqt file
            # 14 = @varNm not found in tqpt file(general mssg)
            # 15 = @varDat is same value as found @varNm but there is no created svvs sub-file
            # 16 = svvs stalk-entry element list for @varName is not there
            # 17 = begin stalkvar var data is identical to @varDat param
            # 18 = @stalkVarName has invalid chars in naming
            # 19 = @varNameList is empty
            # 20 = svvs stalk-entry element list for @stlkVarNm is not there
            # 21 = @initialTreePathList is empty
            # 22 = @initialTreePathList has invalid chars
            # 23 = invalid chars for a smvt tree branch id/key
            # 24 = invalid chars for a smvt tree branch value
            if altErrCd == 1: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid folder name chars; allowed -a-zA-Z')
            elif altErrCd == 2: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid directory name chars; allowed -a-zA-Z')
            elif altErrCd == 3: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid folder name, cannot be the same as directory name')
            elif altErrCd == 4: raise Exception(f'staqtapp1.2 ({clnFnc}) error: char ":" is not allowed for staqtapp vfs filenames')
            elif altErrCd == 5: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no vfs directory path set for a tqpt or tpqt file action')
            elif altErrCd == 6: raise Exception(f'staqtapp1.2 ({clnFnc}) error: empty vfs path setting file, cannot resolve a tqpt file path')
            elif altErrCd == 7: raise Exception(f'staqtapp1.2 ({clnFnc}) error: default set vfs directory path to tqpt file is corrupted...')
            elif altErrCd == 8: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid chars for a variable name; allowed _a-zA-Z0-9')
            elif altErrCd == 9: raise Exception(f'staqtapp1.2 ({clnFnc}) error: newline chars are not allowed in staqtapp variable data')
            elif altErrCd == 10: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no proper @qp(...): data declaring tags found')
            elif altErrCd == 11: raise Exception(f'staqtapp1.2 ({clnFnc}) error: missing closing ): for @qp( variable data declaring')
            elif altErrCd == 12: raise Exception(f'staqtapp1.2 ({clnFnc}) error: variable name duplicate, use changevar for variable edits')
            elif altErrCd == 13: raise Exception(f'staqtapp1.2 ({clnFnc}) error: variable not found in tqpt var file for add to tpqt file')
            elif altErrCd == 14: raise Exception(f'staqtapp1.2 ({clnFnc}) error: variable was not found in tqpt var file')
            elif altErrCd == 15: raise Exception(f'staqtapp1.2 ({clnFnc}) error: svvs sub-file is not created, cannot begin stalkvar with identical values')
            elif altErrCd == 16: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found svvs commons stalk-entry element list for @varNm')
            elif altErrCd == 17: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varData matches var to begin stalk; nothing is impossible, not is possible')
            elif altErrCd == 18: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid chars for @stalkVarName; allowed _a-zA-Z0-9')
            elif altErrCd == 19: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varNameList is empty')
            elif altErrCd == 20: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found svvs commons stalk-entry element list for @stalkVarName')
            elif altErrCd == 21: raise Exception(f'staqtapp1.2 ({clnFnc}) error: param @initialTreePathList is empty')
            elif altErrCd == 22: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars @initialTreePathList; non-allowed chars are \n,':{}☆")
            elif altErrCd == 23: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars for a smv branch tree id; invalid chars: \n,':{}☆")
            elif altErrCd == 24: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars for a smv branch tree value; invalid chars: \n,':{}☆")
        else:
            if self._sRtrn == 'FNC-ERR': raise Exception(f'staqtapp1.2 {clnFnc}-->{self._sErr}')
            elif self._sRtrn == 'FOO-BAR': raise Exception('staqtapp1.2 io error: unable to perform file reads or writes')
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_________________________MAIN PARSING FUNCTIONS:
#_______________________________________________________________________________________
class SqtppFncs(Sqtpp):
    __slots__ = ('_sf_sVfs', '_sf_sVfsFldr', '_sf_sSrc', '_sf_sQp', '_sf_sPq', '_sf_sVd', '_sf_sRtrn', '_sf_sKntId', '_sf_rStrA', '_sf_rStrB', '_sf_rStrC', '_sf_rStrD', '_sf_rStrE', '_sf_rLstA', '_sf_rLstB', '_sf_rLstC', '_sf_rLstD', '_sf_rIntA', '_sf_rIntB', '_sf_rIntC', '_sf_rIntD', '_sf_rIntE', '_sf_rIntF', '_sf_rIntG', '_sf_rBoolA', '_sf_rBoolB', '_sf_rBoolC', '_sf_rBoolD')
    
    def __init__(self):
        pass
#_______________________________________________________________________________________
#_______________________________________________________________________________________
    def sqtpp_vfs_make(self, vfsNm: str, dirNm: str, fldrNm: str) -> int:
        # Handles staqtapp's vfs .sqtpp file makes & edits.
        # __slots__ in use: ()
        # returns: 8,
        try:
            if not os.path.isdir(f'{SQTPP_MDL_DIR}/staqtapp1_2'): os.makedirs(f'{SQTPP_MDL_DIR}/staqtapp1_2')
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{vfsNm}.sqtpp', f':☆staqtapp-v1.2.55\n|:{dirNm}<{fldrNm}>\n_|:{fldrNm}<sub-{fldrNm}>\n__|:sub-{fldrNm}<tqpt-{fldrNm},tpqt-{fldrNm},null>\n___|:tqpt-{fldrNm}<tqpt,null,n>:\nnull:\n___|:(tqpt-{fldrNm})\n___|:tpqt-{fldrNm}<tpqt,null,n>:\nnull:\n___|:(tpqt-{fldrNm})\n__|:(sub-{fldrNm})\n_|:({fldrNm})\n|:({dirNm})')
            self.sqtpp_tqpt_path(True, f'{vfsNm}:{dirNm}:{fldrNm}:sub-{fldrNm}:tqpt-{fldrNm}')
            return 8
        except Exception as err_vfs_make:
            self._sErr = f'staqtapp1.2 (vfs_make) error: {err_vfs_make}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vfs_tqpt_file(self, isTqpt: bool):
        # Sets _sf_sQp to the set path tqpt file contents. Unlike the Staqtapp-Koch
        # version this is a direct list order directory locate, no security at all.
        # This env-vars library is built for speed, not tor like vfs-dir encrypts.
        # __slots__ in use: (_sf_sQp)
        # returns: -1=path not found
        if isTqpt:
            self.sqtpp_vfs_pointer([f'|:{self._sf_rLstA[1]}<', f'_|:{self._sf_rLstA[2]}<', f'__|:{self._sf_rLstA[3]}<', f'___|:{self._sf_rLstA[4]}<'])
            if self._sf_rIntA != -1: self._sf_sQp = self._sf_sSrc[self._sf_rIntA:self._sf_sSrc.find('___|:',self._sf_rIntA+5)-2]
            else:
                return -1
        else:
            pass
#_______________________________________________________________________________________
    def sqtpp_vfs_tpqt_file(self, isTpqt: bool):
        # Sets _sf_sPq to the set path tpqt file contents.
        # __slots__ in use: (_sf_sPq)
        # returns: -1=path not found
        if isTpqt:
            self._sf_rLstA[4] = self._sf_rLstA[4].replace('tqpt', 'tpqt')
            self.sqtpp_vfs_pointer([f'|:{self._sf_rLstA[1]}<', f'_|:{self._sf_rLstA[2]}<', f'__|:{self._sf_rLstA[3]}<', f'___|:{self._sf_rLstA[4]}<'])
            if self._sf_rIntA != -1: self._sf_sPq = self._sf_sSrc[self._sf_rIntA:self._sf_sSrc.find('___|:',self._sf_rIntA+5)-2]
            else:
                return -1
        else:
            pass
#_______________________________________________________________________________________
    def sqtpp_vfs_sub_file(self, isAddFl: bool, isRplcFl: bool, flNm: str, src: str):
        # Read, insert or replace sub-file from a set vfs file/top sub-folder path.
        # __slots__ in use: (_sf_sSrc, _sf_sRtrn, _sf_rStrA, _sf_rIntA, _sf_rIntB)
        # returns: -1=cannot locate sub-folder, -2=sub file not found
        self._sf_rIntA = self._sf_sSrc.find(f'__|:sub-{self._sf_sVfsFldr}<')
        self._sf_rIntB = self._sf_sSrc.find(f'___|:tqpt-{self._sf_sVfsFldr}<')
        if self._sf_rIntA > -1 and self._sf_rIntB > -1:
            self._sf_rStrA = self._sf_sSrc[self._sf_rIntA:self._sf_rIntB-1]
            if isAddFl:
                self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, f'{self._sf_rStrA}\n<sbf-{self._sf_sVfsFldr}-{flNm}:\n{src}//>')
                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                self._sf_rStrA = None
                return 8
            else:
                self._sf_rIntA = self._sf_rStrA.find(f'<sbf-{self._sf_sVfsFldr}-{flNm}:')
                if self._sf_rIntA > -1:
                    self._sf_rIntB = self._sf_rStrA.find('//>', self._sf_rIntA)
                    self._sf_sRtrn = self._sf_rStrA[self._sf_rIntA:self._sf_rIntB]
                    self._sf_rStrA = None
                    if isRplcFl:
                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_sRtrn, f'<sbf-{self._sf_sVfsFldr}-{flNm}:\n{src}')
                        self._sf_sRtrn = None
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                    else:
                        return self._sf_sRtrn
                else:
                    return -2
        else:
            return -1
#_______________________________________________________________________________________
    def sqtpp_set_vfs_file(self):
        # Sets the set path vfs file contents to the slots attribute _sf_sSrc.
        # __slots__ in use: (_sf_sSrc, _sf_rLstA, _sf_sVfs, _sf_sVfsFldr)
        self.sqtpp_tqpt_path(False, None)
        if len(self._sf_sSrc) > 0:
            self._sf_rLstA = self._sf_sSrc.split(':')
            self._sf_sVfs = self._sf_rLstA[0]
            self._sf_sVfsFldr = self._sf_rLstA[2]
            self.sqtpp_file(False, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', None)
            return 1
        else:
            return -1
#_______________________________________________________________________________________
    def sqtpp_vfs_pointer(self, pthLst: list):
        # Searches a vfs path integrity @pthLst, returns last index found.
        # __slots__ in use: (_sf_rIntA)
        # returns: -1=path not found
        for pth in range(len(pthLst)):
            if pth < 1: self._sf_rIntA = self._sf_sSrc.find(pthLst[pth])
            else: self._sf_rIntA = self._sf_sSrc.find(pthLst[pth], self._sf_rIntA+1)
            if self._sf_rIntA < 0:
                break
#_______________________________________________________________________________________
    def sqtpp_vars_add(self, isStlkVar: bool, varNm: str, varDat: str):
        # Adds variables to a vfs type tqpt file from set vfs dir path.
        # __slots__ in use: (_sf_rStrA, _sf_rIntA)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=newline chars found
        # -4=no @qp(...): data declaring found
        # -5=no closing ): for @qp( data tag found
        # -6=@varNm is a duplicate
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rIntA = self.sqtpp_tqpt_spdr(True, False, None, varDat)
                    if self._sf_rIntA == 2:
                        return -3
                    elif self._sf_rIntA == 6:
                        return -4
                    elif self._sf_rIntA == 7:
                        return -5
                    else:
                        if not isStlkVar:
                            if self._sf_sQp.find(f'\n{varNm}<@qp(') < 0:
                                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}<{varDat}>:\n'))
                                self._sf_sSrc = None
                                self._sf_sQp = None
                                return 8
                            else:
                                return -6
                        else:
                            return self.sqtpp_var_stalk(varNm, varDat)      
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_add:
            if not isStlkVar: self._sErr = f'staqtapp1.2 (vars_add) error: {err_vars_add}'
            else: self._sErr = f'staqtapp1.2 (var_stalk) error: {err_vars_add}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_spok_mv_tree(self, trNm: str, initPthLst: list):
        # Adds a depth dict struct for a spahk-mv type tree edits in vfs tqpt source.
        # **Allows staqtapp rev9 seg-read tree operations in layer(s) to stalkvar() &
        # faster protocols--smoother error corrections encountered in build cycles.**
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_rIntA, _sf_rIntB)
        # returns:
        # -1=@initPthLst is empty
        # -2=@initPthLst has invalid chars
        # -3=empty vfs path settings file
        # -4=invalid vfs path
        # -5=duplicate @trNm
        try:
            self._sf_rIntB = len(initPthLst)
            if self._sf_rIntB > 0:
                self._sf_rStrA = str(initPthLst[0])
                if self.sqtpp_smvt_chars_check(self._sf_rStrA): self._sf_rLstA = ["{'"+self._sf_rStrA+"'"]
                else:
                    return -2
                self._sf_rIntA = 1
                if self._sf_rIntB > 1:
                    while self._sf_rIntA < self._sf_rIntB:
                        self._sf_rStrA = str(initPthLst[self._sf_rIntA])
                        if self.sqtpp_smvt_chars_check(self._sf_rStrA): self._sf_rLstA.append(":{'"+self._sf_rStrA+"'")
                        else:
                            return -2
                        self._sf_rIntA+=1
                    self._sf_rStrB = ''.join(self._sf_rLstA)
                    self._sf_rIntA = 0
                    self._sf_rLstA = []
                    while self._sf_rIntA < self._sf_rIntB:
                        self._sf_rLstA.append('}')
                        self._sf_rIntA+=1
                    self._sf_rStrB = f'{self._sf_rStrB}{"".join(self._sf_rLstA)}'
                else: self._sf_rStrB = self._sf_rLstA[0]+'}'
            else:
                return -1
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self._sf_sQp.find(f'\n{trNm}<@qp(') < 0:
                        pSmvt = pickle.dumps(AbsSmvt(ast.literal_eval(self._sf_rStrB)),0).decode().replace('\n','☆')
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{trNm}<@qp({pSmvt}):>:\n'))
                        self._sf_sQp = None
                        self._sf_sSrc = None
                    else:
                        return -5
                else:
                    return -4
            else:
                return -3
        except Exception as err_spok_mv_tree:
            self._sErr = f'staqtapp1.2 (spok_mv_tree) error: {err_spok_mv_tree}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_spok_mv_tree_add_branch(self, trNm: str, smvBrncId, newSmvBrnchId, newSmvBrnchVl):
        # Adds, replaces, shifts or removes branching to mv-tree type. See addbranch_stx
        # __slots__ in use: (_sf_sRtrn, _sf_sSrc, _sf_sVd, _sf_sQp)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@trNm not found in vfs tqpt source
        # -4=@newSmvBrnchId is of invalid chars
        # -5=@newSmvBrnchVl is of invalid chars
        try:
            twRwSrc = None
            if newSmvBrnchVl == None: newSmvBrnchVl = 'None'
            if newSmvBrnchId == None: newSmvBrnchId = 'None'
            if smvBrncId == None: raise Exception('staqtapp1.2 (spok_mv_tree_add_branch) error: @branchId cannot be None')
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self.sqtpp_var_value(trNm):
                        twRwSrc = self._sf_sVd[4:len(self._sf_sVd)-2]
                        self._sf_sVd = None
                        if self.sqtpp_smvt_chars_check(str(newSmvBrnchId)):
                            if self.sqtpp_smvt_chars_check(str(newSmvBrnchVl)):
                                if self._sf_sQp.find(f'\n__KLF__DSG__<@qp(') < 0:
                                    self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n__KLF__DSG__<@qp(null):>:\n')
                                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                                    self.sqtpp_limit_var_domain('__KLF__DSG__', ['sqtpp_mv_prometes_kn','sqtpp_mv_prometes_eb','sqtpp_mv_prometes_gt'])
                                    self.sqtpp_set_vfs_file()
                                    self.sqtpp_vfs_tqpt_file(True)
                                self._sf_sRtrn = self.sqtpp_mv_prometes_kn(False,'ab',str(pickle.loads(str.encode(twRwSrc.replace('☆','\n')))),str(smvBrncId),str(newSmvBrnchId),str(newSmvBrnchVl))
                                if self._sf_sRtrn == -1: raise Exception(f'staqtapp1.2 (mv_tree_add_branch) error: "{smvBrncId}" is a invalid position branch, not found')
                                elif self._sf_sRtrn == -2: raise Exception(f'staqtapp1.2 (mv_tree_add_branch) error: "{smvBrncId}" is a branch-value, not a valid branch-key')
                                elif self._sf_sRtrn == -3: raise Exception('staqtapp1.2 (mv_tree_add_branch) error: invalid parameter(s) @branchId or/and @newBranchId')
                                #print(str(pickle.loads(str.encode(self._sf_sRtrn.replace("☆","\n"))))) #Too many stars for you to count.
                                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{trNm}<@qp({twRwSrc}):>', f'{trNm}<@qp({self._sf_sRtrn}):>'))
                                self._sf_sQp = None
                                self._sf_sSrc = None
                                self._sf_sRtrn = None
                                trRwSrc = None
                            else: 
                                return -5
                        else:
                            return -4
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_spok_mv_tree_add_branch:
            self._sErr = f'staqtapp1.2 (spok_mv_tree_add_branch) error: {err_spok_mv_tree_add_branch}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_spok_mv_tree_get_branch(self, isAlf: bool, trNm: str, brnchId):
        # Mv-tree main spider, get branch value. Very precise, manually, for rev9 vfs-register feature futures. Do not edit.
        # __slots__ in use: (_sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rBoolA)
        # returns: 
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@trNm not found in vfs tqpt source
        try:
            twRwSrc = None
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self.sqtpp_var_value(trNm):
                        twRwSrc = self._sf_sVd[4:len(self._sf_sVd)-2]
                        twRwSrc = str(pickle.loads(str.encode(twRwSrc.replace('☆','\n')))).replace(' ','')
                        self._sf_sVd = None
                        if isAlf and brnchId == None:
                            return self.sqtpp_spok_mv_tree_get_branch_alf(str(brnchId), twRwSrc)
                        elif isAlf and brnchId != None:
                            pass
                        else:
                            brnchId = str(brnchId)
                            if len(brnchId) > 0:
                                if brnchId.find('.') > -1:
                                    self._sf_rLstA = brnchId.split('.')
                                    self._sf_rLstB = []
                                    self._sf_rIntA = len(self._sf_rLstA)
                                    self._sf_rIntB = 0
                                    self._sf_rBoolA = True
                                    while self._sf_rIntB < self._sf_rIntA:
                                        try:
                                            self._sf_rIntD = re.search(r"\'"+re.escape(self._sf_rLstA[self._sf_rIntB])+r"\'", twRwSrc).span(0)
                                        except Exception as e:
                                            self.sqtpp_spok_mv_tree_get_branch_ohm(True, False, None)
                                            return self._sf_rLstB
                                        if self._sf_rBoolA == True:
                                            self._sf_rBoolA = False
                                            sqtpp_spok_mv_tree_get_branch_ohm(False, True, twRwSrc)
                                        else:
                                            if self._sf_rIntD[1] > self._sf_rIntC: sqtpp_spok_mv_tree_get_branch_ohm(False, True, twRwSrc)
                                            else:
                                                self.sqtpp_spok_mv_tree_get_branch_ohm(True, False, None)
                                                return self._sf_rLstB
                                        self._sf_rIntC = self._sf_rIntD[1]
                                        self._sf_rIntB+=1
                                    self.sqtpp_spok_mv_tree_get_branch_ohm(True, False, None)
                                    return self._sf_rLstB
                                else:
                                    if twRwSrc.find(brnchId) > -1:
                                        self._sf_rStrA = re.compile(r"'"+re.escape(brnchId)+r"'\:'.*?'")
                                        self._sf_rStrB = self._sf_rStrA.findall(twRwSrc)
                                        if len(self._sf_rStrB) > 0:
                                            self._sf_rStrB = self._sf_rStrB[0].split(':')
                                            self._sf_rStrB = self._sf_rStrB[1].replace("'",'')
                                            self.sqtpp_spok_mv_tree_get_branch_ohm(True, False, None)
                                            return self._sf_rStrB
                                        else:
                                            self.sqtpp_spok_mv_tree_get_branch_ohm(True, False, None)
                                            return None
                                    else: raise Exception('staqtapp1.2 (spok_mv_tree_get_branch_ohm) error: "' + brnchId + '" not found')
                            else: raise Exception('staqtapp1.2 (spok_mv_tree_get_branch_ohm) error: @branchId cannot be nothing')
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_spok_mv_tree_get_branch_ohm:
            self._sErr = f'staqtapp1.2 (spok_mv_tree_get_branch_ohm) error: {err_spok_mv_tree_get_branch_ohm}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_spok_mv_tree_get_branch_alf(self, brnchId, trSrc):
        # Returns list of all original branch key(s) + value(s) to an @brnchId merged.
        # This parse function should not replace well written logical code, that uses
        # the above function or other to know when merged add branch will be of value.
        # A expensive function to rely upon with compounded calls frequently for trace
        # when a staqtapp mv-tree env-var is many keys & values in a large length dict.
        # As naming applied cannot avoid alf for any find yet in most cases you should.
        # __slots__ in use: (_sf_rLstC, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rBoolB, _sf_rBoolC, _sf_rBoolD)
        # returns: list --> ['br_br:br:bv',...]
        self._sf_rStrC = ''
        self._sf_rStrE = None
        self._sf_rLstC = []
        self._sf_rIntE = 0
        self._sf_rIntF = -1
        self._sf_rIntG = 0
        self._sf_rBoolB = False
        self._sf_rBoolC = False
        self._sf_rBoolD = False
        for self._sf_rStrD in trSrc:
            if self._sf_rBoolB == False and self._sf_rStrE == '}' and self._sf_rStrD == ',': self._sf_rBoolB = True
            elif self._sf_rBoolB == True:
                if self._sf_rBoolC == False and self._sf_rStrD == "'": self._sf_rBoolC = True
                else:
                    if self._sf_rBoolC == False: self._sf_rBoolB = False
                    else:
                        if self._sf_rStrD == '_':
                            self._sf_rIntG+=1
                            if self._sf_rIntG < 2 and len(self._sf_rStrC) > 0:
                                self._sf_rLstC.append(self._sf_rStrC)
                                self._sf_rIntF+=1
                                self._sf_rBoolD = True
                                self._sf_rStrC = ''
                            else:
                                self._sf_rBoolB = False
                                self._sf_rBoolC = False
                                self._sf_rBoolD = False
                                self._sf_rStrC = ''
                                self._sf_rIntG = 0
                                self._sf_rLstC.pop(self._sf_rIntF)
                                self._sf_rIntF-=1
                        else:
                            if self._sf_rStrD == "'":
                                self._sf_rBoolB = False
                                self._sf_rBoolC = False
                                self._sf_rIntG = 0
                                if self._sf_rBoolD == True and len(self._sf_rStrC) > 0:
                                    self._sf_rLstC.append(self._sf_rStrC)
                                    self._sf_rIntF+=1
                                self._sf_rBoolD = False
                                self._sf_rStrC = ''
                            else: self._sf_rStrC = f'{self._sf_rStrC}{self._sf_rStrD}'
            self._sf_rStrE = self._sf_rStrD
            self._sf_rIntE+=1
        if len(self._sf_rLstC) > 0:
            self._sf_rBoolD = []
            self._sf_rIntG = 0
            self._sf_rIntE = int(len(self._sf_rLstC)/2)
            for x in range(self._sf_rIntE):
                self._sf_rBoolD.append(f'{self._sf_rLstC[self._sf_rIntG]}_{self._sf_rLstC[self._sf_rIntG+1]}')
                self._sf_rIntG+=2
                self._sf_rIntF = re.compile(r"'" + re.escape(self._sf_rBoolD[x]) + r"':\{'.*?'")
                self._sf_rStrE = self._sf_rIntF.findall(trSrc)
                self._sf_rStrE = self._sf_rStrE[0].split('{')
                self._sf_rStrE = self._sf_rStrE[1].replace("'", '')
                self._sf_rStrC = self._sf_rBoolD[x]
                self._sf_rBoolD[x] = f'{self._sf_rBoolD[x]}:{self._sf_rStrE}'
                self._sf_rIntF = re.compile(r"'" + re.escape(self._sf_rStrC) + r"':\{'" + re.escape(self._sf_rStrE) + r"'\:'.*?'")
                self._sf_rStrE = self._sf_rIntF.findall(trSrc)
                if len(self._sf_rStrE) > 0:
                    self._sf_rStrE = self._sf_rStrE[0].split(':')
                    self._sf_rStrE = self._sf_rStrE[2].replace("'", '')
                    self._sf_rBoolD[x] = f'{self._sf_rBoolD[x]}:{self._sf_rStrE}'
                else: self._sf_rBoolD[x] = f'{self._sf_rBoolD[x]}:None'
            return self._sf_rBoolD
        else:
            return None
#_______________________________________________________________________________________
    def sqtpp_spok_mv_tree_get_branch_ohm(self, isClr: bool, isOhm: bool, trSrc):
        # Extension for added register record; rev9 vfs integration, thru any fovae-mantis embedded script runs.
        # __slots__ in use: (*_sf_sVd*, _sf_rLstA, _sf_rLstB, _sf_rStrA, /_sf_rStrB/, _sf_rIntB)
        # returns: none
        if isOhm:
            self._sf_rStrA = re.compile(r"'"+re.escape(self._sf_rLstA[self._sf_rIntB])+r"'\:'.*?'")
            self._sf_rStrB = self._sf_rStrA.findall(trSrc)
            if len(self._sf_rStrB) > 0:
                self._sf_rStrB = self._sf_rStrB[0].split(':')
                self._sf_rStrB = self._sf_rStrB[1].replace("'",'')
                self._sf_rLstB.append(f'{self._sf_rLstA[self._sf_rIntB]}:{self._sf_rStrB}')
            else: self._sf_rLstB.append(f'{self._sf_rLstA[self._sf_rIntB]}:None')
        elif isClr:
            self._sf_sSrc = None
            self._sf_sQp = None
        else:
            pass
#_______________________________________________________________________________________
    def sqtpp_var_stalk(self, varNm: str, varDat: str):
        # Re-actions stalkvar instruction sets for pairing ordered var name sequences.
        # **Allows smarter staqtapp rev9 module building gen features in a vfs file**
        # __slots__ in use: (_sf_sSrc, _sf_sVd, _sf_rStrA, _sf_rStrB, _sf_rLstA, _sf_rIntA)
        # returns:
        # -6=var not found in tqpt var source...
        # -7=var to stalk same data @varDat and there is no svvs sub-file present
        # -8=no found svvs commons stalk-entry element list for @varNm
        # -9=tried to begin a stalked env-var with same @varDat for @varNm's data
        try:
            if self._sf_sSrc.find(f'<sbf-{self._sf_sVfsFldr}-svvs:') > -1:
                if self.sqtpp_svvs_list(varNm) == 8:
                    if self.sqtpp_var_value(varNm):
                        if len(self._sf_rLstA) > 1: self._sf_rStrA = ','.join(self._sf_rLstA)
                        else: self._sf_rStrA = self._sf_rLstA[0]
                        if varDat != self._sf_sVd:
                            self._sf_rIntA = len(self._sf_rLstA)+1
                            self._sf_rLstA.append(f'{varNm}_{self._sf_rIntA}')
                            self._sf_rLstA = ','.join(self._sf_rLstA)
                            self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_{self._sf_rIntA}<{varDat}>:\n')
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'({varNm}={self._sf_rStrA})', f'({varNm}={self._sf_rLstA})'))
                        else:
                            self._sf_rStrB = self._sf_sQp
                            self.sqtpp_var_remove(self._sf_rLstA)
                            if self._sf_sSrc.find(f';({varNm}={self._sf_rStrA})') > -1: self._sf_sSrc = self._sf_sSrc.replace(f';({varNm}={self._sf_rStrA})', '')
                            elif self._sf_sSrc.find(f'\n({varNm}={self._sf_rStrA});') > -1: self._sf_sSrc = self._sf_sSrc.replace(f'({varNm}={self._sf_rStrA});', '')
                            else: self._sf_sSrc = self._sf_sSrc.replace(f'\n<sbf-{self._sf_sVfsFldr}-svvs:\n({varNm}={self._sf_rStrA})//>', '')
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_rStrB}:\n', f'{self._sf_sQp}:\n'))
                        self._sf_rLstA = None
                        self._sf_rStrA = None
                        self._sf_rStrB = None
                        self._sf_sSrc = None
                        self._sf_sQp = None
                        return 8
                    else:
                        return -6
                else:
                    if self.sqtpp_var_value(varNm):
                        if varDat != self._sf_sVd:
                            self._sf_rStrA = self.sqtpp_vfs_sub_file(False, False, 'svvs', None)
                            self._sf_rStrB = f'{self._sf_rStrA};({varNm}={varNm}_1)'
                            self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_rStrB)
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_1<{varDat}>:\n'))
                            self._sf_rStrA = None
                            self._sf_rStrB = None
                            self._sf_sSrc = None
                            self._sf_sQp = None
                        else:
                            return -9
                    else:
                        return -6
            else:
                if self.sqtpp_var_value(varNm):
                    if varDat != self._sf_sVd:
                        self.sqtpp_vfs_sub_file(True, None, 'svvs', f'({varNm}={varNm}_1)')
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_1<{varDat}>:\n'))
                        self._sf_sSrc = None
                        self._sf_sQp = None
                    else:
                        return -7
                else:
                    return -6
        except Exception as err_var_stalk:
            self._sErr = f'staqtapp1.2 (var_stalk) error: {err_var_stalk}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_locate_var_stx(self, varNmLst: list, stlkVarNm: str):
        # Multi-vars search, with optional env-var spawned poly-matching find returns.
        # **Allows next-gen staqtapp rev9 bluetooth coms/cmds features in a vfs file**
        # __slots__ in use: (•_rIntA, _sf_sSrc, _sf_sQp, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rIntA, _sf_rIntD)
        # returns: 
        # -1=@varNmLst is empty
        # -2=invalid vfs path
        # -3=empty vfs path settings file
        # -4=@stlkVarNm was not found in a svvs stalk category
        try:
            self._sf_rIntD = len(varNmLst)
            if isinstance(stlkVarNm, str):
                if self._sf_rIntD > 0:
                    if self.sqtpp_set_vfs_file() == 1:
                        if self.sqtpp_vfs_tqpt_file(True) != -1:
                            if self.sqtpp_svvs_list(stlkVarNm) == 8:
                                self._rIntA = 0
                                self._sf_rLstB = []
                                self._sf_rIntA = len(self._sf_rLstA)
                                while self._rIntA < self._sf_rIntD:
                                    if self._rIntA == self._sf_rIntA:
                                        self._sf_rLstA = None
                                        self._sf_sSrc = None
                                        self._sf_sQp = None
                                        return self._sf_rLstB
                                    else:
                                        if self.sqtpp_var_value(self._sf_rLstA[self._rIntA]):
                                            self._sf_rStrA = self._sf_sVd
                                            if self.sqtpp_var_value(varNmLst[self._rIntA]):
                                                if self._sf_rStrA == self._sf_sVd: self._sf_rLstB.append(f'{self._sf_rLstA[self._rIntA]}=1')
                                                else: self._sf_rLstB.append(f'{self._sf_rLstA[self._rIntA]}=-1')
                                            else: self._sf_rLstB.append(f'!searched-var ({varNmLst[self._rIntA]}) data not found:None')
                                        else: self._sf_rLstB.append(f'!spawned-var ({self._sf_rLstA[self._rIntA]}) data not found:None')
                                    self._rIntA+=1
                                self._sf_rLstA = None
                                self._sf_sSrc = None
                                self._sf_sQp = None
                                return self._sf_rLstB
                            else:
                                return -4
                        else:
                            return -3
                    else:
                        return -2
                else:
                    return -1
            else:
                # Standard boaring multi-finds for @varNmLst, True or False list return.
                if self._sf_rIntD > 0:
                    if self.sqtpp_set_vfs_file() == 1:
                        if self.sqtpp_vfs_tqpt_file(True) != -1:
                            self._rIntA = 0
                            self._sf_rLstA = []
                            while self._rIntA < self._sf_rIntD:
                                if self._sf_sQp.find(f'\n{varNmLst[self._rIntA]}<') > -1: self._sf_rLstA.append(True)
                                else: self._sf_rLstA.append(False)
                                self._rIntA+=1
                            self._sf_sSrc = None
                            self._sf_sQp = None
                            return self._sf_rLstA
                        else:
                            return -3
                    else:
                        return -2
                else:
                    return -1
        except Exception as err_locate_var_stx:
            self._sErr = f'staqtapp1.2 (locate_var_stx) error: {err_locate_var_stx}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_locate_var(self, rmv: bool, varNm: str):
        # Searches for @varNm in a set vfs path tqpt file, returns True if found.
        # __slots__ in use: (_sf_rBoolA)
        # returns: -1=invalid vfs path, -3=empty vfs path settings file
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self._sf_sQp.find(f'\n{varNm}<@qp(') > -1: self._sf_rBoolA = True
                    else: self._sf_rBoolA = False
                    if rmv:
                        self._sf_sSrc = None
                        self._sf_sQp = None
                    return self._sf_rBoolA
                else:
                    return -3
            else:
                return -1
        except Exception as err_locate_var:
            self._sErr = f'staqtapp1.2 (locate_var) error: {err_locate_var}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_limit_var_domain(self, varNm: str, fncNm):
        # Adds lock-in function name(s) or other to set path vfs tpqt file for env-vars.
        # __slots__ in use: (_sf_sPq, _sf_sRtrn, _sf_rStrA, _sf_rStrB, _sf_sVfsFldr)
        # returns: -1=empty vfs path stg file, -2=@varNm not found in tqpt vars source
        try:
            self._sf_sRtrn = self.sqtpp_locate_var(False, varNm)
            if self._sf_sRtrn == -3:
                return -1
            elif self._sf_sRtrn:
                if self.sqtpp_vfs_tpqt_file(True) != -1:
                    if self._sf_sPq.find('null') > -1: self.sqttp_tpqt_spok(False, False, varNm, fncNm)
                    else:
                        self._sf_rStrA = self._sf_sPq
                        self._sf_rStrB = re.compile(r'___\|:tpqt-'+re.escape(self._sf_sVfsFldr)+r'<.*?>:')
                        self._sf_sPq = re.sub(self._sf_rStrB, '', self._sf_sPq, count=1)
                        self.sqttp_tpqt_spok(False, True, varNm, fncNm)
                    self._sf_rStrA = None
                    self._sf_sSrc = None
                    self._sf_sQp = None
                    self._sf_sPq = None
                    return 8
            else:
                return -2
        except Exception as err_limit_var_domain:
            self._sErr = f'staqtapp1.2 (limit_var_domain) error: {err_limit_var_domain}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_tqpt_path(self, isSetPth: bool, pth: str):
        # Sets or gets the vfs tqpt file path.
        # __slots__ in use: (none)
        # returns: none
        if isSetPth: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', pth)
        else: self.sqtpp_file(False, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', None)
#_______________________________________________________________________________________
    def sqtpp_file(self, isWrt: bool, pth: str, src: str):
        # Standard read or write file operations.
        # __slots__ in use: (_sf_sSrc)
        # returns: none
        if isWrt:
            with open(pth, mode='w', encoding='utf-8') as wrtFlObj:
                wrtFlObj.write(src)
                wrtFlObj.close()
            wrtFlObj = None
        else:
            with open(pth, mode='r', encoding='utf-8') as rdrFlObj:
                self._sf_sSrc = rdrFlObj.read()
                rdrFlObj.close()
            rdrFlObj = None
#_______________________________________________________________________________________
    def sqtpp_var_value(self, varNm: str) -> bool:
        # Sets variable data(_sf_sVd) of @varNm from set vfs tqpt file content _sf_sQp.
        # __slots__ in use: (_sf_sSrc, _sf_sVd)
        # returns: True or False
        # ):> = m∓ ... {◑>i,...} ⍅ U◐ⁿ⁺ⁱ-U◑ⁱ⁻ⁿ
        self._sf_sVd = re.findall(r'(?s:)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
        if len(self._sf_sVd) > 0:
            self._sf_sVd = self._sf_sVd[0].replace(f'{varNm}<','')
            self._sf_sVd = self._sf_sVd[0:len(self._sf_sVd)-1]
            return True
        else:
            return False
#_______________________________________________________________________________________
    def sqtpp_var_change(self, varNm: str, varDat: str):
        # Changes @varNm's data to @varDat; does no checking of name or data here.
        # Assumes _sf_sSrc & _sf_sQp slots attrs have been set to their constants.
        # __slots__ in use: (_sf_rStrA)
        # returns: none
        rtrn = re.findall(r'(?s:)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
        if len(rtrn) > 0:
            self._sf_rStrA = self._sf_sQp
            self._sf_sQp = self._sf_sQp.replace(f'{rtrn[0]}', f'{varNm}<{varDat}>')
            self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sQp)
            self._sf_rStrA = None
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
#_______________________________________________________________________________________
    def sqtpp_var_remove(self, varNmLst: list):
        # Removes env-var listed stacks from @varNmLst in vfs slots attribute _sf_sQp.
        # __slots__ in use: (_sf_rIntC, _sf_rIntD)
        # returns: none
        self._sf_rIntD = len(varNmLst)
        for self._sf_rIntC in range(self._sf_rIntD): self._sf_sQp = re.sub(r'(?s:.)'+re.escape(varNmLst[self._sf_rIntC])+r'<@qp\(.*?\):>', '', self._sf_sQp)
#_______________________________________________________________________________________
    def sqtpp_svvs_list(self, varNm: str):
        # Sets _sf_rLstA to the viable svvs associated and expanded @varNm category.
        # __slots__ in use: (_sf_rLstA, _sf_rIntA, _sf_rIntB)
        # returns: -8=no found svvs commons stalk-entry element list for @varNm
        self._sf_rLstA = self.sqtpp_vfs_sub_file(False, False, 'svvs', None).split('\n')
        if self._sf_rLstA[1].find(';') > -1: self._sf_rLstA = self._sf_rLstA[1].split(';')
        else: self._sf_rLstA = self._sf_rLstA[1]
        if isinstance(self._sf_rLstA, str):
            if self._sf_rLstA.find(f'({varNm}=') > -1:
                self._sf_rLstA = self._sf_rLstA.split('=')
                self._sf_rLstA = self._sf_rLstA[1]
                if self._sf_rLstA.find(',') > -1:
                    self._sf_rLstA = self._sf_rLstA.split(',')
                    self._sf_rLstA[len(self._sf_rLstA)-1] = self._sf_rLstA[len(self._sf_rLstA)-1].replace(')','')
                else: self._sf_rLstA = [self._sf_rLstA.replace(')','')]
            else:
                return -8
        else:
            self._sf_rIntA = len(self._sf_rLstA)
            self._sf_rIntB = -1
            for sv in range(self._sf_rIntA):
                if self._sf_rLstA[sv].find(f'({varNm}=') > -1:
                    self._sf_rIntB = sv
                    break
            if self._sf_rIntB > -1:
                self._sf_rLstA = self._sf_rLstA[self._sf_rIntB].split('=')
                if self._sf_rLstA[1].find(',') > -1:
                    self._sf_rLstA = self._sf_rLstA[1].split(',')
                    self._sf_rLstA[len(self._sf_rLstA)-1] = self._sf_rLstA[len(self._sf_rLstA)-1].replace(')','')
                else: self._sf_rLstA = [self._sf_rLstA[1].replace(')','')]
            else:
                return -8
        return 8
#_______________________________________________________________________________________
    def sqtpp_tqpt_spdr(self, isRdr: bool, isAllNmbrs: bool, callFnc: str, src: str):
        # Parsing spider for tqpt env-var data. Very precise and tricky, do not edit.
        # __slots__ in use: (_sf_rLstA, _sf_StrA, _sf_StrB, _sf_StrC, _sf_IntA, _sf_IntB)
        # returns:
        # 1 = is all numbers
        # 2 = new line in data, not allowed
        # 3 = is proper @qp(...): char staqtapp tag(s) observe find(s)
        # 4 = proper tag check return with found comma use in variable data
        # 5 = false check for isAllNmbrs
        # 6 = no proper @qp(...): variables' data tags found
        # 7 = missing a closing ): for data declare @qp(
        self._sf_rLstA = [False for _ in range(9)]
        nmbrChrs = set('.-, 0123456789')
        dqRtn = deque()
        lstRtn = []
        dqLst = None
        qdLst = None
        self._sf_rStrB = ''
        self._sf_rStrC = None
        self._sf_rIntA = 0
        self._sf_rIntB = 0
        for self._sf_rStrA in src:
            self._sf_rIntA+=1
            if not self._sf_rLstA[3]:
                if self._sf_rLstA[2]:
                    self._sf_rLstA[0] = False
                    self._sf_rLstA[1] = False
                    self._sf_rLstA[2] = False
                if self._sf_rStrA == '@': self._sf_rStrC = self._sf_rStrA
                elif self._sf_rStrC == '@' and self._sf_rStrA == 'q': self._sf_rStrC = self._sf_rStrA
                elif self._sf_rStrC == 'q' and self._sf_rStrA == 'p': self._sf_rStrC = self._sf_rStrA
                elif self._sf_rStrC == 'p' and self._sf_rStrA == '(':
                    self._sf_rLstA[0] = True
                    self._sf_rLstA[3] = True
            else:
                if self._sf_rStrA == '.':
                    self._sf_rLstA[6] = True
                    if not isRdr: self._sf_rStrB = f'{self._sf_rStrB}{self._sf_rStrA}'
                elif self._sf_rStrA == ',':
                    self._sf_rLstA[4] = True
                    if not isRdr: self._sf_rStrB = f'{self._sf_rStrB}{self._sf_rStrA}'
                elif self._sf_rStrA == '\n':
                    return 2
                elif self._sf_rStrA == ')': self._sf_rStrC = self._sf_rStrA
                elif self._sf_rStrA == ':' and self._sf_rStrC == ')':
                    self._sf_rIntB+=1
                    self._sf_rLstA[1] = True
                    self._sf_rLstA[3] = False
                    if not isRdr and isAllNmbrs:
                        if self._sf_rLstA[4] and self._sf_rLstA[6]:
                            dqLst = self._sf_rStrB.split(',')
                            if callFnc == 'lvsd':
                                qdLst = [dcml(x.strip(' ')) for x in dqLst]
                                dqRtn.append(qdLst)
                            elif callFnc == 'lvss': lstRtn.append(dqLst)
                        elif not self._sf_rLstA[4] and self._sf_rLstA[6]:
                            if callFnc == 'lvsd': dqRtn.append(dcml(self._sf_rStrB.strip(' ')))
                            elif callFnc == 'lvss': lstRtn.append(self._sf_rStrB)
                        elif self._sf_rLstA[4] and not self._sf_rLstA[6]:
                            dqLst = self._sf_rStrB.split(',')
                            if callFnc == 'lvsd':
                                qdLst = [int(x.strip(' ')) for x in dqLst]
                                dqRtn.append(qdLst)
                            elif callFnc == 'lvss': lstRtn.append(dqLst)
                        elif not self._sf_rLstA[4] and not self._sf_rLstA[6]:
                            if callFnc == 'lvsd': dqRtn.append(int(self._sf_rStrB.strip(' ')))
                            elif callFnc == 'lvss': lstRtn.append(self._sf_rStrB)
                    elif not isRdr and not isAllNmbrs:
                        if self._sf_rLstA[4]:
                            dqLst = self._sf_rStrB.split(',')
                            for ds in range(len(dqLst)):
                                self._sf_rLstA[7] = False
                                self._sf_rLstA[8] = False
                                for dChr in dqLst[ds]:
                                    if set(dChr).issubset(nmbrChrs): self._sf_rLstA[7] = True
                                    else:
                                        self._sf_rLstA[7] = False
                                        break
                                    if dChr == '.': self._sf_rLstA[8] = True
                                if self._sf_rLstA[7] and self._sf_rLstA[8]:
                                    if callFnc == 'lvsd': dqRtn.append(dcml(dqLst[ds].strip(' ')))
                                    elif callFnc == 'lvss': lstRtn.append(dqLst[ds])
                                elif self._sf_rLstA[7] and not self._sf_rLstA[8]:
                                    if callFnc == 'lvsd': dqRtn.append(int(dqLst[ds].strip(' ')))
                                    elif callFnc == 'lvss': lstRtn.append(dqLst[ds])
                                elif not self._sf_rLstA[7]:
                                    if callFnc == 'lvsd': dqRtn.append(dqLst[ds])
                                    elif callFnc == 'lvss': lstRtn.append(dqLst[ds])
                        else:
                            self._sf_rLstA[7] = False
                            self._sf_rLstA[8] = False
                            for sChr in self._sf_rStrB:
                                if set(sChr).issubset(nmbrChrs): self._sf_rLstA[7] = True
                                else:
                                    self._sf_rLstA[7] = False
                                    break
                                if sChr == '.': self._sf_rLstA[8] = True
                            if self._sf_rLstA[7] and self._sf_rLstA[8]:
                                if callFnc == 'lvsd': dqRtn.append(dcml(self._sf_rStrB.strip(' ')))
                                elif callFnc == 'lvss': lstRtn.append(self._sf_rStrB)
                            elif self._sf_rLstA[7] and not self._sf_rLstA[8]:
                                if callFnc == 'lvsd': dqRtn.append(int(self._sf_rStrB.strip(' ')))
                                elif callFnc == 'lvss': lstRtn.append(self._sf_rStrB)
                            elif not self._sf_rLstA[7]:
                                if callFnc == 'lvsd': dqRtn.append(self._sf_rStrB)
                                elif callFnc == 'lvss': lstRtn.append(self._sf_rStrB)
                    self._sf_rLstA[2] = True
                    if self._sf_rLstA[4]: self._sf_rLstA[5] = True
                    self._sf_rLstA[4] = False
                    self._sf_rLstA[6] = False
                    if not isRdr: self._sf_rStrB = ''
                elif self._sf_rStrA != ')' and self._sf_rStrA != ':' and self._sf_rStrA != '.' and self._sf_rStrA != ',':
                    if isAllNmbrs:
                        if not set(self._sf_rStrA).issubset(nmbrChrs):
                            return 5
                    if not isRdr: self._sf_rStrB = f'{self._sf_rStrB}{self._sf_rStrA}'            
        if self._sf_rLstA[0] and not self._sf_rLstA[1]:
            return 7
        else:
            if not isRdr:
                if callFnc == 'lvsd':
                    return dqRtn
                elif callFnc == 'lvss':
                    return lstRtn
            else:
                if isAllNmbrs:
                    return 1
                else:
                    if self._sf_rIntB > 0:
                        if callFnc != 'savn':
                            return 3
                        else:
                            if self._sf_rLstA[5]:
                                return 4
                            else:
                                return 3
                    else:
                        return 6
#_______________________________________________________________________________________
    def sqttp_tpqt_spok(self, pq_isRdr: bool, pq_isExst: bool, pq_varNm: str, pq_fncNm):
        # Handles vfs tpqt lock var file reads & writes. Is very accurate, do not edit!
        # __slots__ in use: (_sf_sPq, _sf_rLstA, _sf_rLstB, _sf_rIntA, _sf_rIntB, _sf_rStrA, _sf_rStrB, _sf_rBoolA, _sf_rBoolB)
        # returns: 8, '<:!!'=no locks block find
        self._sf_rBoolA = None
        self._sf_rBoolB = None
        self._sf_rLstA = None
        self._sf_rLstB = None
        self._sf_rIntA = None
        self._sf_rIntB = None
        self._sf_rStrB = None
        if pq_isRdr:
            self._sf_rBoolA = False
            self._sf_sPq = self._sf_sPq[1:len(self._sf_sPq)]
            self._sf_rStrB = re.compile(r'<:'+re.escape(pq_varNm)+r'=(?s:.*?).*:>')
            for vrMtc in self._sf_rStrB.findall(self._sf_sPq):
                if len(vrMtc) > 0:
                    self._sf_rBoolA = True
                    self._sf_rLstB = vrMtc
                    break
            if self._sf_rBoolA:
                return self._sf_rLstB
            else:
                return '<:!!'
        else:
            if isinstance(pq_fncNm, str): self._sf_rBoolB = False
            elif isinstance(pq_fncNm, list): self._sf_rBoolB = True
            if pq_isExst:
                self._sf_rBoolA = False
                self._sf_sPq = self._sf_sPq[1:len(self._sf_sPq)]
                self._sf_rStrB = re.compile(r'<:'+re.escape(pq_varNm)+r'=(?s:.*?).*:>')
                for vrMtc in self._sf_rStrB.findall(self._sf_sPq):
                    if len(vrMtc) > 0:
                        self._sf_rBoolA = True
                        self._sf_rLstB = vrMtc
                        break
                if self._sf_rBoolA:
                    self._sf_sPq = self._sf_sPq.replace(f'\n{self._sf_rLstB}', '')
                    self._sf_rLstA = self._sf_rLstB.split('\n')
                    self._sf_rLstA[len(self._sf_rLstA)-1] = self._sf_rLstA[len(self._sf_rLstA)-1].strip(':>')
                    self._sf_rLstA.pop(0)
                fncSet = set()
                if self._sf_rBoolB:
                    for stA in range(len(pq_fncNm)): fncSet.add(pq_fncNm[stA])
                if self._sf_rBoolA:
                    for stB in range(len(self._sf_rLstA)): fncSet.add(self._sf_rLstA[stB])
                if not self._sf_rBoolB: fncSet.add(pq_fncNm)
                self._sf_rIntB = 0
                self._sf_rLstB = []
                self._sf_rIntA = len(fncSet)-1
                if self._sf_rIntA < 0:
                    return 8
                else:
                    for f in fncSet:
                        if self._sf_rIntB == 0:
                            self._sf_rLstB.append(f'<:{pq_varNm}=\n')
                            if self._sf_rIntA > 0: self._sf_rLstB.append(f'{f}\n')
                            else:
                                self._sf_rLstB.append(f'{f}:>')
                                break
                        elif self._sf_rIntB == self._sf_rIntA:
                            self._sf_rLstB.append(f'{f}:>')
                            break
                        else: self._sf_rLstB.append(f'{f}\n')
                        self._sf_rIntB+=1
                self._sf_rLstB = ''.join(self._sf_rLstB)
                self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_rStrA}:\n', f'___|:tpqt-{self._sf_sVfsFldr}<tpqt,{len(pq_varNm)},[E*]>:\n{self._sf_sPq}\n{self._sf_rLstB}:\n')
                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
            else:
                self._sf_rLstB = []
                if self._sf_rBoolB:
                    self._sf_rIntA = len(pq_fncNm)
                    for f in range(self._sf_rIntA):
                        if f < 1:
                            self._sf_rLstB.append(f'<:{pq_varNm}=\n')
                            if self._sf_rIntA > 1: self._sf_rLstB.append(f'{pq_fncNm[f]}\n')
                            else:
                                self._sf_rLstB.append(f'{pq_fncNm[f]}:>')
                                break
                        elif f == self._sf_rIntA-1:
                            self._sf_rLstB.append(f'{pq_fncNm[f]}:>')
                            break
                        else: self._sf_rLstB.append(f'{pq_fncNm[f]}\n')
                else: self._sf_rLstB = [f'<:{pq_varNm}=\n{pq_fncNm}:>']
                self._sf_rLstB = ''.join(self._sf_rLstB)
                self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sPq}:\n', f'___|:tpqt-{self._sf_sVfsFldr}<tpqt,{len(pq_varNm)},n>:\n{self._sf_rLstB}:\n')
                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
#_______________________________________________________________________________________
    def sqtpp_mv_prometes_kn(self, isRead: bool, dsgFnc: str, srcStr: str, brId: str, brNwId: str, brNwVl: str):
        # __slots__ in use: (none)
        # returns: (mv-tree dict ast encoded)
        if not isRead:
            if dsgFnc == 'ab':
                if len(brId) > 0 and len(brNwId) > 0:
                    srcStr = srcStr.replace(' ', '')
                    if srcStr.find(":'" + brId + "'") == -1:
                        pxLst = None
                        try:
                            pxLst = re.search(r"\'" + re.escape(brId) + r"\'", srcStr).span(0)
                        except Exception as e:
                            return -1
                        slLst = [srcStr[0:pxLst[1]], srcStr[pxLst[1]:len(srcStr)]]
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
                        return pickle.dumps(AbsSmvt(ast.literal_eval(self.sqtpp_mv_prometes_eb(cfgL, cfgR, slLst, brId, brNwId, brNwVl))),0).decode().replace('\n','☆')
                    else:
                        return -2
                else:
                    return -3
#_______________________________________________________________________________________
    def sqtpp_mv_prometes_eb(self, hldL: int, hldR: int, slTr: list, br: str, brNw: str, brVl: str):
        # __slots__ in use: (none)
        # returns: (sqtpp_mv_prometes_gt encoded)
        pxLst = None
        if hldL == 1:
            if hldR == 1:
                pxLst = self.sqtpp_smvt_char_seeks('plr', slTr[1], None)
                if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                    self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                    return self.sqtpp_mv_prometes_gt(":'", None, slTr, pxLst, br, brNw, brVl)
                else:
                    pass
            elif hldR == 2:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:2):')
                return self.sqtpp_mv_prometes_gt(":{", None, slTr, pxLst, br, brNw, brVl)
            elif hldR == 3:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                return self.sqtpp_mv_prometes_gt("},", None, slTr, pxLst, br, brNw, brVl)
            else:
                pass
        elif hldL == 2:
            if hldR == 1:
                pxLst = self.sqtpp_smvt_char_seeks('plr', slTr[1], None)
                if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                    self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                    return self.sqtpp_mv_prometes_gt(":'", None, slTr, pxLst, br, brNw, brVl)
                else:
                    pass
            elif hldR == 2:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:2):')
                return self.sqtpp_mv_prometes_gt(":{", None, slTr, pxLst, br, brNw, brVl)
            elif hldR == 3:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                return self.sqtpp_mv_prometes_gt("},", None, slTr, pxLst, br, brNw, brVl)
            else:
                pass
        elif hldL == 3:
            if hldR == 1:
                pxLst = self.sqtpp_smvt_char_seeks('plr', slTr[1], None)
                if slTr[1].find(",", pxLst[1]+1, pxLst[1]+2) > -1 or slTr[1].find("}", pxLst[1]+1, pxLst[1]+2) > -1:
                    self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                    return self.sqtpp_mv_prometes_gt(":'", None, slTr, pxLst, br, brNw, brVl)
                else:
                    pass
            elif hldR == 2:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:2):')
                return self.sqtpp_mv_prometes_gt(":{", None, slTr, pxLst, br, brNw, brVl)
            elif hldR == 3:
                self.sqtpp_var_change('__KLF__DSG__', f'@qp({hldL}:{hldR}:1):')
                return self.sqtpp_mv_prometes_gt("},", None, slTr, pxLst, br, brNw, brVl)
            else:
                pass
        else:
            pass
#_______________________________________________________________________________________
    def sqtpp_mv_prometes_gt(self, dsg: str, extDsg: str, slTr: list, pxLst: list, br: str, brNw: str, brVl: str) -> str:
        # Brackets assembler for mv-tree dict type return. Resets slots attr _sf_sKntId.
        # __slots__ in use: (_sf_sKntId, _sf_rLstA, _sf_rStrA)
        self._sf_rStrA = None
        self._sf_rLstA = None
        self._sf_sKntId = None
        if dsg == ":'":
            self._sf_rLstA = [slTr[1][0:pxLst[1]+1], slTr[1][pxLst[1]+1:len(slTr[1])]]
            slTr[1] = None
            self._sf_rStrA = slTr[0] + self._sf_rLstA[0] + ",'" + br + "':{'" + brNw + "':"
            if len(brVl) > 0: self._sf_rStrA += "'" + brVl + "'}" + self._sf_rLstA[1]
            else:
                self._sf_sKntId = random.randint(11111111,99999999)
                self._sf_rStrA += "'knt__" + str(self._sf_sKntId) +"'}" + self._sf_rLstA[1]
            return self._sf_rStrA
        elif dsg == ":{":
            brkId = None
            if self.sqtpp_var_value('__KLF__DSG__'): self._sf_sVd = self._sf_sVd.replace('@qp(','').replace('):','')
            else: raise Exception('staqtapp1.2 (mv_prometes_gt) error: __KLF__DSG__ mv-tree setting values not found!')
            if self._sf_sVd != 'null': brkId = int(self._sf_sVd[len(self._sf_sVd)-1:len(self._sf_sVd)])
            else: brkId = 0
            if brkId < 5:
                self._sf_rStrA = slTr[0] + ":{'" + brNw + "':'"
                if len(brVl) > 0: self._sf_rStrA += brVl + "'},'" + br + "_" + brNw + "'" + slTr[1]
                else:
                    self._sf_sKntId = random.randint(11111111,99999999)
                    self._sf_rStrA += "'knt__" + str(self._sf_sKntId) + "'},'" + br + "_" + brNw + "'" + slTr[1]
                return self._sf_rStrA
            else:
                pass
        elif dsg == "},":
            slTr[0] = slTr[0].replace(br + "'", brNw + "':'")
            if len(brVl) > 0: slTr[0] += brVl + "'"
            else:
                self._sf_sKntId = random.randint(11111111,99999999)
                slTr[0] += "knt__"+ str(self._sf_sKntId) + "'"
            return ''.join(slTr)
#_______________________________________________________________________________________
    def sqtpp_smvt_char_seeks(self, dsg: str, src: str, pos: list):
        # Returns char positionals for @sqtpp_mv_prometes_eb() brackets decisions.
        # __slots__ in use: (_sf_rLstB, _sf_rIntA, _sf_rStrB, _sf_rStrC, _sf_rBoolA, _sf_rBoolB)
        self._sf_rStrC = None
        if dsg == 'plr':
            self._sf_rLstB = [None, None]
            self._sf_rBoolA = True
            self._sf_rBoolB = False
            self._sf_rIntA = 0
            for self._sf_rStrB in src:
                if self._sf_rStrB == "'" and self._sf_rBoolA:
                    self._sf_rBoolA = False
                    self._sf_rLstB[0] = self._sf_rIntA
                elif self._sf_rStrB == "'" and not self._sf_rBoolA and not self._sf_rBoolB:
                    self._sf_rBoolB = True
                elif self._sf_rBoolB:
                    if self._sf_rStrC == "'" and self._sf_rStrB == ":":
                        self._sf_rLstB[1] = self._sf_rIntA-1
                        return self._sf_rLstB
                    elif self._sf_rStrC == "'" and self._sf_rStrB == "}":
                        self._sf_rLstB[1] = self._sf_rIntA-1
                        return self._sf_rLstB
                    elif self._sf_rStrC == "'" and self._sf_rStrB == ",":
                        self._sf_rLstB[1] = self._sf_rIntA-1
                        return self._sf_rLstB
                self._sf_rStrC = self._sf_rStrB
                self._sf_rIntA+=1
#_______________________________________________________________________________________
    def sqtpp_chars_check(self, dsg: int, txt: str) -> bool:
        # Returns True if @txt is of allowed chars from the selected set comparison chars.
        # __slots__ in use: (_sf_rBoolA)
        # returns: True or False
        self._sf_rBoolA = False
        if dsg == 1:
            vfsDirAllwdChars = set('-ABCDEFGHIJKLMNOPQURSTVWXYZabcdefghijklmnopqurstvwxyz')
            if set(txt).issubset(vfsDirAllwdChars): self._sf_rBoolA = True
        elif dsg == 2:
            if set(txt).issubset(SQTPP_SET_VARS): self._sf_rBoolA = True
        return self._sf_rBoolA
#_______________________________________________________________________________________
    def sqtpp_smvt_chars_check(self, src: str) -> bool:
        # Spok-mv tree operations chars checks specific. Non-allowed chars for
        # the branch-keys & branch-values: \n ,:'{ }☆ Staqtapp will not write
        # @qp(...): tagged env-var data with '\n' chars, includes all versions.
        # __slots__ in use: (none)
        # returns: True or False
        nc = [":", ",", "{", "}", "'", "\n", "☆"]
        if isinstance(src, str):
            for chr in src:
                if chr in nc:
                    return False
            return True
        elif src != None:
            srcLen = len(src)
            for x in range(srcLen):
                for chr in src[x]:
                    if chr in nc:
                        return False
            return True
        else:
            return True
#_______________________________________________________________________________________
    def sqtpp_err_rcrd(self, errMsg: str) -> str:
        # Writes any main parsing function type errors to a err-log file to staqtapp1_2 folder.
        # __slots__ in use: (none)
        # returns: FNC-ERR or FOO-BAR
        try:
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/err-log.txt', errMsg)
            return 'FNC-ERR'
        except Exception as err_err_rcrd:
            return 'FOO-BAR'
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_________________________IMPORT CALLABLE FRONT FUNCTIONS:
#_______________________________________________________________________________________
def makevfs(vfsFileName: str, directoryName: str, folderName:str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_makevfs(vfsFileName, directoryName, folderName)
#_______________________________________________________________________________________
def addvar(varName: str, varData: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_addvar(varName, varData)
#_______________________________________________________________________________________
def addtree_stx(treeName: str, initialTreePathList: list):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_addtree_stx(treeName, initialTreePathList)
#_______________________________________________________________________________________
def addbranch_stx(treeName: str, branchKey, newBranchKey, newBranchValue):
    # @branchKey, @newBranchKey and @newBranchValue either str or int.
    sqtppCls = Sqtpp()
    sqtppCls.mcf_addbranch_stx(treeName, branchKey, newBranchKey, newBranchValue)
#_______________________________________________________________________________________
def getbranch_stx(isAlf: bool, treeName: str, branchKey):
    # @branchKey either str or int.
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_getbranch_stx(isAlf, treeName, branchKey)
#_______________________________________________________________________________________
def lockvar(varName: str, fncName):
    # @fncName can be either a single str or list of str elements
    sqtppCls = Sqtpp()
    sqtppCls.mcf_lockvar(varName, fncName)
#_______________________________________________________________________________________
def findvar(varName: str) -> bool:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_findvar(varName)
#_______________________________________________________________________________________
def findvar_stx(varNameList: list, stalkVarName: str) -> list:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_findvar_stx(varNameList, stalkVarName)
#_______________________________________________________________________________________
def stalkvar(varName: str, varData: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_stalkvar(varName, varData)
#_______________________________________________________________________________________

def test():
    #sfCls = SqtppFncs()
    # ><)))))))))))))))))'>-------------------------------------------------------
    #makevfs('vfs-test','dir-test','folder-test')
    #addvar('stalk_var1', '@qp(78000,xrp):')
    #print(findvar('faster_stacks'))
    #lockvar('faster_stacks3', ['someFnc12','someFnc8','someFnc14','someFnc19'])
    #stalkvar('faster_stacks3', '@qp(1,2,3,4,5):@qp(6,7,8,9,0):')
    #print(findvar_stx(['faster_stacks2','faster_stacks4'], 'faster_stacks3'))
    #addtree_stx('tree_test1', ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    #addbranch_stx('tree_test1', 'b', 'knt', 7948233)
    print(getbranch_stx(True, 'tree_test1', None))
    #--------------------------------------------------------------------<'(((((>< 
test()
        
