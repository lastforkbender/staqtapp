#Staqtapp-v1.2.194
#//////////••        .                           .
#/////////••                 .                                   •
#////////••    .                                        •            
#///////••                        / //__|__\\ \             .             •
#//////•• .         .            / //___|___\\ \       .   •          
#\\\\\\••      .                 \.\\_._|_._//./                                .
#//////••                 .      / //___|___\\ \         .         
#///////••  .      .              / //_____\\ \                         •
#////////••     .                  / //___\\ \     •            .
#////////••              __________/ //___\\ \_________                     •
#//////////••          __________________________________     •





# UPDATE SUN, JUN16: Ready to complete the run lambda fnc from tqpt source call using
# a manifested slots performance module instead of eval function: sqtpp_lambda_lambda
# _rplc() parsing function works great now, rather use .replace() but had to have slicing.



# SQTPP V1.2 VFS Env-Vars Library Description:
    
# A rework of the original Staqtapp env-vars library. Uses a vfs system for both tqpt,
# tpqt and other needed files. Built to last in one concentrated module for __slots__
# performance, with same thorough error checking and stpx type function calling. You
# set the vfs dir path to a tqpt variables file & all else handled with min param use.
# (A vfs staqtapp 1.2 file must be created first. Auto sets the tqpt vars set path.)

# This env-var library has features included for simulations in q-bit computing via
# stalkvar(), joinvars(), changevar(), addtree_stx(), addbranch_stx(), getbranch_stx(),
# revar() and findvar_stx(). Nicknamed the tangent-8 for all Staqtapp versions. With
# these 8 functions, can be implementations of gate splicing across the env-var stacks
# in multiple vfs files, static recursions optional from a sliding deque of tree vals,
# and merged spawned interlinking gates with lockvar() and keyvar() in outer-phasing
# to a tri-junction with stalkvar spawned vars; assigned to lockvar as move|lock|key,
# with the addbranch_stx() & getbranch_stx() merge branch and shift specific feature.

# If you need the most secure env-vars library in the world, Staqtapp-Koch version,
# then you can contact me by the email below, with agreements by voice/phone arranged.
# (See the renamevar_stx() function description for details on why is Staqtapp-Koch.)

#_______________________________________________________________________________________
#     SQTPP V1.2 MODULE IMPORT FUNCTIONS USE:
#
#
#     ** this all in one staqtapp module has no third party libraries depends **
#
#
# --> makevfs(vfsFileName, directoryName, folderName), builds a .sqtpp vfs file
#     in current ../staqtapp/* directory; @vfsFileName cannot include ':' chars,
#     tqpt file auto inserted to sub-folder naming of @folderName & is set path.
#
# --> setpath(vfsFileName, directoryName, folderName), sets the working path for
#     the .sqtpp vfs file @vfsFileName, inline with @directoryName + @folderName
#     paths given to a env-var stack/tqpt file. This can also be done by opening
#     the .stg file in the current working module dir .../staqtapp1_2/ where for
#     a path example: 'vfs-A:dir-A:folder-A:subFolder-A:tqpt-A' can be editted.
#     A subfolder name required and only dash chars - allowed, not underscores _.
#     By use of this function is assumed @folderName is same for subfolder name.
#     (This wouldn't be true for a rev9 built vfs file having many dirs+folders.)
#
# --> addvar(varName, varData), adds variable to path set vfs tqpt file. @varData
#     must be tagged with '@qp(...):' for staqtapps unique read parsing routines.
#     Can be as many @qp(...): tags as needed, with commenting in between. Read as
#     a comma separation for a list return when more than one. This function does
#     not change variable data, see changevar to edit stacked variable datas. Is
#     suggested to use lockvar after adding a variable with this function. **If 
#     storing a lambda function as a env-var runnable, only use one @qp(...): tag
#     for that lambda function use, including the lambda name & equal sign for the
#     function. @varName is ignored in this case. You can also skip qp tagging for
#     this type env-var storing of which gets cat tagged anyway. See lambdavar().
#
# --> listvars(), returns stack list names of current env-vars in tqpt vfs source.
#
# --> joinvars(newVarName, varNames), as a list of str names @varNames, this will
#     join together those env-var datas at the qp(...): taggings merged into one
#     new env-var @newVarName. Precaution assumed, if does not find a valid name
#     listed in tqpt env-var source then does not add to joining. If @newVarName is
#     a stalked env-var then will merge all spawned vars from a stalkvar use. (No
#     spawned vars are removed from svvs listing or the tqpt vars stack.) No join
#     for any env-var data having chars ☆ in it, will raise exception that it is a
#     smv-tree type error that cannot be merged with other env-vars. This is power-
#     ful feature in connect of stalkvar function env-var spawned data use, of which
#     is possible to do multiple layered recursion from just a singular event loop.
#     However in some adv cases, would need the raw @qp(...): tagging to manipulate
#     ast converted smv-tree dict type for this mathematically, via some other dict
#     type conversions or abstract reductions of paired branching, see loadvar_stx.
#
# --> changevar(varName, newVarData), change @varName env-var data to @newVarData
#     if @newVarData has proper @qp(...): data tag(s) found. To change the names
#     of env-vars in a vfs tqpt source, see renamevar. Duplicates only allowed for
#     the stalkvar() feature. *This function should be used with lockvar & keyvar.
#     If the @varName is a stalked env-var, the original stalked and not the other
#     incremented spawned vars from it, then this function will check if any of --
#     the incremented spawned var data matches the @newVarData string. If it does
#     then any spawned vars matching @newVarData are removed; and any spawned vars
#     left are renamed of a new incremented naming, re-named to a new number order.
#     This changes no env-var data. Becomes a find and remove operation allowing a
#     programmer more advanced control over stalkvar spawned env-vars, in a larger
#     scope use of stalkvar env-var spawnings in the tqpt source. If any spawned
#     env-var is removed from tqpt and svvs sub file listings, is also removed @ a
#     lockvar tpqt listing if found. Will not do any of this if the stalked var is
#     read as having only one spawned env-var. Raises a non-allowed svvs exception.
#     If this function switches to this type find & del, returns named list of the
#     spawned env-var(s) it deleted or else returns None.
#
# --> addtree_stx(treeName, initialTreePathList), adds a initial dict type tree
#     structure to vfs tqpt stacks for deep spahk-mv type tree edits. @initial-
#     TreePathList is simply a list elements of strings or int values. Chars not
#     allowed @initialTreePathList string element(s) are \n,':{} and ☆ The ---
#     other functions that edit this type, all stalkvar() type similiar actions.
#
# --> addbranch_stx(treeName, branchId, newBranchId, newBranchValue), Adds, shifts,
#     replaces, or spawns merged branch for a mv-tree. Behavior of mv-tree branch
#     edits are in exotic relation to stalkvar. The examples below show this. The
#     first dict key cannot be changed, will raise exception. Is 'a' in examples:
#
#       Example A:
#       smvt-state {'a':{'b':{'c':'vl1','d':'vl2'}, 'e':'vl3'}}
#       .addbranch_stx('smvt_tree_a', 'c', 2035, None)
#       results ---> {'a':{'b':{'c':{'2035':'knt'}, 'd':'vl2'}, 'e':'vl3'}}
#       'vl1' now a nested branch, not a separate value
#  
#       Example B:
#       smvt-state {'a':{'b':{'c':'vl1'},'e':'vl3'}}
#       .addbranch_stx('smvt_tree_b', 'b', 2056, None)
#       results ---> {'a':{'b':{'2056':'knt'},'b_2056':{'c':'vl1'},'e':'vl3'}}
#       'b' hoplinked to branch&value, however not full link replace parse 
#       @'b_2056', feature serves as replace options and other features
#  
#       Example C:
#       smvt-state {'a':{'b':{'c'},'e':'vl3'}}
#       .addbranch_stx('smvt_tree_c', 'c', 2032, 2051)
#       results ---> {'a':{'b':{'2032':'2051'},'e':'vl3'}}
#       'c' replaced by {'2032':'2051'} branch
#
# --> getbranch_stx(isAlf, treeName, branchId), returns a found branch value or
#     None. @branchId can be either int or str for param usage. @isAlf is for a
#     return list of all original branch key(s) + value(s) to an @brnchId merge.
#     The return list format as ['br_br:br:bv',...], whereof first after :orig:
#     Avoid using alf as much as possible on large mv-trees. If use, @branchId=
#     None. A tip to this type dict tree type: Record env-var any adds done last
#     to a branch, that can be then known replaced or merged with other branch.
#     The staqtapp mv-tree type can be difficult to use at first, however opens
#     a whole other world for *indirect & *adapt recursion unions with stalkvar.
#
# --> lockvar(varName, fncName), adds a function name or else associated to a var-
#     Name in a tpqt type file. This can then be used with keyvar to gate what is
#     allowed to edit the env-var. There no real security/math to it like the Koch
#     version Staqtapp, however is very useful in preventing any env-vars mishaps.
#     @fncName can be either a string; or, list parameter of string names properly.
#     To delete vfs entries from a lockvar use, see lockdel to do that effectively.
#
# --> locklist(varName), returns listed fnc/etc. names for a lockvar tpqt vfs entry.
#
# --> keyvar(varName, fncName), returns True if @fncNm is allowed to edit @varNm,
#     is a listed key to @varNm. Other very useful conditions of this include ---
#     @fncNm being a env-var name of a spawned var set, from use of the stalkvar
#     function, with multi-processing. Unlike Staqtapp Koch version has no vfs --
#     tpqt directory restriction features via a directory split route linkers. The
#     listed keys to the @varName are a clear text read in view of .sqtpp vfs file.
#     Attempting to encrypt vfs file yourself, with standard encrypt libraries will
#     not only prove poor performance but will also be insecure in the near future.
#     (That includes Kyber lattice encrypt that can be cracked by parentheses char
#     chewing attacks using a dual side channel repeater from a mere single phone.)
#
# --> revar(isNewSetVfsPath, newVfsFileName, newVfsDirName, newVfsFldrName),
#     replicates a new .sqtpp vfs file in the .../staqtapp/ folder, having only the
#     env-var(s) from the current set vfs file that are linked to a tpqt lockvar
#     entry. @isNewSetVfsPath as True will reset current set vfs file path to the
#     now new vfs file and it's tqpt path. (If this function is called and the ----
#     current set vfs file has no tpqt lockvar entries found a exception is raised.)
#     **This function is used for advanced rev9 staqtapp features in building custom
#     env-var library modules from within a staqtapp1.2 vfs thru self-replications.
#     Can respawn any missing stalkvar() env-vars to a new self-made svvs sub file.
#     The svvs file from the current set vfs file is lost on the new transfer.**
#
# --> lambdavar(lambdaName, inputVars), finds @lambdaName function in tqpt vfs file,
#     creates a low footprint temp module with found lambda function, imports it and
#     runs it for the return. (To get a list of all stored lambda functions in a tqpt
#     vfs sqtpp subfile use lambdalist()) Once this function is used, makes a module
#     in current staqtapp1_2/ working folder for returns use: .../sqtpp_1_2_LMB.py If
#     @lambdaName found in module then direct runs it from there, no checks | loading.
#     @inputVars as a list only of correct format as ['x=8','y=7,6,5,4,3','z=l,i,s,t']
#     **The module sqtpp_1_2_LMB.py written does use slots attributes performance ---
#     mapping any new lambda parameters variables to newly added created slots attrs.
#     Keeping the lambda params names generic lowers the amount of slots attrs made.**
#     (NOT YET IMPLEMENTED)
#
# --> lambdalist(isComplete), returns list of all found lambda functions in tqpt src,
#     with the element(s) format being the function name and it's parameters if any.
#     Example list return: ['my_lambda_function1(i,j,k)','my_lambda_function2(l)'] or
#     if @isComplete true then returns the complete string of the lambda function(s).
#     This staqtapp method returns an empty list if no lambda function(s) were found.
#     (NOT YET IMPLEMENTED)
#
# --> removevar(varName), removes env-var from tqpt stack and any tpqt lockvar block.
#     Will not delete a stalked env-var or a dark env-var, raises a exception that
#     the @varNm parameter choice is connected to a vfs dependency function only.
#     This is a dangerous function; well not as dangerous as us, to rely on for env
#     var use. It is much better to just rename a env-var and go from there, when
#     then use of changevar function. Keeps your env-var stack smaller and more
#     easily controlled instead of wild adding until you don't know what to remove.
#     Which could then result in bad collisions of a spawned or dark env-var group
#     if using those to protect a hidden database of passwords or drone config file.
#
# --> darkvar(), mirrors any removal of a stalked env-var, placing the then removed
#     spawned vars datas to a assigned address, that is all the incremented numbers
#     of the spawned var namings to be removed. After this assigns a pointer to the
#     address by dash, example 56791218-3095903, a random 7-digit palindrome number
#     that will then be of a vssv sub-file content. A darkvar, or dark env-var does
#     not repeat any char when saving the data of the removed vars to a @qp(...):
#     tagging. It only interacts with other env-vars by any palindrome sequences of
#     those chars, if is visible/matching @ the new address to env-var(s) data. This
#     type env-var uses menorah base numbering, non-znero by shifting the pointer to
#     a most probable next match in chars of a recent env-var data viewed. The slots
#     attributes specific to this env-var are _sf_sLstX, _sf_sStrX and _sf_sIntX. To
#     call on this non-parameter method it will react either two ways: One, _sf_sLstX
#     is of a visible relevant list of env-var(s) in the tqpt source and is spawned
#     set of env-var(s) with at least one tpqt lock block visible. This will cause a
#     assignment probable str to @_sf_sStrX and a new palindrome pointer @_sf_sIntX.
#     Or two, then uses what is done by the first to build a new env-var having ---
#     data of a probable set of decisions chars relevant to a new spawned var added.
#     The rev9 features of this library to be added later, uses this to vastly alter
#     any module building it does from another, by decisions in conditionals choice;
#     by lengthing a klf id depend string or splicing it to lesser address probables.
#     (The Staqtapp-Koch does this similar type env-var actions by numerous modules
#     classed Seten modules, yet for random length key padding in vfs-dir routing.)
#     The type mathematical looping of this function with palindrome address shifts
#     is tri-half looping, just as seen on the Menorah. Where a pairing loop is not
#     matched to a static center necessary pairing(Base10), however of LR.R or RL.L
#     rotation, of which either larger loop with middle exact to 1 | smaller " to 1.
#     (NOT YET IMPLEMENTED)
#
# --> renamevar_stx(varName newVarName), this function a important one to the data
#     structure of this new staqtapp one version. It actions a normal renaming of a
#     env-var if does not conflict with other namings and can also change the ----
#     spawned var(s) naming(s) from a stalkvar() use just as staqtapp koch version.
#     To do this there must be more than one spawned env-var from a stalked var. By
#     param @newVarName being a int and @varName being the stalked var, the renames
#     of the spawned vars take order increasing from the int value; but if negative
#     number or zero for @newVarName then will remove the spawned var(s) until reach
#     of int one or is only one spawned var left..if negative int, replaced positive.
#     That explained, removes spawned vars by nearest increment of the spawned names.
#     With negative param does not rename any individual spawned of env-var namings,
#     the renaming is central of svvs list, shifted left after any number of removes.
#     This is tricky at first to use with negative del order, however a very powerful
#     useable when matching spawned env-vars to a replaced branching of smv-tree use.
#     (The Staqtapp Koch version does this in between multi-layered encryption key --
#     padding, while encrypt of vdf path directories as most secure env-var vfs ever.)
#     Returns 1 if renamed env-var, 2 if renamed spawned var(s) and there is only --
#     one left spawned var of the stalked var and 3 if renamed spawned env-var(s).
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
# --> vardata_stx(isRegex, varNameList, search), returns list type from search on
#     the @varNameList if @search terms found in a env-var data; returns names of
#     env-var(s) from @varNameList, not the env-var data. @isRegEx instructs the
#     @search is a regex type pattern search. Can search mv-tree stx var types of
#     their keys & values for a listed name return also if @search pattern found.
#     Either way, regular find or regex of no found results returns a empty list.
#
# --> loadvar(isAllNumbers, varName, mode), returns a env-var data from @varName.
#     @mode either 'd' for deque type return or 's' for a string type return. All
#     tqpt env-var data parsing is smart on if is a list return, has numbers with
#     decimals for decimal type returns and etc. via @qp(...): env-var data tags.
#     Be aware if @isAllNumbers set to True then will return list within list if
#     reads multiple qp tags having commas. This will also convert to decimal if
#     tqpt_spdr() finds use of '.' with numbers for a deque type returns. (By use
#     of char * only @varName, load most recent added spawned var from stalkvar()
#     function use. This spawned var tracking found in the tpqt lockvar stacks --
#     with the special header naming as '___SQTPP___MRSV___' and can be editted.)
#
# --> stalkvar(varName, varData), keeps the original env-var as a static read only
#     var and makes a new but same @varName, with extension '_#' as a numbered
#     increment _1~#. If the @varData matches the original, is no longer a stalked
#     env-var and all the incremented spawns are removed from both the tqpt & svvs
#     set vfs path files contents. This feature is used for recursive analysis or
#     chained events hidden from a pivot conclusion or escape type params forming.
#
# --> lockdel(isRemoveAll, varName, fncName), removes lockvar entries from a tpqt
#     block of names that are associated to a env-var name. The @fncName parameter
#     can be str or a list for the entries to remove. The previous Staqtapp 1 ver.
#     had a log function name when a keyvar is called option. That is no longer in
#     use. If @isRemoveAll then the entire tpqt block is removed for @varName. If
#     you need a list return of what @fncName exist of a tpqt block, see getlocks.
#     Once again, there is no security measures added of this function. To have
#     full password & tor like vfs dir encryption security for this, you must have
#     the Staqtapp-Koch version. The full ver is not open freeware and is the most
#     secure env-var library on earth, that does not use any online third party to
#     to store any env-var data or passwords. If you are relying on a third party
#     cloud profit service, to keep your env-vars data safe or private? Their not.
#     Especially in the United States of America or the aka United Kingdom.
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

# email: rcttcr5@gmail.com
# contact: https://pastebin.com/eumqiBAx
# github: https://github.com/lastforkbender/staqtapp


from decimal import Decimal as dcml
from collections import deque, Counter

import statistics
import pickle
import random
import math
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
        rgr = self[ent]=type(self)()
        return rgr
        
    def __init__(self, dt = {}):
        for ix, dt in dt.items():
            if isinstance(dt, dict): self[ix]=type(self)(dt)
            else: self[ix]=dt
                
    def __eq__(self, other):
        return isinstance(self, AbsSmvt) and self.dt == other.dt
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
    def mcf_setpath(self, vfsFlNm: str, vfsDirNm: str, vfsFldrNm: str):
        # Sets a direct virtual path to a tqpt file/env-var @qp(): stack.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if vfsFlNm.find(':') < 0:
            if vfsDirNm != vfsFldrNm:
                if sfCls.sqtpp_chars_check(1, vfsDirNm):
                    if sfCls.sqtpp_chars_check(1, vfsFldrNm):
                        self._sRtrn = sfCls.sqtpp_change_vfs_path(vfsFlNm, vfsDirNm, vfsFldrNm)
                        if self._sRtrn == -1: self.mcf_err_handler(35, 'setpath')
                        elif self._sRtrn == -2: self.mcf_err_handler(36, 'setpath')
                        elif self._sRtrn == -3: self.mcf_err_handler(37, 'setpath')
                        elif self._sRtrn == -4: self.mcf_err_handler(38, 'setpath')
                        elif self._sRtrn == -5: self.mcf_err_handler(39, 'setpath')
                        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'setpath')
                    else: self.mcf_err_handler(1, 'setpath')
                else: self.mcf_err_handler(2, 'setpath')
            else: self.mcf_err_handler(3, 'setpath')
        else: self.mcf_err_handler(4, 'setpath')
#_______________________________________________________________________________________
    def mcf_addvar(self, varNm: str, varDat: str):
        # Adds variables to the set path vfs tqpt file. If finds the word 'lambda' in
        # varDat will bypass a normal addvar() in exchange for storing a runnable var.
        # In that special case, the parameter @varNm is ignored for writing to tqpt.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        sfCls._sf_rBoolE = False
        if varDat.find('lambda') > -1: sfCls._sf_rBoolE = True
        if os.path.isfile(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg'):
            if not sfCls._sf_rBoolE:
                if sfCls.sqtpp_chars_check(2, varNm):
                    self._sRtrn = sfCls.sqtpp_vars_add(False, varNm, varDat)
                    if self._sRtrn == -1: self.mcf_err_handler(6, 'addvar')
                    elif self._sRtrn == -2: self.mcf_err_handler(7, 'addvar')
                    elif self._sRtrn == -3: self.mcf_err_handler(9, 'addvar')
                    elif self._sRtrn == -4: self.mcf_err_handler(10, 'addvar')
                    elif self._sRtrn == -5: self.mcf_err_handler(11, 'addvar')
                    elif self._sRtrn == -6: self.mcf_err_handler(12, 'addvar')
                    elif self._sRtrn == -7: self.mcf_err_handler(40, 'addvar')
                    elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'addvar')
                else: self.mcf_err_handler(8, 'addvar')
            else: sfCls.sqtpp_vars_add(False, None, varDat)
        else: self.mcf_err_handler(5, 'addvar')
#_______________________________________________________________________________________
    def mcf_renamevar_stx(self, varNm: str, newVarNm):
        # Returns 1 if renamed var, 2 if renamed spawned vars with one left spawned
        # var or 3 if renamed spawned vars and more than one left from stalked var.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_vars_rename_stx(varNm, newVarNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'renamevar_stx')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'renamevar_stx')
            elif self._sRtrn == -3: self.mcf_err_handler(31, 'renamevar_stx')
            elif self._sRtrn == -4: self.mcf_err_handler(14, 'renamevar_stx')
            elif self._sRtrn == -5: self.mcf_err_handler(8, 'renamevar_stx')
            elif self._sRtrn == -6: self.mcf_err_handler(32, 'renamevar_stx')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'renamevar_stx')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'renamevar_stx')
#_______________________________________________________________________________________
    def mcf_removevar(self, varNm: str):
        # Deletes a env-var from vfs tqpt source and tpqt lockvar block if any.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_vars_remove(varNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'removevar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'removevar')
            elif self._sRtrn == -3: self.mcf_err_handler(33, 'removevar')
            elif self._sRtrn == -4: self.mcf_err_handler(34, 'removevar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'removevar')
        else: self.mcf_err_handler(8, 'removevar')
#_______________________________________________________________________________________
    def mcf_listvars(self) -> list:
        # Returns listed names of all env-vars in vfs tqpt source.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_vars_list()
        if self._sRtrn == -1: self.mcf_err_handler(6, 'listvars')
        elif self._sRtrn == -2: self.mcf_err_handler(7, 'listvars')
        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'listvars')
        else:
            return self._sRtrn
#_______________________________________________________________________________________
    def mcf_joinvars(self, newVarNm: str, varNms: list):
        # Joins a list of @varNms into a newly merged env-var in vfs tqpt source or
        # joins list of spawned env-vars data to @newVarNm if @newVarNm is stalked.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, newVarNm):
            self._sRtrn = sfCls.sqtpp_vars_join(newVarNm, varNms)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'joinvars')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'joinvars')
            elif self._sRtrn == -3: self.mcf_err_handler(30, 'joinvars')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'joinvars')
        else: self.mcf_err_handler(8, 'joinvars')
#_______________________________________________________________________________________
    def mcf_changevar(self, varNm: str, newVarDt: str):
        # See changevar at top of this module for description of this linked method.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_vars_change(varNm, newVarDt)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'changevar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'changevar')
            elif self._sRtrn == -3: self.mcf_err_handler(9, 'changevar')
            elif self._sRtrn == -4: self.mcf_err_handler(10, 'changevar')
            elif self._sRtrn == -5: self.mcf_err_handler(11, 'changevar')
            elif self._sRtrn == -6: self.mcf_err_handler(14, 'changevar')
            elif self._sRtrn == -7: self.mcf_err_handler(28, 'changevar')
            elif self._sRtrn == -8: self.mcf_err_handler(29, 'changevar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'changevar')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'changevar')
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
    def mcf_loadvar(self, isAllNmbrs: bool, varNm: str, mode: str):
        # Returns valid stored env-var data from @varNm; from set vfs tqpt path source.
        # ('mode=d' deque), ('mode=s' str)
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            mode = mode.replace(' ','')
            if mode=='mode=deque' or mode=='d': mode=1
            elif mode=='mode=str' or mode=='s': mode=2
            else: raise Exception('staqtapp1.2 (loadvar) error: param mode choice for type of variable return not found')
            self._sRtrn = sfCls.sqtpp_loadvar(isAllNmbrs, varNm, mode)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'loadvar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'loadvar')
            elif self._sRtrn == -3: self.mcf_err_handler(14, 'loadvar')
            elif self._sRtrn == -4: self.mcf_err_handler(9, 'loadvar')
            elif self._sRtrn == -5: self.mcf_err_handler(10, 'loadvar')
            elif self._sRtrn == -6: self.mcf_err_handler(11, 'loadvar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'loadvar')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'loadvar')
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
    def mcf_locklist(self, varNm: str):
        # Returns list type for listed fnc/etc. names in use from lockvar use @varNm.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_list_lock(varNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'locklist')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'locklist')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'locklist')
            else:
                return self._sRtrn
#_______________________________________________________________________________________
    def mcf_lockdel(self, isDelAll: bool, varNm: str, fncNm):
        # Removes tpqt lock entries @fncNm for a env-var @varNm tagged blocks.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_del_locks(isDelAll, varNm, fncNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'lockdel')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'lockdel')
            elif self._sRtrn == -3: self.mcf_err_handler(13, 'lockdel')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'lockdel')
        else: self.mcf_err_handler(8, 'lockdel')
#_______________________________________________________________________________________
    def mcf_keyvar(self, varNm: str, fncNm: str) -> bool:
        # Returns False if @fncNm is not a listed key name for any @varNm edits.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_var_key(varNm, fncNm)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'keyvar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'keyvar')
            elif self._sRtrn == -3: self.mcf_err_handler(13, 'keyvar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'keyvar')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'keyvar')
#_______________________________________________________________________________________
    def mcf_darkvar(self):
        # See darkvar() info at top of this module. Has no returns or any error returns.
        sfCls = SqtppFncs()
        sfCls.sqtpp_darkvar()
#_______________________________________________________________________________________
    def mcf_revar(self, isNewSetPth: bool, newVfsFlNm: str, newVfsDirNm: str, newVfsFldrNm: str):
        # Respawns a new .sqtpp vfs file via tpqt lockvar tagged env-vars only content.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if newVfsFlNm.find(':') < 0:
            if newVfsDirNm != newVfsFldrNm:
                if sfCls.sqtpp_chars_check(1, newVfsDirNm):
                    if sfCls.sqtpp_chars_check(1, newVfsFldrNm):
                        self._sRtrn = sfCls.sqtpp_revar(isNewSetPth, newVfsFlNm, newVfsDirNm, newVfsFldrNm)
                        if self._sRtrn == -1: self.mcf_err_handler(6, 'revar')
                        elif self._sRtrn == -2: self.mcf_err_handler(7, 'revar')
                        elif self._sRtrn == -3: self.mcf_err_handler(25, 'revar')
                        elif self._sRtrn == -4: self.mcf_err_handler(26, 'revar')
                        elif self._sRtrn == -5: self.mcf_err_handler(27, 'revar')
                        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'revar')
                    else: self.mcf_err_handler(1, 'revar')
                else: self.mcf_err_handler(2, 'revar')
            else: self.mcf_err_handler(3, 'revar')
        else: self.mcf_err_handler(4, 'revar')
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
    def mcf_vardata_stx(self, isRegex: bool, varNmLst: list, srch):
        # Search & find @varNmLst data from srch string option @srch. Returns name list.
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_locate_var_data(isRegex, varNmLst, srch)
        if self._sRtrn == -1: self.mcf_err_handler(6, 'vardata_stx')
        elif self._sRtrn == -2: self.mcf_err_handler(7, 'vardata_stx')
        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'vardata_stx')
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
    def mcf_lambdavar(self, lmbNm: str, lmbPrms: list):
        # Runs a stored & found env-var in tqpt vfs source as @lambda function return(s).
        # __slots__ in use: (_sRtrn)
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, lmbNm):
            self._sRtrn = sfCls.sqtpp_vars_run_lambda(lmbNm, lmbPrms)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'lambdavar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'lambdavar')
            elif self._sRtrn == -3: self.mcf_err_handler(41, 'lambdavar')
            elif self._sRtrn == -4: self.mcf_err_handler(42, 'lambdavar')
            elif self._sRtrn == -5: self.mcf_err_handler(43, 'lambdavar')
            elif self._sRtrn == -6: self.mcf_err_handler(44, 'lambdavar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'lambdavar')
            else:
                return self._sRtrn
        else:
            self.mcf_err_handler(8, 'lambdavar')
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
            # 25 = revar: new vfs file name same as current set vfs file name
            # 26 = no found tpqt lockvar entries
            # 27 = revar: no found tqpt env-vars matched to tpqt lockvar entries
            # 28 = svvs file has only one spawned var from stalkvar
            # 29 = cannot remove all spawned env-vars(changevar)
            # 30 = found '☆' char for join of var data
            # 31 = @varNm is a stalked var but @newVarNm is not a int type
            # 32 = no renamevar for stalked var having only one spawn
            # 33 = @varNm is a stalked env-var, cannot remove with removevar
            # 34 = @varNm is a dark env-var, cannot remove with removevar
            # 35 = @vfsFile .sqtpp vfs file was not found
            # 36 = @vfsDirName .sqtpp vfs file was not found
            # 37 = @vfsFolderName .sqtpp vfs file was not found
            # 38 = subfolder naming @vfsFolderName .sqtpp vfs file was not found
            # 39 = tqpt file naming @vfsFolderName .sqtpp vfs file was not found
            # 40 = unable to add runnable lambda env-var as a stalked env-var
            # 41 = @lambdaName was not found in tqpt env-var @q|p(...): sources
            # 42 = no proper constructed lambda function found to run
            # 43 = mismatch params length @lambdaParams for lambda function run
            # 44 = parameters names for found lambda function do not matchup
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
            elif altErrCd == 13: raise Exception(f'staqtapp1.2 ({clnFnc}) error: variable not found in tpqt var lock file')
            elif altErrCd == 14: raise Exception(f'staqtapp1.2 ({clnFnc}) error: variable was not found in tqpt var file')
            elif altErrCd == 15: raise Exception(f'staqtapp1.2 ({clnFnc}) error: svvs sub-file is not created, cannot begin stalkvar with identical values')
            elif altErrCd == 16: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found svvs commons stalk-entry element list for @varNm')
            elif altErrCd == 17: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varData matches env-var to begin stalk; nothing is impossible, not is possible')
            elif altErrCd == 18: raise Exception(f'staqtapp1.2 ({clnFnc}) error: invalid chars for @stalkVarName; allowed _a-zA-Z0-9')
            elif altErrCd == 19: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varNameList is empty')
            elif altErrCd == 20: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found svvs commons stalk-entry element list for @stalkVarName')
            elif altErrCd == 21: raise Exception(f'staqtapp1.2 ({clnFnc}) error: param @initialTreePathList is empty')
            elif altErrCd == 22: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars @initialTreePathList; non-allowed chars are \n,':{}☆")
            elif altErrCd == 23: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars for a smv branch tree id; invalid chars: \n,':{}☆")
            elif altErrCd == 24: raise Exception("staqtapp1.2 (" + clnFnc + ") error: invalid chars for a smv branch tree value; invalid chars: \n,':{}☆")
            elif altErrCd == 25: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @newVfsFileName cannot be the same as the current set vfs file name')
            elif altErrCd == 26: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found tpqt lockvar entries...')
            elif altErrCd == 27: raise Exception(f'staqtapp1.2 ({clnFnc}) error: no found tqpt env-vars matched to tpqt lockvar entries')
            elif altErrCd == 28: raise Exception(f'staqtapp1.2 ({clnFnc}) error: svvs has one spawned env-var, only stalkvar can remove a stalked variable and a svvs listing')
            elif altErrCd == 29: raise Exception(f'staqtapp1.2 ({clnFnc}) error: cannot remove all spawned vars, only stalkvar can remove all spawned env-vars')
            elif altErrCd == 30: raise Exception(f'staqtapp1.2 ({clnFnc}) error: cannot join a smv-tree type data with other env-var data')
            elif altErrCd == 31: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @newVarName not a int type, @varName was found as a svvs listed stalked env-var')
            elif altErrCd == 32: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varName is a stalked var having only one spawned env-var, no increment order can be applied')
            elif altErrCd == 33: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varName is a stalked listed env-var, removal by vfs sub-file dependency functions only')
            elif altErrCd == 34: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @varName is a dark listed env-var, removal by vfs sub-file dependency functions only')
            elif altErrCd == 35: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @vfsFileName was not a found .sqtpp file in .../staqtapp1_2/ working module folder')
            elif altErrCd == 36: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @vfsDirName was not found in .sqtpp vfs file')
            elif altErrCd == 37: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @vfsFolderName was not found in .sqtpp vfs file')
            elif altErrCd == 38: raise Exception(f'staqtapp1.2 ({clnFnc}) error: subfolder naming for @vfsFolderName was not found in .sqtpp vfs file')
            elif altErrCd == 39: raise Exception(f'staqtapp1.2 ({clnFnc}) error: tqpt subfolder naming for @vfsFolderName was not found in .sqtpp vfs file')
            elif altErrCd == 40: raise Exception(f'staqtapp1.2 ({clnFnc}) error: cannot store a env-var lambda runnable as a stalked env-var')
            elif altErrCd == 41: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @lambdaName was not found in vfs tqpt source @q|p(...): tagged type env-vars')
            elif altErrCd == 42: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @lambdaName was found but not a properly constructed lambda function for run')
            elif altErrCd == 43: raise Exception(f'staqtapp1.2 ({clnFnc}) error: mismatch params lengths @lambdaParams, number of args does not match the found lambda')
            elif altErrCd == 44: raise Exception(f'staqtapp1.2 ({clnFnc}) error: param name(s) for found lambda function do not matchup, unable to run lambda')
        else:
            if self._sRtrn == 'FNC-ERR': raise Exception(f'staqtapp1.2 {clnFnc}-->{self._sErr}')
            elif self._sRtrn == 'FOO-BAR': raise Exception('staqtapp1.2 io error: unable to perform basic file reads or writes')
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_________________________MAIN PARSING FUNCTIONS:
#_______________________________________________________________________________________
class SqtppFncs(Sqtpp):
    __slots__ = ('_sf_sVfs', '_sf_sVfsFldr', '_sf_sSrc', '_sf_sRplc', '_sf_sQp', '_sf_sQpRplcX', '_sf_sPq', '_sf_sDv', '_sf_sVd', '_sf_sVn', '_sf_sRtrn', '_sf_sKntId', '_sf_sLstX', '_sf_sStrX', '_sf_sIntX', '_sf_sBoolX', '_sf_sBoolCxv', '_sf_sLstA', '_sf_rStrA', '_sf_rStrB', '_sf_rStrC', '_sf_rStrD', '_sf_rStrE', '_sf_rStrF', '_sf_rLstA', '_sf_rLstB', '_sf_rLstC', '_sf_rLstD', '_sf_rLstE', '_sf_rLstF', '_sf_rIntA', '_sf_rIntB', '_sf_rIntC', '_sf_rIntD', '_sf_rIntE', '_sf_rIntF', '_sf_rIntG', '_sf_rIntH', '_sf_rIntI', '_sf_rBoolA', '_sf_rBoolB', '_sf_rBoolC', '_sf_rBoolD', '_sf_rBoolE')
    
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
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{vfsNm}.sqtpp', f':☆Staqtapp-v1.2.194\n|:{dirNm}<{fldrNm}>\n_|:{fldrNm}<sub-{fldrNm}>\n__|:sub-{fldrNm}<tqpt-{fldrNm},tpqt-{fldrNm},null>\n___|:tqpt-{fldrNm}<tqpt,null,n>:\nnull:\n___|:(tqpt-{fldrNm})\n___|:tpqt-{fldrNm}<tpqt,null,n>:\nnull:\n___|:(tpqt-{fldrNm})\n__|:(sub-{fldrNm})\n_|:({fldrNm})\n|:({dirNm})')
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
        # Sets _sf_sPq to the set vfs path tpqt lockvar sub-file type contents.
        # __slots__ in use: (_sf_sPq)
        # returns: -1=path not found
        if isTpqt:
            self._sf_rLstA[4] = self._sf_rLstA[4].replace('tqpt','tpqt')
            self.sqtpp_vfs_pointer([f'|:{self._sf_rLstA[1]}<', f'_|:{self._sf_rLstA[2]}<', f'__|:{self._sf_rLstA[3]}<', f'___|:{self._sf_rLstA[4]}<'])
            if self._sf_rIntA != -1: self._sf_sPq = self._sf_sSrc[self._sf_rIntA:self._sf_sSrc.find('___|:',self._sf_rIntA+5)-2]
            else:
                return -1
        else:
            pass
#_______________________________________________________________________________________
    def sqtpp_vfs_folder_write_dvcpn(self, dvAddrPntr: str):
        # Writes DVCPN file containing listed darkvar addrs or/and dimensional pntr cXV.
        # (Only rev9 integrated classes/functions removes contents of a DVCPN vfs-file.)
        # __slots__ in use: (_sf_rIntA, _sf_rIntB)
        # returns: none
        self._sf_rIntA = self._sf_sSrc.find(f'_|:{self._sf_sVfsFldr}<sub-{self._sf_sVfsFldr}>')
        self._sf_rIntB = self._sf_sSrc.find(f'__|:sub-{self._sf_sVfsFldr}<')
        if self._sf_rIntA > -1 and self._sf_rIntB > -1:
            dvcStr = self._sf_sSrc[self._sf_rIntA:self._sf_rIntB-1]
            dvcLst = re.findall(r'<:DVCPN=(?s:.*?).*\/\/:>', dvcStr)
            if len(dvcLst) > 0:
                dvcStr = dvcLst[0]
                dvcLst = dvcLst[0].split('\n')
                dvcLst.pop(0)
                dvcLst.pop(0)
                dvcLst[len(dvcLst)-1] = dvcLst[len(dvcLst)-1].replace('//:>','')
                dvcLst.append(dvAddrPntr)
                self.sqtpp_vssv_menorah_cxv_rod(dvAddrPntr, dvcLst[len(dvcLst)-2])
                self.sqtpp_reset_slots(False)
                self._sf_sSrc = self._sf_sSrc.replace(dvcStr, '<:DVCPN=\n' + self._sf_sRplc + '\n' + '\n'.join(dvcLst) + '//:>')
            else: self._sf_sSrc = self._sf_sSrc.replace(dvcStr, f'{dvcStr}\n<:DVCPN=\nnull\n{dvAddrPntr}//:>')
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
    def sqtpp_change_vfs_path(self, flNm: str, dirNm: str, fldrNm: str):
        # Sets the vfs file dir + folder + subfolder + tqpt working path @.stg file.
        # __slots__ in use: (_sf_sSrc, _sf_rLstA, _sf_rStrA, _sf_rIntA, _sf_rIntB, _sf_rBoolA)
        # returns: none
        try:
            self._sf_rLstA = glob.glob(f'{SQTPP_MDL_DIR}/staqtapp1_2/*.sqtpp')
            self._sf_rIntB = len(self._sf_rLstA)
            self._sf_rBoolA = False
            for self._sf_rIntA in range(self._sf_rIntB):
                if self._sf_rLstA[self._sf_rIntA].find(f'{flNm}.sqtpp') > -1: self._sf_rBoolA = True
            if self._sf_rBoolA:
                with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/{flNm}.sqtpp', mode='r') as sqtppFl: self._sf_rStrA = sqtppFl.read()
                if self._sf_rStrA.find(f'\n:|{dirNm}<{fldrNm}>\n') > -1:
                    if self._sf_rStrA.find(f'\n:_|{fldrNm}<sub-{fldrNm}>\n') > -1:
                        if self._sf_rStrA.find(f'\n:__|sub-{fldrNm}<') > -1:
                            if self._sf_rStrA.find(f'\n:___|tqpt-{fldrNm}<') > -1:
                                self._sf_rStrA = None
                                with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', mode='w') as sqtppStgFl: sqtppStgFl.write(f'{flNm}:{dirNm}:{fldrNm}:sub-{fldrNm}:tqpt-{fldrNm}')
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
        except Exception as err_change_vfs_path:
            self._sErr = f'staqtapp1.2 (change_vfs_path) error: {err_change_vfs_path}'
            return self.sqtpp_err_rcrd(self._sErr)
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
        # -7=cannot store env-var lambda runnable as a stalked env-var
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
                        if not isStlkVar and not self._sf_rBoolE:
                            if self._sf_sQp.find(f'\n{varNm}<@qp(') < 0:
                                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}<{varDat}>:\n'))
                                self._sf_sSrc = None
                                self._sf_sQp = None
                                return 8
                            else:
                                return -6
                        else:
                            if not self._sf_rBoolE:
                                return self.sqtpp_var_stalk(varNm, varDat)
                            else:
                                return -7
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_add:
            if not isStlkVar: self._sErr = f'staqtapp1.2 (vars_add) error: {err_vars_add}'
            else: self._sErr = f'staqtapp1.2 (vars_add) error: {err_vars_add}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_list(self) -> list:
        # Returns vfs stack list names of env-vars currently in the tqpt file.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rIntA, _sf_rIntB)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rLstA = self._sf_sQp.split('\n')
                    self._sf_rLstA.pop(0)
                    self._sf_rLstA.pop(0)
                    self._sf_rIntB = len(self._sf_rLstA)
                    self._sf_rLstC = []
                    for self._sf_rIntA in range(self._sf_rIntB):
                        self._sf_rLstB = self._sf_rLstA[self._sf_rIntA].split('<')
                        self._sf_rLstC.append(self._sf_rLstB[0])
                    self._sf_sSrc = None
                    self._sf_sQp = None
                    return self._sf_rLstC
                return -2
            else:
                return -1
        except Exception as err_vars_list:
            self._sErr = f'staqtapp1.2 (listvars) error: {err_vars_list}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_join(self, newVarNm: str, varNms: list):
        # Joins multiple env-var data as a new env-var added to tqpt stack from @varNms.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_rStrA, _sf_rStrB, _sf_rLstA, _sf_rLstB, _sf_rIntA, _sf_rIntB, _sf_rBoolA)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=found '☆' char in var data
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    spok = bytes('☆','utf-8')
                    self._sf_rBoolA = False
                    if self._sf_sSrc.find(f'<sbf-{self._sf_sVfsFldr}-svvs:') > -1:
                        if self.sqtpp_svvs_list(newVarNm) == 8: self._sf_rBoolA = True
                    self._sf_rLstB = []
                    if not self._sf_rBoolA:
                        self._sf_rIntB = len(varNms)
                        for self._sf_rIntA in range(self._sf_rIntB):
                            if self.sqtpp_var_value(varNms[self._sf_rIntA]):
                                self._sf_rStrB = bytes(self._sf_sVd,'utf-8')
                                if self._sf_rStrB.find(spok) > -1:
                                    return -3
                                else: self._sf_rLstB.append(self._sf_sVd)
                    else:
                        self._sf_rIntB = len(self._sf_rLstA)
                        for self._sf_rIntA in range(self._sf_rIntB):
                            if self.sqtpp_var_value(self._sf_rLstA[self._sf_rIntA]):
                                self._sf_rStrB = bytes(self._sf_sVd,'utf-8')
                                if self._sf_rStrB.find(spok) > -1:
                                    return -3
                                else: self._sf_rLstB.append(self._sf_sVd)
                    if len(self._sf_rLstB) > 0:
                        if self._sf_rBoolA:
                            self._sf_rLstA = re.findall(r'(?s:)\~__'+re.escape(newVarNm)+r'__\~<@qp\(.*?\):>', self._sf_sQp)
                            if len(self._sf_rLstA) > 0:
                                self._sf_rStrA = self._sf_sQp
                                self._sf_sQp = self._sf_sQp.replace(self._sf_rLstA[0], f'~__{newVarNm}__~<{"".join(self._sf_rLstB)}>')
                                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_rStrA}:\n', f'{self._sf_sQp}:\n'))
                            else: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n~__{newVarNm}__~<{"".join(self._sf_rLstB)}>:\n'))
                        else: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{newVarNm}<{"".join(self._sf_rLstB)}>:\n'))
                        self._sf_sSrc = None
                        self._sf_sQp = None
                        self._sf_rStrA = None
                        return 8
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_join:
            self._sErr = f'staqtapp1.2 (joinvars) error: {err_vars_join}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_rename_stx(self, varNm: str, newVarNm):
        # This module heavy env-var quality slots, see renamevar_stx info. Do not edit!
        # Renames stalked env-vars just like the Staqtapp-Koch version but has no tor
        # like vfs dir renaming, with different random encryption sets being applied.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rIntA, _sf_rIntB, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rBoolA, _sf_rBoolB)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@newVarNm must be int if @varNm is a stalked env-var
        # -4=@varNm not found in tqpt source, normal renaming
        # -5=@newVarNm is of invalid chars, normal renaming
        # -6=@varNm is a stalked var having only one spawned var
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self.sqtpp_vfs_tpqt_file(True) != -1:
                        self._sf_rBoolA = False
                        if self.sqtpp_svvs_list(varNm) == 8:
                            if isinstance(newVarNm, int): self._sf_rBoolA = True
                            else:
                                return -3
                        if not self._sf_rBoolA:
                            if self.sqtpp_var_value(varNm):
                                if self.sqtpp_chars_check(2, newVarNm):
                                    self._sf_rStrA = self._sf_sQp
                                    self._sf_sQp = self._sf_sQp.replace(f'{varNm}<{self._sf_sVd}>', f'{newVarNm}<{self._sf_sVd}>')
                                    self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_rStrA}:\n', f'{self._sf_sQp}:\n')
                                    self._sf_sQp = None
                                    self._sf_rBoolB = False
                                    if self._sf_sPq.find(f'<:{varNm}=') > -1:
                                        self._sf_rBoolB = True
                                        self._sf_rStrA = self._sf_sPq
                                        self._sf_sPq = self._sf_sPq.replace(f'<:{varNm}=',f'<:{newVarNm}=')
                                    if self._sf_rBoolB: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(self._sf_rStrA, self._sf_sPq))
                                    else: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                                    self._sf_sPq = None
                                    self._sf_sSrc = None
                                    self._sf_rStrA = None
                                    return 1
                                else:
                                    return -5
                            else:
                                return -4
                        else:
                            if len(self._sf_rLstA) > 1:
                                self._sf_rLstC = []
                                self._sf_rIntB = len(self._sf_rLstA)
                                for self._sf_rIntA in range(self._sf_rIntB):
                                    self._sf_rLstB = self._sf_rLstA[self._sf_rIntA].split('_')
                                    self._sf_rLstC.append(int(self._sf_rLstB[len(self._sf_rLstB)-1]))
                                self._sf_rLstA = []
                                while self._sf_rLstC:
                                    if not self._sf_rLstC:
                                        break
                                    else:
                                        self._sf_rIntA = min(range(len(self._sf_rLstC)), key=lambda _: abs(self._sf_rLstC[_]-newVarNm))
                                        self._sf_rLstA.append(self._sf_rLstC[self._sf_rIntA])
                                        self._sf_rLstC.pop(self._sf_rIntA)
                                if newVarNm > 0:
                                    # True mastership of this return3 by the programmer, not ai...that is impossible,
                                    # can make this env-var lib escape any env-var reality they would push corpo-off.
                                    self._sf_rStrA = self.sqtpp_vfs_sub_file(False, False, 'svvs', None)
                                    self._sf_rStrD = self._sf_rStrA
                                    self._sf_rStrB = self._sf_sQp
                                    self._sf_rLstB = self._sf_sPq
                                    for self._sf_rIntA in range(self._sf_rIntB):
                                        self._sf_rStrC = f'{varNm}_{self._sf_rLstA[self._sf_rIntA]}<@qp('
                                        if self._sf_sQp.find(self._sf_rStrC) > -1: self._sf_sQp = self._sf_sQp.replace(self._sf_rStrC, f'{varNm}_{newVarNm}<@qp(')
                                        self._sf_rStrC = f'{varNm}_{self._sf_rLstA[self._sf_rIntA]}'
                                        if self._sf_rStrA.find(self._sf_rStrC) > -1: self._sf_rStrA = self._sf_rStrA.replace(self._sf_rStrC, f'{varNm}_{newVarNm}')
                                        self._sf_rStrC = f'<:{varNm}_{self._sf_rLstA[self._sf_rIntA]}='
                                        if self._sf_sPq.find(self._sf_rStrC) > -1: self._sf_sPq = self._sf_sPq.replace(self._sf_rStrC, f'<:{varNm}_{newVarNm}=')
                                        newVarNm+=1
                                    self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrB, self._sf_sQp)
                                    self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrD, self._sf_rStrA)
                                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(self._sf_rLstB, self._sf_sPq))
                                    self._sf_sSrc = None
                                    self._sf_rStrB = None
                                    self._sf_sQp = None
                                    self._sf_rLstB = None
                                    self._sf_sPq = None
                                    return 3
                                else:
                                    self._sf_rLstC = []
                                    self._sf_rBoolA = False
                                    self._sf_rBoolB = False
                                    for self._sf_rIntA in range(self._sf_rIntB):
                                        if newVarNm < 1:
                                            self._sf_rStrA = f'{varNm}_{self._sf_rLstA[self._sf_rIntA]}'
                                            self._sf_rLstB = re.findall(r'(?s:)'+re.escape(self._sf_rStrA)+r'<@qp\(.*?\):>', self._sf_sQp)
                                            if len(self._sf_rLstB) > 0:
                                                self._sf_rLstC.append(self._sf_rStrA)
                                                if not self._sf_rBoolA:
                                                    self._sf_rBoolA = True
                                                    self._sf_rStrB = self._sf_sQp
                                                self._sf_sQp = self._sf_sQp.replace(f'\n{self._sf_rLstB[0]}','')
                                            if self._sf_rIntA+1 == self._sf_rIntB-1:
                                                self._sf_rBoolB = True
                                                break
                                            else: newVarNm+=1
                                        else:
                                            break
                                    if len(self._sf_rLstC) > 0:
                                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrB, self._sf_sQp)
                                        self.sqtpp_silent_lock_remove(self._sf_rLstC)
                                    self._sf_rStrA = self.sqtpp_vfs_sub_file(False, False, 'svvs', None)
                                    self._sf_rStrB = self._sf_rStrA
                                    self._sf_rIntB = len(self._sf_rLstC)
                                    for self._sf_rIntA in range(self._sf_rIntB):
                                        if self._sf_rStrA.find(f'={self._sf_rLstC[self._sf_rIntA]},') > -1: self._sf_rStrA = self._sf_rStrA.replace(f'{self._sf_rLstC[self._sf_rIntA]},','')
                                        else: self._sf_rStrA = self._sf_rStrA.replace(f',{self._sf_rLstC[self._sf_rIntA]}','')
                                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(self._sf_rStrB, self._sf_rStrA))
                                    self._sf_sSrc = None
                                    self._sf_sQp = None
                                    self._sf_sPq = None
                                    if self._sf_rBoolB:
                                        return 2
                                    else:
                                        return 3
                            else:
                                return -6
                    else:
                        return -2
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_rename_stx:
            self._sErr = f'staqtapp1.2 (renamevar_stx) error: {err_vars_rename_stx}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_change(self, varNm: str, newVarDt: str):
        # This module heavy quality slots, see changevar at top for method description.
        # Edit of this function is problematic and may cause rev9 to fight against you
        # having any further use of this module as an advanced purpose env-var usage.
        # **All rev9 features/methods are of UXRG obfuscation and hardened trained on
        # the fovea-mantis script engine to recognize standard methods have changed.**
        # __slots__ in use: (||_*)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=newline chars found
        # -4=no @qp(...): data declaring found
        # -5=no closing ): for @qp( data tag found
        # -6=@varNm not found in tqpt source
        # -7=only one spawned env-var from stalkvar
        # -8=changevar cannot remove all spawned vars
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rIntA = self.sqtpp_tqpt_spdr(True, False, None, newVarDt)
                    if self._sf_rIntA == 2:
                        return -3
                    elif self._sf_rIntA == 6:
                        return -4
                    elif self._sf_rIntA == 7:
                        return -5
                    self._sf_rBoolA = False
                    if self._sf_sSrc.find(f'<sbf-{self._sf_sVfsFldr}-svvs:') > -1:
                        if self.sqtpp_svvs_list(varNm) == 8: self._sf_rBoolA = True
                    if not self._sf_rBoolA:
                        if self.sqtpp_var_value(varNm):
                            self._sf_rStrA = self._sf_sQp
                            self._sf_sQp = self._sf_sQp.replace(f'{varNm}<{self._sf_sVd}>', f'{varNm}<{newVarDt}>')
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_rStrA}:\n', f'{self._sf_sQp}:\n'))
                            self._sf_sSrc = None
                            self._sf_sQp = None
                            self._sf_rStrA = None
                            return 8
                        else:
                            return -6
                    else:
                        self._sf_rIntD = len(self._sf_rLstA)
                        if self._sf_rIntD > 1:
                            self._sf_rBoolB = False
                            self._sf_rBoolC = False
                            self._sf_rLstB = []
                            self._sf_rIntE = 0
                            for self._sf_rIntC in range(self._sf_rIntD):
                                if self.sqtpp_var_value(self._sf_rLstA[self._sf_rIntC]):
                                    if newVarDt == self._sf_sVd:
                                        if not self._sf_rBoolB:
                                            self._sf_rBoolB = True
                                            self._sf_rStrB = self.sqtpp_vfs_sub_file(False, False, 'svvs', None)
                                            self._sf_rStrC = self._sf_rStrB
                                        self._sf_rIntE+=1
                                        if self._sf_rIntE != self._sf_rIntD:
                                            self._sf_rLstB.append(self._sf_rLstA[self._sf_rIntC])
                                            if not self._sf_rBoolC:
                                                self._sf_rBoolC = True
                                                self._sf_rStrD = self._sf_sQp
                                            self._sf_sQp = self._sf_sQp.replace(f'\n{self._sf_rLstA[self._sf_rIntC]}<{self._sf_sVd}>','')
                                            if self._sf_rStrB.find(f'={self._sf_rLstA[self._sf_rIntC]},') > -1: self._sf_rStrB = self._sf_rStrB.replace(f'{self._sf_rLstA[self._sf_rIntC]},','')
                                            else: self._sf_rStrB = self._sf_rStrB.replace(f',{self._sf_rLstA[self._sf_rIntC]}','')
                                        else:
                                            return -8
                            if self._sf_rIntE > 0:
                                self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrC, self._sf_rStrB)
                                self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_rStrD}:\n', f'{self._sf_sQp}:\n')
                                self._sf_sRtrn = self._sf_rLstB
                                self._sf_sQp = None
                                self.sqtpp_reset_slots(False)
                                with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg','r') as stgFl: self._sf_rLstA = stgFl.read().split(':')
                                self.sqtpp_vfs_tpqt_file(True)
                                if len(self._sf_sPq) > 0 and self._sf_sPq != 'null':
                                    self._sf_rBoolA = False
                                    self._sf_rStrA = None
                                    self._sf_rIntB = len(self._sf_sRtrn)
                                    for self._sf_rIntA in range(self._sf_rIntB):
                                        self._sf_rLstB = re.findall(r'<:'+re.escape(self._sf_sRtrn[self._sf_rIntA])+r'=(?s:.*?).*:>', self._sf_sPq)
                                        if len(self._sf_rLstB) > 0:
                                            if not self._sf_rBoolA:
                                                self._sf_rBoolA = True
                                                self._sf_rStrA = self._sf_sPq
                                            self._sf_sPq = self._sf_sPq.replace(self._sf_rLstB[0],'')
                                            self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                                    if self._sf_rStrA != None:
                                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sPq)
                                        self._sf_rStrA = None
                                self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                                self._sf_sSrc = None
                                self._sf_sPq = None
                                return self._sf_sRtrn
                            else:
                                return None
                        else:
                            return -7
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_change:
            self._sErr = f'staqtapp1.2 (changevar) error: {err_vars_change}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_remove(self, varNm: str):
        # Will delete @varNm from tqpt stack and then delete a @varNm tpqt block if find.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_sPq, _sf_rLstA, _sf_rLstB, _sf_rStrA)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@varNm is a stalked env-var, wrong function to remove
        # -4=@varNm is a dark env-var, wrong function to remove
        if self.sqtpp_set_vfs_file() == 1:
            if self._sf_sSrc.find(f'<sbf-{self._sf_sVfsFldr}-svvs:') > -1:
                self._sf_rLstB = self._sf_rLstA
                if self.sqtpp_svvs_list(varNm) == 8:
                    return -3
                self._sf_rLstA = self._sf_rLstB
            if self.sqtpp_vfs_tqpt_file(True) != -1:
                if self._sf_sQp.find(f'____d__v____{varNm}<@qp:...:vd(') > -1:
                    return -4
                else:
                    self._sf_rLstB = re.findall(r'(?s:)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
                    if len(self._sf_rLstB) > 0:
                        self._sf_rStrA = self._sf_sQp
                        self._sf_sQp = self._sf_sQp.replace(f'\n{self._sf_rLstB[0]}','')
                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sQp)
                        self._sf_sQp = None
                        if self.sqtpp_vfs_tpqt_file(True) != -1:
                            self._sf_rLstB = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                            if len(self._sf_rLstB) > 0:
                                self._sf_rStrA = self._sf_sPq
                                self._sf_sPq = self._sf_sPq.replace(f'{self._sf_rLstB[0]}','')
                                self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                                self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sPq)
                                self._sf_sPq = None
                        else:
                            return -2
                    if self._sf_sQp == None: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                    self._sf_sSrc = None
                    self._sf_rStrA = None
            else:
                return -2
        else:
            return -1
#_______________________________________________________________________________________
    def sqtpp_darkvar(self):
        # See darkvar info for explain. Very complex env-var vfs functionals connected, do not edit.
        # __slots__ in use: (_sf_sLstX, _sf_sStrX, _sf_sIntX, _sf_sBoolX, _sf_rLstA, _sf_rStrA, _sf_IntA, _sf_IntB)
        # returns: (none)
        self._sf_sBoolCxv = False
        if self._sf_sBoolX:
            mAddr = None
            try:
                mAddr = f'{random.randint(1111111111,9999999999)}{random.randint(1111111111,9999999999)}{random.randint(1111111111,9999999999)}{random.randint(1,9)}'
                self.sqtpp_plndrm(2)
                self.sqtpp_darkvar_menorah_outer_loop_resum(self._sf_sDv, mAddr)
                self.sqtpp_reset_slots(False)
            except Exception as e:
                raise Exception(f'staqtapp1.2 (darkvar) error: inauthentic staqtapp1.2 menorah mirror-address algorithm')
            self._sf_rStrA = f'____d__v____{self._sf_sVn}<@qp:...:vd(@qp(st1.2={self._sf_sDv},zny=tetbase34,lpm=13:12,drome-r=y,drome-s=n,drome-v=n,rev9-btb=n,rev9-blb=n):@qp(addr='
            if self._sf_sQp.find(self._sf_rStrA) < 0:
                self._sf_rLstA = set()
                self._sf_rIntB = len(self._sf_sLstX)
                for self._sf_rIntA in range(self._sf_rIntB):
                    if self.sqtpp_var_value(self._sf_sLstX[self._sf_rIntA]):
                        self._sf_sVd = self._sf_sVd.replace('@qp(','').replace('):','').replace(' ','')
                        self._sf_rLstA.add(self._sf_sVd)
                if len(self._sf_rLstA) > 0:
                    self._sf_rStrA = f'{self._sf_rStrA}{self._sf_sStrX}-{mAddr},atdl=31,m-lrs=y,m-rlv=y,rev9-sldq=n):@qp({str(self._sf_rLstA)}):>'
                    self._sf_sQpRplcX = self._sf_sQp
                    self._sf_sQp = f'{self._sf_sQp}\n{self._sf_rStrA}'
                    self.sqtpp_vfs_folder_write_dvcpn(f'{mAddr},{self._sf_sDv}')
                else:
                    self._sf_rStrA = None
                    self._sf_sSrc = None
                    self._sf_sQp = None
                    self._sf_sPq = None
            else:
                pass 
        else:
            # Is read & parse dark env-var with vssv sub-file. Even or Odd.
            pass
#_______________________________________________________________________________________
    def sqtpp_darkvar_menorah_outer_loop_resum(self, tetBase: int, vssvAddr: str) -> str:
        # Outer-halfloop encoded 7-digit palindrome int for a vssv-addr pointer list.
        # __slots__ in use: (_sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rBoolA)
        # returns: (int)
        self._sf_rBoolA = False
        self._sf_rStrA = str(tetBase)[0:3]
        self._sf_rIntA = int(self._sf_rStrA)
        self._sf_rStrB = str(tetBase)[2:5]
        self._sf_rIntB = int(self._sf_rStrB)
        if self._sf_rIntA == self._sf_rIntB: self._sf_rIntC = 3
        elif self._sf_rIntA > self._sf_rIntB:
            self._sf_rIntD = math.floor(math.tan(self._sf_rIntA-self._sf_rIntB))
            if self._sf_rIntD+self._sf_rIntB >= self._sf_rIntA-self._sf_rIntD: self._sf_rIntC = 4
            else: self._sf_rIntC = 3
        elif self._sf_rIntA < self._sf_rIntB:
            self._sf_rIntD = math.floor(math.tan(self._sf_rIntB+self._sf_rIntA))
            if self._sf_rIntD-self._sf_rIntA <= self._sf_rIntB+self._sf_rIntD: self._sf_rIntC = 4
            else: self._sf_rIntC = 3
        self._sf_rIntD = len(vssvAddr)-1
        self._sf_rIntE = 0
        self._sf_rIntH = 0
        self._sf_rLstA = []
        self._sf_rLstB = []
        self._sf_rLstC = []
        while self._sf_rIntE < self._sf_rIntD:
            self._sf_rIntH+=1
            if len(self._sf_rLstA) == self._sf_rIntC:
                if self._sf_rLstA[0] == '0': self._sf_rLstA[0] = '1'
                if self._sf_rLstB[0] == '0': self._sf_rLstB[0] = '1'
                self._sf_rIntF = int(''.join(self._sf_rLstA))
                self._sf_rIntG = int(''.join(self._sf_rLstB))
                if self._sf_rIntF == self._sf_rIntG: self._sf_rLstC.append(str(self._sf_rIntC+2))
                elif self._sf_rIntF > self._sf_rIntG:
                    if (self._sf_rIntF-self._sf_rIntG)*2 < self._sf_rIntC+self._sf_rIntG: self._sf_rLstC.append(str(self._sf_rIntC+1))
                    else: self._sf_rLstC.append(str(self._sf_rIntC-1))
                elif self._sf_rIntF < self._sf_rIntG:
                    if (self._sf_rIntG-self._sf_rIntF)*2 > self._sf_rIntC+self._sf_rIntG: self._sf_rLstC.append(str(self._sf_rIntC-1))
                    else: self._sf_rLstC.append(str(self._sf_rIntC+1))
                self._sf_rLstA = [f'{vssvAddr[self._sf_rIntD]}']
                self._sf_rLstB = [f'{vssvAddr[self._sf_rIntE]}']
            else:
                self._sf_rLstA.append(f'{vssvAddr[self._sf_rIntD]}')
                self._sf_rLstB.append(f'{vssvAddr[self._sf_rIntE]}')  
            self._sf_rIntD-=1
            self._sf_rIntE+=1
        if self._sf_rLstB[0] == '0': self._sf_rLstB[0] = '1'
        if self._sf_rIntH+self._sf_rIntH < len(vssvAddr): self._sf_rStrC = f'{"".join(self._sf_rLstB)}{vssvAddr[self._sf_rIntE]}{"".join(self._sf_rLstA)[::-1]}'
        else: self._sf_rStrC = f'{"".join(self._sf_rLstB)}{"".join(self._sf_rLstA)[::-1]}'
        tetBase = str(tetBase)
        self._sf_rLstC = ''.join(self._sf_rLstC)
        if self._sf_rLstC == '4224': self._sf_sStrX = 'E'
        elif self._sf_rLstC == '535': self._sf_sStrX = 'O'
        else:
            self._sf_rBoolA = True
            self._sf_sStrX = 'N'
            self._sf_sDv = f'1{str(tetBase)}1'
        if not self._sf_rBoolA:
            self._sf_rIntH = 0
            for self._sf_rStrD in tetBase:
                self._sf_rIntI = 0
                for self._sf_rStrE in self._sf_rStrC:
                    self._sf_rIntI+=1
                    self._sf_rIntF = int(self._sf_rStrD)
                    self._sf_rIntG = int(self._sf_rStrE)
                    if self._sf_sStrX == 'O':
                        if self._sf_rIntI < 4:
                            if (self._sf_rIntF+self._sf_rIntG)/3 > 0: self._sf_rIntH+=1
                        else:
                            if self._sf_rIntF > 4:
                                if self._sf_rIntG+2 < self._sf_rIntF: self._sf_rIntH-=1
                                else:
                                    if self._sf_rIntG+3 <= self._sf_rIntF: self._sf_rIntH+=1
                    else:
                        if self._sf_rIntI > 3:
                            if (self._sf_rIntF+self._sf_rIntG)/3 <= 2: self._sf_rIntH-=1
                            else: self._sf_rIntH+=1
                        else:
                            if self._sf_rIntF-self._sf_rIntG > 0: self._sf_rIntH+=1   
                            else:
                                if self._sf_rIntG > self._sf_rIntF+1: self._sf_rIntH-=1
                                else:
                                    if (self._sf_rIntG+4)/2 > 3: self._sf_rIntH-=1
                                    else: self._sf_rIntH+=1
            self._sf_rIntH = str(self._sf_rIntH).replace('0','1')
            if self._sf_rIntH == self._sf_rIntH[::-1]: self._sf_sDv = f'{self._sf_rIntH[0]}{str(tetBase)}{self._sf_rIntH[0]}'
            else:
                if len(self._sf_rIntH) > 1 and int(self._sf_rIntH) < 36: self._sf_sDv = f'{self._sf_rIntH[1]}{str(tetBase)}{self._sf_rIntH[1]}'
                else: self._sf_sDv = f'{self._sf_rIntH[0]}{str(tetBase)}{self._sf_rIntH[0]}'
#_______________________________________________________________________________________
    def sqtpp_revar(self, isCurrVfsPth: bool, newVfsFlNm: str, newVfsDirNm: str, newVfsFldrNm: str):
        # Replicates a new .sqtpp vfs file from current set vfs file, having env-vars
        # from the current set vfs that are only associated with a tpqt lockvar entry.
        # __slots__ in use: (_sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_StrA, _sf_rIntA, _sf_rIntB)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@newVfsFlNm same as the current set vfs file name
        # -4=no found lockvar env-var entries
        # -5=no found tqpt env-var entries for a new revar vfs
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if self.sqtpp_vfs_tpqt_file(True) != -1:
                        if newVfsFlNm != self._sf_sVfs:
                            self._sf_rLstA = re.findall(r'<\:.*?=', self._sf_sPq)
                            if len(self._sf_rLstA) > 0:
                                self._sf_rIntB = len(self._sf_rLstA)
                                self._sf_rLstC = []
                                for self._sf_rIntA in range(self._sf_rIntB):
                                    self._sf_rStrA = self._sf_rLstA[self._sf_rIntA].replace('<:','').replace('=','')
                                    self._sf_rLstB = re.findall(r'(?s:)'+re.escape(self._sf_rStrA)+r'<@qp\(.*?\):>', self._sf_sQp)
                                    if len(self._sf_rLstB) > 0: self._sf_rLstC.append(self._sf_rLstB[0])
                                    else:
                                        self._sf_rLstD = re.findall(r'<:'+re.escape(self._sf_rStrA)+r'=(?s:.*?).*:>', self._sf_sPq)
                                        if len(self._sf_rLstD) > 0:
                                            self._sf_sPq = self._sf_sPq.replace(self._sf_rLstD[0], '')
                                            self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                                if len(self._sf_rLstC) > 0:
                                    self._sf_rLstC = '\n'.join(self._sf_rLstC)
                                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{newVfsFlNm}.sqtpp', f':☆Staqtapp-v1.2.194\n|:{newVfsDirNm}<{newVfsFldrNm}>\n_|:{newVfsFldrNm}<sub-{newVfsFldrNm}>\n__|:sub-{newVfsFldrNm}<tqpt-{newVfsFldrNm},tpqt-{newVfsFldrNm},null>\n___|:tqpt-{newVfsFldrNm}<tqpt,null,n>:\nnull\n{self._sf_rLstC}:\n___|:(tqpt-{newVfsFldrNm})\n{self._sf_sPq}:\n___|:(tpqt-{newVfsFldrNm})\n__|:(sub-{newVfsFldrNm})\n_|:({newVfsFldrNm})\n|:({newVfsDirNm})')
                                    if isCurrVfsPth:
                                        self.sqtpp_file(False, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', None)
                                        self._sf_rLstB = self._sf_sSrc.split(':')
                                        self._sf_rLstB[0] = newVfsFlNm
                                        self._sf_rLstB[1] = newVfsDirNm
                                        self._sf_rLstB[2] = newVfsFldrNm
                                        self._sf_rLstB[3] = f'sub-{newVfsFldrNm}'
                                        self._sf_rLstB[4] = f'tqpt-{newVfsFldrNm}'
                                        self._sf_rLstB = ':'.join(self._sf_rLstB)
                                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', self._sf_rLstB)
                                    self._sf_rLstC = None
                                    self._sf_sQp = None
                                    self._sf_sPq = None
                                else:
                                    return -5
                            else:
                                return -4
                        else:
                            return -3
                    else:
                        return -2
                else:
                    return -2
            else:
                return -1
        except Exception as err_revar:
            self._sErr = f'staqtapp1.2 (revar) error: {err_revar}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_loadvar(self, isAllNmbrs: bool, varNm: str, mode):
        # Returns env-var data as str, list or a deque type.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_sPq, _sf_sRtrn, _sf_rLstA, _sf_rIntA)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@varNm was not found
        # -4=newline chars found
        # -5=no @qp(...): data declaring found
        # -6=no closing ): for @qp( data tag found
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if varNm == '*':
                        varNm = '___SQTPP___MRSV___'
                        if self.sqtpp_vfs_tpqt_file(True) != -1:
                            self._sf_rLstA = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                            if len(self._sf_rLstA) > 0:
                                self._sf_rLstA = self._sf_rLstA[0].split('\n')
                                varNm = self._sf_rLstA[len(self._sf_rLstA)-1].replace(':>','')
                            else:
                                return None
                        else:
                            return None
                    self._sf_sSrc = None
                    if self.sqtpp_var_value(varNm):
                        if mode==1: self._sf_sRtrn = self.sqtpp_tqpt_spdr(False, isAllNmbrs, 'lvsd', self._sf_sVd)
                        elif mode==2: self._sf_sRtrn = self.sqtpp_tqpt_spdr(False, isAllNmbrs, 'lvss', self._sf_sVd)
                        if self._sf_sRtrn == 2:
                            return -4
                        elif self._sf_sRtrn == 6:
                            return -5
                        elif self._sf_sRtrn == 7:
                            return -6
                        else:
                            self._sf_sQp = None
                            self._sf_sPq = None
                            return self._sf_sRtrn
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_loadvar:
            self._sErr = f'staqtapp1.2 (loadvar) error: {err_loadvar}'
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
                                            self.sqtpp_spok_mv_tree_get_branch_ohm(False, True, twRwSrc)
                                        else:
                                            if self._sf_rIntD[1] > self._sf_rIntC: self.sqtpp_spok_mv_tree_get_branch_ohm(False, True, twRwSrc)
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
            if not self._sf_rBoolB and self._sf_rStrE == '}' and self._sf_rStrD == ',': self._sf_rBoolB = True
            elif self._sf_rBoolB:
                if not self._sf_rBoolC and self._sf_rStrD == "'": self._sf_rBoolC = True
                else:
                    if not self._sf_rBoolC: self._sf_rBoolB = False
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
                                if self._sf_rBoolD and len(self._sf_rStrC) > 0:
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
                            self._sf_rIntA = self.sqtpp_svvs_next_int()
                            self._sf_rLstA.append(f'{varNm}_{self._sf_rIntA}')
                            self._sf_rLstA = ','.join(self._sf_rLstA)
                            self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_{self._sf_rIntA}<{varDat}>:\n')
                            self._sf_sSrc = self._sf_sSrc.replace(f'({varNm}={self._sf_rStrA})', f'({varNm}={self._sf_rLstA})')
                            self.sqtpp_silent_lock_add('___SQTPP___MRSV___', [f'{varNm}_{self._sf_rIntA}'])
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                        else:
                            lstA_cpy = self._sf_rLstA
                            strA_cpy = self._sf_rStrA
                            self._sf_sVn = varNm
                            self.sqtpp_silent_lock_remove(True, lstA_cpy)
                            self._sf_rLstA = re.findall(r'(?s:.)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
                            self._sf_sQp = self._sf_sQp.replace(self._sf_rLstA[0],'')
                            self.sqtpp_var_remove(lstA_cpy)
                            if self._sf_sSrc.find(f';({varNm}={strA_cpy})') > -1: self._sf_sSrc = self._sf_sSrc.replace(f';({varNm}={strA_cpy})','')
                            elif self._sf_sSrc.find(f'\n({varNm}={strA_cpy});') > -1: self._sf_sSrc = self._sf_sSrc.replace(f'({varNm}={strA_cpy});','')
                            else: self._sf_sSrc = self._sf_sSrc.replace(f'\n<sbf-{self._sf_sVfsFldr}-svvs:\n({varNm}={strA_cpy})//>','')
                            self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQpRplcX}:\n', f'{self._sf_sQp}:\n')
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                        self._sf_sQpRplcX = None
                        self._sf_rStrA = None
                        self._sf_sSrc = None
                        self._sf_sQp = None
                        self._sf_sPq = None
                        return 8
                    else:
                        return -6
                else:
                    if self.sqtpp_var_value(varNm):
                        if varDat != self._sf_sVd:
                            self._sf_rStrA = self.sqtpp_vfs_sub_file(False, False, 'svvs', None)
                            self._sf_rStrB = f'{self._sf_rStrA};({varNm}={varNm}_1)'
                            self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_rStrB)
                            self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_1<{varDat}>:\n')
                            self.sqtpp_silent_lock_add('___SQTPP___MRSV___', [f'{varNm}_1'])
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
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
                        self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}_1<{varDat}>:\n')
                        self.sqtpp_silent_lock_add('___SQTPP___MRSV___', [f'{varNm}_1'])
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
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
    def sqtpp_var_key(self, varNm: str, fncNm: str) -> bool:
        # Returns True if @fncNm is allowed to edit @varNm, is a listed key to @varNm.
        # Other very useful conditions of this include @fncNm being a env-var name of
        # a spawned var set, from use of the stalkvar function with multi-processing.
        # __slots__ in use: (_sf_sSrc, _sf_sPq, _sf_rLstA)
        # returns: -1=invalid vfs path, -2=bad path in vfs path setting file, -3=@varNm was not found in tpqt vfs file
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tpqt_file(True) != -1:
                    if self._sf_sPq.find(f'<:{varNm}=') > -1:
                        self._sf_rLstA = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                        if len(self._sf_rLstA) > 0:
                            if self._sf_rLstA[0].find(f'\n{fncNm}') > -1:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_var_key:
            self._sErr = f'staqtapp1.2 (var_key) error: {err_var_key}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_list_lock(self, varNm: str) -> list:
        # Returns list type of the vfs tpqt lock block fnc/etc. names for @varNm.
        # __slots__ in use: (_sf_sSrc, _sf_sPq, _sf_rLstA, _sf_rIntA)
        # returns:
        # -1=invalid vfs path
        # -2=bad path in vfs path setting file
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tpqt_file(True) != -1:
                    self._sf_rLstA = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                    self._sf_rIntA = len(self._sf_rLstA)
                    if self._sf_rIntA > 0:
                        self._sf_rLstA = self._sf_rLstA[0].split('\n')
                        self._sf_rLstA.pop(0)
                        self._sf_rIntA-=2
                        self._sf_rLstA[self._sf_rIntA] = self._sf_rLstA[self._sf_rIntA].replace(':>','')
                        self._sf_sSrc = None
                        self._sf_sPq = None
                        return self._sf_rLstA
                    else:
                        return []
                else:
                    return -2
            else:
                return -1
        except Exception as err_list_lock:
            self._sErr = f'staqtapp1.2 (list_lock) error: {err_list_lock}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_locate_var_data(self, isRgx: bool, varNmLst: list, srch: str):
        # "The fact that our Universe may be simulatable by a quite short computer
        # program calls into question wether it makes any ontological difference
        # wether simulations are run or not." - Max Tegmark
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_sVd, _sf_rLstA, _sf_rLstB, _sf_rIntA, _sf_rIntB, _sf_rBoolA)
        # returns:
        # -1=invalid vfs path
        # -2=empty vfs path settings file
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rIntA = 0
                    self._sf_rLstA = []
                    self._sf_rIntB = len(varNmLst)
                    while self._sf_rIntA < self._sf_rIntB:
                        self._sf_rBoolA = False
                        if self.sqtpp_var_value(varNmLst[self._sf_rIntA]):
                            if self._sf_sVd.find('(c__main__') > -1 and self._sf_sVd.find('c__builtin__') > -1:
                                try:
                                    self._sf_sVd = str(pickle.loads(str.encode(self._sf_sVd)))
                                except Exception as e:
                                    self._sf_rBoolA = True
                            if not self._sf_rBoolA:
                                if not isRgx:
                                    if self._sf_sVd.find(srch) > -1: self._sf_rLstA.append(varNmLst[self._sf_rIntA])
                                else:
                                    self._sf_rLstB = re.findall(srch, self._sf_sVd)
                                    if len(self._sf_rLstB) > 0: self._sf_rLstA.append(varNmLst[self._sf_rIntA])
                        self._sf_rIntA+=1
                    return self._sf_rLstA
                return -2
            return -1
        except Exception as err_locate_var_data:
            self._sErr = f'staqtapp1.2 (locate_var_data) error: {err_locate_var_data}'
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
        # __slots__ in use: (_sf_rLstA, _sf_rIntA, _sf_rIntB)
        # returns: none
        self._sf_rIntB = len(varNmLst)
        for self._sf_rIntA in range(self._sf_rIntB):
            self._sf_rLstA = re.findall(r'(?s:.)'+re.escape(varNmLst[self._sf_rIntA])+r'<@qp\(.*?\):>', self._sf_sQp)
            if len(self._sf_rLstA) > 0: self._sf_sQp = self._sf_sQp.replace(self._sf_rLstA[0],'')
        self._sf_sQp = self._sf_sQp.replace('):>\n:','):>:')
#_______________________________________________________________________________________
    def sqtpp_silent_lock_add(self, varNm: str, lckNmLst: list):
        # Adds tpqt fnc/var lock blocks quietly. Assumes _sf_sSrc already vfs content.
        # __slots__ in use: (_sf_sSrc, _sf_sPq, _sf_rLstA)
        # returns: none
        try:
            xLst = None
            xStr = None
            with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', 'r') as fObjStg: self._sf_rLstA = fObjStg.read().split(':')
            if self.sqtpp_vfs_tpqt_file(True) != -1:
                xLst = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                xStr = self._sf_sPq
                if len(xLst) > 0: self._sf_sPq = self._sf_sPq.replace(xLst[0], '<:' + varNm + '=\n' + '\n'.join(lckNmLst) + ':>')
                else:
                    self._sf_sPq = self._sf_sPq.replace(':>:',':>')
                    self._sf_sPq = self._sf_sPq + '\n<:' + varNm + '=\n' + '\n'.join(lckNmLst) + ':>'
                self._sf_sSrc = self._sf_sSrc.replace(f'{xStr}:', f'{self._sf_sPq}:')
                xStr = None
        except Exception as e:
            pass
#_______________________________________________________________________________________
    def sqtpp_silent_lock_remove(self, isStlkVar: bool, varNmLst: list):
        # Removes tpqt func/var lock block(s) quietly. Assumes _sf_sSrc already vfs content.
        # *Slots attribute _sf_sLstX retains any var name(s) to block(s) that got removed.*
        # __slots__ in use: (_sf_sSrc, _sf_sPq, _sf_sLstX, _sf_sBoolX)
        # returns: none
        try:
            x = None
            xLst = None
            xStr = None
            with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', 'r') as fObjStg: self._sf_sLstX = fObjStg.read().split(':')
            self._sf_sLstX[4] = self._sf_sLstX[4].replace('tqpt', 'tpqt')
            self._sf_sLstX = [f'|:{self._sf_sLstX[1]}<', f'_|:{self._sf_sLstX[2]}<', f'__|:{self._sf_sLstX[3]}<', f'___|:{self._sf_sLstX[4]}<']
            for pth in range(4):
                if pth < 1: x = self._sf_sSrc.find(self._sf_sLstX[pth])
                else: x = self._sf_sSrc.find(self._sf_sLstX[pth],x+1)
                if x < 0:
                    break
            if x > -1:
                self._sf_sPq = self._sf_sSrc[x:self._sf_sSrc.find('___|:',x+5)-2]
                self._sf_sBoolX = False
                self._sf_sLstX = []
                for x in range(len(varNmLst)):
                    xLst = re.findall(r'<:'+re.escape(varNmLst[x])+r'=(?s:.*?).*:>', self._sf_sPq)
                    if len(xLst) > 0:
                        if not self._sf_sBoolX:
                            self._sf_sBoolX = True
                            if isStlkVar:
                                self._sf_sLstX = varNmLst
                                self.sqtpp_darkvar()
                                self._sf_sLstX = []
                            xStr = self._sf_sPq
                        self._sf_sLstX.append(varNmLst[x])
                        self._sf_sPq = self._sf_sPq.replace(xLst[0],'')
                        self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                if len(self._sf_sLstX) > 0:
                    self._sf_sSrc = self._sf_sSrc.replace(xStr, self._sf_sPq)
                    self._sf_sSrc = self._sf_sSrc.replace(':>\n:',':>:')
                    self._sf_sBoolX = False
                    xStr = None
        except Exception as e:
            pass
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
    def sqtpp_svvs_next_int(self) -> int:
        # Returns the next int increment naming for a added spawned env-var or related.
        # __slots__ in use: (_sf_rLstA, _sf_sLstX, _sf_sIntX)
        # returns: (int)
        xRtrn = 1
        for x in range(len(self._sf_rLstA)):
            self._sf_sLstX = self._sf_rLstA[x].split('_')
            self._sf_sIntX = int(self._sf_sLstX[len(self._sf_sLstX)-1])
            if  self._sf_sIntX > xRtrn: xRtrn = self._sf_sIntX
        xRtrn+=1
        return xRtrn
#_______________________________________________________________________________________
    def sqtpp_vssv_menorah_cxv_rod(self, adrsNws: str, adrsPrv: str):
        # Applies an cXV calculation involving Base10 shift conversion owned palindromes.
        # Very accurate palindrome % calculation; like hitting a dime a 1,000 miles down.
        # (No need for a double equal right now, is left in the try block for later usage)
        # __slots__ in use: (_sf_rLstA, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rStrD, _sf_rStrE, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rBoolA)
        # returns: (menorah inverse type palindrome medians collide of a timed LR-analogous)
        self._sf_rLstC = adrsNws.split(',')
        self._sf_rStrD = self._sf_rLstC[1].replace('0','1')
        self._sf_rLstC[0] = self._sf_rLstC[0].replace('0','1')
        self._sf_rLstD = [int(dgt) for dgt in self._sf_rLstC[0]]
        self._sf_rLstC = adrsPrv.split(',')
        self._sf_rStrE = self._sf_rLstC[1].replace('0','1')
        self._sf_rLstC[0] = self._sf_rLstC[0].replace('0','1')
        self._sf_rLstE = [int(dgt) for dgt in self._sf_rLstC[0]]
        self._sf_rLstF = [(self._sf_rLstD[len(self._sf_rLstD)-1],self._sf_rLstE[len(self._sf_rLstE)-1]),(int(self._sf_rStrD[4]),int(self._sf_rStrE[6])),(int(self._sf_rStrD[3]),int(self._sf_rStrE[5])),(int(self._sf_rStrD[2]),int(self._sf_rStrE[4])),(int(self._sf_rStrD[1]),int(self._sf_rStrE[3])),(int(self._sf_rStrD[0]),int(self._sf_rStrE[2])),(int(self._sf_rStrD[5]),int(self._sf_rStrE[1]))]
        dfRtrn = None
        x = None
        self._sf_rLstA = []
        for x in range(2):
            for self._sf_rIntC in range(30):
                if x == 1:
                    self._sf_rIntD = math.sqrt(self._sf_rLstD[self._sf_rIntC-1])
                    self._sf_rIntE = math.sqrt(self._sf_rLstD[(self._sf_rIntC+1)%len(self._sf_rLstD)])
                    if (self._sf_rIntE+self._sf_rIntC)/2 > 14: self._sf_rIntF = (self._sf_rIntD+self._sf_rIntE)/(2*math.sqrt(self._sf_rLstD[self._sf_rIntC]))
                    else: self._sf_rIntF = ((self._sf_rIntD+self._sf_rIntE)/(2*math.sqrt(self._sf_rLstD[self._sf_rIntC]))+1)
                else:
                    self._sf_rIntD = math.sqrt(self._sf_rLstE[self._sf_rIntC-1])
                    self._sf_rIntE = math.sqrt(self._sf_rLstE[(self._sf_rIntC+1)%len(self._sf_rLstE)])
                    if (self._sf_rIntE+self._sf_rIntC)/2 < 14: self._sf_rIntF = (self._sf_rIntD+self._sf_rIntE)/(2*math.sqrt(self._sf_rLstE[self._sf_rIntC]))
                    else: self._sf_rIntF = ((self._sf_rIntD+self._sf_rIntE)/(2*math.sqrt(self._sf_rLstE[self._sf_rIntC]))+1)
                self._sf_rLstA.append(self._sf_rIntF)
        for self._sf_rIntC in range(7):
            self._sf_rIntD = math.sqrt(self._sf_rLstF[self._sf_rIntC-1][0])
            self._sf_rIntE = math.sqrt(self._sf_rLstF[(self._sf_rIntC)%len(self._sf_rLstF)][0])
            self._sf_rIntF = (self._sf_rIntD+self._sf_rIntE)/(2*math.sqrt(self._sf_rLstF[self._sf_rIntC][0]))
            self._sf_rLstA.append(self._sf_rIntF)
        self._sf_rIntE = int(f'{self._sf_rStrD[0]}{self._sf_rStrD[1]}{self._sf_rStrD[2]}{math.floor(math.sqrt(statistics.median(self._sf_rLstA)))}')
        self._sf_rIntF = len(self._sf_rLstA)
        for self._sf_rIntC in range(self._sf_rIntF):
            if self._sf_rLstA[self._sf_rIntC] > 1: self._sf_rIntE = self._sf_rIntE+self._sf_rLstA[self._sf_rIntC]
            else: self._sf_rIntE = self._sf_rIntE-self._sf_rLstA[self._sf_rIntC]
        self._sf_sIntX = self._sf_rIntE
        self._sf_rLstD = ''.join(map(str, self._sf_rLstD))
        self._sf_rStrF = str(math.floor(self._sf_rIntE))
        self._sf_rIntE = len(self._sf_rStrF)
        self._sf_rIntG = 0
        for self._sf_rIntC in range(31):
            self._sf_rIntF = self._sf_rIntC+self._sf_rIntE
            if self._sf_rIntF < 31:
                self._sf_rIntG+=1
                if self._sf_rIntG > 3: self._sf_rIntG = 1
                if self._sf_rLstD[self._sf_rIntC:self._sf_rIntF-self._sf_rIntG] == self._sf_rStrF[:self._sf_rIntG]: self._sf_rLstD = f'{self._sf_rLstD[:self._sf_rIntC]}.={self._sf_rLstD[self._sf_rIntC:]}'
            else:
                break
        if self._sf_rLstD.find('.=') < 0: self._sf_sRplc = f'{self._sf_sIntX},{self._sf_rStrF[::-1]}!={self._sf_rLstD}'
        else:
            self._sf_sRplc = f'{self._sf_sIntX},{self._sf_rLstD}'
            try:
                self._sf_rLstE = [_ for _, e in enumerate(self._sf_rLstD) if e == '.=']
                self._sf_rLstC = []
                self._sf_rIntC = len(self._sf_rLstE)-1
                for self._sf_rIntE in range(self._sf_rIntC):
                    self._sf_rIntD = self._sf_rLstE[self._sf_rIntE+1]-self._sf_rLstE[self._sf_rIntE]
                    self._sf_rLstF = []
                    for xv in range(1, self._sf_rIntD):
                        if self._sf_rIntD%xv == 0: self._sf_rLstF.append(xv)
                    xvLst = [math.sqrt(srl) for srl in self._sf_rLstF]
                    self._sf_rLstC.append(statistics.median(xvLst))
                self._sf_rIntH = max(self._sf_rLstC)
                self._sf_rLstF = [drl for drl, rbxNv in enumerate(self._sf_rLstC) if rbxNv == self._sf_rIntH]
                for self._sf_rIntC in self._sf_rLstF:
                    if self._sf_rIntC+1 <= len(self._sf_rLstE)-1:
                        self._sf_rIntD = self._sf_rLstE[self._sf_rIntC+1]-self._sf_rLstE[self._sf_rIntC]
                        self._sf_rLstD = f'{self._sf_rLstD[:self._sf_rLstE[self._sf_rIntC]+self._sf_rIntD]}=={self._sf_rLstD[self._sf_rLstE[self._sf_rIntC]+self._sf_rIntD:]}'
                self._sf_sRplc = f'{self._sf_sIntX},{self._sf_rLstD}'
            except Exception as e:
                pass
#_______________________________________________________________________________________
    def sqtpp_combined_addr_darkvar_search(self, cmbAddr: str, srchWndw: str):
        # Performs an sliding window search over a joined darkvar addrs, either finding
        # palindromes or anagrams. @srchWndw is the digit sequence in question of find.
        # Also performs a reduction count left to right & right to left for cvx lists.
        # __slots__ in use: (_sf_sLstX, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG)
        # returns: (none), _sf_sLstX is the search results
        self._sf_sLstX = {}
        self._sf_rLstA = deque(srchWndw)
        self._sf_rIntA = Counter(srchWndw)
        self._sf_rStrA = None
        self._sf_rIntB = len(cmbAddr)-len(srchWndw)+1
        for self._sf_rIntC in range(self._sf_rIntB):
            self._sf_rStrB = cmbAddr[self._sf_rIntC:self._sf_rIntC+len(srchWndw)]
            if self._sf_rStrB == self._sf_rStrB[::-1]:
                if self._sf_rStrA:
                    self._sf_rIntD = sum(self._sf_rIntF != self._sf_rIntG for self._sf_rIntF, self._sf_rIntG in zip(self._sf_rStrB, self._sf_rStrA))
                    self._sf_rIntE = sum(self._sf_rIntF != self._sf_rIntG for self._sf_rIntF, self._sf_rIntG in zip(self._sf_rStrB[::-1], self._sf_rStrA))
                    self._sf_sLstX[self._sf_rStrA].setdefault('rdc',{})[self._sf_rStrB] = {'l': self._sf_rIntD,'r': self._sf_rIntE}
                self._sf_sLstX.setdefault(self._sf_rStrB,{'pld':[(self._sf_rIntC,self._sf_rIntC+len(srchWndw)-1)]})
            elif Counter(self._sf_rStrB) == self._sf_rIntA:
                self._sf_rStrA = self._sf_rStrB
                self._sf_sLstX.setdefault(self._sf_rStrB, {'ang':[]})['ang'].append((self._sf_rIntC,self._sf_rIntC+len(srchWndw)-1))
                self._sf_rIntD = sum(self._sf_rIntF != self._sf_rIntG for self._sf_rIntF, self._sf_rIntG in zip(self._sf_rStrB, srchWndw))
                self._sf_rIntE = sum(self._sf_rIntF != self._sf_rIntG for self._sf_rIntF, self._sf_rIntG in zip(self._sf_rStrB[::-1], srchWndw))
                self._sf_sLstX[self._sf_rStrB].setdefault('rdc',{})[self._sf_rStrB] = {'l': self._sf_rIntD,'r': self._sf_rIntE}
            self._sf_rLstA.popleft()
            if self._sf_rIntC+len(srchWndw) < len(cmbAddr): self._sf_rLstA.append(cmbAddr[self._sf_rIntC+len(srchWndw)])
            else:
                break
            self._sf_rIntA = Counter(''.join(self._sf_rLstA))
#_______________________________________________________________________________________
    def sqtpp_plndrm(self, ttBranch: int) -> int:
        # Sets palindrome @_sf_sDv, @ttBranch half semi-loops before center1 rod/candle.
        # Example: 3 half semi-loops = 7 digits, 4 half semi-loops = 9 digits........
        # __slots__ in use: (_sf_rLstA, _sf_rLstB, _sf_rIntA, _sf_rIntB, _sf_rBoolA)
        # returns: none
        self._sf_rBoolA = False
        self._sf_rLstA = []
        self._sf_rLstB = ['8','6','7','5','3','1','9','4','2']
        self._sf_rIntA = -1
        self._sf_rIntB = 9
        while True:
            self._sf_rIntA+=1
            if self._sf_rIntA == 0: self._sf_rLstA.append(self._sf_rLstB[random.randint(0,8)])
            else:
                if not self._sf_rBoolA:
                    self._sf_rLstB.append('0')
                    self._sf_rBoolA = True
                    self._sf_rIntB+=1
                self._sf_rLstA.append(self._sf_rLstB[random.randint(0,9)])
                if self._sf_rIntA+1 == ttBranch:
                    self._sf_rLstA = ''.join(self._sf_rLstA)
                    self._sf_sDv = int(f'{self._sf_rLstA}{self._sf_rLstB[random.randint(0,9)]}{self._sf_rLstA[::-1]}')
                    break
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
        # Check to see if @src has formats for being a lambda function string.
        if self._sf_rBoolE: self._sf_rBoolE = self.sqtpp_lambda_scan_write(src)
        if not self._sf_rBoolE:
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
        else:
            self._sf_sSrc = None
            self._sf_sQp = None
            return 9
#_______________________________________________________________________________________
    def sqtpp_lambda_scan_write(self, src: str) -> bool:
        # Handles find & write of any found lambda function src/str to a tqpt source.
        # The spider method above would store a lambda function as a list because of
        # any comma uses. This writes @q|p(...): tagging to tqpt source as one liner.
        # With this function & the lambdavar() import run function, is very possible
        # to write entire python programs that would use lambda functions completely,
        # without a confusing framework of the lambda functions stored @ module(s).
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_sLstA, _sf_rStrA)
        try:
            src = src.replace('):',"")
            self._sf_sLstA = re.findall(r'lambda(?:\s*[a-zA-Z_][a-zA-Z_0-9]*(?:\s*,\s*[a-zA-Z_][a-zA-Z_0-9]*)*)?\s*:\s*.+', src)
            if len(self._sf_sLstA[0]) > 0:
                fndLmb = False
                for self._sf_rStrA in src:
                    if self._sf_rStrA != '=': self._sf_sLstA.append(self._sf_rStrA)
                    else:
                        fndLmb = True
                        break
                if fndLmb and len(self._sf_sLstA) > 1:
                    self._sf_rStrA = f' = {self._sf_sLstA[0]}'
                    self._sf_sLstA.pop(0)
                    self._sf_rStrA = f'{"".join(self._sf_sLstA)}{self._sf_rStrA}'
                    if self._sf_rStrA.find('@qp(') > -1:
                        self._sf_rStrA = self._sf_rStrA.replace('@qp(','@q|p(')
                        self._sf_rStrA = f'{self._sf_rStrA}):'
                    elif self._sf_rStrA.find('@q|p(') > -1: self._sf_rStrA = f'{self._sf_rStrA}):'
                    else: self._sf_rStrA = f'@q|p({self._sf_rStrA}):'
                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\nst1_atlaspice_{random.randint(111111111,999999999)}<{self._sf_rStrA}>:\n'))
                    return True
                else:
                    return False
            else:
                return False
        except Exception as err_lambda_scan_write:
            print(f'staqtapp1.2 (lambda_scan_write) error: {err_lambda_scan_write}')
#_______________________________________________________________________________________
    def sqtpp_del_locks(self, isDelAll: bool, varNm:str, fncNm):
        # Deletes tpqt lock entries from @varNm listed block or removes the entire block.
        # __slots__ in use: (_sf_sSrc, _sf_sPq, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rBoolA)
        # returns:
        # -1=invalid vfs path
        # -2=bad path in vfs path setting file
        # -3=@varNm was not found in tpqt vfs file
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tpqt_file(True) != -1:
                    self._sf_rLstA = re.findall(r'<:'+re.escape(varNm)+r'=(?s:.*?).*:>', self._sf_sPq)
                    if len(self._sf_rLstA) > 0:
                        self._sf_rStrA = self._sf_sPq
                        if not isDelAll:
                            self._sf_rLstB = self._sf_rLstA[0]
                            self._sf_rLstA = self._sf_rLstA[0].split('\n')
                            self._sf_rLstA.pop(0)
                            self._sf_rLstA[len(self._sf_rLstA)-1] = self._sf_rLstA[len(self._sf_rLstA)-1].replace(':>','')
                            if isinstance(fncNm, str): fncNm = [fncNm]
                            self._sf_rIntB = len(fncNm)
                            self._sf_rBoolA = False
                            for self._sf_rIntA in range(self._sf_rIntB):
                                if self._sf_rBoolA:
                                    break
                                for self._sf_rIntC in range(len(self._sf_rLstA)):
                                    if fncNm[self._sf_rIntA] == self._sf_rLstA[self._sf_rIntC]:
                                        if len(self._sf_rLstA) > 1:
                                            self._sf_rLstA.pop(self._sf_rIntC)
                                            break
                                        else:
                                            self._sf_rBoolA = True
                                            break
                            if not self._sf_rBoolA:
                                self._sf_rLstA = '<:'+varNm+'=\n'+'\n'.join(self._sf_rLstA)+':>'
                                self._sf_sPq = self._sf_sPq.replace(self._sf_rLstB, self._sf_rLstA)
                        if self._sf_rBoolA or isDelAll:
                            if isDelAll: self._sf_sPq = self._sf_sPq.replace(self._sf_rLstA[0],'')
                            else: self._sf_sPq = self._sf_sPq.replace(self._sf_rLstB,'')
                            self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(self._sf_rStrA, self._sf_sPq))
                        self._sf_sSrc = None
                        self._sf_sPq = None
                        self._sf_rStrA = None
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_del_locks:
            self._sErr = f'staqtapp1.2 (del_locks) error: {err_del_locks}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_vars_run_lambda(self, lmbNm: str, lmbPrms: list):
        # See lambdavar() description.
        # __slots__ in use: (_sf_sSrc, _sf_sQp, _sf_sStrX, _sf_rLstA, _sf_rStrD, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rBoolA, _sf_rBoolB)
        # returns:
        # -1=invalid vfs path
        # -2=bad path in vfs path setting file
        # -3=lambda function name not found
        # -4=lambda function found no proper construct
        # -5=mismatch params lengths @lmbPrms
        # -6=params names do not matchup @lmbPrms
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rLstA = re.findall(r'st1_atlaspice_.*?<\@q\|p\('+re.escape(lmbNm)+r'.*?\):>', self._sf_sQp)
                    if len(self._sf_rLstA[0]) > 0:
                        self._sf_sStrX = re.findall(r'st1_atlaspice_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', self._sf_rLstA[0])
                        if len(self._sf_sStrX[0]) > 0: self._sf_sStrX = self._sf_sStrX[0].replace('st1_atlaspice_','')
                        else: self._sf_sStrX = 'unknown'
                        self._sf_sRtrn = self.sqtpp_lambda_spdr()
                        if self._sf_sRtrn == -1:
                            return -4
                        elif self._sf_sRtrn == 1: self._sf_rBoolA = True
                        else: self._sf_rBoolA = False
                        if self._sf_rBoolA:
                            if len(lmbPrms) == len(self._sf_rLstA):
                                self._sf_rIntB = len(lmbPrms)
                                for self._sf_rIntA in range(self._sf_rIntB):
                                    if self._sf_rIntA > 0 and not self._sf_rBoolB:
                                        break
                                    self._sf_rBoolB = False
                                    self._sf_rIntC = 0
                                    while self._sf_rIntC < self._sf_rIntB:
                                        if lmbPrms[self._sf_rIntA].find(f'{self._sf_rLstA[self._sf_rIntC]}=') > -1:
                                            self._sf_rBoolB = True
                                            break
                                        self._sf_rIntC+=1
                                if not self._sf_rBoolB:
                                    return -6
                            else:
                                return -5
                        return self.sqtpp_lambda_lambda_lambda_clsr(lmbNm)
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_run_lambda:
            self._sErr = f'staqtapp1.2 (vars_run_lambda) error: {err_vars_run_lambda}'
            return self.sqtpp_err_rcrd(self._sErr)
#_______________________________________________________________________________________
    def sqtpp_lambda_lambda_lambda_clsr(self, lmbNm: str):
        # Edit/write function for the lambda slots class and import & run.
        # __slots__ in use: (_sf_sStrX, _sf_rStrD, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstE, _sf_rIntA, _sf_rIntB)
        # returns:
        if os.path.isfile(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2_LMB.py'):
            # Do search of lambda function already present in module for import & run.
            pass
        else:
            self._sf_rLstB = ['# This py-module is auto-generated by the Staqtapp1.2 vfs env-var library for lambda functions use. Edit at your own risk, seriously.\n\n\nclass SqtppLLL():\n\n    __slots__ = ()\n\n    def __init__(self):\n        pass\n\n\nclass SqtppLLL_Joints(SqtppLLL):\n\n    __slots__ = (']
            if self._sf_rBoolA:
                self._sf_rLstC = []
                self._sf_rIntB = len(self._sf_rLstA)
                for self._sf_rIntA in range(self._sf_rIntB): self._sf_rLstC.append("'" + self._sf_rLstA[self._sf_rIntA] + "'")
                self._sf_rLstB.append(f'{",".join(self._sf_rLstC)})')
                self._sf_rLstC = []
                for self._sf_rIntA in range(self._sf_rIntB): self._sf_rLstC.append(f' self.{self._sf_rLstA[self._sf_rIntA]} ')
                self._sf_rLstE = ''.join(self._sf_rLstE)
                self._sf_rStrD = self._sf_rStrD.replace(self._sf_rLstE, '')
                self._sf_rStrD = f'~{self._sf_rStrD}~'
                self.sqtpp_lambda_lambda_rplc()
                self._sf_rStrD = f'lambda{",".join(self._sf_rLstC)}: {self._sf_rStrD}'
            else: self._sf_rLstB.append(')')
            self._sf_rLstB.append('\n\n    def __init__(self):\n        pass\n#_______________________________________________________________________________________\n\n    # CTMN-LLL:' + str(self._sf_sStrX) + ':' + lmbNm + '\n')
            self._sf_rLstB.append(f'    {lmbNm} = {self._sf_rStrD.replace("):>","")}')
            with open(f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2_LMB.py', 'w') as lllfObjWrt: lllfObjWrt.write(''.join(self._sf_rLstB))
            # Import it and run it for the return.
#_______________________________________________________________________________________
    def sqtpp_lambda_lambda_rplc(self):
        # Replaces a lambda's fnc body vars to slots classed attr assigned performances.
        # __slots__ in use: (_sf_sLstX, _sf_rLstD, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD)
        # returns: (none)
        self._sf_sLstX = set('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        for self._sf_rIntA in range(self._sf_rIntB):
            self._sf_rIntC = 0
            self._sf_rIntE = 0
            #- - - - - ->◇ What is the price of a 4,800lb+ solid diamond carved into a
            #                outdoor breakfast table, with matching chairs astro? No?
            #                 Not possible? Such diamonds cannot be real? I'm lying?
            #                   We don't lie about Menorah Mathematics or Diamonds.
            while self._sf_rIntC < len(self._sf_rStrD):
                self._sf_rIntE = self._sf_rIntC
                self._sf_rIntC = self._sf_rStrD.find(self._sf_rLstA[self._sf_rIntA], self._sf_rIntC)
                if self._sf_rIntC > -1:
                    self._sf_rIntD = self._sf_rIntC+len(self._sf_rLstA[self._sf_rIntA])
                    if not set(self._sf_rStrD[self._sf_rIntC-1]).issubset(self._sf_sLstX) and not set(self._sf_rStrD[self._sf_rIntD]).issubset(self._sf_sLstX):
                        self._sf_rLstD = [self._sf_rStrD[0:self._sf_rIntC], self._sf_rStrD[self._sf_rIntD:len(self._sf_rStrD)]]
                        self._sf_rStrD = f'{self._sf_rLstD[0]}self.{self._sf_rLstA[self._sf_rIntA]}{self._sf_rLstD[1]}'
                        self._sf_rIntC = self._sf_rIntD+5
                    else: self._sf_rIntC = self._sf_rIntE+1
                else: self._sf_rIntC = self._sf_rIntE+1
        self._sf_rStrD = self._sf_rStrD.replace('~','')
#_______________________________________________________________________________________
    def sqtpp_lambda_spdr(self) -> int:
        # Parses an lambda string declared params for list use on re-assembly & run.
        # __slots__ in use: (_sf_rLstA, _sf_rLstE, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rIntA, _sf_rIntB)
        # returns:
        # -1=no proper lambda function found
        #  1=lambda function has variable params
        #  0=lambda function has no variable params
        self._sf_rStrB = re.findall(r'lambda(?:\s*[a-zA-Z_][a-zA-Z_0-9]*(?:\s*,\s*[a-zA-Z_][a-zA-Z_0-9]*)*)?\s*:\s*.+', self._sf_rLstA[0])
        if len(self._sf_rStrB[0]) > 0:
            self._sf_rStrD = self._sf_rStrB[0]
            self._sf_rStrB = self._sf_rStrB[0].replace('lambda','')
            self._sf_rLstA = []
            self._sf_rLstE = ['l','a','m','b','d','a']
            self._sf_rStrC = ''
            self._sf_rIntA = 0
            self._sf_rIntB = 0
            for self._sf_rStrA in self._sf_rStrB:
                self._sf_rLstE.append(self._sf_rStrA)
                if self._sf_rStrA != ':':
                    if self._sf_rStrA == ',':
                        self._sf_rLstA.append(self._sf_rStrC.replace(' ',''))
                        self._sf_rStrC = ''
                        self._sf_rIntA = 0
                        if self._sf_rIntB == 0: self._sf_rIntB = 1
                    else:
                        self._sf_rStrC = f'{self._sf_rStrC}{self._sf_rStrA}'
                        if self._sf_rIntA == 0: self._sf_rIntA = 1
                else:
                    if self._sf_rIntA == 1:
                        self._sf_rLstA.append(self._sf_rStrC.replace(' ',''))
                        self._sf_rIntB = 1
                        break
            return self._sf_rIntB
        else:
            return -1
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
    def sqtpp_rqnv_menorah_reorder(self, lNms: list, pPrbLen: int, qnvRtm: int) -> str:
        # Scans @lNms for each palindrome probability mirroring threshold @qnvRtm and
        # if match or greater @pPrbLen frequency, will reverse order the loop's window
        # in quest to a made palindrome via previous numbers & shifting right>=.<left.
        # The order of when a probability higher than @qnvRtm to then seeking a nearest
        # palindrome to do reverse order is kept non-apparent as in real shadow cvx and
        # shifted to R-L, aka front of string. There is no neutral-odd or neutral-even
        # darkvar addrs & determining factor of why these function's fastest paths; yet
        # here they are not, because is simulated prob of a observerless cast reorders.
        # __slots__ in use: (_sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rStrA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rIntI, _sf_rBoolA)
        # returns:
        self._sf_rLstA = []
        self._sf_rIntB = len(lNms)
        self._sf_rIntF = self._sf_rIntB-(pPrbLen-1)
        for self._sf_rIntA in range(self._sf_rIntB):
            self._sf_rLstB = []
            self._sf_rIntC = self._sf_rIntA
            if self._sf_rIntC > 0: self._sf_rIntD = self._sf_rIntC+pPrbLen
            else: self._sf_rIntD = pPrbLen
            if self._sf_rIntD <= self._sf_rIntB:
                while self._sf_rIntC < self._sf_rIntD:
                    self._sf_rLstB.append(lNms[self._sf_rIntC])
                    self._sf_rIntC+=1
                for self._sf_rIntE in range(self._sf_rIntF):
                    self._sf_rIntI = 0
                    self._sf_rIntG = 0
                    self._sf_rIntH = pPrbLen-1
                    while self._sf_rIntH > -1:
                        if lNms[self._sf_rIntE+self._sf_rIntG] == self._sf_rLstB[self._sf_rIntH]: self._sf_rIntI+=1
                        self._sf_rIntG+=1
                        self._sf_rIntH-=1
                self._sf_rLstA.append(self._sf_rIntI/(self._sf_rIntB-self._sf_rIntA-(pPrbLen-2)))
            else:
                self._sf_rStrA = ''.join(map(str, lNms))
                self._sf_sIntX = int(self._sf_rStrA[self._sf_rIntA:self._sf_rIntB])
                break
        self._sf_sLstX = []
        self._sf_rIntC = len(self._sf_rLstA)
        while self._sf_rIntA < self._sf_rIntC:
            if self._sf_rLstA[self._sf_rIntA] > qnvRtm:
                self._sf_rLstB = []
                for self._sf_rIntD in range(self._sf_rIntF):
                    self._sf_rLstB.append(lNms[self._sf_rIntD])
                    if len(self._sf_rLstB) == pPrbLen:
                        self._sf_rIntB = self._sf_rIntD+pPrbLen
                        while self._sf_rIntB < len(lNms) and lNms[self._sf_rIntB] < self._sf_rLstB[len(self._sf_rLstB)-1]:
                            self._sf_rIntB+=1
                        if self._sf_rIntB < len(lNms):
                            self._sf_rIntE = self._sf_rIntB-1
                            while self._sf_rIntE > self._sf_rIntD:
                                self._sf_sLstX.append(lNms[self._sf_rIntE])
                                self._sf_rIntE-=1
                        self._sf_rIntE = len(self._sf_rLstB)-1
                        while self._sf_rIntE > -1:
                            self._sf_sLstX.append(self._sf_rLstB[self._sf_rIntE])
                            self._sf_rIntE-=1
                        if self._sf_rIntB < len(lNms): self._sf_rIntD = self._sf_rIntB
                        else: self._sf_rIntD = self._sf_rIntD+pPrbLen
                    else:
                        self._sf_sLstX.append(lNms[self._sf_rIntD])
                        self._sf_rIntD+=1
        self.sqtpp_reset_slots(False)
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
    def sqtpp_reset_slots(self, isStcSlts: bool):
        # Resets slots attribute variables to None.
        # returns: none
        if isStcSlts:
            self._sf_sVfs = None
            self._sf_sVfsFldr = None
            self._sf_sSrc = None
            self._sf_sRplc = None
            self._sf_sQpRplcX = None
            self._sf_sQp = None
            self._sf_sPq = None
            self._sf_sVd = None
            self._sf_sDv = None
            self._sf_sVn = None
            self._sf_sRtrn = None
            self._sf_sKntId = None
            self._sf_sLstX = None
            self._sf_sStrX = None
            self._sf_sIntX = None
            self._sf_sBoolX = None
            self._sf_sBoolCxv = None
            self._sf_sLstA = None
        self._sf_rStrA = None
        self._sf_rStrB = None
        self._sf_rStrC = None
        self._sf_rStrD = None
        self._sf_rStrE = None
        self._sf_rStrF = None
        self._sf_rLstA = None
        self._sf_rLstB = None
        self._sf_rLstC = None
        self._sf_rLstD = None
        self._sf_rLstE = None
        self._sf_rLstF = None
        self._sf_rIntA = None
        self._sf_rIntB = None
        self._sf_rIntC = None
        self._sf_rIntD = None
        self._sf_rIntE = None
        self._sf_rIntF = None
        self._sf_rIntG = None
        self._sf_rIntH = None
        self._sf_rIntI = None
        self._sf_rBoolA = None
        self._sf_rBoolB = None
        self._sf_rBoolC = None
        self._sf_rBoolD = None
        self._sf_rBoolE = None
#_______________________________________________________________________________________
    def sqtpp_slots_rcrd(self) -> bool:
        # Writes cache state of sf s-type slots variables data to vfs file, minus slots
        # _sf_sSrc, _sf_sQp, _sf_sQpRplcX and _sf_sPq that are constant txt replacement.
        # __slots__ in use: (_sf_rLstA, _sf_rLstD, _sf_rStrA)
        # returns: none
        if self.sqtpp_set_vfs_file() == 1:
            if self.sqtpp_vfs_tpqt_file(True) != -1:
                self._sf_rStrA = "___csvfs___stp___zael33M1JC777"
                self._sf_rLstD = re.findall(r'<:'+re.escape(self._sf_rStrA)+r'=(?s:.*?).*:>', self._sf_sPq)
                if len(self._sf_rLstD) > 0:
                    self._sf_sPq = self._sf_sPq.replace(self._sf_rLstD[0],'')
                    self._sf_sPq = self._sf_sPq.replace('\n\n','\n')
                    self._sf_sPq = self._sf_sPq.replace(':>\n:',':>:')
                self._sf_rLstD = []  
                self._sf_rLstD.append(f'_sf_sVfsFldr________{self._sf_sVfsFldr}')
                self._sf_rLstD.append(f'_sf_sBoolCxv________{self._sf_sBoolCxv}')
                self._sf_rLstD.append(f'_sf_sKntId________{self._sf_sKntId}')
                self._sf_rLstD.append(f'_sf_sBoolX________{self._sf_sBoolX}')
                self._sf_rLstD.append('_sf_sRtrn________' + self._sf_sRtrn.replace('\n','☆'))
                self._sf_rLstD.append('_sf_sLstX________' + self._sf_sLstX.replace('\n','☆'))
                self._sf_rLstD.append('_sf_sStrX________' + self._sf_sStrX.replace('\n','☆'))
                self._sf_rLstD.append(f'_sf_sIntX________{self._sf_sIntX}')
                self._sf_rLstD.append('_sf_sRplc________' + self._sf_sRplc.replace('\n','☆'))
                self._sf_rLstD.append(f'_sf_sVfs_______{self._sf_sVfs}')
                self._sf_rLstD.append(f'_sf_sVd________{self._sf_sVd}')
                self._sf_rLstD.append('_sf_sDv________' + self._sf_sDv.replace('\n','☆'))
                self._sf_rLstD.append(f'_sf_sVn________{self._sf_sVn}')
                self.sqttp_tpqt_spok(False, False, self._sf_rStrA, self._sf_rLstD)
                self._sf_rLstD = None
                self._sf_sSrc = None
                self._sf_sPq = None
                return True
            return False
        return False
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
#_______________________________________________________________________________________
#_________________________IMPORT CALLABLE FRONT FUNCTIONS:
#_______________________________________________________________________________________
def makevfs(vfsFileName: str, directoryName: str, folderName:str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_makevfs(vfsFileName, directoryName, folderName)
#_______________________________________________________________________________________
def setpath(vfsFileName: str, directoryName: str, folderName: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_setpath(vfsFileName, directoryName, folderName)
#_______________________________________________________________________________________
def addvar(varName: str, varData: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_addvar(varName, varData)
#_______________________________________________________________________________________
def renamevar_stx(varName: str, newVarName):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_renamevar_stx(varName, newVarName)
#_______________________________________________________________________________________
def removevar(varName: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_removevar(varName)
#_______________________________________________________________________________________
def listvars() -> list:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_listvars()
#_______________________________________________________________________________________
def joinvars(newVarName: str, varNames: list):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_joinvars(newVarName, varNames)
#_______________________________________________________________________________________
def changevar(varName: str, newVarData: str):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_changevar(varName, newVarData)
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
def vardata_stx(isRegex: bool, varNameList: list, search: str) -> list:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_vardata_stx(isRegex, varNameList, search)
#_______________________________________________________________________________________
def lockvar(varName: str, fncName):
    # @fncName can be either a single str or list of str elements
    sqtppCls = Sqtpp()
    sqtppCls.mcf_lockvar(varName, fncName)
#_______________________________________________________________________________________
def locklist(varName: str) -> list:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_locklist(varName)
#_______________________________________________________________________________________
def lockdel(isDelAll: bool, varName: str, fncName):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_lockdel(isDelAll, varName, fncName)
#_______________________________________________________________________________________
def keyvar(varName: str, fncName) -> bool:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_keyvar(varName, fncName)
#_______________________________________________________________________________________
def darkvar():
    sqtppCls = Sqtpp()
    sqtppCls.mcf_darkvar()
#_______________________________________________________________________________________
def revar(isNewSetVfsPath, newVfsFileName, newVfsDirName, newVfsFldrName):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_revar(isNewSetVfsPath, newVfsFileName, newVfsDirName, newVfsFldrName)
#_______________________________________________________________________________________
def findvar(varName: str) -> bool:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_findvar(varName)
#_______________________________________________________________________________________
def findvar_stx(varNameList: list, stalkVarName: str) -> list:
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_findvar_stx(varNameList, stalkVarName)
#_______________________________________________________________________________________
def loadvar(isAllNumbers: bool, varName: str, mode: str):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_loadvar(isAllNumbers, varName, mode)
#_______________________________________________________________________________________
def stalkvar(varName: str, varData: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_stalkvar(varName, varData)
#_______________________________________________________________________________________
def lambdavar(lambdaName: str, lambdaParams: list):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_lambdavar(lambdaName, lambdaParams)
#_______________________________________________________________________________________

#def test():
    #sfCls = SqtppFncs()
    # ><)))))))))))))))))'>-------------------------------------------------------
    #makevfs('vfs-test','dir-test','folder-test')
    #print(findvar('faster_stacks'))
    #lockvar('faster_stacks3', ['someFnc12','someFnc8','someFnc14','someFnc19'])
    #stalkvar('faster_stacks3', '@qp(1,2,3,4,5,6,7,8,9):')
    #print(findvar_stx(['faster_stacks2','faster_stacks4'], 'faster_stacks3'))
    #addtree_stx('tree_test1', ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    #addbranch_stx('tree_test1', 'b', 'knt', 7948233)
    #print(getbranch_stx(True, 'tree_test1', None))
    #print(keyvar('faster_stacks', 'someFnc8'))
    #revar(True, 'new-vfs', 'new-vfs-dir', 'new-vfs-folder')
    #print(loadvar(True, 'faster_stacks3_1', 'mode=deque'))
    #print(changevar('faster_stacks3', '@qp(spawned):'))
    #lockdel(False, 'faster_stacks',['someFnc1','someFnc2','someFnc3','someFnc4','someFnc9','someFnc10'])
    #joinvars('faster_stacks6', ['tree_test1'])
    #print(renamevar_stx('globe', -1))
    #removevar('floating_needles_album1')
    #darkvar()
    #print(listvars())
    #print(locklist('__KLF__DSG__'))
    #tmpLst = [9,3,7,5,3,9,0,4,2,0,4,2,7,8,5,1,8,0,5,9,4,3,1,1,8,5,4,0,0,3,2,7,8,4,5,9]
    #sfCls.sqtpp_combined_addr_darkvar_search('8493028461184743541725210418472696364521749274511', '41725')
    #print(sfCls._sf_sLstX)
    #print(vardata_stx(True, ['faster_stacks3','faster_stacks5'], r'\[\]@'))
    #setpath('vfs','dir','folder')
    #addvar(None, 'bin_srch = lambda l, x, lo, hi: -1 if lo > hi else (lo+hi)//2 if l[(lo+hi)//2] == x else bin_srch(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else bin_srch(l, x, (lo+hi)//2+1, hi)')
    #lambdavar('bin_srch', ['l=3','x=4','lo=5','hi=6'])
    #--------------------------------------------------------------------<'(((((>< 
#test()
        
