#QPython 3SE / Row4 / staqtapp.py (6,901 lines) / 11:11 Tue, Dec 24




##]This py module's authentic/original coding is secured by AHS holographic checksum[##




#Staqtapp-v1.2.615 | Hybrid VFS ENV-VAR Library for Python OS builds or Other | Row4
# <<<
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




# UPDATE TUE, DEC24: Began works for a vitalvar() integration with Staqtapp's registry
#                    after review of this proposed feature & an consent need/crucial.



#_______________________________________________________________________________________
# SQTPP V1.2 HYBRID VFS ENV-VAR LIBRARY DESCRIPTION:


# ***Staqtapp 1.2 currently has 26 callable import functions. This vfs type env-var lib
# is a powerful all in one module for env-vars. See IMPORT_CALLS.TXT before using***



# A rework of the original Staqtapp env-vars library. Uses a vfs system for both tqpt,
# tpqt and other needed files. Built to last in one concentrated module for __slots__
# performance, with same thorough error checking and stpx type function calling. You
# set the vfs dir path to a tqpt variables file & all else handled with min param use.
# (A vfs staqtapp 1.2 file must be created first. Auto sets the tqpt vars set path.)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# This env-var library has features included for simulations in q-bit computing via
# stalkvar(), joinvars(), changevar(), addtree_stx(), addbranch_stx(), getbranch_stx(),
# revar() and findvar_stx(). Nicknamed the tangent-8 for all Staqtapp versions. With
# these 8 functions, can be implementations of gate splicing across the env-var stacks
# in multiple vfs files, static recursions optional from a sliding deque of tree vals,
# and merged spawned interlinking gates with lockvar() and keyvar() in outer-phasing
# to a tri-junction with stalkvar spawned vars; assigned to lockvar as move|lock|key,
# with the addbranch_stx() & getbranch_stx() merge branch and shift specific feature.

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


# ***THIS IS A PUBLIC VERSION OF STAQTAPP, DOES NOT INCLUDE ALL POJISHON FEATURES***


# >>>> See IMPORT_CALLS.TXT for a full description usage of all importable functions

#_______________________________________________________________________________________
#_______________________________________________________________________________________
# For all pojishon features, a non-negotiated price of 1,750,000 US DOLLARS.
# Set price reflects very advanced capability for remote embedded ai systems
# using a similiar python module; or converted C/C++ version of this library.
# Includes custom antenna symmetry interfacing, open modular expansions and
# the other special designed methods for security thru out this library using
# tor like vfs-dir multi-layer encryption(koch) & vfs-file encryption(kyber)
# Is setup straight from the start for advanced imaging classing and other
# dynamic learn & adapt configurations as the goto hybrid env-var/vfs sys,
# that is exclusive tested mathematics in design of it's m/d/f operations.
#_______________________________________________________________________________________
# github.com/lastforkbender/staqtapp
# rcttcr5@gmail.com

from datetime import datetime
from decimal import Decimal as dcml
from collections import deque, Counter

import statistics
import importlib
import pickle
import random
import base64
import math
import glob
import sys
import ast
import os
import re

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

#                          .|MID ERROR-CHECKING FUNCTIONS|.

#_______________________________________________________________________________________
class Sqtpp():
    __slots__ = ('_sErr', '_sRtrn', '_rIntA', '_rIntB', '_rBoolA')
    
    def __init__(self):
        pass
#_______________________________________________________________________________________
    def mcf_sqtpp_rd1(self, src):
        # **** For testing purposes only ****
        sfCls = SqtppFncs()
        sfCls.sqtpp_ntr_mvi8_intrpt(src)
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_______________________________________________________________________________________
    def mcf_vitalvar(self):
        # A timed interfaced/config/sub-config env-var updated @ vfs dir/file associated
        # All vital vars of env-var dsg '@q!p<...>' in the tqpt and/or tpqt stacks both
        sfCls = SqtppFncs()
        pass
#_______________________________________________________________________________________
    def mcf_lll_registry(self, isRd: bool, kyNm: str, kyDt, schm: str):
        # Is access to sqtpp-registry system sqtpp1_2_REG.py
        sfCls = SqtppFncs()
        if kyNm != '____SQTPP_REG_STGS_KEY____':
            if schm != '____SQTPP_REG_STGS_SCHM____':
                self._sRtrn = sfCls.sqtpp_registry_homer(isRd, kyNm, kyDt, schm)
            else:
                raise Exception(f'[sqtpp-reg >> registry] - !! exception warning, harp-schema name is not allowed "____SQTPP_REG_STGS_SCHM____" !!')
        else:
            raise Exception(f'[sqtpp-reg >> registry] - !! exception warning, registry key name is not allowed "____SQTPP_REG_STGS_KEY____" !!')
        return self._sRtrn
#_______________________________________________________________________________________
    def mcf_makevfs(self, vfsNm: str, dirNm: str, fldrNm: str):
        # Creates .sqtpp vfs file in the current working module dir .../staqtapp1_2/
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
    def mcf_list_files(self):
        #Display to console current set vfs m/d/f
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_vfs_display_file_struct()
#_______________________________________________________________________________________
    def mcf_corevar(self, mode: int, varNm: str, blLst: list):
        # See corevar description. @mode 1=write, 2=normal return, 3=delta RLE return
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, varNm):
            self._sRtrn = sfCls.sqtpp_byte_vars(mode, varNm, blLst)
            if self._sRtrn == -1: self.mcf_err_handler(6, 'corevar')
            elif self._sRtrn == -2: self.mcf_err_handler(7, 'corevar')
            elif self._sRtrn == -3: self.mcf_err_handler(12, 'corevar')
            elif self._sRtrn == -4: self.mcf_err_handler(14, 'corevar')
            elif self._sRtrn == -5: self.mcf_err_handler(47, 'corevar')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'corevar')
            else:
                return self._sRtrn
        else: self.mcf_err_handler(8, 'corevar')
#_______________________________________________________________________________________
    def mcf_pojishon(self, mode: str, varDat, varNm, dirLst: list):
        # A labyrinth of env-var use connected to staqtapp's embedded mount/directory
        # vfs file system for custom operations. See IMPORT_CALLS.TXT for mode usage.
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_emb_vfs_pojishon(mode, varDat, varNm, dirLst)
        if isinstance(self._sRtrn, bool):
            return self._sRtrn
        if isinstance(self._sRtrn, int):
            if self._sRtrn == -1: self.mcf_err_handler(48, 'pojishon')
            elif self._sRtrn == -2: self.mcf_err_handler(49, 'pojishon')
            elif self._sRtrn == -3: self.mcf_err_handler(50, 'pojishon')
            elif self._sRtrn == -4: self.mcf_err_handler(51, 'pojishon')
            elif self._sRtrn == -5: self.mcf_err_handler(52, 'pojishon')
            elif self._sRtrn == -6: self.mcf_err_handler(53, 'pojishon')
            elif self._sRtrn == -7: self.mcf_err_handler(54, 'pojishon')
            elif self._sRtrn == -8: self.mcf_err_handler(55, 'pojishon')
            elif self._sRtrn == -9: self.mcf_err_handler(56, 'pojishon')
            elif self._sRtrn == -10: self.mcf_err_handler(57, 'pojishon')
            elif self._sRtrn == -11: self.mcf_err_handler(58, 'pojishon')
            elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'pojishon')
            else:
                return 1
        else:
            return self._sRtrn
#_______________________________________________________________________________________
    def mcf_addvar(self, varNm: str, varDat: str):
        # Adds variables to the set path vfs tqpt file. If finds the word 'lambda' in
        # varDat will bypass a normal addvar() in exchange for storing a runnable var.
        # In that special case, the parameter @varNm is ignored for writing to tqpt.
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
    def mcf_appvar(self, varNms: list, varDts: list, varLks):
        # Adds env-var(s) by lists, including a lock name list for keyvar() coherency.
        sfCls = SqtppFncs()
        if isinstance(varNms, list) and isinstance(varDts, list):
            self._rIntA = 0
            self._rBoolA = True
            self._rIntB = len(varNms)
            while self._rIntA < self._rIntB:
                if not sfCls.sqtpp_chars_check(2, varNms[self._rIntA]):
                    self._rBoolA = False
                    break
                self._rIntA+=1
            if self._rBoolA:
                self._sRtrn = sfCls.sqtpp_applied_vars(varNms, varDts, varLks)
                if self._sRtrn == -1: self.mcf_err_handler(6, 'appvar')
                elif self._sRtrn == -2: self.mcf_err_handler(7, 'appvar')
                elif self._sRtrn == -3: self.mcf_err_handler(9, 'appvar')
                elif self._sRtrn == -4: self.mcf_err_handler(10, 'appvar')
                elif self._sRtrn == -5: self.mcf_err_handler(11, 'appvar')
                elif self._sRtrn == -6: self.mcf_err_handler(8, 'appvar')
                elif self._sRtrn == -7: self.mcf_err_handler(46, 'appvar')
                elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'appvar')
            else: self.mcf_err_handler(8, 'appvar')  
        else: self.mcf_err_handler(45, 'appvar')
#_______________________________________________________________________________________
    def mcf_renamevar_stx(self, varNm: str, newVarNm):
        # Returns 1 if renamed var, 2 if renamed spawned vars with one left spawned
        # var or 3 if renamed spawned vars and more than one left from stalked var.
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
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_vars_list()
        if self._sRtrn == -1: self.mcf_err_handler(6, 'listvars')
        elif self._sRtrn == -2: self.mcf_err_handler(7, 'listvars')
        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'listvars')
        else:
            return self._sRtrn
#_______________________________________________________________________________________
    def mcf_lambdalist(self, asComplete: bool):
        # Returns list type of special tagged @q|p(...): lambda functions in tqpt stack.
        sfCls = SqtppFncs()
        self._sRtrn = sfCls.sqtpp_list_lambda(asComplete)
        if self._sRtrn == -1: self.mcf_err_handler(6, 'lambdalist')
        elif self._sRtrn == -2: self.mcf_err_handler(7, 'lambdalist')
        elif self._sRtrn == 'FNC-ERR' or self._sRtrn == 'FOO-BAR': self.mcf_err_handler(-1, 'lambdalist')
        else:
            return self._sRtrn
#_______________________________________________________________________________________
    def mcf_joinvars(self, newVarNm: str, varNms: list):
        # Joins a list of @varNms into a newly merged env-var in vfs tqpt source or
        # joins list of spawned env-vars data to @newVarNm if @newVarNm is stalked.
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
    def mcf_genicvar(self, mode: str, vrNm, vrDt, vrId):
        # List comprehension storing and the optional running of them.
        sfCls = SqtppFncs()
        if sfCls.sqtpp_chars_check(2, vrNm):
            self._sRtrn = sfCls.sqtpp_lst_gen_lcks(mode, vrNm, vrDt, vrId)
        else: self.mcf_err_handler(8, 'genicvar')
#_______________________________________________________________________________________
    def mcf_addtree_stx(self, trNm: str, initPthLst: list):
        # Adds a spahk-mv type initial path keys built dict tree to vfs tqpt source.
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
            # 45 = @varNms is not a list for @appvar function call
            # 46 = @varLks for appvar missing : format for add lock names
            # 47 = @mode for corevar() is of a invalid int setting argument
            # 48 = [pojishon] >> invalid types balance @varDt and @varNm
            # 49 = [pojishon] >> non-allowed char sequence found @varDt: ':|:>'
            # 50 = [pojishon] >> non-allowed char(s) @varNm, allowed _a-zA-Z0-9
            # 51 = [pojishon] >> no found last added file in settings for cast
            # 52 = [pojishon] >> unable to read/get required vfs mounts source
            # 53 = [pojishon] >> invalid parameters combination for next.splice
            # 54 = [pojishon] >> invalid chars @dirList
            # 55 = [pojishon] >> last used mount in vfs settings was not found
            # 56 = [pojishon] >> last used mount/directory in vfs settings was not found
            # 57 = [pojishon] >> last used mount/directory/file in vfs settings was not found
            # 58 = [pojishon] >> @varData missing, is empty
            # 59 = [pojishon] >> @varData is missing required arguments for pattern splicing
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
            elif altErrCd == 45: raise Exception(f'staqtapp1.2 ({clnFnc}) error: params for @appvar must be list types')
            elif altErrCd == 46: raise Exception(f'staqtapp1.2 ({clnFnc}) error: str format for @varLocks param of appvar invalid, missing proper : seperator')
            elif altErrCd == 47: raise Exception(f'staqtapp1.2 ({clnFnc}) error: @mode for corevar must be 1, 2 or 3: 1=write, 2=normal list return, 3=RLE tuples list return')
            elif altErrCd == 48: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] invalid types balance for @varData &| @varName, both must be str or list')
            elif altErrCd == 49: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] char sequence ":|:>" was found @varData, non-allowed is special read char-seq for end of file')
            elif altErrCd == 50: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] non-allowed char(s) @varNm, allowed _a-zA-Z0-9')
            elif altErrCd == 51: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] no found last added file in vfs settings...')
            elif altErrCd == 52: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] unable to read/get required vfs mounts/dirs sources!')
            elif altErrCd == 53: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] invalid arguments settings for "next.splice", see IMPORT_CALLS.TXT')
            elif altErrCd == 54: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] invalid chars found @dirList, valid chars: _ a-z A-Z 0-9')
            elif altErrCd == 55: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] last used mount in vfs settings was not found')
            elif altErrCd == 56: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] last used mount/directory in vfs settings was not found')
            elif altErrCd == 57: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] last used mount/directory/file in vfs settings was not found')
            elif altErrCd == 58: raise Exception(f'staqtapp1.2 ({clnFnc}) error: [sqtpp-vfs >> pojishon] missing needed arguments @varData, is empty')
        else:
            if self._sRtrn == 'FNC-ERR': raise Exception(f'staqtapp1.2 {clnFnc}-->{self._sErr}')
            elif self._sRtrn == 'FOO-BAR': raise Exception('staqtapp1.2 io error: unable to perform basic file reads or writes')
#_______________________________________________________________________________________

#                          .|VFS/PARSING/UTILITY FUNCTIONS|.

#_______________________________________________________________________________________
class SqtppFncs(Sqtpp):
    __slots__ = ('_sf_sVfs', '_sf_sVfsDir', '_sf_sVfsFldr', '_sf_sSrc', '_sf_sRplc', '_sf_sQp', '_sf_sQpRplcX', '_sf_EfvStrX', '_sf_sPq', '_sf_sDv', '_sf_sVd', '_sf_sVn', '_sf_sRtrn', '_sf_sKntId', '_sf_sLstX', '_sf_sStrX', '_sf_sIntX', '_sf_sBoolX', '_sf_sBoolCxv', '_sf_sLstA', '_rg_sSchm', '_rg_sMdlTrg', '_rg_sMdlEdt', '_rg_rStrA', '_rg_rStrB', '_rg_rStrC', '_rg_rStrD', '_rg_rLstA', '_rg_rLstB', '_rg_rLstC', '_rg_rIntA', '_rg_rIntB', '_rg_rIntC', '_rg_rIntD', '_rg_rIntE', '_rg_rIntF', '_rg_rBoolA', '_rg_rBoolB', '_rg_rBoolC', '_rg_rBoolD', '_sf_rStrA', '_sf_rStrB', '_sf_rStrC', '_sf_rStrD', '_sf_rStrE', '_sf_rStrF', '_sf_rLstA', '_sf_rLstB', '_sf_rLstC', '_sf_rLstD', '_sf_rLstE', '_sf_rLstF', '_sf_rLstG', '_sf_rLstH', '_sf_rLstI', '_sf_rLstJ', '_sf_rIntA', '_sf_rIntB', '_sf_rIntC', '_sf_rIntD', '_sf_rIntE', '_sf_rIntF', '_sf_rIntG', '_sf_rIntH', '_sf_rIntI', '_sf_rIntJ', '_sf_rIntK', '_sf_rBoolA', '_sf_rBoolB', '_sf_rBoolC', '_sf_rBoolD', '_sf_rBoolE', '_sf_rBoolF')
    
    def __init__(self):
        self._sf_rBoolE = False
        self._rg_sMdlTrg = False
        self._rg_sMdlEdt = False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_make(self, vfsNm: str, dirNm: str, fldrNm: str) -> int:
        # FNC_ID=ST12-15976814147762V
        # SqtppFncs slots in use: (non-local)
        # returns: 8
        try:
            if not os.path.isdir(f'{SQTPP_MDL_DIR}/staqtapp1_2'): os.makedirs(f'{SQTPP_MDL_DIR}/staqtapp1_2')
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{vfsNm}.sqtpp', f':☆Staqtapp-v1.2.615\n|:{dirNm}<{fldrNm}>\n_|:{fldrNm}<sub-{fldrNm}>\n__|:sub-{fldrNm}<tqpt-{fldrNm},tpqt-{fldrNm},null>\n___|:tqpt-{fldrNm}<tqpt,null,n>:\nnull:\n___|:(tqpt-{fldrNm})\n___|:tpqt-{fldrNm}<tpqt,null,n>:\nnull:\n___|:(tpqt-{fldrNm})\n__|:(sub-{fldrNm})\n_|:({fldrNm})\n|:({dirNm})')
            self.sqtpp_tqpt_path(True, f'{vfsNm}:{dirNm}:{fldrNm}:sub-{fldrNm}:tqpt-{fldrNm}')
            return 8
        except Exception as err_vfs_make:
            self._sErr = f'staqtapp1.2 (vfs_make) error: {err_vfs_make}'
            return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_tqpt_file(self, isTqpt: bool):
        # FNC_ID=ST12-53391858780301V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rLstA, _sf_sQp, _sf_sSrc)
        # returns:
        # -1=path not found
        if isTqpt:
            self.sqtpp_vfs_pointer([f'|:{self._sf_rLstA[1]}<', f'_|:{self._sf_rLstA[2]}<', f'__|:{self._sf_rLstA[3]}<', f'___|:{self._sf_rLstA[4]}<'])
            if self._sf_rIntA != -1: self._sf_sQp = self._sf_sSrc[self._sf_rIntA:self._sf_sSrc.find('___|:',self._sf_rIntA+5)-2]
            else:
                return -1
        else:
            pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_tpqt_file(self, isTpqt: bool):
        # FNC_ID=ST12-90134370362249V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rLstA, _sf_sPq, _sf_sSrc)
        # returns:
        # -1=path not found
        if isTpqt:
            self._sf_rLstA[4] = self._sf_rLstA[4].replace('tqpt','tpqt')
            self.sqtpp_vfs_pointer([f'|:{self._sf_rLstA[1]}<', f'_|:{self._sf_rLstA[2]}<', f'__|:{self._sf_rLstA[3]}<', f'___|:{self._sf_rLstA[4]}<'])
            if self._sf_rIntA != -1: self._sf_sPq = self._sf_sSrc[self._sf_rIntA:self._sf_sSrc.find('___|:',self._sf_rIntA+5)-2]
            else:
                return -1
        else:
            pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_folder_write_dvcpn(self, dvAddrPntr: str):
        # FNC_ID=ST12-93593218160027V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_sRplc, _sf_sSrc, _sf_sVfsFldr)
        # returns: (none)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_sub_file(self, isAddFl: bool, isRplcFl: bool, flNm: str, src: str):
        # FNC_ID=ST12-93830098777343V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rStrA, _sf_sRtrn, _sf_sSrc, _sf_sVfs, _sf_sVfsFldr)
        # returns:
        # -1=cannot locate sub-folder
        # -2=sub file not found
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_set_vfs_file(self):
        # FNC_ID=ST12-20927427257479V
        # SqtppFncs slots in use: (_sf_rLstA, _sf_sSrc, _sf_sVfs, _sf_sVfsFldr)
        # returns:
        # -1=false tqpt path
        self.sqtpp_tqpt_path(False, None)
        if len(self._sf_sSrc) > 0:
            self._sf_rLstA = self._sf_sSrc.split(':')
            self._sf_sVfs = self._sf_rLstA[0]
            self._sf_sVfsFldr = self._sf_rLstA[2]
            self.sqtpp_file(False, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', None)
            return 1
        else:
            return -1
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_change_vfs_path(self, flNm: str, dirNm: str, fldrNm: str):
        # FNC_ID=ST12-92351394595405U
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rStrA)
        # returns: (none)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_pointer(self, pthLst: list):
        # FNC_ID=ST12-78442583569511V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_sSrc)
        # returns:
        # -1=path not found
        for pth in range(len(pthLst)):
            if pth < 1: self._sf_rIntA = self._sf_sSrc.find(pthLst[pth])
            else: self._sf_rIntA = self._sf_sSrc.find(pthLst[pth], self._sf_rIntA+1)
            if self._sf_rIntA < 0:
                break
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vfs_display_file_struct(self):
        # FNC_ID=ST12-60987808146267
        # SqtppFncs slots in use: (non-local)
        # returns:
        pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vital_vars(self, mode: str, cnfg: str, cnts: list):
        # <<<
        # Normal Modes:
        #  "r:vitalvar name", returns the vitalvar values(auto-updates the vv from a time check if then set time has set or passed set)
        #  "w:vitalvar name", @cnts list expected: Elmnt1="year,month,day,#|##:##,am|pm" Elmnt2="file contents" Elmnt3=config (OPTIONAL, Elmnt4=sub-config)
        # Edit Modes:
        #  "c:vitalvar name", @cnfg expected having comma separated types associated for vitalvar updates via vfs file contents("str,list,set,int,float")
        #  "s:vitalvar name", @cnfg expected as sub-config filtering, Example: "str:xO9K,list:84-2-1024,set:1024-42-1,int:2&4,float:4&2"
        #  "t:vitalvar name", @cnts list expected: Elmnt1="year,month,day,#|##:##,am|pm" (OPTIONAL, Elmnt2=file content[*appended*] Elmnt3=config Elmnt4=sub-config)
        #  "m:vitalvar name A:vitalvar name B", @cnfg & @cnts both ignored on merge, vitalvar B's set time is the then established set update time
        #  "v:vitalvar name A:vitalvar name B", moves the merged vitalvar to staqtapp's registry, vitalvar A's set time is the then established set update time
        #  "d:vitalvar name", removes the vitalvar from current set path .sqtpp vfs file or staqtapp's outer registry module if found
        try:
            pass
        except Exception as err_vital_vars:
            pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_byte_vars(self, mode: int, varNm: str, blLst: list):
        # FNC_ID=ST12-71117222739577P
        # SqtppFncs slots in use: (_sf_rLstA, _sf_rStrA, _sf_sQp, _sf_sSrc, _sf_sVd, _sf_sVfs)
        # modes:
        # 1=write
        # 2=read: return boolean list
        # 3=read: return RLE tuples list
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=@varNm is duplicate
        # -4=@varNm not found in tqpt stack
        # -5=@mode of invalid int arg
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    if mode == 1:
                        if not self.sqtpp_var_value(varNm):
                            self.sqtpp_delta_prle_encd(blLst)
                            self._sf_rStrA = base64.b64encode(pickle.dumps(self._sf_rLstA)).decode('utf-8')
                            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc.replace(f'{self._sf_sQp}:\n', f'{self._sf_sQp}\n{varNm}<@q*p({self._sf_rStrA}):>:\n'))
                            self._sf_sSrc = None
                            self._sf_sQp = None
                            return None
                        else:
                            return -3
                    elif mode == 2 or mode == 3:
                        self._sf_sVd = re.findall(r'(?s:)'+re.escape(varNm)+r'<@q\*p\(.*?\):>', self._sf_sQp)
                        if len(self._sf_sVd) > 0:
                            self._sf_sVd = self._sf_sVd[0].replace(f'{varNm}<','')
                            self._sf_sVd = self._sf_sVd[0:len(self._sf_sVd)-1]
                            self._sf_sVd = self._sf_sVd.replace('@q*p(',"").replace('):',"")
                            if mode == 2: self.sqtpp_delta_prle_decd(pickle.loads(base64.b64decode(self._sf_sVd.encode('utf-8'))))
                            else: self._sf_rLstA = pickle.loads(base64.b64decode(self._sf_sVd.encode('utf-8')))
                            self._sf_sSrc = None
                            self._sf_sQp = None
                            return self._sf_rLstA
                        else:
                            return -4
                    else:
                        return -5
                else:
                    return -2
            else:
                return -1
        except Exception as err_byte_vars:
            self._sErr = f'staqtapp1.2 (corevar) error: {err_byte_vars}'
            return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_add(self, isStlkVar: bool, varNm: str, varDat: str):
        # FNC_ID=ST12-87562753599213P
        # SqtppFncs slots in use: (_sf_rBoolE, _sf_rIntA, _sf_sQp, _sf_sSrc, _sf_sVfs)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_applied_vars(self, varNms: list, varDts: list, varLks):
        # FNC_ID=ST12-61455026636200P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rBoolC, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rStrA, _sf_rStrD, _sf_sPq, _sf_sQp, _sf_sSrc, _sf_sVfs)
        # returns:
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        # -3=newline chars found
        # -4=no @qp(...): data declaring found
        # -5=no closing ): for @qp( data tag found
        # -6=tpqt lock name for env-var invalid chars
        # -7=format for add locks invalid, missing :
        try:
            if self.sqtpp_set_vfs_file() == 1:
                self._sf_rLstC = self._sf_rLstA
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rBoolB = False
                    self._sf_rIntD = len(varNms)
                    self._sf_rStrD = self._sf_sQp
                    for self._sf_rIntC in range(self._sf_rIntD):
                        self._sf_rBoolA = False
                        if self._sf_rIntC < len(varDts):
                            if varDts[self._sf_rIntC] != None and len(varDts[self._sf_rIntC]) > 0:
                                self._sf_rIntE = self.sqtpp_tqpt_spdr(True, False, None, varDts[self._sf_rIntC])
                                if self._sf_rIntE == 2:
                                    return -3
                                elif self._sf_rIntE == 6:
                                    return -4
                                elif self._sf_rIntE == 7:
                                    return -5
                            else: self._sf_rBoolA = True
                        else: self._sf_rBoolA = True
                        if not self._sf_rBoolA:
                            self._sf_rBoolB = True
                            self._sf_sQp = f'{self._sf_sQp}\n{varNms[self._sf_rIntC]}<{varDts[self._sf_rIntC]}>'
                        else:
                            self._sf_rBoolB = True
                            self._sf_sQp = f'{self._sf_sQp}\n{varNms[self._sf_rIntC]}<@qp(null):>'
                    if self._sf_rBoolB:
                        self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_rStrD}:\n', f'{self._sf_sQp}:\n')
                        self._sf_rBoolC = False
                        self._sf_rStrD = None
                        self._sf_sQp = None
                        if varLks != None:
                            self._sf_rIntB = len(varLks)
                            self._sf_rBoolC = True
                            if self._sf_rIntB > 0:
                                self._sf_rLstA = self._sf_rLstC
                                if self.sqtpp_vfs_tpqt_file(True) != -1:
                                    self._sf_rStrA = self._sf_sPq
                                    for self._sf_rIntA in range(self._sf_rIntB):
                                        if varLks[self._sf_rIntA].find(':') > -1:
                                            self._sf_rLstA = varLks[self._sf_rIntA].split(':')
                                            self._sf_rLstA[0] = self._sf_rLstA[0].replace(' ','')
                                            if self.sqtpp_chars_check(2, self._sf_rLstA[0]):
                                                if self._sf_rLstA[1].find(',') > -1:
                                                    self._sf_rLstB = self._sf_rLstA[1].split(',')
                                                    self._sf_rIntD = len(self._sf_rLstB)
                                                    self._sf_rIntC = 0
                                                    while self._sf_rIntC < self._sf_rIntD:
                                                        self._sf_rLstB[self._sf_rIntC] = self._sf_rLstB[self._sf_rIntC].replace(' ','')
                                                        if not self.sqtpp_chars_check(2, self._sf_rLstB[self._sf_rIntC]):
                                                            return -6
                                                        self._sf_rIntC+=1
                                                else:
                                                    self._sf_rLstB = [self._sf_rLstA[1].replace(' ','')]
                                                    if not self.sqtpp_chars_check(2, self._sf_rLstB[0]):
                                                        return -6
                                                if len(self._sf_rLstB) > 1: self._sf_sPq = self._sf_sPq + '\n<:' + self._sf_rLstA[0] + '=\n' + '\n'.join(self._sf_rLstB) + ':>'
                                                else: self._sf_sPq = self._sf_sPq + '\n<:' + self._sf_rLstA[0] + '=\n' + self._sf_rLstB[0] + ':>'
                                            else:
                                                return -6
                                        else:
                                            return -7
                                else:
                                    return -2
                        if self._sf_rBoolC:
                            if self._sf_rStrA != self._sf_sPq:
                                self._sf_sPq = f'{self._sf_sPq}:'
                                self._sf_sPq = self._sf_sPq.replace('::',':')
                                self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sPq)
                            self._sf_sPq = None
                        self._sf_rStrA = None
                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                        self._sf_sSrc = None
                        return 8
                else:
                    return -2
            else:
                return -1
        except Exception as err_applied_vars:
            self._sErr = f'staqtapp1.2 (appvar) error: {err_applied_vars}'
            return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_list(self) -> list:
        # FNC_ID=ST12-13768462694222U
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_sQp, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_list_lambda(self, cmpltLmb: bool):
        # FNC_ID=ST12-95170347920087U
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_sQp)
        # returns: list
        # -1=empty vfs path settings file
        # -2=invalid vfs path
        try:
            if self.sqtpp_set_vfs_file() == 1:
                if self.sqtpp_vfs_tqpt_file(True) != -1:
                    self._sf_rLstA = re.findall(r'st1_atlaspice_.*?<@q\|p.*?\):>', self._sf_sQp)
                    self._sf_rIntB = len(self._sf_rLstA)
                    if self._sf_rIntB > 0:
                        self._sf_rLstC = []
                        for self._sf_rIntA in range(self._sf_rIntB):
                            self._sf_rLstB = re.findall(r'lambda(?:\s*[a-zA-Z_][a-zA-Z_0-9]*(?:\s*,\s*[a-zA-Z_][a-zA-Z_0-9]*)*)?\s*:\s*.+', self._sf_rLstA[self._sf_rIntA])
                            if len(self._sf_rLstB) > 0:
                                if not cmpltLmb:
                                    self._sf_rLstD = re.findall(r'da.*?:', self._sf_rLstB[0])
                                    self._sf_rLstD[0] = self._sf_rLstD[0].replace('da','').replace(':','')
                                    self._sf_rLstE = re.findall(r'\(.*?=', self._sf_rLstA[self._sf_rIntA])
                                    self._sf_rLstE[0] = self._sf_rLstE[0].replace('(','').replace('=','')
                                    self._sf_rLstC.append(f'@.:{self._sf_rLstE[0].replace(" ","")}')
                                    if self._sf_rLstD[0].find(',') > -1:
                                        self._sf_rLstD = self._sf_rLstD[0].split(',')
                                        self._sf_rIntD = len(self._sf_rLstD)
                                        for self._sf_rIntC in range(self._sf_rIntD):
                                            self._sf_rLstC.append(f'{self._sf_rLstD[self._sf_rIntC].replace(" ","")}=')
                                    else:
                                        self._sf_rLstD[0] = self._sf_rLstD[0].replace(' ','')
                                        if len(self._sf_rLstD[0]) > 0: self._sf_rLstC.append(self._sf_rLstD[0])
                                else:
                                    self._sf_rLstF = re.findall(r'\(.*?\):>', self._sf_rLstA[self._sf_rIntA])
                                    self._sf_rLstF[0] = self._sf_rLstF[0].replace("(","").replace(":)>","")
                                    self._sf_rLstC.append(self._sf_rLstF[0].replace('):>',''))
                        if cmpltLmb:
                            return self._sf_rLstC
                        else:
                            return ','.join(self._sf_rLstC)
                    else:
                        return []
                else:
                    return -2
            else:
                return -1
        except Exception as err_list_lambda:
            self._sErr = f'staqtapp1.2 (lambdalist) error: {err_list_lambda}'
            return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_join(self, newVarNm: str, varNms: list):
        # FNC_ID=ST12-49975252842406P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_sQp, _sf_sSrc, _sf_sVd, _sf_sVfs, _sf_sVfsFldr)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_rename_stx(self, varNm: str, newVarNm):
        # FNC_ID=ST12-74328682109875S
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_sPq, _sf_sQp, _sf_sSrc, _sf_sVd, _sf_sVfs)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_change(self, varNm: str, newVarDt: str):
        # FNC_ID=ST12-29435733185667P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rBoolC, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_sPq, _sf_sQp, _sf_sRtrn, _sf_sSrc, _sf_sVd, _sf_sVfs, _sf_sVfsFldr)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_remove(self, varNm: str):
        # FNC_ID=ST12-78916780048877P
        # SqtppFncs slots in use: (_sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_sPq, _sf_sQp, _sf_sSrc, _sf_sVfs, _sf_sVfsFldr)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_darkvar(self):
        # FNC_ID=ST12-68028377117105D
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rStrA, _sf_sBoolCxv, _sf_sBoolX, _sf_sDv, _sf_sLstX, _sf_sPq, _sf_sQp, _sf_sQpRplcX, _sf_sSrc, _sf_sStrX, _sf_sVd, _sf_sVn)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_darkvar_menorah_outer_loop_resum(self, tetBase: int, vssvAddr: str) -> str:
        # FNC_ID=ST12-61233740348884D
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rIntI, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_sDv, _sf_sStrX)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_revar(self, isCurrVfsPth: bool, newVfsFlNm: str, newVfsDirNm: str, newVfsFldrNm: str):
        # FNC_ID=ST12-41344068606299V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rStrA, _sf_sPq, _sf_sQp, _sf_sSrc, _sf_sVfs)
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
                                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{newVfsFlNm}.sqtpp', f':☆Staqtapp-v1.2.615\n|:{newVfsDirNm}<{newVfsFldrNm}>\n_|:{newVfsFldrNm}<sub-{newVfsFldrNm}>\n__|:sub-{newVfsFldrNm}<tqpt-{newVfsFldrNm},tpqt-{newVfsFldrNm},null>\n___|:tqpt-{newVfsFldrNm}<tqpt,null,n>:\nnull\n{self._sf_rLstC}:\n___|:(tqpt-{newVfsFldrNm})\n{self._sf_sPq}:\n___|:(tpqt-{newVfsFldrNm})\n__|:(sub-{newVfsFldrNm})\n_|:({newVfsFldrNm})\n|:({newVfsDirNm})')
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_loadvar(self, isAllNmbrs: bool, varNm: str, mode):
        # FNC_ID=ST12-32234428100934U
        # SqtppFncs slots in use: (_sf_rLstA, _sf_sPq, _sf_sQp, _sf_sRtrn, _sf_sSrc, _sf_sVd)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_spok_mv_tree(self, trNm: str, initPthLst: list):
        # FNC_ID=ST12-72756760162526S
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_sQp, _sf_sSrc, _sf_sVfs)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_spok_mv_tree_add_branch(self, trNm: str, smvBrncId, newSmvBrnchId, newSmvBrnchVl):
        # FNC_ID=ST12-91239509636329S
        # SqtppFncs slots in use: (_sf_sQp, _sf_sRtrn, _sf_sSrc, _sf_sVd, _sf_sVfs)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_spok_mv_tree_get_branch(self, isAlf: bool, trNm: str, brnchId):
        # FNC_ID=ST12-83205842907837S
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_sVd)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_spok_mv_tree_get_branch_alf(self, brnchId, trSrc):
        # FNC_ID=ST12-28502992416320S
        # SqtppFncs slots in use: (_sf_rBoolB, _sf_rBoolC, _sf_rBoolD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rLstC, _sf_rStrC, _sf_rStrD, _sf_rStrE)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_spok_mv_tree_get_branch_ohm(self, isClr: bool, isOhm: bool, trSrc):
        # FNC_ID=ST12-84970566104521S
        # SqtppFncs slots in use: (_sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_sQp, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_var_stalk(self, varNm: str, varDat: str):
        # FNC_ID=ST12-35908606707598P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_sPq, _sf_sQp, _sf_sQpRplcX, _sf_sSrc, _sf_sVd, _sf_sVfs, _sf_sVfsFldr, _sf_sVn)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_locate_var_stx(self, varNmLst: list, stlkVarNm: str):
        # FNC_ID=ST12-76968457094376S
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntD, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_sQp, _sf_sSrc, _sf_sVd)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_delta_prle_encd(self, blLst: list):
        # FNC_ID=ST12-60575485348008P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rLstA, _sf_rLstB)
        # returns: (none)
        self._sf_rLstA = [1 if self._sf_rIntA else 0 for self._sf_rIntA in blLst]
        self._sf_rLstB = [self._sf_rLstA[0]]
        self._sf_rIntB = len(self._sf_rLstA)
        self._sf_rIntA = 1
        while self._sf_rIntA < self._sf_rIntB:
            self._sf_rLstB.append(self._sf_rLstA[self._sf_rIntA] ^ self._sf_rLstA[self._sf_rIntA-1])
            self._sf_rIntA+=1
        self._sf_rIntB = len(self._sf_rLstB)
        self._sf_rLstA = []
        self._sf_rIntC = 1
        for self._sf_rIntA in range(1, self._sf_rIntB):
            if self._sf_rLstB[self._sf_rIntA] == self._sf_rLstB[self._sf_rIntA-1]: self._sf_rIntC+=1
            else:
                self._sf_rLstA.append((self._sf_rLstB[self._sf_rIntA-1], self._sf_rIntC))
                self._sf_rIntC = 1
        self._sf_rLstA.append((self._sf_rLstB[self._sf_rIntA-1], self._sf_rIntC))
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_delta_prle_decd(self, rleLst):
        # FNC_ID=ST12-77666565324124P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB)
        # returns: (none)
        self._sf_rLstA = []
        for self._sf_rIntA, self._sf_rIntB in rleLst: self._sf_rLstA.extend([self._sf_rIntA] * self._sf_rIntB)
        self._sf_rLstB = [self._sf_rLstA[0]]
        self._sf_rIntB = len(self._sf_rLstA)
        self._sf_rIntA = 1
        while self._sf_rIntA < self._sf_rIntB:
            self._sf_rLstB.append(self._sf_rLstB[self._sf_rIntA-1] ^ self._sf_rLstA[self._sf_rIntA])
            self._sf_rIntA+=1
        self._sf_rLstA = [self._sf_rIntA > 0 for self._sf_rIntA in self._sf_rLstB]
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_var_key(self, varNm: str, fncNm: str) -> bool:
        # FNC_ID=ST12-15869682128595U
        # SqtppFncs slots in use: (_sf_rLstA, _sf_sPq)
        # returns:
        # -1=invalid vfs path
        # -2=bad path in vfs path setting file
        # -3=@varNm was not found in tpqt vfs file
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_list_lock(self, varNm: str) -> list:
        # FNC_ID=ST12-28413947443746U
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rLstA, _sf_sPq, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_locate_var_data(self, isRgx: bool, varNmLst: list, srch: str):
        # FNC_ID=ST12-61257731648827U
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_sVd)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_locate_var(self, rmv: bool, varNm: str):
        # FNC_ID=ST12-60961205499908U
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_sQp, _sf_sSrc)
        # returns:
        # -1=invalid vfs path
        # -3=empty vfs path settings file
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_limit_var_domain(self, varNm: str, fncNm):
        # FNC_ID=ST12-62068375105089P
        # SqtppFncs slots in use: (_sf_rStrA, _sf_rStrB, _sf_sPq, _sf_sQp, _sf_sRtrn, _sf_sSrc, _sf_sVfsFldr)
        # returns:
        # -1=empty vfs path stg file
        # -2=@varNm not found in tqpt vars source
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_tqpt_path(self, isSetPth: bool, pth: str):
        # FNC_ID=ST12-49796016410710U
        # SqtppFncs slots in use: (non-local)
        # returns: none
        if isSetPth: self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', pth)
        else: self.sqtpp_file(False, f'{SQTPP_MDL_DIR}/staqtapp1_2/sqtpp1_2.stg', None)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_file(self, isWrt: bool, pth: str, src: str):
        # FNC_ID=ST12-20194103037310U
        # SqtppFncs slots in use: (_sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_var_value(self, varNm: str) -> bool:
        # FNC_ID=ST12-91960815315016P
        # SqtppFncs slots in use: (_sf_sQp, _sf_sVd)
        # returns: True or False
        self._sf_sVd = re.findall(r'(?s:)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
        if len(self._sf_sVd) > 0:
            self._sf_sVd = self._sf_sVd[0].replace(f'{varNm}<','')
            self._sf_sVd = self._sf_sVd[0:len(self._sf_sVd)-1]
            return True
        else:
            return False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_var_change(self, varNm: str, varDat: str):
        # FNC_ID=ST12-18072555690287P
        # SqtppFncs slots in use: (_sf_rStrA, _sf_sQp, _sf_sSrc, _sf_sVfs)
        # returns: none
        rtrn = re.findall(r'(?s:)'+re.escape(varNm)+r'<@qp\(.*?\):>', self._sf_sQp)
        if len(rtrn) > 0:
            self._sf_rStrA = self._sf_sQp
            self._sf_sQp = self._sf_sQp.replace(f'{rtrn[0]}', f'{varNm}<{varDat}>')
            self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sQp)
            self._sf_rStrA = None
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_var_remove(self, varNmLst: list):
        # FNC_ID=ST12-21570101576092P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_sQp)
        # returns: none
        self._sf_rIntB = len(varNmLst)
        for self._sf_rIntA in range(self._sf_rIntB):
            self._sf_rLstA = re.findall(r'(?s:.)'+re.escape(varNmLst[self._sf_rIntA])+r'<@qp\(.*?\):>', self._sf_sQp)
            if len(self._sf_rLstA) > 0: self._sf_sQp = self._sf_sQp.replace(self._sf_rLstA[0],'')
        self._sf_sQp = self._sf_sQp.replace('):>\n:','):>:')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_silent_lock_add(self, varNm: str, lckNmLst: list):
        # FNC_ID=ST12-50629079615163P
        # SqtppFncs slots in use: (_sf_rLstA, _sf_sPq, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_silent_lock_remove(self, isStlkVar: bool, varNmLst: list):
        # FNC_ID=ST12-49736634702942P
        # SqtppFncs slots in use: (_sf_sBoolX, _sf_sLstX, _sf_sPq, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_svvs_list(self, varNm: str):
        # FNC_ID=ST12-20355238173214V
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA)
        # returns:
        # -8=no found svvs commons stalk-entry element list for @varNm
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_svvs_next_int(self) -> int:
        # FNC_ID=ST12-40663287376385V
        # SqtppFncs slots in use: (_sf_rLstA, _sf_sIntX, _sf_sLstX)
        # returns: (int)
        xRtrn = 1
        for x in range(len(self._sf_rLstA)):
            self._sf_sLstX = self._sf_rLstA[x].split('_')
            self._sf_sIntX = int(self._sf_sLstX[len(self._sf_sLstX)-1])
            if  self._sf_sIntX > xRtrn: xRtrn = self._sf_sIntX
        xRtrn+=1
        return xRtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vssv_menorah_cxv_rod(self, adrsNws: str, adrsPrv: str):
        # FNC_ID=ST12-67730865259864D
        # SqtppFncs slots in use: (_sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rLstA, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_rStrD, _sf_rStrE, _sf_rStrF, _sf_sIntX, _sf_sRplc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_combined_addr_darkvar_search(self, cmbAddr: str, srchWndw: str):
        # FNC_ID=ST12-56307656299472D
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_sLstX)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_plndrm(self, ttBranch: int) -> int:
        # FNC_ID=ST12-58878149731260U
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_sDv)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_tqpt_spdr(self, isRdr: bool, isAllNmbrs: bool, callFnc: str, src: str):
        # FNC_ID=ST12-34970343946932P
        # SqtppFncs slots in use: (_sf_rBoolE, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_sQp, _sf_sSrc)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lambda_scan_write(self, src: str) -> bool:
        # FNC_ID=ST12-23904241191810P
        # SqtppFncs slots in use: (_sf_rStrA, _sf_sLstA, _sf_sQp, _sf_sSrc, _sf_sVfs)
        # returns: (boolean)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_del_locks(self, isDelAll: bool, varNm:str, fncNm):
        # FNC_ID=ST12-81395077548719P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_sPq, _sf_sSrc, _sf_sVfs)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_vars_run_lambda(self, lmbNm: str, lmbPrms: list):
        # FNC_ID=ST12-35405944673660P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rLstA, _sf_rStrA, _sf_sLstX, _sf_sQp, _sf_sRtrn, _sf_sSrc, _sf_sStrX)
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
                    self._sf_rLstA = re.findall(r'st1_atlaspice_.*?<@q\|p\('+re.escape(lmbNm)+r'.*?\):>', self._sf_sQp)
                    if len(self._sf_rLstA[0]) > 0:
                        self._sf_sSrc = None
                        self._sf_sQp = None
                        self._sf_sStrX = re.findall(r'st1_atlaspice_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', self._sf_rLstA[0])
                        if len(self._sf_sStrX[0]) > 0: self._sf_sStrX = self._sf_sStrX[0].replace('st1_atlaspice_','')
                        else: self._sf_sStrX = 'unknown ctmn number'
                        self._sf_sRtrn = self.sqtpp_lambda_spdr()
                        if self._sf_sRtrn == -1:
                            return -4
                        elif self._sf_sRtrn == 1: self._sf_rBoolA = True
                        else: self._sf_rBoolA = False
                        if self._sf_rBoolA:
                            if len(lmbPrms) == len(self._sf_rLstA):
                                self._sf_sLstX = []
                                self._sf_rIntB = len(lmbPrms)
                                for self._sf_rIntA in range(self._sf_rIntB):
                                    if self._sf_rIntA > 0 and not self._sf_rBoolB:
                                        break
                                    self._sf_rBoolB = False
                                    self._sf_rIntC = 0
                                    while self._sf_rIntC < self._sf_rIntB:
                                        if lmbPrms[self._sf_rIntA].find(f'{self._sf_rLstA[self._sf_rIntC]}=') > -1:
                                            self._sf_rStrA = lmbPrms[self._sf_rIntA].split('=')
                                            self._sf_sLstX.append(self._sf_rStrA[0])
                                            self._sf_rBoolB = True
                                            break
                                        self._sf_rIntC+=1
                                if not self._sf_rBoolB:
                                    return -6
                            else:
                                return -5
                        return self.sqtpp_lambda_lambda_lambda_clsr(lmbNm, lmbPrms)
                    else:
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as err_vars_run_lambda:
            self._sErr = f'staqtapp1.2 (vars_run_lambda) error: {err_vars_run_lambda}'
            return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lambda_lambda_lambda_clsr(self, lmbNm: str, lmbPrms: list):
        # FNC_ID=ST12-60560777779500P
        # SqtppFncs slots in use: (_sf_rBoolC, _sf_rLstB, _sf_rStrA, _sf_rStrD, _sf_sStrX)
        # returns: (lambda function results)
        if os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_LMB.py'):
            with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_LMB.py', 'r') as lllfObjRdr: self._sf_rStrA = lllfObjRdr.read()
            self._sf_rLstB = re.findall(r'\#CTMN-LLL<[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]\:' + re.escape(lmbNm) + r'>', self._sf_rStrA)
            if len(self._sf_rLstB) > 0: self._sf_rBoolC = False
            else:
                self._sf_rStrA = self._sf_rStrA.replace('\n\ndef sqtpp_lll_run(lName: str, lPrms: list):\n    lllCls = SqtppLLL_Joints()\n    return lllCls.sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run(lName, lPrms)',"")
                self.sqtpp_lambda_lambda_lambda_clsr_remap_slots(False)
                self._sf_rStrD = self._sf_rStrD.replace("):>","")
                with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_LMB.py', 'w') as lllfObjA_wrt: lllfObjA_wrt.write(self._sf_rStrA + '\n    ' + '#CTMN-LLL<' + self._sf_sStrX + ':' + lmbNm + '>\n    ' + lmbNm + ' = ' + self._sf_rStrD + '\n\ndef sqtpp_lll_run(lName: str, lPrms: list):\n    lllCls = SqtppLLL_Joints()\n    return lllCls.sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run(lName, lPrms)')
                self._sf_rBoolC = True
        else:
            self._sf_rLstB = ['# This py-module is auto-generated by the Staqtapp1.2 vfs env-var library for lambda functions use. Edit at your own risk.\n\nimport math\n\nclass SqtppLLL():\n\n    __slots__ = ()\n\n    def __init__(self):\n        pass\n\n\nclass SqtppLLL_Joints(SqtppLLL):\n\n    __slots__ = (']
            self.sqtpp_lambda_lambda_lambda_clsr_remap_slots(True)
            self._sf_rLstB.append('\n\n    def __init__(self):\n        pass\n#_______________________________________________________________________________________')
            self._sf_rLstB.append('\n    def sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run(self, lmbNm: str, lmbVls: list):\n        self._lll_set_n = set("1234567890")\n        try:\n            self._lll_lst_d = [None,len(lmbVls),None,None,None,None]\n            for self._lll_lst_d[0] in range(self._lll_lst_d[1]):\n                self._lll_lst_a = lmbVls[self._lll_lst_d[0]].split("=")\n                if len(self._lll_lst_a) == 2:\n                    self._lll_lst_a[0] = self._lll_lst_a[0].replace(" ","")')
            self._sf_rLstB.append('\n                    self._lll_lst_a[1] = self._lll_lst_a[1].replace(" ","")\n                    if self._lll_lst_a[1].find(",") > -1:\n                        self._lll_lst_b = self._lll_lst_a[1].split(",")\n                        self._lll_lst_d[3] = len(self._lll_lst_b)\n                        self._lll_lst_c = []')
            self._sf_rLstB.append('\n                        for self._lll_lst_d[2] in range(self._lll_lst_d[3]):\n                            self._lll_lst_d[4] = True\n                            for self._lll_lst_d[5] in self._lll_lst_b[self._lll_lst_d[2]]:\n                                if set(self._lll_lst_d[5]).issubset(self._lll_set_n):')
            self._sf_rLstB.append('\n                                    pass\n                                else:\n                                    self._lll_lst_d[4] = False\n                                    break\n                            if not self._lll_lst_d[4]: self._lll_lst_c.append(self._lll_lst_b[self._lll_lst_d[2]])')
            self._sf_rLstB.append('\n                            else: self._lll_lst_c.append(int(self._lll_lst_b[self._lll_lst_d[2]]))\n                        setattr(self, self._lll_lst_a[0], self._lll_lst_c)\n                    else:\n                        self._lll_lst_d[4] = True\n                        for self._lll_lst_d[5] in self._lll_lst_a[1]:\n                            if set(self._lll_lst_d[5]).issubset(self._lll_set_n):')
            self._sf_rLstB.append('\n                                pass\n                            else:\n                                self._lll_lst_d[4] = False\n                                break\n                        if not self._lll_lst_d[4]: setattr(self, self._lll_lst_a[0], self._lll_lst_a[1])\n                        else: setattr(self, self._lll_lst_a[0], int(self._lll_lst_a[1]))')
            self._sf_rLstB.append('\n                else:\n                    raise AttributeError(f"sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run error: lambda {lmbNm} param ({lmbVls[self._lll_lst_d[0]]}) invalid param declaring, see lambdavar() description")')
            self._sf_rLstB.append('\n            self._lll_set_n = getattr(self, lmbNm)\n            return self._lll_set_n()\n        except Exception as e_set_slots_attrs:\n            raise AttributeError(f"sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run error: {e_set_slots_attrs}")')
            self._sf_rLstB.append('\n#_______________________________________________________________________________________\n    #WE OWN THE SPICE, NOT ARTIFICIAL INTELLIGENCE:\n\n    #CTMN-LLL<' + self._sf_sStrX + ':' + lmbNm + '>\n')
            self._sf_rLstB.append(f'    {lmbNm} = {self._sf_rStrD.replace("):>","")}')
            self._sf_rLstB.append('\n\ndef sqtpp_lll_run(lName: str, lPrms: list):\n    lllCls = SqtppLLL_Joints()\n    return lllCls.sqtpp_lambda_lambda_lambda_set_slots_attrs_and_run(lName, lPrms)')
            with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_LMB.py', 'w') as lllfObjN_wrt: lllfObjN_wrt.write(''.join(self._sf_rLstB))
            self._sf_rBoolC = True
            self._sf_rLstB = None
        if not self._sf_rBoolC:
            import sqtpp1_2_LMB
        else:
            if 'sqtpp1_2_LMB' in sys.modules:
                importlib.reload(sqtpp1_2_LMB)
                sys.modules.pop('sqtpp1_2_LMB', None)
            else:
                import sqtpp1_2_LMB
        return sqtpp1_2_LMB.sqtpp_lll_run(lmbNm, lmbPrms)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lambda_lambda_lambda_clsr_remap_slots(self, isNewlllMdl: bool):
        # FNC_ID=ST12-81604510638526P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rBoolC, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rStrA, _sf_rStrB, _sf_rStrD, _sf_rStrE, _sf_sLstX)
        # returns: (none)
        if self._sf_rBoolA:
            if isNewlllMdl:
                self._sf_rLstC = []
                for self._sf_rIntA in range(len(self._sf_rLstA)): self._sf_rLstC.append("'" + self._sf_rLstA[self._sf_rIntA] + "'")
                self._sf_rLstB.append(f"'_lll_set_n','_lll_lst_a','_lll_lst_b','_lll_lst_c','_lll_lst_d',{','.join(self._sf_rLstC)})")
            else:
                self._sf_rLstC = re.findall(r'__slots__.*?\)', self._sf_rStrA)
                self._sf_rLstC = self._sf_rLstC[1]
                self._sf_rStrB = self._sf_rLstC
                self._sf_rLstC = self._sf_rLstC.replace('__slots__ = (',"")
                self._sf_rLstC = self._sf_rLstC.replace(')','')
                self._sf_rLstC = self._sf_rLstC.replace("'",'')
                self._sf_rLstC = self._sf_rLstC.split(',')
                self._sf_rIntB = len(self._sf_rLstC)
                self._sf_rBoolC = True
                for self._sf_rIntA in range(self._sf_rIntB):
                    self._sf_rBoolB = True
                    self._sf_rIntC = 0
                    while self._sf_rIntC < len(self._sf_rLstA):
                        if self._sf_rLstC[self._sf_rIntA] == self._sf_rLstA[self._sf_rIntC]:
                            self._sf_rBoolB = False
                            break
                        self._sf_rIntC+=1
                    if not self._sf_rBoolB:
                        if len(self._sf_rLstA) > 1: self._sf_rLstA.pop(self._sf_rIntC)
                        else:
                            self._sf_rBoolC = False
                            break
                if self._sf_rBoolC:
                    self._sf_rLstD = []
                    for self._sf_rIntA in range(len(self._sf_rLstA)): self._sf_rLstD.append("'" + self._sf_rLstA[self._sf_rIntA] + "'")
                    self._sf_rStrE = f'__slots__ = ({self._sf_rStrB.replace("__slots__ = (","")},{",".join(self._sf_rLstD)}'
                    self._sf_rStrE = self._sf_rStrE.replace(')','')
                    self._sf_rStrA = self._sf_rStrA.replace(self._sf_rStrB, f'{self._sf_rStrE})')
                self._sf_rLstA = self._sf_sLstX
            self._sf_rLstE = ''.join(self._sf_rLstE)
            self._sf_rStrD = self._sf_rStrD.replace(self._sf_rLstE, '')
            self._sf_rStrD = f'~~~~~{self._sf_rStrD}~~~~~'
            self.sqtpp_lambda_lambda_rplc()
            self._sf_rStrD = f'lambda self: {self._sf_rStrD}'
        else:
            if isNewlllMdl: self._sf_rLstB.append("'_lll_set_n','_lll_lst_a','_lll_lst_b','_lll_lst_c','_lll_lst_d')")
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lambda_lambda_rplc(self):
        # FNC_ID=ST12-35098889431831P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rLstA, _sf_rLstD, _sf_rLstF, _sf_rStrD)
        # returns: (none)
        self._sf_rLstF = set('_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        self._sf_rIntB = len(self._sf_rLstA)
        for self._sf_rIntA in range(self._sf_rIntB):
            self._sf_rIntC = 5
            self._sf_rIntE = 5
            while self._sf_rIntC < len(self._sf_rStrD):
                self._sf_rIntE = self._sf_rIntC
                if self._sf_rIntC >= len(self._sf_rStrD)-4:
                    break
                else:
                    self._sf_rIntC = self._sf_rStrD.find(self._sf_rLstA[self._sf_rIntA], self._sf_rIntC)
                if self._sf_rIntC > -1:
                    self._sf_rIntD = self._sf_rIntC+len(self._sf_rLstA[self._sf_rIntA])
                    if not set(self._sf_rStrD[self._sf_rIntC-1]).issubset(self._sf_rLstF) and not set(self._sf_rStrD[self._sf_rIntD]).issubset(self._sf_rLstF):
                        self._sf_rLstD = [self._sf_rStrD[0:self._sf_rIntC], self._sf_rStrD[self._sf_rIntD:len(self._sf_rStrD)]]
                        self._sf_rStrD = f'{self._sf_rLstD[0]}self.{self._sf_rLstA[self._sf_rIntA]}{self._sf_rLstD[1]}'
                        self._sf_rIntC = self._sf_rIntD+5
                    else: self._sf_rIntC = self._sf_rIntE+1
                else: self._sf_rIntC = self._sf_rIntE+1
        self._sf_rStrD = self._sf_rStrD.replace('~~~~~','')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lambda_spdr(self) -> int:
        # FNC_ID=ST12-32132539142540P
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstE, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqttp_tpqt_spok(self, pq_isRdr: bool, pq_isExst: bool, pq_varNm: str, pq_fncNm):
        # FNC_ID=ST12-60243290032517P
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_rStrB, _sf_sPq, _sf_sSrc, _sf_sVfs, _sf_sVfsFldr)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_lst_gen_lcks(self, mode: str, vrNm, vrDt, vrId):
        # <<<
        # returns:
        self.sqtpp_set_vfs_file()
        if self.sqtpp_vfs_tpqt_file(True) != -1:
            self._sf_rLstB = re.findall(r'<:' + re.escape('__SQTPP__GENIC__CMPRH__') + r'=(?s:.*?).*:>', self._sf_sPq)
            if len(self._sf_rLstB) > 0:
                self._sf_rLstB = self._sf_rLstB[0]
                #self._sf_rLstB = self._sf_rLstB[0:len(self._sf_rLstB)-2]
                #self._sf_rLstB = self._sf_rLstB.split('\n')
                if mode == 'w' or mode == 'mode=w':
                    self._sf_rStrB = self._sf_sPq
                    if isinstance(vrNm, str) and isinstance(vrDt, list): self._sf_rBoolB = True
                    else: self._sf_rBoolB = False
                    if not self._sf_rBoolB:
                        pass
                        #self._sf_sPq = self._sf_sPq.replace(self._sf_rLstB[0], '<:' + vrNm + '=\n' + '\n'.join(vrDt) + ':>')
                    else:
                        if self._sf_rLstB.find(f'SNG=]lC[://{vrNm}') > -1:
                            pass
                        elif self._sf_rLstB.find(f'SEQ=]lC[://{vrNm}__') > -1:
                            self._sf_rLstC = re.findall(r'SEQ=\]lC\[:\/\/' + re.escape(vrNm) + r'__.*?@.*?:\/\/\^', self._sf_rLstB)
                            
                        else:
                            pass
            else:
                if mode == 'w' or mode == 'mode=w':
                    pass
                    #self._sf_sPq = self._sf_sPq.replace(':>:',':>')
                    #self._sf_sPq = self._sf_sPq + '\n<:' + vrNm + '=\n' + '\n'.join(vrDt) + ':>'
                    #self._sf_sSrc = self._sf_sSrc.replace(f'{self._sf_rStrB}:', f'{self._sf_sPq}:')
                    #self._sf_rStrB = None
                else:
                    pass
        else:
            pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_rqnv_menorah_reorder(self, lNms: list, pPrbLen: int, qnvRtm: int) -> str:
        # FNC_ID=ST12-17710590476882D
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rIntI, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_sIntX, _sf_sLstX)
        # returns: (none)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_mv_prometes_kn(self, isRead: bool, dsgFnc: str, srcStr: str, brId: str, brNwId: str, brNwVl: str):
        # FNC_ID=ST12-23073391030325S
        # SqtppFncs slots in use: (non-local)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_mv_prometes_eb(self, hldL: int, hldR: int, slTr: list, br: str, brNw: str, brVl: str):
        # FNC_ID=ST12-72739982417464S
        # SqtppFncs slots in use: (non-local)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_mv_prometes_gt(self, dsg: str, extDsg: str, slTr: list, pxLst: list, br: str, brNw: str, brVl: str) -> str:
        # FNC_ID=ST12-52313792799266S
        # SqtppFncs slots in use: (_sf_rLstA, _sf_rStrA, _sf_sKntId, _sf_sVd)
        # returns: (multipass)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_smvt_char_seeks(self, dsg: str, src: str, pos: list):
        # FNC_ID=ST12-18028086676345S
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rIntA, _sf_rLstB, _sf_rStrB, _sf_rStrC)
        # returns: (none)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_chars_check(self, dsg: int, txt: str) -> bool:
        # FNC_ID=ST12-29859877733999U
        # SqtppFncs slots in use: (_sf_rBoolA)
        # returns: True or False
        self._sf_rBoolA = False
        if dsg == 1:
            vfsDirAllwdChars = set('-ABCDEFGHIJKLMNOPQURSTVWXYZabcdefghijklmnopqurstvwxyz')
            if set(txt).issubset(vfsDirAllwdChars): self._sf_rBoolA = True
        elif dsg == 2:
            if set(txt).issubset(SQTPP_SET_VARS): self._sf_rBoolA = True
        return self._sf_rBoolA
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_smvt_chars_check(self, src: str) -> bool:
        # FNC_ID=ST12-40065746246812U
        # SqtppFncs slots in use: (non-local)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_reset_slots(self, isStcSlts: bool):
        # FNC_ID=ST12-43003520219156U
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rBoolB, _sf_rBoolC, _sf_rBoolD, _sf_rBoolE, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rIntI, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_rStrF, _sf_sBoolCxv, _sf_sBoolX, _sf_sDv, _sf_sIntX, _sf_sKntId, _sf_sLstA, _sf_sLstX, _sf_sPq, _sf_sQp, _sf_sQpRplcX, _sf_sRplc, _sf_sRtrn, _sf_sSrc, _sf_sStrX, _sf_sVd, _sf_sVfs, _sf_sVfsFldr, _sf_sVn)
        # returns: (none)
        if isStcSlts:
            self._sf_sVfs = None
            self._sf_sVfsFldr = None
            #self._sf_sVfsDir = None (Reserved for pojishon features)
            self._sf_sSrc = None
            self._sf_sRplc = None
            self._sf_sQpRplcX = None
            self._sf_EfvStrX = None
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
        if self._rg_rBoolA:
            #self._rg_sMdlTrg = None
            self._rg_sSchm = None
            self._rg_rStrA = None
            self._rg_rStrB = None
            self._rg_rStrC = None
            self._rg_rStrD = None
            self._rg_rLstA = None
            self._rg_rLstB = None
            self._rg_rLstC = None
            self._rg_rIntA = None
            self._rg_rIntB = None
            self._rg_rIntC = None
            self._rg_rIntD = None
            self._rg_rBoolA = None
            self._rg_rBoolB = None
            self._rg_rBoolC = None
            self._rg_rBoolD = None
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
        self._sf_rLstG = None
        self._sf_rLstH = None
        self._sf_rLstI = None
        self._sf_rLstJ = None
        self._sf_rIntA = None
        self._sf_rIntB = None
        self._sf_rIntC = None
        self._sf_rIntD = None
        self._sf_rIntE = None
        self._sf_rIntF = None
        self._sf_rIntG = None
        self._sf_rIntH = None
        self._sf_rIntI = None
        self._sf_rIntJ = None
        self._sf_rIntK = None
        self._sf_rBoolA = None
        self._sf_rBoolB = None
        self._sf_rBoolC = None
        self._sf_rBoolD = None
        self._sf_rBoolE = None
        #self._sf_rBoolF (Reserved for pojishon features)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_slots_rcrd(self) -> bool:
        # FNC_ID=ST12-46251614079358U
        # SqtppFncs slots in use: (_sf_rLstD, _sf_rStrA, _sf_sBoolCxv, _sf_sBoolX, _sf_sDv, _sf_sIntX, _sf_sKntId, _sf_sLstX, _sf_sPq, _sf_sRplc, _sf_sRtrn, _sf_sSrc, _sf_sStrX, _sf_sVd, _sf_sVfs, _sf_sVfsFldr, _sf_sVn)
        # returns: (none)
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
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_err_rcrd(self, errMsg: str) -> str:
        # FNC_ID=ST12-78724239473714U
        # SqtppFncs slots in use: (non-local)
        # returns: (FNC-ERR or FOO-BAR)
        try:
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/err-log.txt', errMsg)
            return 'FNC-ERR'
        except Exception as err_err_rcrd:
            return 'FOO-BAR'
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
# <<<          ________________                                                .
#  .          /.,------------,.\           •                .
#            ///  .---------__|\\
#            \\\   `------.   .//                                  .
#    .        `\\`--...._  `;//'              .                             •
#               `\\.-,___;.//'                  .
#                 `\\-..-//'                                            `
#               .   `\\//'              •                         .      :
#        .            ""
#
# |~.~|
#  __//._  _/./  .//_/  _././_  _//.//  .//_/  _././_  /.__/  _././_  __/.//
#  __/.//  __/._/_  __/._/_  _/./  __//._  _././_  _././_  _././_  /.__/  .//_/
#  __/.//  _/./__  __//._  _//.//  __/._/_  _././_  __/.//  _/./  /.__/  __/._/_
#  /.__/  /.__/  _/./__  __/.//  _//.//  .//_/  _/./__  /.__/  /_._  _/./  _/./
#  __//._  /.__/  _/./__  __//._  /_._  _/./  /_._  _././_  __//._  .//_/  _/./__
#  __/.//  _//.//  __/.//  /_._  _././_  __/.//  _././_  /.__/  _//.//  /.__/
#  /.__/  /_._  _/./  __/._/_  /.__/  __/._/_  _//.//  _//.//  .//_/  .//_/
#  /.__/  _/./  _//.//  _//.//  _/./__  _/./__  /.__/  __/._/_  .//_/  _/./
#  /.__/  /_._  __/.//  __/._/_  _././_  _//.//  _/./__  _//.//  /.__/  .//_/
#  __/.//  _/./  /_._  /.__/  /.__/  .//_/  _/./  __/._/_  _././_  _//.//  _/./__
#  .//_/  /_._  __//._  _/./  _/./  /.__/  _/./__  _././_  __//._  _././_  .//_/
#  /.__/  .//_/  _././_  _/./  __/._/_  .//_/  __//._  _/./  .//_/  /.__/  .//_/
#  /_._  .//_/  _//.//  /_._  _//.//  _//.//  /.__/  __/._/_  _././_  _././_
#  .//_/  /_._  __/.//  _//.//  _//.//  __//._  /.__/  __//._  __/._/_  _././_
#  __//._  _/./  __/._/_  __//._  __/.//  _//.//  /.__/  .//_/  __/._/_  _/./
#  __//._  _././_  /.__/  __/._/_  /_._  _././_  __//._  /_._  _/./__  /_._
#  __/.//  .//_/  /.__/  _/./__  /_._  __//._  _/./  _/./  __//._  _//.//  __//._
#  /_._  _././_  __/._/_  __/._/_  __//._  /.__/  _././_  _/./__  __/.//  .//_/
#  .//_/  /.__/  _/./  /.__/  _/./__  /.__/  __/._/_  __/._/_  _//.//  __/._/_
#  __//._  __/._/_  __/._/_  _//.//  __/._/_  __//._  /.__/  _/./__  /.__/  .//_/
#  /_._  _/./__  .//_/  __/.//  _/./  /_._  /.__/  __/.//  /.__/  __/.//  /.__/
#  /_._  _/./__  _././_  __/.//  __/.//  _/./__  _././_  _/./__  _././_  __//._
#  _././_  /.__/  _././_  __/._/_  __/.//  _//.//  .//_/  __//._  .//_/  /_._
#  /_._  _/./  _//.//  /.__/  /.__/  /_._  /_._  _././_  /.__/  _/./  /_._  .//_/
#  _/./  _/./  _//.//  _/./  _/./__  /_._  __/._/_  /_._  __//._  _/./  /_._
#  .//_/  __/.//  _//.//  _/./__  __//._  /_._  _././_  /.__/  _././_  .//_/
#  _/./  _/./  _/./  __/.//  /.__/  __//._  /.__/  _/./  __//._  _././_  _././_
#  _/./__  .//_/  _/./  /_._  __/._/_  .//_/  _././_  __//._  __/.//  __//._
#  _././_  _/./__  _/./__  __/._/_  _././_  /.__/  __//._  __/.//  _././_  /_._
#  __/._/_  __/.//  _/./__  __/._/_  __//._  _/./  _/./  /.__/  _././_  /_._
#  __/.//  _././_  __/._/_  __//._  /.__/  .//_/  __/._/_  /.__/  _//.//  _././_
#  __//._  /_._  .//_/  .//_/  /.__/  .//_/  .//_/  __//._  _//.//  __/._/_
#  /.__/  .//_/  _//.//  /.__/  __/.//  /_._  .//_/  /.__/  __/._/_  _//.//
#  __//._  /.__/  _/./  __/._/_  /.__/  /.__/  _//.//  _/./  __//._  __/.//
#  __/.//  __/.//  _././_  _/./__  /_._  __/.//  __//._  __/._/_  _//.//  _././_
#  _//.//  __/.//  /.__/  /.__/  _//.//  __/.//  _/./  _/./  __/.//  _/./  .//_/
#  __/.//  /.__/  _//.//  .//_/  _//.//  _/./__  _//.//  _/./__  __/._/_  _/./__
#  /.__/  .//_/  __//._  __//._  _././_  /_._  __/.//  .//_/  /_._  _././_  .//_/
#  /_._  __/.//  .//_/  _//.//  _//.//  /.__/  .//_/  __//._  _/./__  __/._/_
#  __/._/_  _//.//  .//_/  _/./  __/._/_  _/./__  .//_/  _././_  .//_/  .//_/
#  /.__/  /.__/  _/./  __/._/_  __//._  __/.//  /.__/  /.__/  __/.//  _/./  .//_/
#  .//_/  _././_  __/.//  __//._  _/./  _/./__  .//_/  __/._/_  __//._  /.__/
#  _/./  /_._  __/.//  _/./__  .//_/  _/./__  /.__/  __/._/_  __/._/_  _/./__
#  _/./  _//.//  _//.//  _/./  _././_  _//.//  _//.//  _/./__  .//_/  /_._
#  __/.//  __//._  __/.//  /.__/  __/._/_  __/.//  __/.//  _/./  _/./__  _//.//
#  _/./  /_._  _././_  _/./  _/./  __//._  _//.//  _././_  __/.//  __/.//
#  __/._/_  .//_/  _././_  .//_/  .//_/  _//.//  __/._/_  .//_/  __/.//  __/.//
#  _/./  _//.//  __//._  __//._  __//._  /_._  _/./  __//._  __//._  _//.//  _/./
#  __/._/_  __/._/_  .//_/  /_._  _/./__  _/./  /_._  _//.//  /.__/  __/._/_
#  __//._  __/._/_  __/._/_  _//.//  __/._/_  .//_/  __/._/_  __/.//  __//._
#  __//._  /.__/  /.__/  __//._  _//.//  _/./  .//_/  .//_/  _/./__  /_._  /_._
#  /.__/  /_._  /_._  .//_/  .//_/  .//_/  __//._  /.__/  _/./__  _//.//  _//.//
#  __/.//  _/./__  __/.//  /.__/  /.__/  _//.//  /.__/  _././_  _/./__  /_._
#  /_._  _././_  .//_/  __/._/_  __/._/_  _././_  __/.//  /.__/  _././_  _././_
#  _/./  _//.//  __/.//  .//_/  _././_  .//_/  _//.//  _/./__  _//.//  /_._
#  __//._  __//._  _././_  _/./__  __//._  __/._/_  __/.//  /.__/  _//.//
#  __/._/_  _//.//  .//_/  __/.//  .//_/  _/./__  /_._  _././_  __//._  _/./__
#  _/./  _/./  _//.//  _././_  /.__/  _//.//  _/./__  __/._/_  __//._  __//._
#  _//.//  _/./  _//.//  __/._/_  _././_  /.__/  __/.//  _/./  __/.//  __/.//
#  __/._/_  __/.//  __//._  _././_  __//._  .//_/  _/./__  _//.//  _././_  _/./__
#  /.__/  __/.//  __/.//  /_._  _//.//  __/.//  _//.//  __/._/_  __/._/_  .//_/
#  __//._  _//.//  _//.//  /.__/  .//_/  __/.//  __//._  /.__/  _././_  /.__/
#  __//._  __//._  _/./__  _././_  /.__/  _/./__  _//.//  /.__/  _//.//  __//._
#  __/._/_  /_._  __/._/_  .//_/  __//._
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon(self, mode: str, varDt, varNm, dirLst: list):
        # <<<
        #_____________________________________________________________________________
        #_____________________________________________________________________________
        # For all pojishon features, a non-negotiated price of 2,750,000 US DOLLARS.
        # Set price reflects very advanced capability for remote embedded ai systems
        # using a similiar python module; or completed C/C++ version of this library.
        # Includes custom antenna symmetry interfacing, open modular expansions and
        # the other special designed methods for security thru out this library using
        # tor like vfs-dir multi-layer encryption(koch) & vfs-file encryption(kyber)
        # Is setup straight from the start for advanced imaging classing and other
        # dynamic learn & adapt configurations as the goto hybrid env-var/vfs sys,
        # that is of exclusive tested mathematics in design of it's m/d/f operations.
        #_____________________________________________________________________________
        # modes:
        #   NEXT:
        #    ("next", required, required, required) -> FULLY IMPLEMENTED
        #    ("next.cast.<optional>", non-required, non-required, required) -> FULLY IMPLEMENTED
        #    ("next.ghost.<optional>", required, non-required, required) -> FULLY IMPLEMENTED
        #    ("next.omega.<optional>", required, required, non-required) -> FULLY IMPLEMENTED
        #    ("next.splice.<optional>", required, required, required) -> FULLY IMPLEMENTED
        #    ("next.refill.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("next.remove.<optional>", required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #   JUMP:
        #    ("jump.add.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #    ("jump.cast.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("jump.ghost.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("jump.refill.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #   TQPT:
        #    ("tqpt.add.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("tqpt.remove.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #    ("tqpt.select.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("tqpt.selectall.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #   TPQT:
        #    ("tpqt.add.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("tpqt.remove.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #    ("tpqt.joinall.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("tpqt.joinrecorded.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #   WATCH:
        #    ("watch.move.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("watch.join.<optional>", required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("watch.pivot.<optional>", non-required, required, non-required) -> NOT PUBLIC IMPLEMENTED
        #    ("watch.clearall.<optional>", required, non-required, non-required) -> NOT PUBLIC IMPLEMENTED
        #   RECORD:
        #    ("record.join.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("record.restart.<optional>", required, non-required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("record.readall.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        #    ("record.forcemap.<optional>", non-required, required, required) -> NOT PUBLIC IMPLEMENTED
        # optionals:
        #    ****setfreq, removefreq, retag and quantumf cannot be combined optionals
        #    ****quantumf is a read only optional from an auto-generated slots module
        #
        #    open(varDt=list, occurence=#[index]) | open(varNm=list, occurence=#[index]) -> FULLY IMPLEMENTED
        #    closed(varNm=str, start=#, end=#) | closed(varNm=list, start=#, end=#) -> FULLY IMPLEMENTED
        #    compare(varDt=str, dirLst=list, freq=str) | compare(varDt=list, dirLst=list, freq=str) -> NOT PUBLIC IMPLEMENTED
        #    cache(varNm=str, occurence=#) | cache(varNm=list, occurence=#[index]) -> NOT PUBLIC IMPLEMENTED
        #    seal(dirLst=list, match=str, freq=str, type=unlocked=0|locked=1) -> NOT PUBLIC IMPLEMENTED
        #    setfreq(varNm=str, dirLst=list, occurence=#) | setfreq(varNm=list, dirLst=list, occurence=#[index]) -> NOT PUBLIC IMPLEMENTED
        #    removefreq(varNm=str, dirLst=list, freq=str) | removefreq(varNm=list, dirLst=list, freq=str) -> NOT PUBLIC IMPLEMENTED
        #    retag(varDt=str, freq=str, span=#, removeat=#) | retag(varDt=list, freq=str, span=#[index], removeat=#[index]) -> NOT PUBLIC IMPLEMENTED
        #    quantumf(varNm=str, dirLst=list, span=#) | quantumf(varNm=list, dirLst=list, span=#[index]) -> NOT PUBLIC IMPLEMENTED
        #try:
            vfsEmbEfo = None
            vfsRtrn = None
            optAplc = False
            rtrn = 1
            if mode.find('.') > -1: vfsEmbEfo = mode.split('.')
            else: vfsEmbEfo = [mode]
            #________________________________________________________________________
            #___________________________________NEXT_________________________________
            if vfsEmbEfo[0] == 'next' or vfsEmbEfo[0] == 'NEXT':
                if len(vfsEmbEfo) == 1:
                    vfsRtrn = self.sqtpp_emb_vfs_pojishon_mkfile('next', varDt, varNm, dirLst)
                    if vfsRtrn < 0: rtrn = self.sqtpp_emb_vfs_pojishon_err_rtrn('next', vfsRtrn)
                else:
                    optAplc = True
                    if vfsEmbEfo[1] == 'cast' or vfsEmbEfo[1] == 'CAST':
                        vfsRtrn = self.sqtpp_emb_vfs_pojishon_mkfile('next.cast', None, None, dirLst)
                        if not self._sf_rBoolF and vfsRtrn < 0: rtrn = self.sqtpp_emb_vfs_pojishon_err_rtrn('next', vfsRtrn)
                        elif self._sf_rBoolF and vfsRtrn < 0: self.sqtpp_emb_vfs_pojishon_err_router_rtrn(vfsRtrn)
                    elif vfsEmbEfo[1] == 'ghost' or vfsEmbEfo[1] == 'GHOST':
                        vfsRtrn = self.sqtpp_emb_vfs_pojishon_mkfile('next.ghost', None, None, dirLst)
                        if vfsRtrn == -1:
                            raise Exception(f'[sqtpp-vfs >> pojishon] - mode/next err: could not read mount(s)/dirs........is an unresolved error from lack of a .sqtpp emb-vfs valid lego style/mnt(s)|:dir(s) configuration; or the current set vfs file...sqtpp file, may be corrupted as a whole')
                    elif vfsEmbEfo[1] == 'omega' or vfsEmbEfo[1] == 'OMEGA':
                        vfsRtrn = self.sqtpp_emb_vfs_pojishon_mkfile('next.omega', varDt, varNm, None)
                        if vfsRtrn < 0: rtrn = self.sqtpp_emb_vfs_pojishon_err_rtrn('next', vfsRtrn)
                    elif vfsEmbEfo[1] == 'splice' or vfsEmbEfo[1] == 'SPLICE':
                        vfsRtrn = self.sqtpp_emb_vfs_pojishon_mkfile('next.splice', varDt, varNm, dirLst)
                        if vfsRtrn < 0: rtrn = self.sqtpp_emb_vfs_pojishon_err_rtrn('splice', vfsRtrn)
                        else:
                            if vfsRtrn == 1:
                                return True
                            else:
                                return False
                    else:
                        raise Exception(f'[sqtpp-vfs >> pojishon] - mode/next err: invalid next command, see IMPORT_CALLS.TXT for all pojishon next commands')
            #________________________________________________________________________
            #______________________________OPTIONALS_________________________________
            if len(vfsEmbEfo) == 3 and optAplc and rtrn == 1:
                self.sqtpp_emb_vfs_pojishon_set_optional_list(vfsEmbEfo[2])
                if self._sf_rLstD[0] == 'open' or self._sf_rLstD[0] == 'OPEN':
                    return self.sqtpp_emb_vfs_pojishon_opt_open()
                elif self._sf_rLstD[0] == 'closed' or self._sf_rLstD[0] == 'CLOSED':
                    return self.sqtpp_emb_vfs_pojishon_opt_closed()
                else:
                    raise Exception(f'[sqtpp-vfs >> pojishon] - mode/optional err: invalid optional, see IMPORT_CALLS.TXT for all pojishon optionals')
            return rtrn
        #except Exception as err_emb_vfs_pojishon:
            #self._sErr = f'staqtapp1.2 (emb_vfs_pojishon) error: {err_emb_vfs_pojishon}'
            #return self.sqtpp_err_rcrd(self._sErr)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_mkfile(self, mode: str, varDt, varNm, dirLst) -> int:
        # <<<
        # returns:
        # -1=invalid type balance @varDt and @varNm
        # -2=non-allowed char sequence found @varDt: ':|:>'
        # -3=non-allowed char(s) @varNm
        rtrn = None
        if mode.find('.') < 0:
            if isinstance(varDt, str) and isinstance(varNm, str):
                if varDt.find(':|:>') > -1: rtrn = -2
                else:
                    if self.sqtpp_chars_check(2, varNm):
                        if mode == 'next':
                            rtrn = self.sqtpp_emb_vfs_pojishon_write(1, varNm, varDt, dirLst)
                            if rtrn < 0: self.sqtpp_emb_vfs_pojishon_err_router_rtrn(rtrn)
                    else: rtrn = -3
            elif isinstance(varDt, list) and isinstance(varNm, list):
                pass
        else:
            if mode == 'next.cast': rtrn = self.sqtpp_emb_vfs_pojishon_write(2, None, None, dirLst)
            elif mode == 'next.ghost': rtrn = self.sqtpp_emb_vfs_pojishon_write(3, None, None, dirLst)
            elif mode == 'next.omega': rtrn = self.sqtpp_emb_vfs_pojishon_write(4, varNm, varDt, None)
            elif mode == 'next.splice': rtrn = self.sqtpp_emb_vfs_pojishon_write(5, varNm, varDt, dirLst)
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_read(self, dsg: int):
        # <<<
        # returns: (1, -1=invalid mnt path, -2=invalid dir path, -3=invalid file path)
        rtrn = 1
        embFndLst = None
        # Reads SQTPP_MNT_STGS/STGS file, returns last used mnt/dir/file list
        if dsg == 1:
            self._sf_sVd = self.sqtpp_emb_ext_vfs_read_file(['SQTPP_MNT_STGS','STGS','STGS'])
            self._sf_sDv = self._sf_sVd
            self._sf_sVd = self._sf_sVd.replace(f'<STGS:S:\n','').replace(':|:>','')
            if self._sf_sVd != 'none':
                embFndLst = re.findall(r'lfd\=.*?\;', self._sf_sVd)
                if len(embFndLst) > 0:
                    embFndLst = embFndLst[0].replace('lfd=','').replace(';','')
                    rtrn = embFndLst.split('/')
                else: rtrn -4
            else: rtrn = -4
        # Read any mnt/dir->file, _sf_sVfsDir slot has to be mnt/dir/file path list
        elif dsg == 2:
            self._sf_sVd = self.sqtpp_emb_ext_vfs_read_file(self._sf_sVfsDir)
            if self._sf_sVd.find('!MNT_.:_:!!:_:._MNT!') > -1: rtrn = -1
            elif self._sf_sVd.find('!DIR_.:_:!!:_:._DIR!') > -1: rtrn = -2
            elif self._sf_sVd.find('!FILE_.:_:!!:_:._FILE!') > -1: rtrn = -3
            else:
                self._sf_sDv = self._sf_sVd
                self._sf_sVd = self._sf_sVd.replace(f'<{self._sf_sVfsDir[2]}:S:\n','').replace(':|:>','')
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_write(self, dsg: int, varNm, varDt, dirLst: list) -> int:
        # <<<
        # returns: (returns from sqtpp_emb_vfs_router())
        fncLst = None
        fncLen = None
        rtrn = None
        if dsg == 1: # New mount; new dir and a new env-var(s) file.
            rtrn = self.sqtpp_emb_vfs_router(False, True, True, 1, dirLst, None, None)
            if rtrn > 0: rtrn = self.sqtpp_emb_vfs_router(False, False, False, 5, dirLst, None, [varNm,varDt])
            if rtrn > 0:
                self.sqtpp_emb_vfs_pojishon_write_stgs(1, [dirLst[0], dirLst[1], varNm])
                rtrn = self.sqtpp_emb_vfs_router(True, False, False, 9, None, None, None)
        elif dsg == 2: # Copy env-var(s) file to new dir from last added file.
                rtrn = self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
                if rtrn > 0:
                    fncLst = self.sqtpp_emb_vfs_pojishon_read(1)
                    if isinstance(fncLst, int):
                        return fncLst
                    else:
                        if dirLst[0] == fncLst[0]:
                            if dirLst[1] != fncLst[1]:
                                self._sf_rBoolF = True
                                if self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt([fncLst[0], dirLst[1]]) == -1:
                                    rtrn = self.sqtpp_emb_vfs_router(False, False, False, 1, dirLst, None, None)
                                if rtrn > 0: rtrn = self.sqtpp_emb_vfs_router(False, False, False, 6, fncLst, [dirLst[len(dirLst)-1]], None)
                                if rtrn > 0:
                                    self._sf_sVfsDir = [fncLst[0], dirLst[len(dirLst)-1], fncLst[2]]
                                    self.sqtpp_emb_vfs_pojishon_write_stgs(1, self._sf_sVfsDir)
                                    rtrn = self.sqtpp_emb_vfs_router(True, False, False, 9, None, None, None)
                            else:
                                raise Exception(f'[sqtpp-vfs >> pojishon] - directory placement err: directory ({dirLst[1]}) is the same directory of last used directory ({fncLst[1]}) for cast')
                        else:
                            raise Exception(f'[sqtpp-vfs >> pojishon] - mount placement err: mount ({dirLst[0]}) does not match last used mount ({fncLst[0]}) for cast')
                else: self.sqtpp_emb_vfs_pojishon_err_router_rtrn(rtrn)
        elif dsg == 3: # Line match file add from compare with last added file to @dirLst file(s)
            rtrn = self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
            if rtrn > 0:
                fncLst = self.sqtpp_emb_vfs_pojishon_opt_file_search(True, 2, dirLst, None, None)
                fncLen = len(fncLst)
                if fncLen > 0:
                    flNm = f'{self._sf_sVfsDir[2]}_{fncLen}'
                    rtrn = self.sqtpp_emb_vfs_router(False, False, False, 5, dirLst, None, [flNm, '\n'.join(fncLst)])
                    if rtrn == -13:
                        self.sqtpp_emb_vfs_router(False, False, False, 8, [dirLst[0], dirLst[1], flNm], None, None)
                        self.sqtpp_emb_vfs_router(False, False, False, 5, dirLst, None, [flNm, '\n'.join(fncLst)])
                    self.sqtpp_emb_vfs_router(True, False, False, 9, None, None, None)
                rtrn = 1
            else: rtrn = -1
        elif dsg == 4:
            rtrn = self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
            if rtrn > 0:
                fncLst = self.sqtpp_emb_vfs_pojishon_read(1)
                if isinstance(fncLst, int):
                    return fncLst
                else: self.sqtpp_emb_vfs_pojishon_omega_ctpk(fncLst, varNm, varDt)
            else: rtrn = -1
        elif dsg == 5:
            rtrn = self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
            if rtrn > 0:
                rtrn = self.sqtpp_emb_vfs_pojishon_splice(varNm, varDt, dirLst)
            else: rtrn -1
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice(self, varNm, varDt, dirLst: list):
        # FNC_ID=ST12-99106486643732
        # SqtppFncs slots in use: (_sf_rBoolE, _sf_rBoolF, _sf_rIntB, _sf_rIntC, _sf_rLstC, _sf_rStrD, _sf_rStrE, _sf_rStrF, _sf_sBoolX, _sf_sLstX)
        # returns: (1=True or 0=False)
        # -2=invalid parameter settings for next.splice
        # -3=invalid chars @dirLst[]
        # -4=no last mnt/dir/file used vfs setting
        # -5=last used mount in vfs settings not found
        # -6=last used mount/directory in vfs settings not found
        # -7=last used mount/directory/file in vfs settings not found
        # -8=@varData is empty
        try:
            rtrn = 1
            ptrnSplc = None
            self._sf_sBoolX = True
            self.sqtpp_ntr_tree_context(False)
            if isinstance(varNm, list) and isinstance(dirLst, list): ptrnSplc = False
            elif isinstance(varDt, list) and isinstance(varNm, str) and isinstance(dirLst, list): ptrnSplc = True
            else:
                return -2
            if len(dirLst) > 1:
                if set(dirLst[0]).issubset(SQTPP_SET_VARS) and set(dirLst[1]).issubset(SQTPP_SET_VARS):
                    if self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dirLst[0]) == 1:
                        self._sf_rBoolE = True
                        if self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dirLst): self._sf_rBoolF = True
                        else: self._sf_rBoolF = False
                    else: self._sf_rBoolE = False
                    self._sf_sLstX = self.sqtpp_emb_vfs_pojishon_read(1)
                    if isinstance(self._sf_sLstX, int): rtrn = -4
                    else:
                        self._sf_rStrF = self.sqtpp_emb_ext_vfs_get_mnt(True, [self._sf_sLstX[0]])
                        if self._sf_rStrF != None:
                            self._sf_rStrE = self.sqtpp_emb_ext_vfs_get_dir(self._sf_sLstX[1], self._sf_rStrF)
                            if self._sf_rStrE != None:
                                self._sf_rStrD = self.sqtpp_emb_ext_vfs_get_file(self._sf_sLstX[2], self._sf_rStrE)
                                if self._sf_rStrD != None:
                                    self._sf_rStrD = self._sf_rStrD[len(self._sf_sLstX[2])+5:]
                                    if not ptrnSplc:
                                        self._sf_rIntC = len(varNm)
                                        self._sf_rIntB = (len(self._sf_rStrD)+self._sf_rIntC-1)//self._sf_rIntC
                                        self._sf_rLstC = [self._sf_rStrD[i*self._sf_rIntB:(i+1)*self._sf_rIntB] for i in range(self._sf_rIntC)]
                                    else:
                                        if len(varDt) > 0:
                                            self._sf_rStrD = self._sf_rStrD.replace('\n', '●•')
                                            if not isinstance(varDt[0], str): varDt[0] = str(varDt[0])
                                            if all(isinstance(x, (int, float)) for x in varDt): rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_gnmbrs(varDt)
                                            elif varDt[0].find("*>") > -1 or varDt[0].find("*<") > -1: rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn(varDt)
                                            else: rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_gptrn(varDt)
                                        else: rtrn = -8
                                    if rtrn > 0:
                                        self._sf_rLstC[len(self._sf_rLstC)-1] = self._sf_rLstC[len(self._sf_rLstC)-1][:len(self._sf_rLstC[len(self._sf_rLstC)-1])-4]
                                        self._sf_rIntC = len(self._sf_rLstC)
                                        for self._sf_rIntB in range(self._sf_rIntC): self._sf_rLstC[self._sf_rIntB] = self._sf_rLstC[self._sf_rIntB].replace('●•','\n')
                                        self.sqtpp_emb_vfs_pojishon_splice_ext_wrt_dir(ptrnSplc, True, dirLst, varNm)
                                else: rtrn = -7
                            else: rtrn = -6
                        else: rtrn = -5
                else: rtrn = -3
            else: rtrn = -2
            return rtrn
        except Exception as err_sqtpp_emb_vfs_pojishon_slice:
            raise Exception(f'[sqtpp-vfs >> pojishon] - next.splice, unexpected exception/direct function err: {err_sqtpp_emb_vfs_pojishon_slice}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_wrt_dir(self, isPtrnSplice: bool, isRstSlts: bool, dirLst: list, varNm):
        # FNC_ID=ST12-34867692065199
        # SqtppFncs slots in use: (_sf_EfvStrX, _sf_rBoolE, _sf_rLstC, _sf_sLstX, _sf_sSrc, _sf_sStrX, _sf_sVfs)
        # returns: (none)
        if isPtrnSplice: self._rg_rStrA = f'{varNm}_{self._sf_sLstX[1]}_'
        if not self._sf_rBoolE: self._rg_rBoolA = True
        else: self._rg_rBoolA = False
        self._rg_rIntB = len(self._sf_rLstC)
        self._rg_rLstA = self._sf_rLstC
        self._sf_rLstC = None
        for self._rg_rIntA in range(self._rg_rIntB):
            if not isPtrnSplice: self.sqtpp_emb_vfs_router(False, False, self._rg_rBoolA, 5, dirLst, None, [varNm[self._rg_rIntA], self._rg_rLstA[self._rg_rIntA]])
            else: self.sqtpp_emb_vfs_router(False, False, self._rg_rBoolA, 5, dirLst, None, [f'{self._rg_rStrA}{self._rg_rIntA+1}', self._rg_rLstA[self._rg_rIntA]])
            if self._rg_rBoolA: self._rg_rBoolA = False
        self._sf_sSrc = self._sf_sSrc.replace(self._sf_EfvStrX, self._sf_sStrX)
        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
        if isRstSlts: self.sqtpp_reset_slots(True)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_gptrn(self, varDt: list) -> int:
        # FNC_ID=ST12-93305047072458
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntB, _sf_rIntC, _sf_rLstB, _sf_rStrB, _sf_rStrD)
        # returns:
        rtrn = 1
        self._sf_rBoolA = False
        varDt = [str(self._sf_rIntB) for self._sf_rIntB in varDt]
        self._sf_rIntC = 0
        self._sf_rStrB = None
        self._sf_rIntB = len(varDt)
        while self._sf_rIntC < self._sf_rIntB:
            if self._sf_rStrD.find(varDt[self._sf_rIntC]) > -1:
                self._sf_rStrB = varDt[self._sf_rIntC]
                break
            self._sf_rIntC+=1
        if self._sf_rStrB != None:
            self.sqtpp_emb_vfs_pojishon_splice_ext_pos_nmbr(self._sf_rStrB)
            rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_cnt_apd(self._sf_rLstB, len(self._sf_rStrB))
        else: rtrn = 0
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_gnmbrs(self, varDt: list) -> int:
        # FNC_ID=ST12-97036264152285
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntH, _sf_rLstB, _sf_rStrD)
        # returns:
        rtrn = 1
        self._sf_rBoolA = False
        self._sf_rLstB = re.findall(r'\b\d+(?:\.\d+)?\b', self._sf_rStrD)
        if len(self._sf_rLstB) > 0:
            self._sf_rIntC = len(self._sf_rLstB)
            self._sf_rIntE = len(varDt)
            for self._sf_rIntB in range(self._sf_rIntC):
                if not self._sf_rBoolA: self._sf_rIntD = 0
                else:
                    break
                while self._sf_rIntD < self._sf_rIntE:
                    if self._sf_rLstB[self._sf_rIntB] == str(varDt[self._sf_rIntD]):
                        self._sf_rIntH = self._sf_rLstB[self._sf_rIntB]
                        self._sf_rBoolA = True
                        break
                    self._sf_rIntD+=1
            if self._sf_rBoolA:
                self.sqtpp_emb_vfs_pojishon_splice_ext_pos_nmbr(self._sf_rIntH)
                rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_cnt_apd(self._sf_rLstB, self._sf_rIntF)
            else: rtrn = 0
        else: rtrn = 0
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn(self, varDt: list) -> int:
        # FNC_ID=ST12-91706299587792
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntB, _sf_rIntF, _sf_rLstB, _sf_rLstC, _sf_rLstE, _sf_rStrC, _sf_rStrD)
        # returns: (1=True or 0=False)
        # -9=pattern matching for splicing is not defined
        rtrn = 1
        self._sf_rBoolD = False
        self._sf_rStrC = set('>*<')
        if set(varDt[0]).issubset(self._sf_rStrC):
            self._sf_rBoolD = False
            if varDt[0].find("*>") > -1: self._sf_rBoolD = True
            self._sf_rLstB = re.findall(r'\b\d+(?:\.\d+)?\b', self._sf_rStrD)
            if len(self._sf_rLstB) > 0:
                if self._sf_rBoolD:
                    self._sf_rLstC = max(self._sf_rLstB.count(self._sf_rIntB) for self._sf_rIntB in self._sf_rLstB)
                    self._sf_rLstC = [self._sf_rIntB for self._sf_rIntB in self._sf_rLstB if self._sf_rLstB.count(self._sf_rIntB) == self._sf_rLstC]
                else:
                    self._sf_rLstC = min(self._sf_rStrD.count(self._sf_rIntB) for self._sf_rIntB in self._sf_rLstB)
                    self._sf_rLstC = [self._sf_rIntB for self._sf_rIntB in self._sf_rLstB if self._sf_rStrD.count(self._sf_rIntB) == self._sf_rLstC]
            else: rtrn = 0
            if rtrn > 0 and len(self._sf_rLstC) > 0:
                self.sqtpp_emb_vfs_pojishon_splice_ext_pos_nmbr(self._sf_rLstC[0])
                rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_cnt_apd(self._sf_rLstB, self._sf_rIntF)
            else: rtrn = 0
        else:
            if varDt[0].find("*>") > -1: self._sf_rBoolD = True
            varDt = varDt[0].replace('*>','').replace('*<','')
            if varDt.find(',') > -1: self._sf_rLstB = varDt.split(',')
            else: self._sf_rLstB = [varDt]
            if self.sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn_max_or_min() > 0:
                rtrn = self.sqtpp_emb_vfs_pojishon_splice_ext_cnt_apd(self._sf_rLstE[self._sf_rIntF], len(self._sf_rLstB[self._sf_rIntF]))
            else: rtrn = 0
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_pos_nmbr(self, nmbrPtrn: str):
        # FNC_ID=ST12-91166422274631
        # SqtppFncs slots in use: (_sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rLstB, _sf_rLstD, _sf_rStrD)
        # returns: (_sf_rLstB is resulting nmbrPtrn list)
        self._sf_rIntD = 0
        self._sf_rLstB = []
        self._sf_rIntF = len(nmbrPtrn)
        self._sf_rLstD = set('.1234567890')
        self._sf_rIntE = len(self._sf_rStrD)
        while 1:
            if self._sf_rIntD < self._sf_rIntE: self._sf_rIntC = self._sf_rStrD.find(nmbrPtrn, self._sf_rIntD)
            else:
                break
            if self._sf_rIntC > -1:
                if self._sf_rIntC+self._sf_rIntF < self._sf_rIntE and self._sf_rIntC > 0:
                    if not set(self._sf_rStrD[self._sf_rIntC+self._sf_rIntF]).issubset(self._sf_rLstD) and not set(self._sf_rStrD[self._sf_rIntC-1]).issubset(self._sf_rLstD): self._sf_rLstB.append(self._sf_rIntC)
                else:
                    if self._sf_rIntC < 1:
                        if not set(self._sf_rStrD[self._sf_rIntC+self._sf_rIntF]).issubset(self._sf_rLstD): self._sf_rLstB.append(self._sf_rIntC)
                    else: self._sf_rLstB.append(self._sf_rIntC)
                self._sf_rIntD = self._sf_rIntC+1
            else:
                break
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_cnt_apd(self, idxLst: list, ptrnLen: int):
        # FNC_ID=ST12-14042503326485
        # SqtppFncs slots in use: (_sf_rIntC, _sf_rIntD, _sf_rLstC, _sf_rStrD)
        # returns: (0=False or 1=True/_sf_rLstC spliced contents from _sf_rStrD)
        self._sf_rLstC = []
        self._sf_rIntD = len(idxLst)
        if self._sf_rIntD > 0:
            if self._sf_rIntD > 1:
                for self._sf_rIntC in range(self._sf_rIntD):
                    if self._sf_rIntC < 1: self._sf_rLstC.append(self._sf_rStrD[:idxLst[self._sf_rIntC]+ptrnLen])
                    else:
                        if self._sf_rIntC+1 < self._sf_rIntD: self._sf_rLstC.append(self._sf_rStrD[idxLst[self._sf_rIntC-1]+ptrnLen+1:idxLst[self._sf_rIntC]+ptrnLen])
                        else: self._sf_rLstC.append(self._sf_rStrD[idxLst[self._sf_rIntC-1]+ptrnLen+1:])
            else:
                self._sf_rLstC.append(self._sf_rStrD[:idxLst[self._sf_rIntC]+ptrnLen])
                self._sf_rLstC.append(self._sf_rStrD[idxLst[self._sf_rIntC]:])
            return 1
        else:
            return 0
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn_max_or_min(self):
        # FNC_ID=ST12-37162293979311
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rLstB, _sf_rLstD, _sf_rLstE, _sf_rStrD)
        # returns: (0=False or 1=True/_sf_rIntF index of max or min ptrn occurence)
        self._sf_rLstE = []
        self._sf_rIntF = len(self._sf_rStrD)
        self._sf_rIntC = len(self._sf_rLstB)
        for self._sf_rIntB in range(self._sf_rIntC):
            self._sf_rIntE = 0
            self._sf_rLstD = []
            self._sf_rIntG = len(self._sf_rLstB[self._sf_rIntB])
            while 1:
                if self._sf_rIntE < self._sf_rIntF: self._sf_rIntD = self._sf_rStrD.find(self._sf_rLstB[self._sf_rIntB], self._sf_rIntE)
                else: self._sf_rIntE = -1
                if self._sf_rIntD > -1 and self._sf_rIntE > -1:
                    self._sf_rLstD.append(self._sf_rIntD)
                    self._sf_rIntE = self._sf_rIntD+self._sf_rIntG
                else: self._sf_rIntE = -1
                if self._sf_rIntE < 0:
                    if len(self._sf_rLstD) > 0: self._sf_rLstE.append(self._sf_rLstD)
                    else: self._sf_rLstE.append(None)
                    break
        if len(self._sf_rLstE) > 0:
            if self._sf_rBoolD: self._sf_rIntE = 0
            else: self._sf_rIntE = 9999999
            self._sf_rIntF, self._sf_rIntG = 0,0
            for self._sf_rIntB in range(self._sf_rIntC):
                if self._sf_rLstE[self._sf_rIntB] != None: self._sf_rIntD = len(self._sf_rLstE[self._sf_rIntB])
                else: self._sf_rIntD = -1
                if self._sf_rIntD > -1:
                    if self._sf_rBoolD:
                        if self._sf_rIntD > self._sf_rIntE: self.sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn_max_or_min_rcrd()
                    else:
                        if self._sf_rIntD < self._sf_rIntE: self.sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn_max_or_min_rcrd()
                else: self._sf_rIntG+=1
            if self._sf_rIntG != self._sf_rIntC: rtrn = 1
            else: rtrn = 0
        else: rtrn = 0
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_splice_ext_gl_ptrn_max_or_min_rcrd(self):
        # FNC_ID=ST12-61771787879225
        # SqtppFncs slots in use: (_sf_rIntB, _sf_rIntD, _sf_rIntE, _sf_rIntF)
        # returns: (none)
        self._sf_rIntE = self._sf_rIntD
        self._sf_rIntF = self._sf_rIntB
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk(self, luf: list, vrNm: str, vrDt):
        # FNC_ID=ST12-90267412427944
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rLstC, _sf_rLstG, _sf_rStrA, _sf_rStrB, _sf_rStrE, _sf_rStrF, _sf_sIntX, _sf_sLstX, _sf_sQp, _sf_sRplc, _sf_sSrc, _sf_sVfs)
        # returns: (none)
        try:
            self._sf_rStrE = self.sqtpp_emb_ext_vfs_get_mnt(True, [luf[0]])
            if self._sf_rStrE != None:
                self._sf_rStrF = self.sqtpp_emb_ext_vfs_get_dir(luf[1], self._sf_rStrE)
                if self._sf_rStrF != None:
                    if set(vrNm).issubset(SQTPP_SET_VARS):
                        if isinstance(vrDt, str) or isinstance(vrDt, list):
                            if isinstance(vrDt, list): vrDt = ''.join(vrDt)
                            if vrDt.find('{') > -1 or vrDt.find('}') > -1:
                                if vrDt.find('[') > -1 or vrDt.find(']') > -1:
                                    if not os.path.isfile(f'{SQTPP_MDL_DIR}/__sqtpp__default__omega__key__.txt'):
                                        self._sf_rLstC = ['__sqtpp__default__omega__key__ = (','    __dok__type: (','    type: ( list,','    validator [','        lambda x: if len(x) > 0','    ]','    )','    )',')']
                                        with open(f'{SQTPP_MDL_DIR}/__sqtpp__default__omega__key__.txt', 'w') as fObjWrtSchm: fObjWrtSchm.write('\n'.join(self._sf_rLstC))
                                        self.sqtpp_registry_homer(False, None, None, f'{SQTPP_MDL_DIR}/__sqtpp__default__omega__key__.txt')
                                    rtrn = self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr(luf, vrNm, vrDt)
                                    if rtrn < 0: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(6)
                                    else:
                                        if len(self._sf_sLstX) > 0:
                                            self._sf_rBoolA = True
                                            self.sqtpp_reset_slots(False)
                                            if self.sqtpp_set_vfs_file() == 1:
                                                if self.sqtpp_vfs_tqpt_file(True) != -1:
                                                    self._sf_rStrA = '\n'
                                                    self._sf_rStrB = self._sf_sQp
                                                    if self._sf_sQp.find(f'{vrNm}<@qp(') == -1:
                                                        self._sf_rLstC = [str(_) for _ in self._sf_sLstX]
                                                        self._sf_sQp = f'{self._sf_sQp}{self._sf_rStrA}{vrNm}<@qp({")@ctpk!(".join(self._sf_rLstC)}):>'
                                                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrB, self._sf_sQp)
                                                        if self._sf_sIntX > -1: self._sf_sSrc = self._sf_sSrc.replace(f'lfd={"/".join(luf)};:|:>', f'lfd={luf[0]}/{luf[1]}/{self._sf_sRplc[self._sf_sIntX]};:|:>')
                                                        self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                                                        self._sf_rStrB = None
                                                        self._sf_rLstC = None
                                                        self._sf_sQp = None
                                                        self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis()
                                                        self.sqtpp_registry_homer(False, f'{vrNm}_ctpk_O', self._sf_rLstG, '__sqtpp__default__omega__key__')
                                                    else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(9)
                                                else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(8)
                                            else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(7)
                                else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(5)
                        else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(4)
                    else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(3)
                else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(2)
            else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_err(1)
        except Exception as err_sqtpp_emb_vfs_pojishon_omega_ctpk:
            raise Exception(f'[sqtpp-vfs >> pojishon] - next.omega, unexpected exception/direct function err: {err_sqtpp_emb_vfs_pojishon_omega_ctpk}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_genesis(self):
        # FNC_ID=ST12-18291619832468
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_rLstG, _sf_rLstH, _sf_sBoolX, _sf_sLstX)
        # returns: (top reg-key with ordered ctpk-span matched values, _sf_rLstG)
        self._sf_rLstA, self._sf_rLstB, self._sf_rLstC, self._sf_rLstD, self._sf_rLstE = [],[],[],[],[]
        self._sf_rIntA, self._sf_rIntB, self._sf_rIntC, self._sf_rIntD, self._sf_rIntE = 0, 0, 0, 0, 0
        self._sf_rIntG = len(self._sf_sLstX)
        self._sf_rLstF = []
        for self._sf_rIntF in range(self._sf_rIntG):
            if isinstance(self._sf_sLstX[self._sf_rIntF], (int, float)): self._sf_rLstF.append(str(self._sf_sLstX[self._sf_rIntF]))
            else:
                if self._sf_sLstX[self._sf_rIntF].find('NTC.-:=:*.') > -1: self._sf_rLstA.append(self._sf_sLstX[self._sf_rIntF][10:])
                elif self._sf_sLstX[self._sf_rIntF].find('NTL.-:=:*.') > -1: self._sf_rLstB.append(self._sf_sLstX[self._sf_rIntF][10:])
                elif self._sf_sLstX[self._sf_rIntF].find('SKR.-:=:*.') > -1: self._sf_rLstC.append(self._sf_sLstX[self._sf_rIntF][10:])
                elif self._sf_sLstX[self._sf_rIntF].find('FWD.-:=:*.') > -1: self._sf_rLstD.append(self._sf_sLstX[self._sf_rIntF][10:])
                elif self._sf_sLstX[self._sf_rIntF].find('REV.-:=:*.') > -1: self._sf_rLstE.append(self._sf_sLstX[self._sf_rIntF][10:])
        self._sf_rIntG-=1
        self._sf_rIntF = 0
        self._sf_rIntH = -1
        self._sf_rLstG = []
        self._sf_sBoolX = [False]*2
        self._sf_rLstH = [len(self._sf_rLstA),len(self._sf_rLstB),len(self._sf_rLstC),len(self._sf_rLstD),len(self._sf_rLstE),len(self._sf_rLstF)]
        while 1:
            if not self._sf_sBoolX[0] and self._sf_rIntA < self._sf_rLstH[0]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstA[self._sf_rIntA])
                self._sf_sBoolX[0] = True
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(1)
            elif not self._sf_sBoolX[0] and self._sf_rIntB < self._sf_rLstH[1]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstB[self._sf_rIntB])
                self._sf_sBoolX[0] = True
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(2)
            if self._sf_sBoolX[0] and self._sf_rIntD < self._sf_rLstH[3]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstD[self._sf_rIntD])
                self._sf_sBoolX[0] = False
                self._sf_sBoolX[1] = True
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(4)
            elif self._sf_rIntD < self._sf_rLstH[3]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstD[self._sf_rIntD])
                self._sf_sBoolX[1] = True
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(4)
            if self._sf_rIntF < self._sf_rLstH[5]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstF[self._sf_rIntF])
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(6)
            if not self._sf_sBoolX[0] and self._sf_sBoolX[1] and self._sf_rIntE < self._sf_rLstH[4]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstE[self._sf_rIntE])
                self._sf_sBoolX[1] = False
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(5)
            elif self._sf_sBoolX[0] and self._sf_rIntE < self._sf_rLstH[4]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(True, self._sf_rLstE[self._sf_rIntE])
                self._sf_sBoolX[0] = False
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(5)
            if self._sf_rIntC < self._sf_rLstH[2]:
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(False, self._sf_rLstC[self._sf_rIntC])
                self.sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(3)
            if self._sf_rIntH == self._sf_rIntG:
                break
            else: self._sf_sBoolX[0], self._sf_sBoolX[1] = False, False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_apd(self, isRla: bool, mtchDt):
        # FNC_ID=ST12-63787847672650
        # SqtppFncs slots in use: (_sf_rIntI, _sf_rIntJ, _sf_rLstG, _sf_rLstI)
        # returns: (none)
        if mtchDt.find(',') > -1:
            self._sf_rLstI = mtchDt.split(',')
            self._sf_rIntJ = len(self._sf_rLstI)
            for self._sf_rIntI in range(self._sf_rIntJ):
                if len(self._sf_rLstI[self._sf_rIntI]) > 0:
                    if not isRla: self._sf_rLstG.append(self._sf_rLstI[self._sf_rIntI])
                    else: self._sf_rLstG.append(f'^;^{self._sf_rLstI[self._sf_rIntI]}')
        else:
            if not isRla: self._sf_rLstG.append(mtchDt)
            else: self._sf_rLstG.append(f'^;^{mtchDt}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_genesis_ext_mup(self, dsg: int):
        # FNC_ID=ST12-30228206637146
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntH)
        # returns: (none)
        if dsg == 1: self._sf_rIntA+=1
        elif dsg == 2: self._sf_rIntB+=1
        elif dsg == 3: self._sf_rIntC+=1
        elif dsg == 4: self._sf_rIntD+=1
        elif dsg == 5: self._sf_rIntE+=1
        elif dsg == 6: self._sf_rIntF+=1
        self._sf_rIntH+=1
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_err(self, errCd: int):
        # FNC_ID=ST12-77376225068820
        # SqtppFncs slots in use: (_sf_sVn)
        # returns:
        # 1=mnt not found from last mnt used read setting
        # 2=dir not found from last dir used read setting
        # 3=variable name is of invalid chars
        # 4=variable data is not a string or list
        # 5=variable data missing proper search pairing brackets
        # 6=empty search data string pattern
        # 7=empty vfs path settings file
        # 8=invalid vfs path
        # 9=@vrNm already present in tqpt file
        if errCd == 1:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, vfs mount was not found from last mount used in vfs m/d/f setting, current set sqtpp vfs file may be corrupted...')
        elif errCd == 2:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, vfs mount/directory was not found from last mount/directory used in vfs m/d/f setting, current set sqtpp vfs file may be corrupted...')
        elif errCd == 3:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, @varName has invalid chars, valid chars are _ a-z A-Z 0-9')
        elif errCd == 4:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, invalid search construct, @varData must be either a list of str elements or a single str type')
        elif errCd == 5:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, @varData is missing proper brackets for a "next.omega" search & match, see IMPORT_CALLS.TXT')
        elif errCd == 6:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, @varData cannot be None for a "next.omega" call, see IMPORT_CALLS.TXT')
        elif errCd == 7:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, unexpected error, empty vfs path settings file found!')
        elif errCd == 8:
            raise Exception('[sqtpp-vfs >> pojishon] - next.omega, unexpexted error, missing vfs file for .../staqtapp1_2 directory set path!')
        elif errCd == 9:
            raise Exception(f'[sqtpp-vfs >> pojishon] - next.omega, ctpk omega type env-var "{self._sf_sVn}" is already listed as a env-var name in the current set vfs/tqpt file, cannot overwrite ctpk omega type env-var, must be removed first by an admin decision')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_scnr(self, luf: list, vrNm: str, vrDt: str):
        # FNC_ID=ST12-25063980369720
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_rLstG, _sf_rLstH, _sf_rLstI, _sf_rStrD, _sf_rStrF, _sf_sLstX, _sf_sVn)
        # returns:
        # -1=empty search data string pattern
        rtrn = 1
        self._sf_sVn = f'{vrNm}_ctpk_0'
        self.sqtpp_emb_ext_vfs_set_file_list(True, luf[1], self._sf_rStrF)
        self._sf_rIntD = len(self._sf_rLstC)
        self._sf_sRplc = self._sf_rLstC
        self._sf_sIntX = -1
        self._sf_rLstF = []
        for self._sf_rIntC in range(self._sf_rIntD): self._sf_rLstF.append(self.sqtpp_emb_ext_vfs_get_file(self._sf_rLstC[self._sf_rIntC], self._sf_rStrF).replace(f'<{self._sf_rLstC[self._sf_rIntC]}:S:\n','').replace(':|:>',''))
        self.sqtpp_emb_vfs_pojishon_omega_ctpk_spdr(vrDt)
        if len(self._sf_rStrD) > 0:
            self._sf_rLstE = [':^%/F/W/D/=',':^%/R/E/V/=',':^%/N/T/C/=',':^%/N/T/L/=',':^%/N/A/B/=',':^%/N/A/L/=']
            self._sf_rIntF = sum(self._sf_rStrD.count(qp) for qp in self._sf_rLstE)
            self._sf_rStrD = f'~{self._sf_rStrD}:^%'
            self._sf_rIntD = len(self._sf_rLstF)
            self._sf_rBoolD = [False, False]
            self._sf_sLstX = []
            for self._sf_rIntC in range(self._sf_rIntD):
                self._sf_rStrF = self._sf_rLstF[self._sf_rIntC].replace('\n',' ')
                self._sf_rLstB, self._sf_rLstC, self._sf_rLstD, self._sf_rLstG, self._sf_rLstH, self._sf_rLstI = [-1],[-1],[-1],[-1],[-1],[-1]
                for self._sf_rIntE in range(self._sf_rIntF):
                    self._sf_rBoolD[0] = False
                    self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[2], self._sf_rLstD[len(self._sf_rLstD)-1]+1)
                    if not self._sf_rIntG in self._sf_rLstD: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(1)
                    if not self._sf_rBoolD[0]:
                        self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[3], self._sf_rLstG[len(self._sf_rLstG)-1]+1)
                        if not self._sf_rIntG in self._sf_rLstG: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(2)
                        if not self._sf_rBoolD[0]:
                            self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[0], self._sf_rLstB[len(self._sf_rLstB)-1]+1)
                            if not self._sf_rIntG in self._sf_rLstB: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(3)
                            if not self._sf_rBoolD[0]:
                                self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[4], self._sf_rLstH[len(self._sf_rLstH)-1]+1)
                                if not self._sf_rIntG in self._sf_rLstH: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(4)
                                if not self._sf_rBoolD[0]:
                                    self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[1], self._sf_rLstC[len(self._sf_rLstC)-1]+1)
                                    if not self._sf_rIntG in self._sf_rLstC: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(5)
                                    if not self._sf_rBoolD[0]:
                                        self._sf_rIntG = self._sf_rStrD.find(self._sf_rLstE[5], self._sf_rLstI[len(self._sf_rLstI)-1]+1)
                                        if not self._sf_rIntG in self._sf_rLstI: self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(6)
        else: rtrn = -1
        return rtrn 
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_srch(self, dsg: int):
        # FNC_ID=ST12-67372420340719
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntG, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstG, _sf_rLstH, _sf_rLstI)
        # returns: (none)
        self._sf_rBoolD[0] = True
        if dsg == 1:
            self._sf_rLstD.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/N\/T\/C\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'NTC')
        elif dsg == 2:
            self._sf_rLstG.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/N\/T\/L\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'NTL')
        elif dsg == 3:
            self._sf_rLstB.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/F\/W\/D\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'FWD')
        elif dsg == 4:
            self._sf_rLstH.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/N\/A\/B\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'NAB')
        elif dsg == 5:
            self._sf_rLstC.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/R\/E\/V\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'REV')
        elif dsg == 6:
            self._sf_rLstI.append(self._sf_rIntG)
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(r':\^%\/N\/A\/L\/=.*?:\^%')
            self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(False, 'NAL')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad(self, isPck: bool, dsgStr: str):
        # FNC_ID=ST12-87602220811041
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntC, _sf_rStrC, _sf_rStrE, _sf_rStrF, _sf_sIntX, _sf_sLstA, _sf_sLstX, _sf_sVn)
        # returns: (none)
        swA = True
        if not self._sf_rBoolD[1]:
            try:
                if self._sf_rStrF.find(self._sf_rStrE) > -1:
                    if dsgStr != 'NTL' and dsgStr != 'NAB' and dsgStr != 'NAL':
                        self._sf_sLstX.append(f'{dsgStr}.-:=:*.{self._sf_rStrE}')
                        self._sf_sIntX = self._sf_rIntC
                    else:
                        if dsgStr == 'NTL':
                            if set(self._sf_rStrE).issubset(SQTPP_SET_NMB):
                                self._sf_sLstX.append(f'SKR.-:=:*.{self._sf_rStrE}')
                                self._sf_sIntX = self._sf_rIntC
                            else:
                                self._sf_rStrE = re.findall(r'\d+', self._sf_rStrE)
                                if len(self._sf_rStrE) > 0:
                                    self._sf_sLstX.append(f'{dsgStr}.-:=:*.{"".join(self._sf_rStrE)}')
                                    self._sf_sIntX = self._sf_rIntC
                        elif dsgStr == 'NAB' or dsgStr == 'NAL':
                            self._sf_rStrC = set('.1234567890')
                            if dsgStr == 'NAB':
                                self._sf_rStrE = self._sf_rStrE.replace(' ','')
                                if set(self._sf_rStrE).issubset(self._sf_rStrC): self._sf_rStrE = float(self._sf_rStrE)
                                elif set(self._sf_rStrE).issubset(SQTPP_SET_NMB): self._sf_rStrE = int(self._sf_rStrE)
                                else: swA = False
                                if swA:
                                    self._sf_sLstX.append(self._sf_rStrE)
                                    self._sf_sIntX = self._sf_rIntC
                            else:
                                if self.sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad_nal():
                                    self._sf_sIntX = self._sf_rIntC
                                    self._sf_sLstA = list(self._sf_sLstA)
                                    self.sqtpp_emb_vfs_pojishon_omega_ctpk_next_reg_key_name()
                                    self.sqtpp_registry_homer(False, self._sf_sVn, self._sf_sLstA, '__sqtpp__default__omega__key__')
            except Exception as err_ctpk_scnr_rad_fnd:
                pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_rad_nal(self) -> bool:
        # FNC_ID=ST12-81973634278148
        # SqtppFncs slots in use: (_sf_rIntH, _sf_rIntI, _sf_rIntJ, _sf_rIntK, _sf_rLstJ, _sf_rStrB, _sf_rStrC, _sf_rStrE, _sf_rStrF, _sf_sLstA)
        # returns: (True or False)
        rtrn = False
        self._sf_rStrB = re.findall(r'\(' + re.escape(self._sf_rStrE) + r'.*?\)', self._sf_rStrF)
        if len(self._sf_rStrB) > 0:
            self._sf_sLstA = set()
            self._sf_rIntI = len(self._sf_rStrB)
            for self._sf_rIntH in range(self._sf_rIntI):
                self._sf_rStrB[self._sf_rIntH] = self._sf_rStrB[self._sf_rIntH].replace('(','').replace(')','')
                if self._sf_rStrB[self._sf_rIntH].find(',') > -1: self._sf_rLstJ = self._sf_rStrB[self._sf_rIntH].split(',')
                else: self._sf_rLstJ = [self._sf_rStrB[self._sf_rIntH]]
                self._sf_rIntK = len(self._sf_rLstJ)
                for self._sf_rIntJ in range(self._sf_rIntK):
                    self._sf_rLstJ[self._sf_rIntJ] = self._sf_rLstJ[self._sf_rIntJ].replace(' ','')
                    if len(self._sf_rLstJ[self._sf_rIntJ]) > 0:
                        if set(self._sf_rLstJ[self._sf_rIntJ]).issubset(self._sf_rStrC):
                            if not rtrn: rtrn = True
                            self._sf_sLstA.add(float(self._sf_rLstJ[self._sf_rIntJ]))
                        elif set(self._sf_rLstJ[self._sf_rIntJ]).issubset(SQTPP_SET_NMB):
                            if not rtrn: rtrn = True
                            self._sf_sLstA.add(int(self._sf_rLstJ[self._sf_rIntJ]))
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_scnr_ext_fss(self, ptrn: str):
        # FNC_ID=ST12-38064561646360
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntG, _sf_rStrD, _sf_rStrE)
        # returns: (none)
        self._sf_rStrE = re.search(ptrn, self._sf_rStrD[self._sf_rIntG:])
        ptrn = ptrn.replace('\u005C','').replace('.*?:^%','')
        self._sf_rStrE = self._sf_rStrE.group().replace(ptrn,'')
        self._sf_rBoolD[1] = False
        if len(self._sf_rStrE) > 0:
            self._sf_rStrE = self._sf_rStrE[:len(self._sf_rStrE)-3]
            if self._sf_rStrE == '|:': self._sf_rBoolD[1] = True
        else: self._sf_rBoolD[1] = True
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_spdr(self, vrDt):
        # FNC_ID=ST12-17602015027970
        # SqtppFncs slots in use: (_sf_rBoolC, _sf_rBoolD, _sf_rIntC, _sf_rIntD, _sf_rStrD, _sf_rStrE, _sf_sLstX)
        # returns:  _sf_rStrD=
        #           (FWD=forward txt search, REV=reverse txt search, NTC=neutral curly
        #            brackets search, NTL=neutral line brackets search[numbers apply],
        #            NAB=numerical block search, NAL=numerical list ordered search)
        self._sf_rIntC = -1
        self._sf_rStrD = ''
        self._sf_rIntD = None
        self._sf_rBoolC = False
        self._sf_rBoolD = [False]*6
        for self._sf_rStrE in vrDt:
            self._sf_rIntC+=1
            if self._sf_rBoolD[2]: self._sf_rBoolD[2] = False
            if self._sf_rBoolD[3] or self._sf_rBoolD[4]:
                if self._sf_rIntC > self._sf_rIntD:
                    if self._sf_rBoolD[3]: self.sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_clb_end(']')
                    else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_clb_end('}')
            else:
                if not self._sf_rBoolC and not self._sf_rBoolD[0] and not self._sf_rBoolD[1] and self._sf_rStrE == '|':
                    try:
                        if vrDt[self._sf_rIntC+1] == ':' and vrDt[self._sf_rIntC+2] == '{' and vrDt[self._sf_rIntC+3] == ':':
                            self._sf_rBoolD[3] = True
                            self._sf_rStrD = f'{self._sf_rStrD}:^%/N/A/B/='
                        elif vrDt[self._sf_rIntC+1] == ':' and vrDt[self._sf_rIntC+2] == '[' and vrDt[self._sf_rIntC+3] == ':':
                            self._sf_rBoolD[4] = True
                            self._sf_rStrD = f'{self._sf_rStrD}:^%/N/A/L/='
                        if self._sf_rBoolD[3] or self._sf_rBoolD[4]:
                            self._sf_sLstX = []
                            self._sf_rIntD = self._sf_rIntC+3
                    except Exception as err_lte:
                        self._sf_rBoolC = True
            if not self._sf_rBoolD[3] and not self._sf_rBoolD[4]:
                if not self._sf_rBoolD[1] and self._sf_rStrE == '{':
                    self._sf_sLstX = []
                    self._sf_rBoolD[0] = True
                    self._sf_rStrD = f'{self._sf_rStrD}:^%/F/W/D/='
                elif self._sf_rBoolD[0]:
                    if self._sf_rStrE == ']':
                        self._sf_rIntD = 2
                        self._sf_rBoolD[2] = True
                        self._sf_rBoolD[5] = True
                        self._sf_rBoolD[0] = False
                        self._sf_rStrD = f'{self._sf_rStrD}{"".join(self._sf_sLstX)}'
                    else: self._sf_sLstX.append(self._sf_rStrE)
                if not self._sf_rBoolD[2] and not self._sf_rBoolD[0] and self._sf_rStrE == '[':
                    self._sf_sLstX = []
                    self._sf_rBoolD[1] = True
                    self._sf_rStrD = f'{self._sf_rStrD}:^%/R/E/V/='
                elif self._sf_rBoolD[1]:
                    if self._sf_rStrE == '}':
                        self._sf_rIntD = 1
                        self._sf_rBoolD[5] = True
                        self._sf_rBoolD[1] = False
                        self._sf_rStrD = f'{self._sf_rStrD}{"".join(self._sf_sLstX)}'
                    else: self._sf_sLstX.append(self._sf_rStrE)
            if self._sf_rBoolD[5]:
                self._sf_rBoolD[5] = False
                if self._sf_rIntD == 1: self.sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_ntc_ntl(vrDt, '^%/N/T/C/', r'\}.*?\{')
                else: self.sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_ntc_ntl(vrDt, '^%/N/T/L/', r'\].*?\[')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_clb_end(self, dsgBrkt: str):
        # FNC_ID=ST12-79377023287442
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntD, _sf_rStrD, _sf_rStrE, _sf_sLstX)
        # returns: (none)
        if self._sf_rStrE == dsgBrkt:
            if dsgBrkt == '}': self._sf_rIntD = 1
            else: self._sf_rIntD = 2
            self._sf_rBoolD[5] = True
            if self._sf_rIntD == 1: self._sf_rBoolD[4] = False
            else: self._sf_rBoolD[3] = False
            self._sf_rStrD = f'{self._sf_rStrD}{"".join(self._sf_sLstX)}'
        else: self._sf_sLstX.append(self._sf_rStrE)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_spdr_ext_ntc_ntl(self, vrDt: str, dsg: str, ptrn: str):
        # FNC_ID=ST12-23664466477756
        # SqtppFncs slots in use: (_sf_rIntC, _sf_rStrD, _sf_sLstX)
        # returns: (none)
        self._sf_sLstX = re.search(ptrn, vrDt[self._sf_rIntC:], re.IGNORECASE)
        if self._sf_sLstX:
            self._sf_sLstX = self._sf_sLstX.group().replace(f'{ptrn[1]}','').replace(f'{ptrn[6]}','')
            self._sf_rStrD = f'{self._sf_rStrD}:{dsg}={self._sf_sLstX}'
            self._sf_rStrD = self._sf_rStrD.replace(':/N/T/C/=|:','').replace(':/N/T/L/=|:','')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_omega_ctpk_next_reg_key_name(self):
        # FNC_ID=ST12-26643611230867
        # SqtppFncs slots in use: (_sf_sVn)
        # returns: (none)
        self._rg_rStrA = re.search(r'_(\d+)$', self._sf_sVn)
        self._rg_rIntA = int(self._rg_rStrA.group(1))
        self._rg_rIntA+=1
        self._sf_sVn = re.sub(r'_(\d+)$', f'_{self._rg_rIntA}', self._sf_sVn)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_opt_open(self) -> bool:
        # FNC_ID=ST12-83487123024989
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rStrA, _sf_rStrB, _sf_sLstX, _sf_sQp, _sf_sSrc, _sf_sVd, _sf_sVfs)
        # returns: (True or False)
        swVarDt = False
        swOcrBp = False
        swVarCd = False
        try:
            self._sf_rLstB = ast.literal_eval(self._sf_rLstD[1])
        except Exception as open_opt_param1_err:
            raise Exception(f'[sqtpp-vfs >> pojishon] - open optional param1/ast conversion err: {open_opt_param1_err}, "{self._sf_rLstD[1]}"')
        try:
            self._sf_rLstC = ast.literal_eval(self._sf_rLstD[2])
        except Exception as open_opt_param2_err:
            raise Exception(f'[sqtpp-vfs >> pojishon] - open optional param2/ast conversion err: {open_opt_param2_err}, "{self._sf_rLstD[2]}"')
        self._sf_rIntB = len(self._sf_rLstB)
        self._sf_rIntA = 0
        self._sf_rIntC = 0
        if self._sf_rIntB > 0:
            if isinstance(self._sf_rLstB, list):
                while self._sf_rIntA < self._sf_rIntB:
                    if isinstance(self._sf_rLstB[self._sf_rIntA], str):
                        if self._sf_rLstB[self._sf_rIntA].find('@qp(') > -1 and self._sf_rLstB[self._sf_rIntA].find('):') > -1: self._sf_rIntC+=1
                    else:
                        raise Exception('[sqtpp-vfs >> pojishon] - open optional param1 list element(s) must be all string type')
                    self._sf_rIntA+=1
                if self._sf_rIntC > 0:
                    if self._sf_rIntC == self._sf_rIntB: swVarDt = True
                    else:
                        raise Exception('[sqtpp-vfs >> pojishon] - open optional param1 has @qp(...): tagged search list element(s) for @varDt open find & add, yet is missing proper qp-tagging for all list elements')
            else:
                raise Exception('[sqtpp-vfs >> pojishon] - open optional param1 is not a list type, see IMPORT_CALLS.TXT')
        else:
            raise Exception('[sqtpp-vfs >> pojishon] - open optional param1 has no list element(s) see IMPORT_CALLS.TXT')
        self._sf_rIntB = len(self._sf_rLstC)
        if self._sf_rIntB > 0:
            if isinstance(self._sf_rLstC, list):
                if self._sf_rIntB == 1 and isinstance(self._sf_rLstC[0], str):
                    if self._sf_rLstC[0] == '*': swOcrBp = True
                else:
                    self._sf_rIntA = 0
                    while self._sf_rIntA < self._sf_rIntB:
                        if not isinstance(self._sf_rLstC[self._sf_rIntA], int):
                            raise Exception('[sqtpp-vfs >> pojishon] - open optional param2 must be a list of int number(s) for any tqpt env-var data add length cutoff(s) see IMPORT_CALLS.TXT')
                        self._sf_rIntA+=1
            else:
                raise Exception('[sqtpp-vfs >> pojishon] - open optional param2 is not a list type, see IMPORT_CALLS.TXT')
        else:
            raise Exception('[sqtpp-vfs >> pojishon] - open optional param2 has no list element(s) see IMPORT_CALLS.TXT')
        if swVarDt: self._sf_rLstD = self.sqtpp_emb_vfs_pojishon_opt_tqpt_search(True, True, True, self._sf_rLstB, None)
        else: self._sf_rLstD = self.sqtpp_emb_vfs_pojishon_opt_tqpt_search(False, True, True, self._sf_rLstB, self._sf_rLstC)
        if len(self._sf_rLstD) > 0:
            self._sf_rIntD = -1
            self._sf_rStrA = self._sf_sQp
            self._sf_rIntB = len(self._sf_rLstD)
            for self._sf_rIntA in range(self._sf_rIntB):
                self._sf_rLstE = self._sf_rLstD[self._sf_rIntA].split(".>:<.")
                self._sf_rIntC = int(self._sf_rLstE[0])
                self._sf_rBoolA = False
                if self._sf_rLstE[1].find('@qp(') > -1:
                    self._sf_rLstE = [self._sf_rLstE[1]]
                    swVarCd = True
                else:
                    if self._sf_rLstE[1].find('\n') > -1 and self._sf_rLstE[1].find(',') > -1:
                        self._sf_rLstE = [e for nlS in self._sf_sVd.split('\n') for e in nlS.split(',')]
                        self._sf_rBoolA = True
                    elif self._sf_rLstE[1].find('\n') > -1:
                        self._sf_rLstE = self._sf_rLstE[1].split('\n')
                        self._sf_rBoolA = True
                    elif self._sf_rLstE[1].find(',') > -1:
                        self._sf_rLstE = self._sf_rLstE[1].split(',')
                        self._sf_rBoolA = True
                    else: self._sf_rLstE = [self._sf_rLstE[1]]
                if not swVarCd and swOcrBp:
                    if swVarDt: self.sqtpp_emb_vfs_pojishon_opt_open_ext()
                else:
                    if swVarDt:
                        self._sf_rIntD+=1
                        if self._sf_rIntD < len(self._sf_rLstC):
                            if self._sf_rBoolA:
                                self._sf_rIntF = len(self._sf_rLstE)
                                for self._sf_rIntE in range(self._sf_rIntF):
                                    try:
                                        self._sf_rLstE[self._sf_rIntE] = self._sf_rLstE[self._sf_rIntE][0:self._sf_rLstC[self._sf_rIntD]]
                                        self._sf_rLstE[self._sf_rIntE] = f'@qp({self._sf_rLstE[self._sf_rIntE]}):'
                                    except Exception as opt_opn_ocr_slc_err:
                                        raise Exception(f'[sqtpp-vfs >> pojishon] - invalid index occurence length({self._sf_rLstC[self._sf_rIntD]}) for an add tqpt env-var data sliced @ length({len(self._sf_rLstE[self._sf_rIntE])})')
                            else:
                                try:
                                    self._sf_rLstE[0] = self._sf_rLstE[0][0:self._sf_rLstC[self._sf_rIntD]]
                                    self._sf_rLstE[0] = f'@qp({self._sf_rLstE[0]}):'
                                except Exception as opt_opn_ocr_slc_err:
                                    raise Exception(f'[sqtpp-vfs >> pojishon] - invalid index occurence length({self._sf_rLstC[self._sf_rIntD]}) for an add tqpt env-var data sliced @ length({len(self._sf_rLstE[0])})')
                        else: self.sqtpp_emb_vfs_pojishon_opt_open_ext()
                    else:
                        if not swVarCd: self.sqtpp_emb_vfs_pojishon_opt_open_ext()
                self._sf_rStrB = self._sf_sLstX[self._sf_rIntC].replace('):>','')
                if self._sf_rBoolA: self._sf_rStrB = f'{self._sf_rStrB}):{"".join(self._sf_rLstE)}>'
                else: self._sf_rStrB = f'{self._sf_rStrB}):{self._sf_rLstE[0]}>'
                self._sf_sQp = self._sf_sQp.replace(self._sf_sLstX[self._sf_rIntC], self._sf_rStrB)
            self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrA, self._sf_sQp)
            self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
            self._sf_sLstX = None
            self._sf_sSrc = None
            self._sf_sQp = None
            return True
        else:
            return False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_opt_open_ext(self):
        # FNC_ID=ST12-12081513214724
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntE, _sf_rIntF, _sf_rLstE)
        # returns: (none)
        if self._sf_rBoolA:
            self._sf_rIntF = len(self._sf_rLstE)
            for self._sf_rIntE in range(self._sf_rIntF): self._sf_rLstE[self._sf_rIntE] = f'@qp({self._sf_rLstE[self._sf_rIntE]}):'
        else: self._sf_rLstE[0] = f'@qp({self._sf_rLstE[0]}):'
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_opt_closed(self) -> bool:
        # FNC_ID=ST12-91962393199835
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rBoolE, _sf_rIntA, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rLstF, _sf_rStrB, _sf_rStrF, _sf_sLstX, _sf_sQp, _sf_sSrc, _sf_sStrX, _sf_sVd, _sf_sVfs, _sf_sVfsDir)
        # returns: (True or False)
        ocFncLstA = None
        try:
            self._sf_rLstD[1] = self._sf_rLstD[1].replace(' ','')
            self._sf_rLstB = ast.literal_eval(self._sf_rLstD[1])
        except Exception as closed_opt_param1_err:
            raise Exception(f'[sqtpp-vfs >> pojishon] - closed optional param1/ast conversion err: {closed_opt_param1_err}, "{self._sf_rLstD[1]}"')
        try:
            self._sf_rLstD[2] = self._sf_rLstD[2].replace(' ','')
            self._sf_rLstC = ast.literal_eval(self._sf_rLstD[2])
        except Exception as closed_opt_param2_err:
            raise Exception(f'[sqtpp-vfs >> pojishon] - closed optional param2/ast conversion err: {closed_opt_param2_err}, "{self._sf_rLstD[2]}"')
        try:
            self._sf_rLstD[3] = self._sf_rLstD[3].replace(' ','')
            self._sf_rLstD = ast.literal_eval(self._sf_rLstD[3])
        except Exception as closed_opt_param3_err:
            raise Exception(f'[sqtpp-vfs >> pojishon] - closed optional param3/ast conversion err: {closed_opt_param3_err}, "{self._sf_rLstD[3]}"')
        swFncStr = False
        if len(self._sf_rLstB) > 0:
            if isinstance(self._sf_rLstB, str) or isinstance(self._sf_rLstB, list):
                if isinstance(self._sf_rLstB, str):
                    if self._sf_rLstB.find('=') > -1 and self._sf_rLstB.find(':') > -1: swFncStr = True
                if swFncStr:
                    if self._sf_rLstB.find('::') > -1: self._sf_rLstB = self._sf_rLstB.split('::')
                    else: self._sf_rLstB = [self._sf_rLstB]
                    self._sf_rIntF = len(self._sf_rLstB)
                    nclSet = set(':1234567890')
                    self._sf_rLstE = []
                    seVls = None
                    for self._sf_rIntA in range(self._sf_rIntF):
                        self._sf_rLstF = self._sf_rLstB[self._sf_rIntA].split('=')
                        if len(self._sf_rLstF) == 2:
                            if set(self._sf_rLstF[1]).issubset(nclSet):
                                self._sf_rLstB[self._sf_rIntA] = self._sf_rLstF[0]
                                seVls = self._sf_rLstF[1].split(':')
                                if len(seVls) == 2:
                                    seVls[0] = int(seVls[0])
                                    seVls[1] = int(seVls[1])
                                    if seVls[0] < seVls[1]: self._sf_rLstE.append(f'{seVls[0]}:{seVls[1]}')
                                    else:
                                        raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 has invalid #start:#end value(s) start index must be lesser than end index')
                                else:
                                    raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 has missing #start:#end format(s) see IMPORT_CALLS.TXT')
                            else:
                                raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 has invalid #start:#end format(s) only numbers or ":" allowed, see IMPORT_CALLS.TXT')
                        else:
                            raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 is an invalid closed phase string declaring, see IMPORT_CALLS.TXT')
                else:
                    if isinstance(self._sf_rLstC, int) and isinstance(self._sf_rLstD, int):
                        if isinstance(self._sf_rLstB, str): self._sf_rLstB = [self._sf_rLstB]
                        if self._sf_rLstC < self._sf_rLstD: self._sf_rLstE = [self._sf_rLstC, self._sf_rLstD]
                        else:
                            raise Exception('[sqtpp-vfs >> pojishon] - closed optional param2 & param3 are invalid #start to #end value(s) start index must be lesser than end index')
                        self._sf_rIntF = len(self._sf_rLstB)
                    else:
                        raise Exception('[sqtpp-vfs >> pojishon] - closed optional param2 & param3 must be of an int type only, see IMPORT_CALLS.TXT')
                self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
                self.sqtpp_vfs_tqpt_file(True)
                qpEntVld = self.sqtpp_emb_vfs_pojishon_skip_srch()
                self._sf_rIntD = len(self._sf_sLstX)
                self._sf_rStrB = self._sf_sLstX
                self._sf_rBoolD = False
                self._sf_rBoolE = False
                swRdLstF = True
                for self._sf_rIntC in range(self._sf_rIntD):
                    if qpEntVld[self._sf_rIntC]:
                        self._sf_rIntE = 0
                        while self._sf_rIntE < self._sf_rIntF:
                            if self._sf_sLstX[self._sf_rIntC].find(f'{self._sf_rLstB[self._sf_rIntE]}<@qp(') > -1:
                                if swFncStr:
                                    ocFncLstA = self._sf_rLstE[self._sf_rIntE].split(':')
                                    self._sf_rIntG = self.sqtpp_emb_vfs_pojishon_opt_file_search(swRdLstF, 1, self._sf_rIntC, int(ocFncLstA[0]), int(ocFncLstA[1]))
                                else: self._sf_rIntG = self.sqtpp_emb_vfs_pojishon_opt_file_search(swRdLstF, 1, self._sf_rIntC, self._sf_rLstE[0], self._sf_rLstE[1])
                                if self._sf_rIntG == 2:
                                    if not self._sf_rBoolD: self._sf_rBoolD = True
                                    if not self._sf_rBoolE: self._sf_rBoolE = True
                                elif self._sf_rIntG == 3:
                                    if not self._sf_rBoolE: self._sf_rBoolE = True
                                elif self._sf_rIntG == 1:
                                    if not self._sf_rBoolD: self._sf_rBoolD = True
                                if swRdLstF: swRdLstF = False
                            self._sf_rIntE+=1
                if not self._sf_rBoolD and not self._sf_rBoolE:
                    return False
                else:
                    if self._sf_rBoolE:
                        self._sf_sSrc = self._sf_sSrc.replace('\n'.join(self._sf_rStrB), '\n'.join(self._sf_sLstX))
                        self._sf_rStrB = None
                        self._sf_sLstX = None
                    if self._sf_rBoolD:
                        self._sf_rStrF = self._sf_sStrX
                        self.sqtpp_emb_ext_vfs_edit_file(self._sf_sVfsDir, self._sf_sVd)
                        self._sf_sSrc = self._sf_sSrc.replace(self._sf_rStrF, self._sf_sStrX)
                        self._sf_rStrF = None
                        self._sf_sStrX = None
                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                    self._sf_sSrc = None
                    self._sf_sQp = None
                    return True
            else:
                raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 is neither str type or a list type, see IMPORT_CALLS.TXT')
        else:
            raise Exception('[sqtpp-vfs >> pojishon] - closed optional param1 is invalid, see IMPORT_CALLS.TXT')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_write_stgs(self, dsg: int, dirLst: list):
        # <<<
        # returns: (none)
        if dsg == 1: # Last file added path.
            if self._sf_sDv.find('__|::|STGS<:\n<STGS:S:\nnone:|:>') > -1: self._sf_sStrX = self._sf_sStrX.replace('<STGS:S:\nnone:|:>', '<STGS:S:\nlfd=' + '/'.join(dirLst) + ';:|:>')
            else:
                self._sf_rLstB = re.findall(r'lfd=.*?\;', self._sf_sDv)
                self._sf_rStrB = self._sf_sDv
                if len(self._sf_rLstB) > 0: self._sf_sDv = self._sf_sDv.replace(self._sf_rLstB[0], f'lfd={"/".join(dirLst)};')
                else:
                    self._sf_sDv = self._sf_sDv.replace(':|:>','')
                    self._sf_sDv = self._sf_sDv + '\nlfd=' + '/'.join(dirLst) + ';:|:>'
                self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrB, self._sf_sDv)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_set_optional_list(self, optSrc: str):
        # FNC_ID=ST12-12510980977778
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstE, _sf_rStrB, _sf_rStrC)
        # returns: (_sf_rLstD=[optional name, ~params, ~...])
        self._sf_rLstB = deque()
        self._sf_rLstC = ['open','closed','compare','cache','seal','setfreq','removefreq','retag','quantumf']
        self._sf_rLstD = []
        self._sf_rLstE = [False, False, False, False]
        self._sf_rIntC = 0
        self._sf_rIntD = len(optSrc)-1
        for self._sf_rStrB in optSrc:
            if not self._sf_rLstE[1]:
                if self._sf_rStrB == '(':
                    self._sf_rIntA = 0
                    self._sf_rLstE[0] = True
                    self._sf_rStrC = ''.join(self._sf_rLstB)
                    while self._sf_rIntA < 9:
                        if self._sf_rStrC == self._sf_rLstC[self._sf_rIntA]:
                            self._sf_rLstD.append(self._sf_rStrC)
                            self._sf_rLstE[1] = True
                            self._sf_rLstB = deque()
                            break
                        self._sf_rIntA+=1
                else: self._sf_rLstB.append(self._sf_rStrB)
            else:
                if self._sf_rIntC == self._sf_rIntD:
                    if self._sf_rStrB == ')':
                        self._sf_rLstE[2] = True
                        self._sf_rStrC = ''.join(self._sf_rLstB)
                        if self._sf_rStrC.find(';') > -1:
                            self._sf_rLstB = self._sf_rStrC.split(';')
                            self._sf_rIntB = len(self._sf_rLstB)
                            if self._sf_rLstD[0] == 'open' or self._sf_rLstD[0] == 'cache':
                                if self._sf_rIntB == 2: self._sf_rLstE[3] = True
                            elif self._sf_rLstD[0] == 'closed' or self._sf_rLstD[0] == 'compare' or self._sf_rLstD[0] == 'setfreq' or self._sf_rLstD[0] == 'removefreq' or self._sf_rLstD[0] == 'quantumf':
                                if self._sf_rIntB == 3: self._sf_rLstE[3] = True
                            elif self._sf_rLstD[0] == 'seal' or self._sf_rLstD[0] == 'retag':
                                if self._sf_rIntB == 4: self._sf_rLstE[3] = True
                            if self._sf_rLstE[3]:
                                for self._sf_rIntA in range(self._sf_rIntB): self._sf_rLstD.append(self._sf_rLstB[self._sf_rIntA])
                        else:
                            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: invalid arguments for optional ({self._sf_rLstD[0]}) see IMPORT_CALLS.TXT')
                    else:
                        break
                else: self._sf_rLstB.append(self._sf_rStrB)
            self._sf_rIntC+=1
        if not self._sf_rLstE[0]:
            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: no begin arguments "(" for optional found')
        if not self._sf_rLstE[1]:
            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: no valid optional found, see IMPORT_CALLS.TXT')
        if not self._sf_rLstE[2]:
            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: no close arguments ")" for optional ({self._sf_rLstD[0]})')
        if not self._sf_rLstE[3]:
            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: number of arguments for optional ({self._sf_rLstD[0]}) is invalid, see IMPORT_CALLS.TXT')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_opt_file_search(self, isRdLstFile: bool, dsg: int, lstIdx, start: int, end: int) -> int:
        # FNC_ID=ST12-56193255559549
        # SqtppFncs slots in use: (_sf_rStrB, _sf_rStrC, _sf_sLstX, _sf_sVd, _sf_sVfsDir)
        # returns: (-1=no change, 1=changed file, 2=changed file & qp, 3=changed qp)
        if isRdLstFile:
            self._sf_sVfsDir = self.sqtpp_emb_vfs_pojishon_read(1)
            if isinstance(self._sf_sVfsDir, list):
                if self.sqtpp_emb_vfs_pojishon_read(2) != 1:
                    raise Exception('[sqtpp-vfs >> pojishon] - optional err: bad pojishon vfs mnt|dir|file path encountered, cannot read file for a optional search & find procedures')
            else:
                raise Exception('[sqtpp-vfs >> pojishon] - optional err: bad pojishon vfs mnt|dir|file path encountered, cannot read file for a optional search & find procedures')
        else:
            pass
        qpLst = None
        qpVnm = None
        qpLen = None
        qpRmLst = None
        qpChng = False
        flSlc = None
        flChng = False
        swLenCf = False
        swLenDa = False
        if dsg == 1: # file slice vs env-var's qp tagged data observe/close
            if start > -1 and end > start and end <= len(self._sf_sVd):
                qpLst = re.findall(r'@qp.*?\):', self._sf_sLstX[lstIdx])
                qpVnm = self._sf_sLstX[lstIdx].split('<')
                qpVnm = qpVnm[0]
                qpLen = len(qpLst)
                if len(qpLst) > 0:
                    flSlc = self._sf_sVd[start:end]
                    if len(flSlc) == len(self._sf_sVd): swLenCf = True
                    rmvEnvVar = False
                    rtSlc = flSlc
                    qpRmLst = []
                    for repcl in range(qpLen): qpLst[repcl] = qpLst[repcl].replace('@qp(','').replace('):','')
                    for qp in range(qpLen):
                        if qpLst[qp] == flSlc:
                            if not flChng: flChng = True
                            flSlc = flSlc.replace(qpLst[qp], '')
                            if not rmvEnvVar:
                                if not qpChng: qpChng = True
                                qpRmLst.append(qp)
                            if not rmvEnvVar and len(qpRmLst) == qpLen: rmvEnvVar = True
                            if swLenCf and len(flSlc) < 1:
                                swLenDa = True
                                break
                        else:
                            if flSlc.find(qpLst[qp]) > -1:
                                if not flChng: flChng = True
                                flSlc = flSlc.replace(qpLst[qp], '')
                                if swLenCf and len(flSlc) < 1:
                                    swLenDa = True
                                    break
                    if not flChng and not qpChng:
                        return -1
                    else:
                        rtrn = -1
                        if flChng:
                            rtrn = 1
                            if swLenDa: self._sf_sVd = 'none'
                            else: self._sf_sVd = self._sf_sVd.replace(rtSlc, flSlc)
                        if qpChng:
                            if rtrn == 1: rtrn = 2
                            else: rtrn = 3
                            if not rmvEnvVar:
                                if len(qpRmLst) > 0:
                                    for q in sorted(qpRmLst, reverse=True): qpLst.pop(q)
                                    for p in range(len(qpLst)): qpLst[p] = f'@qp({qpLst[p]}):'
                                    self._sf_sLstX[lstIdx] = f'{qpVnm}<{"".join(qpLst)}>'
                                else:
                                    if rtrn == 2: rtrn = 1
                                    elif rtrn == 3: rtrn = -1
                            else: self._sf_sLstX.pop(lstIdx)
                        return rtrn
                else:
                    return -1
            else:
                raise Exception('[sqtpp-vfs >> pojishon] - optional err: invalid start index or/and end index value(s) for a file data search length comparison with any qp tagged env-var data, see IMPORT_CALLS.TXT')
        elif dsg == 2:
            self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, lstIdx)
            if self._sf_rStrB != None:
                self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(lstIdx[1], self._sf_rStrB)
                if self._sf_rStrC != None:
                    return self.sqtpp_emb_vfs_file_lines_match(self._sf_sVd, self._sf_rStrC)
                else:
                    raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: sqtpp-vfs directory "{lstIdx[1]}" was not found')
            else:
                raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: sqtpp-vfs mount "{lstIdx[0]}" was not found')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_opt_tqpt_search(self, qpSrch: bool, setDirs: bool, setTqpt: bool, srchLst: list, occrLst: list) -> list:
        # FNC_ID=ST12-77514908040587
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rIntG, _sf_rIntH, _sf_rIntI, _sf_rLstE, _sf_rLstF, _sf_sLstX, _sf_sQp, _sf_sStrX, _sf_sVd)
        # returns: (qpFncRtn, slot sf_sLstX retains tqpt env-var stack after return)
        if setDirs: self.sqtpp_emb_vfs_router(False, True, False, 10, None, None, None)
        if setTqpt: self.sqtpp_vfs_tqpt_file(True)
        occrLen = None
        fsOcr = False
        swOcr = False
        qpFncRtn = []
        varFfdi = -1
        crIdx = None
        if occrLst != None:
            occrLen = len(occrLst)
            if occrLen == 1 and occrLst[0] == '*': fsOcr = True
        qpEntVld = self.sqtpp_emb_vfs_pojishon_skip_srch()
        self._sf_rIntI = len(self._sf_sLstX)
        self._sf_rIntD = len(srchLst)
        if self._sf_rIntD > 0:
            if self.sqtpp_emb_vfs_pojishon_read(2) != 1:
                raise Exception('[sqtpp-vfs >> pojishon] - optional err: bad pojishon vfs mnt|dir|file path encountered, cannot read file for a optional search & find procedures')
            self._sf_rBoolA = True
            for self._sf_rIntH in range(self._sf_rIntI):
                if qpEntVld[self._sf_rIntH]:
                    if not fsOcr or qpSrch:
                        self._sf_rLstF = re.findall(r'@qp.*?\):', self._sf_sLstX[self._sf_rIntH])
                        self._sf_rIntF = len(self._sf_rLstF)
                    if qpSrch:
                        for self._sf_rIntC in range(self._sf_rIntD):
                            if self._sf_rBoolA:
                                if srchLst[self._sf_rIntC].find('@qp(') > -1 and srchLst[self._sf_rIntC].find('):') > -1: srchLst[self._sf_rIntC] = srchLst[self._sf_rIntC].replace('@qp(','').replace('):','')        
                                else:
                                    raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: chosen param @varDt list, missing or invalid @qp(...): tagging @ list index({self._sf_rIntC}) <--> "{srchLst[self._sf_rIntC]}"')
                            if self._sf_rIntF > 0:
                                for self._sf_rIntE in range(self._sf_rIntF):
                                    self._sf_rLstF[self._sf_rIntE] = self._sf_rLstF[self._sf_rIntE].replace('@qp(','').replace('):','')
                                    if self._sf_rLstF[self._sf_rIntE].find(srchLst[self._sf_rIntC]) > -1:
                                        self._sf_rIntG = self._sf_sVd.find(srchLst[self._sf_rIntC])
                                        if self._sf_rIntG > -1:
                                            self._sf_sStrX = self.sqtpp_emb_vfs_pojishon_row_spdr(True, None, self._sf_rIntG+len(srchLst[self._sf_rIntC])-1, None)
                                            if self._sf_sStrX != None: qpFncRtn.append(f'{self._sf_rIntH}.>:<.{self._sf_sStrX}')
                        if self._sf_rBoolA: self._sf_rBoolA = False
                    else:
                        if not fsOcr:
                            crIdx = -1
                            swOcr = False
                            self._sf_sStrX = None
                        else: swOcr = False
                        for self._sf_rIntC in range(self._sf_rIntD):
                            if not fsOcr:
                                if not swOcr: crIdx+=1
                                else:
                                    break
                            else:
                                if swOcr:
                                    break
                            if self._sf_sLstX[self._sf_rIntH].find(f'{srchLst[self._sf_rIntC]}<@qp(') > -1:
                                if not fsOcr:
                                    if crIdx < occrLen:
                                        for self._sf_rIntE in range(self._sf_rIntF):
                                            self._sf_rLstF[self._sf_rIntE] = self._sf_rLstF[self._sf_rIntE].replace('@qp(','').replace('):','')
                                            if len(self._sf_sVd) > len(self._sf_rLstF[self._sf_rIntE]):
                                                self._sf_sStrX = self.sqtpp_emb_vfs_pojishon_row_spdr(False, self._sf_rLstF[self._sf_rIntE], None, occrLst[crIdx])
                                                if self._sf_sStrX != None:
                                                    swOcr = True
                                                    qpFncRtn.append(f'{self._sf_rIntH}.>:<.{self._sf_sStrX}')
                                                    break
                                        crIdx = -1
                                    else:
                                        raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: no pairing index found @occurence list; needed index[{crIdx}] but @occurence list has only a max indice[{occrLen-1}] read pairing')
                                else:
                                    if self._sf_sVd.find('\n') > -1 and self._sf_sVd.find(',') > -1: self._sf_rLstE = [e for nlS in self._sf_sVd.split('\n') for e in nlS.split(',')]
                                    elif self._sf_sVd.find('\n') > -1: self._sf_rLstE = self._sf_sVd.split('\n')
                                    elif self._sf_sVd.find(',') > -1: self._sf_rLstE = self._sf_sVd.split(',')
                                    else: self._sf_rLstE = [self._sf_sVd]
                                    qpFncRtn.append(f'{self._sf_rIntH}.>:<.')
                                    occrLen = len(self._sf_rLstE)
                                    varFfdi+=1
                                    for crIdx in range(occrLen):
                                        if len(self._sf_rLstE[crIdx]) > 0: qpFncRtn[varFfdi] = f'{qpFncRtn[varFfdi]}@qp({self._sf_rLstE[crIdx]}):'
                                    swOcr = True
            return qpFncRtn
        else:
            raise Exception('[sqtpp-vfs >> pojishon] - optional err: param @varDt list or @varNm list is missing, no string element(s) found')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_skip_srch(self) -> list:
        # FNC_ID=ST12-77901525334349
        # SqtppFncs slots in use: (_sf_sLstX, _sf_sQp)
        # returns:
        try:
            self._sf_sLstX = self._sf_sQp.split('\n')
            self._sf_sLstX.pop(0)
            rVarLen = len(self._sf_sLstX)
            if rVarLen < 2:
                raise Exception('[sqtpp-vfs >> pojishon] - insufficient tqpt form/qp tagged env-var(s) missing')
            rtrnLst = [True for _ in range(rVarLen)]
            uVarLst = ['~__globe__~<@qp(','__KLF__DSG__<@qp(','AbsSmvt','<@qp:...:vd(@qp(st1.2=','<@q|p(','<@q*p(']
            for x in range(rVarLen):
                vnm = 0
                while vnm < 6:
                    if self._sf_sLstX[x].find(uVarLst[vnm]) > -1:
                        rtrnLst[x] = False
                        break
                    vnm+=1
            return rtrnLst
        except Exception as skp_srch_err:
            raise Exception('[sqtpp-vfs >> pojishon] - insufficient tqpt form/qp tagged env-var(s) missing')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_file_lines_match(self, flSrc: str, dirSrc: str) -> list:
        # FNC_ID=ST12-49548506083528
        # SqtppFncs slots in use: (_sf_rBoolB, _sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rLstB, _sf_rLstC)
        # returns: (matching line(s) found or empty list)
        rtrnLst = []
        if flSrc.find('\n') > -1: flSrc = flSrc.split('\n')
        else: flSrc = [flSrc]
        self._sf_rIntF = len(flSrc)
        if self._sf_rIntF > 1: self._sf_rBoolB = True
        else: self._sf_rBoolB = False
        self._sf_rLstB = re.findall(r'<.*?\:\S\:', dirSrc)
        self._sf_rIntB = len(self._sf_rLstB)
        if self._sf_rIntB > 0:
            for self._sf_rIntA in range(self._sf_rIntB):
                self._sf_rLstB[self._sf_rIntA] = self._sf_rLstB[self._sf_rIntA].replace('<','').replace(':S:','')
                self._sf_rLstC = self.sqtpp_emb_ext_vfs_get_file(self._sf_rLstB[self._sf_rIntA], dirSrc)
                self._sf_rLstC = self._sf_rLstC.replace(':|:>','')
                self._sf_rLstC = self._sf_rLstC.split('\n')
                try:
                    self._sf_rLstC.pop(0)
                except Exception as flm_pop_err:
                    dirNm = re.findall(r'__\|::\|.*?<', dirSrc)
                    if len(dirNm) > 0: dirNm = dirNm[0].replace('__|::|','').replace('<','')
                    else: dirNm = '...'
                    raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: unable to read file ".../{dirNm}/{self._sf_rLstB[self._sf_rIntA]}" no file contents found!')
                self._sf_rIntD = len(self._sf_rLstC)
                for self._sf_rIntC in range(self._sf_rIntD):
                    if not self._sf_rBoolB:
                        if self._sf_rLstC[self._sf_rIntC] == flSrc[0]:
                            rtrnLst.append(self._sf_rLstC[self._sf_rIntC])
                            return rtrnLst
                    else:
                        for self._sf_rIntE in range(self._sf_rIntF):
                            if flSrc[self._sf_rIntE] == self._sf_rLstC[self._sf_rIntC]:
                                self._sf_rIntC = 0
                                while self._sf_rIntC < self._sf_rIntD:
                                    self._sf_rIntE = 0
                                    while self._sf_rIntE < self._sf_rIntF:
                                        if flSrc[self._sf_rIntE] == self._sf_rLstC[self._sf_rIntC]: rtrnLst.append(self._sf_rLstC[self._sf_rIntC])
                                        self._sf_rIntE+=1
                                    self._sf_rIntC+=1
                                dSet = set()
                                return [_ for _ in rtrnLst if not (_ in dSet or dSet.add(_))]
            return rtrnLst
        else:
            raise Exception(f'[sqtpp-vfs >> pojishon] - optional err: no file(s) found @ "{lstIdx[0]}/{lstIdx[1]}/..." for a file on file line(s) matching search')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_row_spdr(self, isEwwVd: bool, src, pos, ptrn) -> str:
        # FNC_ID=ST12-81565163171470
        # SqtppFncs slots in use: (_sf_rLstE, _sf_rStrE, _sf_rStrF, _sf_sLstA, _sf_sVd)
        # returns: (string)
        if isEwwVd:
            self._sf_rLstE = deque()
            self._sf_rStrE = f'{self._sf_sVd}:|:'
            self._sf_sLstA = [pos, len(self._sf_rStrE), 0, 0]
            while self._sf_sLstA[0] < self._sf_sLstA[1]:
                self._sf_rStrF = self._sf_rStrE[self._sf_sLstA[0]]
                if self._sf_rStrF == '\n':
                    if self._sf_sLstA[3] > 0:
                        self._sf_sLstA[2] = 1
                        break
                    else:
                        return None
                self._sf_rLstE.append(self._sf_rStrF)
                if self._sf_sLstA[3] < 3: self._sf_sLstA[3]+=1
                if self._sf_sLstA[3] == 3 and self._sf_rStrE[self._sf_sLstA[0]-2] == ':' and self._sf_rStrE[self._sf_sLstA[0]-1] == '|' and self._sf_rStrF == ':':
                    if self._sf_sLstA[0]-2 > 0:
                        self._sf_sLstA[2] = 2
                        break
                    else:
                        return None
                self._sf_sLstA[0]+=1
            if self._sf_sLstA[2] == 1 or self._sf_sLstA[2] == 2:
                if self._sf_sLstA[2] == 2: self._sf_rLstE.pop(len(self._sf_rLstE)-1)
                self._sf_rLstE = ''.join(self._sf_rLstE)
                if self._sf_sLstA[2] == 1: self._sf_rLstE = self._sf_rLstE.replace(':|:','')
                self._sf_rStrE = None
                return self._sf_rLstE
            else:
                self._sf_rStrE = None
                return None
        else:
            self._sf_rStrE = src
            self._sf_rLstE = deque(maxlen=ptrn)
            self._sf_sLstA = [len(self._sf_sVd)-ptrn+1, len(self._sf_rStrE)-ptrn+1, 0, 0, 0, len(self._sf_sVd), ptrn]
            for self._sf_sLstA[2] in range(self._sf_sLstA[0]):
                self._sf_sLstA[3] = 0
                while self._sf_sLstA[3] < self._sf_sLstA[1]:
                    if self._sf_sVd[self._sf_sLstA[2]:self._sf_sLstA[2]+self._sf_sLstA[6]] == self._sf_rStrE[self._sf_sLstA[3]:self._sf_sLstA[3]+self._sf_sLstA[6]]:
                        for self._sf_sLstA[4] in range(min(self._sf_sLstA[6], self._sf_sLstA[5]-self._sf_sLstA[2]-self._sf_sLstA[6])): self._sf_rLstE.append(self._sf_sVd[self._sf_sLstA[2]+self._sf_sLstA[6]+self._sf_sLstA[4]])
                        if self._sf_rLstE:
                            self._sf_rStrE = None
                            return ''.join(self._sf_rLstE)
                    self._sf_sLstA[3]+=1
            self._sf_rStrE = None
            return None
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_err_rtrn(self, mode: str, errCd: int) -> int:
        # <<<
        # returns:
        # -1=invalid types balance @varDt and @varNm
        # -2=non-allowed char sequence found @varDt: ':|:>'
        # -3=non-allowed char(s) @varNm
        # -4=no last dir/file setting found for cast
        # -5=unable to read emb vfs mounts/directories/files source
        # -6=invalid parameters combination for next.splice
        # -7=invalid chars @dirList
        # -8=last used mount in vfs settings not found
        # -9=last used mount/directory in vfs settings not found
        # -10=last used mount/directory/file in vfs settings not found
        # -11=@varData missing, is empty
        rtrn = None
        if mode == 'next':
            if errCd == -1: rtrn = -1
            elif errCd == -2: rtrn = -2
            elif errCd == -3: rtrn = -3
            elif errCd == -4: rtrn = -4
        elif mode == 'splice':
            if errCd == -1: rtrn = -5
            elif errCd == -2: rtrn = -6
            elif errCd == -3: rtrn = -7
            elif errCd == -4: rtrn = -4
            elif errCd == -5: rtrn = -8
            elif errCd == -6: rtrn = -9
            elif errCd == -7: rtrn = -10
            elif errCd == -8: rtrn = -11
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_pojishon_err_router_rtrn(self, errCd: int):
        # <<<
        # returns: (returns from sqtpp_emb_vfs_router())
        vfsRtrErrMsgLst = ['invalid vfs path','main vfs directories are corrupted','a unknown vfs router error occured','mount was not found','directory already exist in mount','mount already exist','main ST1EMB directory is missing','directory not found in mount','directory source not found in mount source','cannot remove mount','mount src not found','a seed directory "___lll" was not found','file already exist in directory listing','file source not found in directory source','non-allowed move, only one file in directory','mount name not allowed, "SQTPP_MNT_STGS"']
        errCd = str(errCd)
        errCd = errCd.replace('-', '')
        raise Exception(f'[sqtpp-vfs >> pojishon] - embedded vfs router err: {vfsRtrErrMsgLst[int(errCd)-1]}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_router(self, rstSlt: bool, reOpn: bool, nwMnt: bool, mode: int, dir: list, dirRsv: list, src) -> int:
        # FNC_ID=ST12-61070362071341
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rStrA, _sf_sBoolX, _sf_sDv, _sf_sRtrn, _sf_sSrc, _sf_sStrX, _sf_sVd, _sf_sVfs)
        # modes: (1=mk_d, 2=mv_d, 3=rm_d, 4=sd_d, 5=ad_f, 6=cp_f, 7=mv_f, 8=dl_f, 9=wrt)
        # returns:
        #   1= emb vfs directory instruction finished
        #  -1=invalid vfs path(reOpn)
        #  -2=main vfs directories corrupted(reOpn)
        #  -3=functional error(general error)
        #  -4=mnt not found
        #  -5=dir already exist in mnt
        #  -6=mnt already exist
        #  -7=ST1EMB top dir is missing
        #  -8=dir not found in mnt
        #  -9=dir src not found in mnt src
        # -10=cannot remove mnt
        # -11=mnt src not found
        # -12=a seed dir "___lll" was not found
        # -13=file already exist in dir listing
        # -14=file src not found in dir src
        # -15=non-allowed move, only one file in dir[1]
        # -16=mnt name not allowed: "SQTPP_MNT_STGS"
        try:
            self._sf_sRtrn = None
            self._sf_sBoolX = False
            if reOpn:
                if self.sqtpp_set_vfs_file() == 1:
                    self._sf_rIntA = self._sf_sSrc.find(f'|:{self._sf_rLstA[1]}<{self._sf_rLstA[2]}>')
                    if self._sf_rIntA > -1:
                        self._sf_rIntB = self._sf_sSrc.find(f'_|:{self._sf_rLstA[2]}<{self._sf_rLstA[3]}>')
                        self._sf_sStrX = self._sf_sSrc[self._sf_rIntA:self._sf_rIntB+len(self._sf_rLstA[2])+len(self._sf_rLstA[3])+5]
                        self._sf_EfvStrX = self._sf_sStrX
                        if self._sf_sStrX.find(self._sf_rLstA[2] + '>\n_|:') > -1:
                            nVfsLst = self._sf_sStrX.split('\n')
                            self._sf_sStrX = nVfsLst[0] + '\n|::|ST1EMB<SQTPP_MNT_STGS>\n_|::|SQTPP_MNT_STGS<STGS:\n__|::|STGS<:\n<STGS:S:\nnone:|:>\n_|:|:|SQTPP_MNT_STGS>\n' + nVfsLst[1]
                    else: self._sf_sRtrn = -2
                else: self._sf_sRtrn = -1
            if mode == 10:
                if self._sf_sRtrn == None:
                    return 1
                else:
                    return self._sf_sRtrn
            if self._sf_sRtrn == None:
                if mode != 2 and mode != 9 and mode != 10:
                    if dir[0] == 'SQTPP_MNT_STGS':
                        return -16
                elif mode == 2:
                    if dir[0] == 'SQTPP_MNT_STGS' or dirRsv[0] == 'SQTPP_MNT_STGS':
                        return -16
                if mode == 1: self.sqtpp_emb_vfs_mkdir(nwMnt, dir, None)
                elif mode == 2: self.sqtpp_emb_vfs_mvdir(nwMnt, dir, dirRsv)
                elif mode == 3: self.sqtpp_emb_vfs_rmdir(nwMnt, dir)
                elif mode == 4:
                    # ?..........set mnt|&directory|&file..........?
                    pass
                elif mode == 5: self.sqtpp_emb_vfs_afile(nwMnt, dir, src)
                elif mode == 6: self.sqtpp_emb_vfs_cfile(dir, dirRsv)
                elif mode == 7: self.sqtpp_emb_vfs_mfile(False, dir, dirRsv)
                elif mode == 8: self.sqtpp_emb_vfs_dfile(dir)
                elif mode == 9:
                    self._sf_sSrc = self._sf_sSrc.replace(self._sf_EfvStrX, self._sf_sStrX)
                    self.sqtpp_file(True, f'{SQTPP_MDL_DIR}/staqtapp1_2/{self._sf_sVfs}.sqtpp', self._sf_sSrc)
                    self.sqtpp_reset_slots(False)
                    self._sf_sStrX = None
                    self._sf_sVd = None
                    self._sf_sDv = None
                    return 1
            if self._sf_sRtrn < 0: self._sf_sStrX = self._sf_rStrA
            if rstSlt: self.sqtpp_reset_slots(False)
            return self._sf_sRtrn
        except Exception as err_emb_vfs_director:
            self._sf_sRtrn = -3
            return -3
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_mkdir(self, nwMnt: bool, dir: list, src):
        # FNC_ID=ST12-70509363082559
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_sBoolX, _sf_sIntX, _sf_sRtrn, _sf_sStrX)
        # returns: (emb_vfs_router returns: 1, -4, -5, -6, -7, -11)
        if not nwMnt:
            self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dir)
            if self._sf_sIntX == -1:
                self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(False, dir)
                if self._sf_rStrB == None:
                    return -11
                self._sf_rStrC = self._sf_rStrB
                self._sf_rStrD = dir[0]
                dir.pop(0)
                if len(self._sf_rLstD) > 1: self._sf_rStrE = ','.join(self._sf_rLstD)
                else: self._sf_rStrE = self._sf_rLstD[0]
                if len(dir) > 1: self._sf_rStrB = self._sf_rStrB.replace(self._sf_rLstB[0], f'_|::|{self._sf_rStrD}<{self._sf_rStrE},{",".join(dir)}:')
                else: self._sf_rStrB = self._sf_rStrB.replace(self._sf_rLstB[0], f'_|::|{self._sf_rStrD}<{self._sf_rStrE},{dir[0]}:')
                self._sf_rLstC = ['\n']
                self._sf_rIntB = len(dir)
                for self._sf_rIntA in range(self._sf_rIntB):
                    if self._sf_rIntA < self._sf_rIntB-1: self._sf_rLstC.append('__|::|' + dir[self._sf_rIntA] + '<null:\n<none:S:\nnone:|:>\n')
                    else: self._sf_rLstC.append('__|::|' + dir[self._sf_rIntA] + '<null:\n<none:S:\nnone:|:>\n_|:|:|' + self._sf_rStrD + '>')  
                self._sf_rStrB = f'{self._sf_rStrB}{"".join(self._sf_rLstC)}'
                self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrC + '\n_|:|:|' + self._sf_rStrD + '>', self._sf_rStrB)
                self._sf_sRtrn = 1
            else:
                if self._sf_sIntX == -2: self._sf_sRtrn = -4
                elif self._sf_sIntX == 1: self._sf_sRtrn = -5
        else:
            self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dir)
            if self._sf_sIntX == -1:
                if len(self._sf_rLstB) > 1: self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrB, f'|::|ST1EMB<{",".join(self._sf_rLstB)},{dir[0]}>')
                else: self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrB, f'|::|ST1EMB<{self._sf_rLstB[0]},{dir[0]}>')
                self._sf_sStrX = self._sf_sStrX.replace('\n_|:' + self._sf_rLstA[2] + '<' + self._sf_rLstA[3] + '>', '')
                self._sf_rLstC = ['\n']
                self._sf_rIntB = len(dir)
                self._sf_rLstB = ['\n_|::|' + dir[0] + '<']
                for self._sf_rIntA in range(1, self._sf_rIntB):
                    if self._sf_rIntA < self._sf_rIntB-1:
                        self._sf_rLstC.append('__|::|' + dir[self._sf_rIntA] + '<null:\n<none:S:\nnone:|:>\n')
                        self._sf_rLstB.append(dir[self._sf_rIntA] + ',')
                    else:
                        if not self._sf_sBoolX: self._sf_rLstC.append('__|::|' + dir[self._sf_rIntA] + '<null:\n<none:S:\nnone:|:>\n_|:|:|' + dir[0] + '>\n')
                        else: self._sf_rLstC.append('__|::|' + dir[self._sf_rIntA] + '<' + src[0] + ':\n<' + src[0] + ':S:\n' + src[1] + ':|:>\n_|:|:|' + dir[0] + '>\n')
                        self._sf_rLstB.append(dir[self._sf_rIntA] + ':')
                self._sf_sStrX = f'{self._sf_sStrX}{"".join(self._sf_rLstB)}{"".join(self._sf_rLstC)}_|:{self._sf_rLstA[2]}<{self._sf_rLstA[3]}>'
                self._sf_sRtrn = 1
            else:
                if self._sf_sIntX == 1: self._sf_sRtrn = -6
                elif self._sf_sIntX == -2: self._sf_sRtrn = -7
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_mvdir(self, nwMnt: bool, dir: list, dirRsv: list):
        # FNC_ID=ST12-37892688595978
        # SqtppFncs slots in use: (_sf_rLstA, _sf_rLstB, _sf_rLstD, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_sIntX, _sf_sRtrn, _sf_sStrX)
        # returns: (emb_vfs_router returns: 1, -4, -5, -6, -7, -8, -9, -11)
        self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dir)
        if self._sf_sIntX == 1:
            self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_mnt(False, dir)
            if self._sf_rStrC == None:
                return -11
            self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dirRsv)
            if nwMnt:
                if self._sf_sIntX == -1:
                    if len(self._sf_rLstB) > 1:
                        self._sf_rLstB = ','.join(self._sf_rLstB)
                        self._sf_sStrX = self._sf_sStrX.replace(f'|::|ST1EMB<{self._sf_rLstB}>', f'|::|ST1EMB<{self._sf_rLstB},{dirRsv[0]}>')
                    else: self._sf_sStrX = self._sf_sStrX.replace(f'|::|ST1EMB<{self._sf_rLstB[0]}>', f'|::|ST1EMB<{self._sf_rLstB[0]},{dirRsv[0]}>')
                    if self.sqtpp_emb_ext_vfs_remove_dir(dir, self._sf_rLstD, self._sf_rStrC):
                        self._sf_sStrX = self._sf_sStrX.replace('\n_|:' + self._sf_rLstA[2] + '<' + self._sf_rLstA[3] + '>', '')
                        self._sf_sStrX = self._sf_sStrX + '\n_|::|' + dirRsv[0] + '<' + dir[1] + ':\n' + self._sf_rStrB + '\n_|:|:|' + dirRsv[0] + '>\n'
                        self._sf_sStrX = f'{self._sf_sStrX}_|:{self._sf_rLstA[2]}<{self._sf_rLstA[3]}>'
                        self._sf_sRtrn = 1
                    else: self._sf_sRtrn = -9
                else:
                    if self._sf_sIntX == 1: self._sf_sRtrn = -6
                    elif self._sf_sIntX == -2: self._sf_sRtrn = -7
            else:
                if self._sf_sIntX == 1:
                    if self.sqtpp_emb_ext_vfs_remove_dir(dir, self._sf_rLstD, self._sf_rStrC):
                        self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt([dirRsv[0],dir[1]])
                        if self._sf_sIntX == -1:
                            self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_mnt(True, dirRsv)
                            self._sf_rStrD = self._sf_rStrC
                            if len(self._sf_rLstD) > 1:
                                self._sf_rLstD = ','.join(self._sf_rLstD)
                                self._sf_rStrC = self._sf_rStrC.replace(f'_|::|{dirRsv[0]}<{self._sf_rLstD}:', f'_|::|{dirRsv[0]}<{self._sf_rLstD},{dir[1]}:')
                            else: self._sf_rStrC = self._sf_rStrC.replace(f'_|::|{dirRsv[0]}<{self._sf_rLstD[0]}:', f'_|::|{dirRsv[0]}<{self._sf_rLstD[0]},{dir[1]}:')
                            self._sf_rStrC = self._sf_rStrC + '\n' + self._sf_rStrB + '\n_|:|:|' + dirRsv[0] + '>'
                            self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrD + '\n_|:|:|' + dirRsv[0] + '>', self._sf_rStrC)
                            self._sf_sRtrn = 1
                        else:
                            if self._sf_sIntX == 1: self._sf_sRtrn = -5
                            elif self._sf_sIntX == -2: self._sf_sRtrn = -4
                    else: self._sf_sRtrn = -9
                else:
                    if self._sf_sIntX == -1: self._sf_sRtrn = -4
                    elif self._sf_sIntX == -2: self._sf_sRtrn = -7
        else:
            if self._sf_sIntX == -1: self._sf_sRtrn = -8
            elif self._sf_sIntX == -2: self._sf_sRtrn = -4
        return self._sf_sRtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_rmdir(self, nwMnt: bool, dir: list):
        # FNC_ID=ST12-77453284060819
        # SqtppFncs slots in use: (_sf_rLstB, _sf_rLstD, _sf_rStrB, _sf_rStrC, _sf_sIntX, _sf_sRtrn, _sf_sStrX)
        # returns: (emb_vfs_router returns: 1, -4, -7, -8, -9, -10, -11)
        self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dir)
        if self._sf_sIntX == 1:
            if not nwMnt:
                if len(self._sf_rLstB) > 1:
                    self._sf_rStrB = ','.join(self._sf_rLstB)
                    self._sf_rLstB.remove(dir[0])
                    if len(self._sf_rLstB) > 1: self._sf_sStrX = self._sf_sStrX.replace(f'|::|ST1EMB<{self._sf_rStrB}>', f'|::|ST1EMB<{",".join(self._sf_rLstB)}>')
                    else: self._sf_sStrX = self._sf_sStrX.replace(f'|::|ST1EMB<{self._sf_rStrB}>', f'|::|ST1EMB<{self._sf_rLstB[0]}>')
                    self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, dir)
                    if self._sf_rStrB != None:
                        self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrB + '\n_|:|:|' + dir[0] + '>\n', '')
                        self._sf_sRtrn = 1
                    else: self._sf_sRtrn = -11
                else: self._sf_sRtrn = -10
            else:
                self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dir)
                if self._sf_sIntX == 1:
                    self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_mnt(True, dir)
                    if self._sf_rStrC == None:
                        return -11
                    if self.sqtpp_emb_ext_vfs_remove_dir(dir, self._sf_rLstD, self._sf_rStrC): self._sf_sRtrn = 1
                    else: self._sf_sRtrn = -9
                else:
                    if self._sf_sIntX == -1: self._sf_sRtrn = -8
                    elif self._sf_sIntX == -2: self._sf_sRtrn = -4
        else:
            if self._sf_sIntX == -1: self._sf_sRtrn = -4
            elif self._sf_sIntX == -2: self._sf_sRtrn = -7    
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_afile(self, nwMnt: bool, dir: list, src: list):
        # FNC_ID=ST12-41579772455440
        # SqtppFncs slots in use: (_sf_rBoolA, _sf_rIntA, _sf_rIntB, _sf_rLstB, _sf_rLstC, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_sBoolX, _sf_sIntX, _sf_sRtrn, _sf_sStrX)
        # returns: (emb_vfs_router returns: 1, -4, -8, -11, -12, -13)
        if nwMnt:
            self._sf_sBoolX = True
            self.sqtpp_emb_vfs_mkdir(True, dir, src)
        else:
            if dir[0] == 'lll':
                self._sf_rLstB = re.search(r'_(?:::|)[^<]+<[^>]*___lll[^>]*>(.*?)\n(?:::|)[^>]+>', self._sf_sStrX, re.DOTALL)
                if self._sf_rLstB:
                    self._sf_rStrB = self._sf_rLstB.group(0)
                    self._sf_rStrC = self._sf_rStrB
                    self._sf_rLstB = re.findall(r'_\|\:\:\|.*?:', self._sf_rStrB)
                    self._sf_rLstC = self._sf_rLstB[0].split('<')
                    self._sf_rLstC[0] = self._sf_rLstC[0].replace('_|::|','')
                    self._sf_rStrD = self._sf_rLstC[1]
                    self._sf_rLstC[1] = self._sf_rLstC[1].replace('___lll', dir[1])
                    self._sf_rStrB = self._sf_rStrB.replace(self._sf_rLstB[0], f'_|::|{self._sf_rLstC[0]}<{self._sf_rLstC[1]}')
                    self._sf_rStrB = self._sf_rStrB.replace('\n__|::|___lll<null:\n<none:S:\nnone:|:>','')
                    self._sf_rStrB = self._sf_rStrB + '\n__|::|' + dir[1] + '<' + src[0] + ':\n<' + src[0] + ':S:\n' + src[1] + ':|:>\n_|:|:|' + self._sf_rLstC[0] + '>'
                    self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrC + '\n_|:|:|' + self._sf_rLstC[0] + '>', self._sf_rStrB)
                    self._sf_sRtrn = 1
                else: self._sf_sRtrn = -12
            else:
                self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dir)
                if self._sf_sIntX == 1:
                    self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, dir)
                    self._sf_rStrE = self._sf_rStrB
                    if self._sf_rStrB != None:
                        self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(dir[1], self._sf_rStrB)
                        self._sf_rStrD = self._sf_rStrC
                        self._sf_rLstB = re.findall(r'__\|:\:\|' + re.escape(dir[1]) + '<.*?:', self._sf_rStrC)
                        self._sf_rLstB[0] = self._sf_rLstB[0].replace(':','')
                        self._sf_rLstB = self._sf_rLstB[0].split('<')
                        if self._sf_rLstB[1].find(',') > -1: self._sf_rLstC = self._sf_rLstB[1].split(',')
                        else: self._sf_rLstC = [self._sf_rLstB[1]]
                        self._sf_rIntB = len(self._sf_rLstC)
                        self._sf_rBoolA = False
                        self._sf_rIntA = 0
                        while self._sf_rIntA < self._sf_rIntB:
                            if self._sf_rLstC[self._sf_rIntA] == src[0]:
                                self._sf_rBoolA = True
                                break
                            self._sf_rIntA+=1
                        if not self._sf_rBoolA:
                            if self._sf_rIntB > 1: self._sf_rStrC = self._sf_rStrC.replace(f'__|::|{dir[1]}<{",".join(self._sf_rLstC)}:', f'__|::|{dir[1]}<{",".join(self._sf_rLstC)},{src[0]}:')
                            else: self._sf_rStrC = self._sf_rStrC.replace(f'__|::|{dir[1]}<{self._sf_rLstC[0]}:', f'__|::|{dir[1]}<{self._sf_rLstC[0]},{src[0]}:')
                            self._sf_rStrC = self._sf_rStrC + '\n<' + src[0] + ':S:\n' + src[1] + ':|:>'
                            self._sf_rStrB = self._sf_rStrB.replace(self._sf_rStrD, self._sf_rStrC)
                            self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrE, self._sf_rStrB)
                            self._sf_sRtrn = 1
                        else: self._sf_sRtrn = -13
                    else: self._sf_sRtrn = -11
                else:
                    if self._sf_sIntX == -1: self._sf_sRtrn = -8
                    elif self._sf_sIntX == -2: self._sf_sRtrn = -4
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_cfile(self, dir: list, dirRsv: list):
        # FNC_ID=ST12-16913167834727
        # SqtppFncs slots in use: (_sf_rLstC, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_rStrF, _sf_sIntX, _sf_sRtrn, _sf_sStrX)
        # returns: (emb_vfs_router returns: 1, -4, -7, -8, -9, -11, -13, -14)
        self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dir)
        if self._sf_sIntX == 1:
            self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_dir_in_mnt(dir)
            if self._sf_sIntX == 1:
                self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, dir)
                if self._sf_rStrB != None:
                    self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(dir[1], self._sf_rStrB)
                    if self._sf_rStrC != None:
                        self._sf_rStrD = self.sqtpp_emb_ext_vfs_get_file(dir[2], self._sf_rStrC)
                        if self._sf_rStrD != None:
                            self._sf_rStrE = self.sqtpp_emb_ext_vfs_get_dir(dirRsv[0], self._sf_rStrB)
                            if self._sf_rStrE != None:
                                self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_file_in_dir(dir[2], dirRsv[0], self._sf_rStrE)
                                if self._sf_sIntX == -1:
                                    self._sf_rStrC = self._sf_rStrE
                                    if len(self._sf_rLstC) > 1:
                                        self._sf_rLstC = ','.join(self._sf_rLstC)
                                        self._sf_rStrE = self._sf_rStrE.replace(f'__|::|{dirRsv[0]}<{self._sf_rLstC}:', f'__|::|{dirRsv[0]}<{self._sf_rLstC},{dir[2]}:')
                                    else: self._sf_rStrE = self._sf_rStrE.replace(f'__|::|{dirRsv[0]}<{self._sf_rLstC[0]}:', f'__|::|{dirRsv[0]}<{self._sf_rLstC[0]},{dir[2]}:')
                                    self._sf_rStrE = self._sf_rStrE + '\n' + self._sf_rStrD
                                    self._sf_rStrF = self._sf_rStrB
                                    self._sf_rStrB = self._sf_rStrB.replace(self._sf_rStrC, self._sf_rStrE)
                                    self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrF, self._sf_rStrB)
                                    self._sf_sRtrn = 1
                                else:
                                    if self._sf_sIntX == 1: self._sf_sRtrn = -13
                                    elif self._sf_sIntX == -2: self._sf_sRtrn = -9
                            else: self._sf_sRtrn = -9
                        else: self._sf_sRtrn = -14
                    else: self._sf_sRtrn = -9
                else: self._sf_sRtrn = -11
            else:
                if self._sf_sIntX == -1: self._sf_sRtrn = -8
                elif self._sf_sIntX == -2: self._sf_sRtrn = -4
        else:
            if self._sf_sIntX == -1: self._sf_sRtrn = -4
            elif self._sf_sIntX == -2: self._sf_sRtrn = -7
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_mfile(self, isDel: bool, dir: list, dirRsv: list):
        # FNC_ID=ST12-73491366416298
        # SqtppFncs slots in use: (_sf_rLstB, _sf_rLstC, _sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_sRtrn)
        # returns: (emb_vfs_router returns: 1, -4, -7, -8, -9, -11, -13, -14, -15)
        if not isDel: self.sqtpp_emb_vfs_cfile(dir, dirRsv)
        if self._sf_sRtrn == 1:
            if not isDel: self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(dir[1], self._sf_rStrB)
            self._sf_rStrE = self._sf_rStrC
            self.sqtpp_emb_ext_vfs_set_file_list(False, dir[1], self._sf_rStrC)
            if self._sf_rLstB[1].find(',') > -1:
                self._sf_rLstC = self._sf_rLstB[1].split(',')
                self._sf_rLstC.remove(dir[2])
                if len(self._sf_rLstC) > 1: self._sf_rStrC = self._sf_rStrC.replace(f'__|::|{dir[1]}<{self._sf_rLstB[1]}:', f'__|::|{dir[1]}<{",".join(self._sf_rLstC)}:')
                else: self._sf_rStrC = self._sf_rStrC.replace(f'__|::|{dir[1]}<{self._sf_rLstB[1]}:', f'__|::|{dir[1]}<{self._sf_rLstC[0]}:')
                self._sf_rStrC = self._sf_rStrC.replace('\n' + self._sf_rStrD, '')
                self.sqtpp_emb_ext_vfs_remove_file()
            else:
                if not isDel:
                    self._sf_sRtrn = -15
                    return -15
                else:
                    self._sf_rStrC = self._sf_rStrC.replace(self._sf_rStrD, '<null:S:\nnone:|:>')
                    self._sf_rStrC = self._sf_rStrC.replace(f'__|::|{dir[1]}<{self._sf_rLstB[1]}:', f'__|::|{dir[1]}<___lll:')
                    self.sqtpp_emb_ext_vfs_remove_file()
            self._sf_sRtrn = 1
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_vfs_dfile(self, dir: list):
        # FNC_ID=ST12-32307643722029
        # SqtppFncs slots in use: (_sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_sIntX, _sf_sRtrn)
        # returns: (emb_vfs_router returns: 1, -4, -7, -9, -14)
        self._sf_sIntX = self.sqtpp_emb_ext_vfs_fnd_mnt_in_stb(dir)
        if self._sf_sIntX == 1:
            self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, dir)
            if self._sf_rStrB != None:
                self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(dir[1], self._sf_rStrB)
                if self._sf_rStrC != None:
                    self._sf_rStrD = self.sqtpp_emb_ext_vfs_get_file(dir[2], self._sf_rStrC)
                    if self._sf_rStrD != None:
                        self._sf_sRtrn = 1
                        self.sqtpp_emb_vfs_mfile(True, dir, None)
                    else: self._sf_sRtrn = -14
                else: self._sf_sRtrn = -9
            else: self._sf_sRtrn = -4
        else:
            if self._sf_sIntX == -1: self._sf_sRtrn = -4
            elif self._sf_sIntX == -2: self._sf_sRtrn = -7
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_fnd_mnt_in_stb(self, dir: list) -> int:
        # FNC_ID=ST12-36503613201829
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstB, _sf_rLstC, _sf_rStrB, _sf_sStrX)
        # returns:
        #  1=mnt found in stb main
        # -1=mnt not found in stb main
        # -2=dir ST1EMB not found
        self._sf_rLstB = re.findall(r'\|\:\:\|ST1EMB<.*?>', self._sf_sStrX)
        if len(self._sf_rLstB) > 0:
            self._sf_rStrB = self._sf_rLstB[0]
            self._sf_rLstB[0] = self._sf_rLstB[0].replace('>', '')
            self._sf_rLstC = self._sf_rLstB[0].split('<')
            if self._sf_rLstC[1].find(',') > -1: self._sf_rLstB = self._sf_rLstC[1].split(',')
            else: self._sf_rLstB = [self._sf_rLstC[1]]
            self._sf_rIntA = 0
            self._sf_rIntB = len(self._sf_rLstB)
            while self._sf_rIntA < self._sf_rIntB:
                if self._sf_rLstB[self._sf_rIntA] == dir[0]:
                    return 1
                self._sf_rIntA+=1
            return -1
        else:
            return -2
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_fnd_dir_in_mnt(self, dir: list) -> int:
        # FNC_ID=ST12-48494006910670
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rIntC, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_sStrX)
        # returns: (*******_sf_rLstD will have all dir name(s) for mnt(dir[0])*******)
        #  1=dir found in mnt
        # -1=dir not found in mnt
        # -2=mnt not found
        self._sf_rLstB = re.findall(r'_\|\:\:\|' + re.escape(dir[0]) + r'<.*?\:', self._sf_sStrX)
        if len(self._sf_rLstB) > 0:
            self._sf_rLstC = self._sf_rLstB[0].split('<')
            if self._sf_rLstC[1].find(',') > -1: self._sf_rLstD = self._sf_rLstC[1].split(',')
            else: self._sf_rLstD = [self._sf_rLstC[1]]
            self._sf_rLstD[len(self._sf_rLstD)-1] = self._sf_rLstD[len(self._sf_rLstD)-1].replace(':','')
            self._sf_rIntC = len(self._sf_rLstD)
            for self._sf_rIntA in range(1, len(dir)):
                self._sf_rIntB = 0
                while self._sf_rIntB < self._sf_rIntC:
                    if self._sf_rLstD[self._sf_rIntB] == dir[self._sf_rIntA]:
                        return 1
                    self._sf_rIntB+=1
            return -1
        else:
            return -2
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_fnd_file_in_dir(self, fNm: str, dNm: str, dirSrc: str) -> int:
        # FNC_ID=ST12-81380194047219
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstB, _sf_rLstC)
        # returns: (*******_sf_rLstC will have all file name(s) for dirSrc*******)
        #  1=file found in dir
        # -1=file not found in dir
        # -2=dir not found
        self._sf_rLstB = re.findall(r'__\|\:\:\|' + re.escape(dNm) + r'<.*?\:', dirSrc)
        if len(self._sf_rLstB) > 0:
            self._sf_rLstB = self._sf_rLstB[0].split('<')
            self._sf_rLstB[1] = self._sf_rLstB[1].replace(':','')
            if self._sf_rLstB[1].find(',') > -1: self._sf_rLstC = self._sf_rLstB[1].split(',')
            else: self._sf_rLstC = [self._sf_rLstB[1]]
            self._sf_rIntA = 0
            self._sf_rIntB = len(self._sf_rLstC)
            while self._sf_rIntA < self._sf_rIntB:
                if self._sf_rLstC[self._sf_rIntA] == fNm:
                    return 1
                self._sf_rIntA+=1
            return -1
        else:
            return -2
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_get_mnt(self, fndMnt: bool, dir: list):
        # FNC_ID=ST12-77691996082789
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB, _sf_rLstB, _sf_sStrX)
        # returns: (sliced mnt dir or None if mnt dir not found)
        if fndMnt: self._sf_rLstB = re.findall(r'_\|\:\:\|' + re.escape(dir[0]) + r'<.*?\:', self._sf_sStrX)
        if len(self._sf_rLstB) > 0:
            self._sf_rIntA = self._sf_sStrX.find(self._sf_rLstB[0])
            self._sf_rIntB = self._sf_sStrX.find(f'_|:|:|{dir[0]}')
            return self._sf_sStrX[self._sf_rIntA:self._sf_rIntB-1]
        else:
            return None
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_get_dir(self, dirNm: str, mntSrc: str):
        # FNC_ID=ST12-45970819858652
        # SqtppFncs slots in use: (_sf_rBoolD, _sf_rIntA, _sf_rIntB)
        # returns: (***None if dir not found; or dir src, found by end of a mnt or start of a new dir***)
        self._sf_rBoolD = True
        mntSrc = f'{mntSrc}\n_|:|:|'
        self._sf_rIntA = mntSrc.find(f'__|::|{dirNm}<')
        self._sf_rIntB = mntSrc.find(':|:>', self._sf_rIntA+5)
        if self._sf_rIntA > -1 and self._sf_rIntB > -1:
            while True:
                if self._sf_rBoolD: self._sf_rBoolD = False
                else: self._sf_rIntB = mntSrc.find(':|:>', self._sf_rIntB+3)
                if self._sf_rIntB > -1:
                    if mntSrc.find(':|:>\n__|::|', self._sf_rIntB, self._sf_rIntB+11) > -1:
                        return mntSrc[self._sf_rIntA:self._sf_rIntB+4]
                    if mntSrc.find(':|:>\n_|:|:|', self._sf_rIntB, self._sf_rIntB+11) > -1:
                        return mntSrc[self._sf_rIntA:self._sf_rIntB+4]
                else:
                    return None
        else:
            return None
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_get_file(self, fNm: str, dirSrc: str):
        # FNC_ID=ST12-75998528800224
        # SqtppFncs slots in use: (_sf_rIntA, _sf_rIntB)
        # returns: (None if file not found or file source if found)
        self._sf_rIntA = dirSrc.find(f'<{fNm}:S:')
        self._sf_rIntB = dirSrc.find(f':|:>', self._sf_rIntA+len(fNm)+3)
        if self._sf_rIntA > -1 and self._sf_rIntB > -1:
            return dirSrc[self._sf_rIntA:self._sf_rIntB+4]
        else:
            return None
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_read_file(self, dirLst: list):
        # FNC_ID=ST12-16438334421513
        # SqtppFncs slots in use: (_sf_rStrB, _sf_rStrC)
        # returns: (Returns file str source, specific mnt|dir|file error string, or a STGS Exception)
        srcStr = None
        errStr = None
        self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_mnt(True, [dirLst[0]])
        if self._sf_rStrB != None:
            self._sf_rStrC = self.sqtpp_emb_ext_vfs_get_dir(dirLst[1], self._sf_rStrB)
            if self._sf_rStrC != None:
                srcStr = self.sqtpp_emb_ext_vfs_get_file(dirLst[2], self._sf_rStrC)
                if srcStr != None:
                    self._sf_rStrB = None
                    self._sf_rStrC = None
                    return srcStr
                else:
                    if dirLst[0] == 'SQTPP_MNT_STGS' and dirLst[1] == 'STGS' and dirLst[2] == 'STGS':
                        raise Exception(f'[sqtpp-vfs >> pojishon] - settings file: unable to read settings file (SQTPP_MNT_STGS/STGS) a settings mnt/dir/file is crucial for several pojishon embedded vfs-dir operations!')
                    else: errStr = '!FILE_.:_:!!:_:._FILE!'
            else:
                if dirLst[0] == 'SQTPP_MNT_STGS' and dirLst[1] == 'STGS':
                    raise Exception(f'[sqtpp-vfs >> pojishon] - settings directory: unable to read settings directory (SQTPP_MNT_STGS/STGS) a settings mnt/dir/file is crucial for several pojishon embedded vfs-dir operations!')
                else: errStr = '!DIR_.:_:!!:_:._DIR!'
        else:
            if dirLst[0] == 'SQTPP_MNT_STGS':
                raise Exception(f'[sqtpp-vfs >> pojishon] - settings mount: unable to read settings mount (SQTPP_MNT_STGS/STGS) a settings mnt/dir/file is crucial for several pojishon embedded vfs-dir operations!')
            else: errStr = '!MNT_.:_:!!:_:._MNT!'
        if errStr != None:
            return errStr
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_edit_file(self, dirLst: list, nwSrc: str):
        # FNC_ID=ST12-82258639862779
        # SqtppFncs slots in use: (_sf_sStrX)
        # returns: (none, assumes _sf_sStrX is contain of all emb-vfs mounts/dirs/files)
        dErr = False
        rtnMnt = self.sqtpp_emb_ext_vfs_get_mnt(True, [dirLst[0]])
        if rtnMnt != None:
            rtnDir = self.sqtpp_emb_ext_vfs_get_dir(dirLst[1], rtnMnt)
            if rtnDir != None:
                rtnFle = self.sqtpp_emb_ext_vfs_get_file(dirLst[2], rtnDir)
                if rtnFle != None:
                    orgA = '<' + dirLst[2] + ':S:\n' + rtnFle + ':|:>'
                    rtnFle = '<' + dirLst[2] + ':S:\n' + nwSrc + ':|:>'
                    orgB = rtnDir
                    rtnDir = rtnDir.replace(orgA, rtnFle)
                    orgA = rtnMnt
                    rtnMnt = rtnMnt.replace(orgB, rtnDir)
                    self._sf_sStrX = self._sf_sStrX.replace(orgA, rtnMnt)
                else: dErr = True 
            else: dErr = True
        else: dErr = True
        if dErr:
            raise Exception(f"[sqtpp-vfs >> pojishon] - unable to edit file '{dirLst[2]}' in mnt/dir({dirLst[0]}/{dirLst[1]}) is an unresolved error, embedded vfs .sqtpp files's mounts/directories/files may be corrupted")
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_set_file_list(self, isCmpltd: bool, dirNm: str, dirSrc: str) -> list:
        # FNC_ID=ST12-41247017839558
        # SqtppFncs slots in use: (_sf_rLstB, _sf_rLstC)
        # returns: none
        self._sf_rLstB = re.findall(r'__\|\:\:\|' + re.escape(dirNm) + r'<.*?\:', dirSrc)
        self._sf_rLstB = self._sf_rLstB[0].split('<')
        self._sf_rLstB[1] = self._sf_rLstB[1].replace(':','')
        if isCmpltd:
            if self._sf_rLstB[1].find(',') > -1: self._sf_rLstC = self._sf_rLstB[1].split(',')
            else: self._sf_rLstC = [self._sf_rLstB[1]]
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_remove_dir(self, dir: list, mntDirs: list, mntSrc: str) -> bool:
        # FNC_ID=ST12-36598772524882
        # SqtppFncs slots in use: (_sf_rStrB, _sf_rStrD, _sf_sStrX)
        # returns: (True or False, ********_sf_rStrB == dir src string********)
        self._sf_rStrB = self.sqtpp_emb_ext_vfs_get_dir(dir[1], mntSrc)
        if self._sf_rStrB != None:
            if len(mntDirs) > 1:
                self._sf_sStrX = self._sf_sStrX.replace('\n' + self._sf_rStrB, '')
                self._sf_rStrD = ",".join(mntDirs)
                if dir[1] in mntDirs: mntDirs.remove(dir[1])
                self._sf_sStrX = self._sf_sStrX.replace(f'_|::|{dir[0]}<{self._sf_rStrD}:', f'_|::|{dir[0]}<{",".join(mntDirs)}:')
            else:
                self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrB, '__|::|___lll<null:\n<none:S:\n:|:>')
                self._sf_sStrX = self._sf_sStrX.replace(f'_|::|{dir[0]}<{mntDirs[0]}:', f'_|::|{dir[0]}<___lll:')
            return True
        else:
            return False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_emb_ext_vfs_remove_file(self):
        # FNC_ID=ST12-63897102649789
        # SqtppFncs slots in use: (_sf_rStrB, _sf_rStrC, _sf_rStrD, _sf_rStrE, _sf_sStrX)
        # returns: none
        self._sf_rStrD = self._sf_rStrB
        self._sf_rStrB = self._sf_rStrB.replace(self._sf_rStrE, self._sf_rStrC)
        self._sf_sStrX = self._sf_sStrX.replace(self._sf_rStrD, self._sf_rStrB)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
#
#//////////           .          ._________|______________________________*
#/////////                    .            .                             /       .
#////////         .                   _____|                            /
#///////              .          . \//_.|._\\/                  .______/         __.
#//////   .         .             ///_/.|.\_\\\                 /      |        /    .  
#/////                          _\|| /.:|:.\ ||/_      ._______/       |       /
#//////                   .    / //||__/|\__||\\ \                 .___|      /   .    
#///////    .      .          / //|| \\   // ||\\ \       .            |_____•   .      
#////////       .           _/ _/_|_| \*  /  ||_ \_ \_  .              |              .   
#/////////                             |                               .              
#//////////      .                     |____________.                                •
#
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_tree_context(self, isRead: bool):
        # <<<
        # returns:
        if not isRead:
            if self._sf_sBoolX:
                if not os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_NTR.py'): self.sqtpp_ntr_tree_build_mdl()
            else:
                pass
        else:
            pass
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_tree_build_mdl(self):
        # <<<
        # returns:
        self._rg_rLstA = []
        self._rg_rLstA.append("# This py-module is auto-generated by the Staqtapp1.2 vfs env-var library for ntr-tree functions use. Edit at your own risk.\u000A")
        self._rg_rLstA.append("\u000Afrom collections import deque\u000A\u000Aimport math\u000Aimport re\u000A\u000Aclass SqtppNtrLLL():\u000A")
        self._rg_rLstA.append("    \u000A    __slots__ = ()\u000A    \u000A    def __init__(self):\u000A        pass\u000A        \u000A")
        self._rg_rLstA.append("class SqtppNtrLLL_Fncs(SqtppNtrLLL):\u000A    \u000A    __slots__ = (\u0027_lll_sNtr\u0027, \u0027_lll_sRtrn\u0027, \u0027_lll_sFncRtrn\u0027, \u0027_lll_sSrchRtrn\u0027, \u0027_lll_sSrchPosRtrn\u0027, \u0027_lll_sLstA\u0027, \u0027_lll_sLstB\u0027, \u0027_lll_sLstC\u0027, \u0027_lll_sLstD\u0027, \u0027_lll_sLstE\u0027, \u0027_lll_sStrA\u0027, \u0027_lll_sIntA\u0027, \u0027_lll_sIntB\u0027, \u0027_lll_sIntC\u0027, \u0027_lll_sIntD\u0027, \u0027_lll_sIntE\u0027, \u0027_lll_sIntF\u0027, \u0027_lll_sIntG\u0027, \u0027_lll_sIntH\u0027, \u0027_lll_sIntI\u0027, \u0027_lll_sIntJ\u0027, \u0027_lll_sIntK\u0027, \u0027_lll_sIntL\u0027, \u0027_lll_sIntM\u0027, \u0027_lll_sBoolA\u0027, \u0027_lll_rLstA\u0027, \u0027_lll_rLstB\u0027, \u0027_lll_rStrA\u0027, \u0027_lll_rStrB\u0027, \u0027_lll_rIntA\u0027, \u0027_lll_rIntB\u0027, \u0027_lll_rIntC\u0027, \u0027_lll_rIntD\u0027, \u0027_lll_rIntE\u0027, \u0027_lll_rIntF\u0027, \u0027_lll_rBoolA\u0027)\u000A")
        self._rg_rLstA.append("    \u000A    def __init__(self):\u000A        \u000A        self._lll_sNtr = deque([\u000A            \u0027<!//.]|>__SQTPP__DEFAULT__NTR__<|[/^%/]<^./>__B1(1441441:1221221:2345)/:/=1,2,4/|:/__R1(1884881:2727272:1568)//:/=1,2,4,7,8/:|//|:/__R2(5159515:3884883:3456)//:/=1,3,4,5,8,9/:|/<./^>[/%^/].//!>\u0027\u000A")
        self._rg_rLstA.append("        ])\u000A    def sqtpp_lll_ntr(self, mode: str, brnchPth, mrgPth: list):\u000A        try:\u000A            if mode == \u0027r\u0027:\u000A")
        self._rg_rLstA.append("                return self.sqtpp_lll_ntr_read(brnchPth)\u000A            elif mode == \u0027r+\u0027:\u000A                return self.sqtpp_lll_ntr_read_whole_branch(brnchPth)\u000A")
        self._rg_rLstA.append("            elif mode == \u0027w\u0027:\u000A                self._lll_sBoolA = True\u000A                return self.sqtpp_lll_ntr_write_new(brnchPth)\u000A")
        self._rg_rLstA.append("            elif mode == \u0027w+\u0027:\u000A                self._lll_sBoolA = False\u000A                return self.sqtpp_lll_ntr_write_merged(brnchPth, mrgPth)\u000A")
        self._rg_rLstA.append("        except Exception as err_sqtpp_lll_ntr:\u000A            raise Exception(f\u0027[SQTPP NTR-TREE] - a direct ntr-tree module error has occured: {err_sqtpp_lll_ntr}\u0027)\u000A")
        self._rg_rLstA.append("#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_write_merged(self, brnchPth, mrgPth: list):\u000A")
        self._rg_rLstA.append("        if isinstance(brnchPth, str) and isinstance(mrgPth, list):\u000A            self._lll_sFncRtrn = self.sqtpp_lll_ntr_write_new(brnchPth)\u000A")
        self._rg_rLstA.append("            if self._lll_sFncRtrn != None and len(mrgPth) > 0:\u000A                self._lll_sIntC = 1\u000A                self._lll_sLstB = []\u000A")
        self._rg_rLstA.append("                self._lll_sIntB = len(mrgPth)\u000A                for self._lll_sIntA in range(self._lll_sIntB):\u000A                    self._lll_sLstA = mrgPth[self._lll_sIntA].split(\u0027:\u0027)\u000A")
        self._rg_rLstA.append("                    if len(self._lll_sLstA) == 4:\u000A                        self._lll_sLstE = self.sqtpp_lll_ntr_read(f\u0027{self._lll_sLstA[1]},{self._lll_sLstA[2]}:{self._lll_sLstA[3]}\u0027)\u000A")
        self._rg_rLstA.append("                        if len(self._lll_sLstE) > 0:\u000A                            self._lll_sLstC = self._lll_sLstE[1].split(\u0027:\u0027)\u000A")
        self._rg_rLstA.append("                            self._lll_sLstC.pop(0)\u000A                            self._lll_sStrA = f\u0027<^./>{self._lll_sLstA[0]}({self._lll_sLstC[0]}:{self._lll_sLstC[1]}:{self._lll_sLstC[2]})/:/={self._lll_sLstC[3]}/|:/\u0027\u000A")
        self._rg_rLstA.append("                            self._lll_sStrA = f\u0027{self._lll_sStrA}{self._lll_sLstA[0]}_mrg_{self._lll_sIntC}(\u0027\u000A                            self._lll_sLstD = self._lll_sLstC[3].split(\u0027,\u0027)\u000A")
        self._rg_rLstA.append("                            self._lll_sLstD = [int(mtr) for mtr in self._lll_sLstD]\u000A                            self.sqtpp_lll_ntr_pgdf([self._lll_sLstC[0], self._lll_sLstC[1]], int(self._lll_sLstC[2]), self._lll_sLstD)\u000A")
        self._rg_rLstA.append("                            self._lll_sFncRtrn = f\u0027{self._lll_sFncRtrn}{self._lll_sStrA}{self._lll_sIntD[0]}:{self._lll_sIntD[1]}:{self._lll_sIntD[2]})//:/={self._lll_sIntD[3]}/:|/<./^>\u0027\u000A")
        self._rg_rLstA.append("                        else:\u000A                            return None\u000A                    else:\u000A                        return None\u000A")
        self._rg_rLstA.append("                self._lll_sFncRtrn = f\u0027{self._lll_sFncRtrn}[/%^/].//!>\u0027\u000A                return self._lll_sFncRtrn\u000A        else:\u000A")
        self._rg_rLstA.append("            return None\u000A#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_write_new(self, brnchPth) -> str:\u000A")
        self._rg_rLstA.append("        self._lll_rLstB = None\u000A        if isinstance(brnchPth, str):\u000A            self._lll_rStrA = re.search(r\u0027:\^:.*?:\^:\u0027, brnchPth)\u000A")
        self._rg_rLstA.append("            if self._lll_rStrA:\u000A                self._lll_rStrA = self._lll_rStrA.group().replace(\u0027:^:\u0027,\u0027\u0027)\u000A                self._lll_rLstA = re.findall(r\u0027</\{.*?\}/>\u0027, brnchPth)\u000A")
        self._rg_rLstA.append("                if len(self._lll_rLstA) > 0:\u000A                    self._lll_rLstB = [f\u0027<!//.]|>{self._lll_rStrA}<|[/^%/]\u0027]\u000A")
        self._rg_rLstA.append("                    self._lll_rIntB = len(self._lll_rLstA)\u000A                    for self._lll_rIntA in range(self._lll_rIntB):\u000A")
        self._rg_rLstA.append("                        self._lll_rLstA[self._lll_rIntA] = self._lll_rLstA[self._lll_rIntA].replace(\u0027</{\u0027,\u0027<^./>\u0027).replace(\u0027}/>\u0027,\u0027<./^>\u0027)\u000A")
        self._rg_rLstA.append("                        self._lll_rLstA[self._lll_rIntA] = self._lll_rLstA[self._lll_rIntA].replace(\u0027:\u0027,\u0027/|:/\u0027).replace(\u0027!\u0027,\u0027/:|/\u0027)\u000A                        self._lll_rLstA[self._lll_rIntA] = self._lll_rLstA[self._lll_rIntA].replace(\u0027==\u0027,\u0027//:/\u0027).replace(\u0027=\u0027,\u0027/:/\u0027)\u000A")
        self._rg_rLstA.append("                        self._lll_rLstB.append(self._lll_rLstA[self._lll_rIntA].replace(\u0027/:/\u0027,\u0027/:/=\u0027).replace(\u0027%\u0027,\u0027:\u0027))\u000A                    if len(self._lll_rLstB) < 2: self._lll_rLstB = None\u000A")
        self._rg_rLstA.append("                    else:\u000A                        if self._lll_sBoolA: self._lll_rLstB.append(\u0027[/%^/].//!>\u0027)\u000A                        self._lll_rLstB = \u0027\u0027.join(self._lll_rLstB)\u000A")
        self._rg_rLstA.append("        return self._lll_rLstB\u000A#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_read(self, brnchPth) -> list:\u000A")
        self._rg_rLstA.append("        self._lll_sRtrn = []\u000A        if isinstance(brnchPth, str): brnchPth = [brnchPth]\u000A        self._lll_rIntB = len(brnchPth)\u000A")
        self._rg_rLstA.append("        for self._lll_rIntA in range(self._lll_rIntB):\u000A            self._lll_rLstA = brnchPth[self._lll_rIntA].split(\u0027,\u0027)\u000A")
        self._rg_rLstA.append("            if self.sqtpp_lll_ntr_lctt(self._lll_rLstA[0]):\u000A                self._lll_rLstB = self._lll_rLstA[1].split(\u0027:\u0027)\u000A")
        self._rg_rLstA.append("                self.sqtpp_lll_ntr_srch(2, r\u0027<\^\./>\u0027 + re.escape(self._lll_rLstB[0]) + r\u0027.*?<\./\^>\u0027, self._lll_rIntC, None)\u000A                if self._lll_sSrchRtrn != None:\u000A")
        self._rg_rLstA.append("                    self._lll_sRtrn.append(f\u0027:^:{self._lll_rLstA[0]}\u0027)\u000A                    self._lll_rStrA = self._lll_rLstB[0]\u000A")
        self._rg_rLstA.append("                    self._lll_rLstB.pop(0)\u000A                    self._lll_rIntE = len(self._lll_rLstB)\u000A                    for self._lll_rIntD in range(self._lll_rIntE):\u000A")
        self._rg_rLstA.append("                        if self._lll_rLstB[self._lll_rIntD] == self._lll_rStrA:\u000A                            self.sqtpp_lll_ntr_srch(2, r\u0027<\^\./>\u0027 + re.escape(self._lll_rStrA) + r\u0027.*?/\|:/\u0027, self._lll_rIntC, None)\u000A")
        self._rg_rLstA.append("                            if self._lll_sSrchRtrn != None: self.sqtpp_lll_ntr_rd_ext_apd()\u000A                        else:\u000A")
        self._rg_rLstA.append("                            self.sqtpp_lll_ntr_srch(5, f\u0027<^./>{self._lll_rStrA}\u0027, self._lll_rIntC, None)\u000A                            self._lll_sSrchPosRtrn+=10\u000A")
        self._rg_rLstA.append("                            self._lll_rIntF = self._lll_sNtr[self._lll_rIntC].find(\u0027<./^>\u0027, self._lll_sSrchPosRtrn)\u000A                            self.sqtpp_lll_ntr_srch(3, r\u0027/\|:/\u0027 + re.escape(self._lll_rLstB[self._lll_rIntD]) + r\u0027.*?/:\|/\u0027, self._lll_rIntC, [self._lll_sSrchPosRtrn, self._lll_rIntF])\u000A")
        self._rg_rLstA.append("                            if self._lll_sSrchRtrn != None:\u000A                                self._lll_sSrchRtrn = self._lll_sSrchRtrn.replace(\u0027/|:/\u0027,\u0027\u0027).replace(\u0027/:|/\u0027,\u0027\u0027)\u000A")
        self._rg_rLstA.append("                                self._lll_sRtrn.append(self._lll_sSrchRtrn.replace(\u0027(\u0027,\u0027:\u0027).replace(\u0027)\u0027,\u0027:\u0027).replace(\u0027//:/=\u0027,\u0027\u0027))\u000A        return self._lll_sRtrn\u000A")
        self._rg_rLstA.append("#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_read_whole_branch(self, brnchPth) -> list:\u000A")
        self._rg_rLstA.append("        self._lll_sRtrn = []\u000A        if isinstance(brnchPth, str):\u000A            self._lll_rLstA = brnchPth.split(\u0027,\u0027)\u000A")
        self._rg_rLstA.append("            if len(self._lll_rLstA) == 2:\u000A                if self.sqtpp_lll_ntr_lctt(self._lll_rLstA[0]):\u000A                    self.sqtpp_lll_ntr_srch(2, r\u0027<\^\./>\u0027 + re.escape(self._lll_rLstA[1]) + r\u0027.*?<\./\^>\u0027, self._lll_rIntC, None)\u000A")
        self._rg_rLstA.append("                    if self._lll_sSrchRtrn != None:\u000A                        self._lll_sRtrn.append(f\u0027:^:{self._lll_rLstA[0]}\u0027)\u000A")
        self._rg_rLstA.append("                        self.sqtpp_lll_ntr_srch(2, r\u0027<\^\./>\u0027 + re.escape(self._lll_rLstA[1]) + r\u0027.*?/\|:/\u0027, self._lll_rIntC, None)\u000A                        if self._lll_sSrchRtrn != None:\u000A")
        self._rg_rLstA.append("                            self.sqtpp_lll_ntr_rd_ext_apd()\u000A                            self.sqtpp_lll_ntr_srch(5, f\u0027<^./>{self._lll_rLstA[1]}\u0027, self._lll_rIntC, None)\u000A")
        self._rg_rLstA.append("                            self._lll_sSrchPosRtrn+=10\u000A                            self._lll_rIntF = self._lll_sNtr[self._lll_rIntC].find(\u0027<./^>\u0027, self._lll_sSrchPosRtrn)\u000A")
        self._rg_rLstA.append("                            self.sqtpp_lll_ntr_srch(4, r\u0027/\|:/.*?/:\|/\u0027, self._lll_rIntC, [self._lll_sSrchPosRtrn, self._lll_rIntF])\u000A                            if self._lll_sSrchRtrn != None:\u000A")
        self._rg_rLstA.append("                                self._lll_rIntB = len(self._lll_sSrchRtrn)\u000A                                for self._lll_rIntA in range(self._lll_rIntB):\u000A")
        self._rg_rLstA.append("                                    self._lll_sSrchRtrn[self._lll_rIntA] = self._lll_sSrchRtrn[self._lll_rIntA].replace(\u0027/|:/\u0027,\u0027\u0027).replace(\u0027/:|/\u0027,\u0027\u0027)\u000A")
        self._rg_rLstA.append("                                    self._lll_sRtrn.append(self._lll_sSrchRtrn[self._lll_rIntA].replace(\u0027(\u0027,\u0027:\u0027).replace(\u0027)\u0027,\u0027:\u0027).replace(\u0027//:/=\u0027,\u0027\u0027))\u000A")
        self._rg_rLstA.append("        return self._lll_sRtrn\u000A#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_rd_ext_apd(self):\u000A")
        self._rg_rLstA.append("        self._lll_sSrchRtrn = self._lll_sSrchRtrn.replace(\u0027<^./>\u0027,\u0027\u0027).replace(\u0027/|:/\u0027,\u0027\u0027)\u000A        self._lll_sSrchRtrn = self._lll_sSrchRtrn.replace(\u0027(\u0027,\u0027:\u0027).replace(\u0027)\u0027,\u0027:\u0027).replace(\u0027/:/=\u0027,\u0027\u0027)\u000A")
        self._rg_rLstA.append("        self._lll_sRtrn.append(f\u0027::^{self._lll_sSrchRtrn}\u0027)\u000A#|___________________________________________________________________________________\u000A")
        self._rg_rLstA.append("    def sqtpp_lll_ntr_lctt(self, ntrNm: str) -> bool:\u000A        self._lll_rIntC = 0\u000A        self._lll_rBoolA = False\u000A")
        self._rg_rLstA.append("        self._lll_rIntD = len(self._lll_sNtr)\u000A        while self._lll_rIntC < self._lll_rIntD:\u000A            self.sqtpp_lll_ntr_srch(5, f\u0027<!//.]|>{ntrNm}<|[/^%/]\u0027, self._lll_rIntC, None)\u000A")
        self._rg_rLstA.append("            if self._lll_sSrchPosRtrn > -1:\u000A                self._lll_rBoolA = True\u000A                break\u000A")
        self._rg_rLstA.append("            self._lll_rIntC+=1\u000A        return self._lll_rBoolA\u000A#|___________________________________________________________________________________\u000A")
        self._rg_rLstA.append("    def sqtpp_lll_ntr_srch(self, dsg: int, ntrPtrn: str, ntrIdx: int, posIdx: list):\u000A        if dsg == 1:\u000A            self._lll_sSrchRtrn = re.findall(ntrPtrn, self._lll_sNtr[ntrIdx])\u000A")
        self._rg_rLstA.append("            if len(self._lll_sSrchRtrn) < 1: self._lll_sSrchRtrn = None\u000A        elif dsg == 2 or dsg == 3:\u000A            if dsg == 2: self._lll_sSrchRtrn = re.search(ntrPtrn, self._lll_sNtr[ntrIdx])\u000A")
        self._rg_rLstA.append("            else: self._lll_sSrchRtrn = re.search(ntrPtrn, self._lll_sNtr[ntrIdx][posIdx[0]:posIdx[1]])\u000A            if not self._lll_sSrchRtrn: self._lll_sSrchRtrn = None\u000A")
        self._rg_rLstA.append("            else: self._lll_sSrchRtrn = self._lll_sSrchRtrn.group()\u000A        elif dsg == 4:\u000A            self._lll_sSrchRtrn = re.findall(ntrPtrn, self._lll_sNtr[ntrIdx][posIdx[0]:posIdx[1]])\u000A")
        self._rg_rLstA.append("            if len(self._lll_sSrchRtrn) < 1: self._lll_sSrchRtrn = None\u000A        else: self._lll_sSrchPosRtrn = self._lll_sNtr[ntrIdx].find(ntrPtrn)\u000A")
        self._rg_rLstA.append("#|___________________________________________________________________________________\u000A    def sqtpp_lll_ntr_pgdf(self, plndrmLst: list, pvtCnd: int, mtrLst: list):\u000A")
        self._rg_rLstA.append("        self._lll_sIntD = [int(plndrmLst[0][:4]),int(plndrmLst[0][3:]),int(plndrmLst[1][:4]),int(plndrmLst[1][3:])]\u000A        self._lll_sIntF = len(mtrLst)\u000A")
        self._rg_rLstA.append("        self._lll_sIntI = set()\u000A        self._lll_sIntL = []\u000A        for self._lll_sIntE in range(self._lll_sIntF):\u000A")
        self._rg_rLstA.append("            self._lll_sBoolA = False\u000A            self._lll_sIntG = math.sqrt(mtrLst[self._lll_sIntE]) + (math.pi * (math.cos(pvtCnd * min(mtrLst)/3)))\u000A")
        self._rg_rLstA.append("            self._lll_sIntH = math.sqrt(mtrLst[self._lll_sIntE]) + (math.pi * (math.tan(pvtCnd * max(mtrLst)/2)))\u000A            if self._lll_sIntG == self._lll_sIntH:\u000A")
        self._rg_rLstA.append("                self._lll_sBoolA = True\u000A                self._lll_sIntI.add(self._lll_sIntG)\u000A            for self._lll_sIntJ in range(4):\u000A")
        self._rg_rLstA.append("                if not self._lll_sBoolA:\u000A                    self._lll_sIntD[self._lll_sIntJ] = math.ceil(mtrLst[self._lll_sIntE] * self._lll_sIntH * (self._lll_sIntD[self._lll_sIntJ] // self._lll_sIntG))\u000A")
        self._rg_rLstA.append("                else:\u000A                    self._lll_sIntK = list(self._lll_sIntI)\u000A                    self._lll_sIntM = min(self._lll_sIntK)\u000A")
        self._rg_rLstA.append("                    self._lll_sIntD[self._lll_sIntJ] = math.ceil(self._lll_sIntM + (mtrLst[self._lll_sIntE] * self._lll_sIntH * (self._lll_sIntD[self._lll_sIntJ] // self._lll_sIntG)))\u000A")
        self._rg_rLstA.append("                if len(str(self._lll_sIntD[self._lll_sIntJ])) == 7: self._lll_sIntL.append(self._lll_sIntD[self._lll_sIntJ])\u000A        if len(self._lll_sIntL) > 1:\u000A")
        self._rg_rLstA.append("            self._lll_sIntD = [max(self._lll_sIntL), min(self._lll_sIntL)]\u000A            self._lll_sIntD.append(math.ceil(((self._lll_sIntD[0] * self._lll_sIntD[1]) / (self._lll_sIntD[0] - self._lll_sIntD[1])) / 144))\u000A")
        self._rg_rLstA.append("            self._lll_sIntE = f\u0027{self._lll_sIntD[0]}{self._lll_sIntD[1]}\u0027\u000A            self._lll_sIntM = set()\u000A            for self._lll_sIntI in self._lll_sIntE: self._lll_sIntM.add(int(self._lll_sIntI))\u000A")
        self._rg_rLstA.append("            self._lll_sIntE = list(self._lll_sIntM)\u000A            self._lll_sIntE = [str(_) for _ in self._lll_sIntE]\u000A            self._lll_sIntD.append(\u0027,\u0027.join(self._lll_sIntE))\u000A")
        self._rg_rLstA.append("        else:\u000A            return None           \u000A#|___________________________________________________________________________________\u000A")
        self._rg_rLstA.append("#| Zechariah 14:9\u000A\u000Adef sqtpp_lll_ntr_run(mode: str, branchPath, mergePath: list):\u000A    lllCls = SqtppNtrLLL_Fncs()\u000A")
        self._rg_rLstA.append("    return lllCls.sqtpp_lll_ntr(mode, branchPath, mergePath)\u000A")
        self._rg_rLstA = ''.join(self._rg_rLstA)
        with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_NTR.py', 'w') as flObjNtrWrt: flObjNtrWrt.write(self._rg_rLstA)
        self._rg_rLstA = None
        if not os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_NTR.py'):
            raise Exception(f"[sqtpp-reg >> NTR-TREE] - could not write the ntr-tree module sqtpp1_2_NTR.py to Staqtapp's current working directory '{SQTPP_MDL_DIR}'")
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_mvi8_intrpt(self, mviSrc):
        # FNC_ID=ST12-55923950305154
        # SqtppFncs slots in use: (_sf_rBoolB, _sf_rBoolC, _sf_rBoolD, _sf_rBoolE, _sf_rIntA, _sf_rIntB, _sf_rLstA, _sf_rLstB, _sf_rLstC, _sf_rLstD, _sf_rLstI, _sf_rStrA, _sf_rStrB, _sf_rStrC, _sf_sBoolX, _sf_sIntX, _sf_sLstX)
        
        # :: EXAMPLE MVI8 RUN ::
        # "::{201,181,223} lock<GRP_LCK1:9521,mode=join,null> ;:<GRP_CRD1:|2,|1,~8> :;<GRP_CRD2:{|2~1},~3>"
        # "map<MAP_GRP_LCK1:R=GRP_CRD2,mode=reflect> |/3 /|0 |/9 /-4 //-5 //6 /7- /^==GRP_LCK1;"
        # "^==/MAP_GRP_LCK1; menorah<GRP_LCK1:125, 224, 9, 28> /|2 lock<TMD:/28-,none>########END MVI"
        
        # returns: (1 or an exception)
        # -1=mvi source code is not a list or a string type
        # -2=invalid map shift declaring found
        # -3=invalid shift lock declaring found
        # -4=invalid bonding digit declaring found
        # -5=invalid palindrome bracket declaring found
        # -6=invalid center-halves declaring found
        # -7=invalid menorah symmetry simulate instruction found
        # -8=invalid map symmetry simulate instruction found
        # -9=invalid lock symmetry simulate instrucion found
        rtrn = 1
        if isinstance(mviSrc, (list, str)):
            if isinstance(mviSrc, list): mviSrc = ''.join(mviSrc)
            mviSrc = mviSrc.replace(' ','')
            self._sf_rLstA = set('-1234567890')
            self._sf_rLstB = set('1234567890')
            self._sf_sBoolX = False
            self._sf_rBoolD = False
            self._sf_rBoolC = False
            self._sf_rBoolB = None
            self._sf_rStrC = None
            self._sf_sIntX = None
            self._sf_rIntA = -1
            self._sf_rLstC = []
            self._sf_rLstD = []
            self._sf_rLstI = []
            for self._sf_rStrB in mviSrc:
                self._sf_rBoolE = False
                self._sf_rIntA+=1
                if not self._sf_sBoolX:
                    self._sf_rLstD.append(self._sf_rStrB)
                    if self._sf_rStrB == '/' and mviSrc[self._sf_rIntA+1] == '^':
                        self._sf_sLstX = re.search(r'\^==.*?\;', mviSrc[self._sf_rIntA+1:])
                        if self._sf_sLstX: self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'SLC', True, True
                        else: rtrn = -2
                    elif self._sf_rStrB == '^' and mviSrc[self._sf_rIntA+1] == '=':
                        self._sf_sLstX = re.search(r'==\/.*?\;', mviSrc[self._sf_rIntA+1:])
                        if self._sf_sLstX: self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'SCR', True, True
                        else: rtrn = -2
                    elif self._sf_rStrB == '/' and mviSrc[self._sf_rIntA+1] == '|':
                        self._sf_rBoolE = True
                        if set(mviSrc[self._sf_rIntA+2]).issubset(self._sf_rLstB): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 2, f'SLR%{mviSrc[self._sf_rIntA+2]}')
                        else: rtrn = -3
                    elif self._sf_rStrB == '|' and mviSrc[self._sf_rIntA+1] == '/':
                        self._sf_rBoolE = True
                        if set(mviSrc[self._sf_rIntA+2]).issubset(self._sf_rLstB): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 2, f'SLL%{mviSrc[self._sf_rIntA+2]}')
                        else: rtrn = -3
                    elif self._sf_rStrB == '/':
                        self._sf_rBoolE = True
                        if mviSrc[self._sf_rIntA+1] == '/': self._sf_rBoolB = True
                        else: self._sf_rBoolB = False
                        if self._sf_rBoolB:
                            if set(mviSrc[self._sf_rIntA+2]).issubset(self._sf_rLstA) and set(mviSrc[self._sf_rIntA+3]).issubset(self._sf_rLstA): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 3, f'DDD%//{mviSrc[self._sf_rIntA+2]}{mviSrc[self._sf_rIntA+3]}')
                            else:
                                if set(mviSrc[self._sf_rIntA+2]).issubset(self._sf_rLstA): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 2, f'DDD%//{mviSrc[self._sf_rIntA+2]}')
                                else: rtrn = -4
                        else:
                            if set(mviSrc[self._sf_rIntA+1]).issubset(self._sf_rLstA) and set(mviSrc[self._sf_rIntA+2]).issubset(self._sf_rLstA): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 2, f'SDD%/{mviSrc[self._sf_rIntA+1]}{mviSrc[self._sf_rIntA+2]}')
                            else:
                                if set(mviSrc[self._sf_rIntA+1]).issubset(self._sf_rLstA): self.sqtpp_ntr_mvi8_intrpt_core(None, True, False, 1, f'SDD%/{mviSrc[self._sf_rIntA+1]}')
                                else: rtrn = -4
                    elif self._sf_rStrB == ':' and mviSrc[self._sf_rIntA+1] == '{':
                        self._sf_sLstX = re.search(r'\{.*?\}', mviSrc[self._sf_rIntA+1:])
                        if self._sf_sLstX:
                            if self._sf_rStrB == ':' and mviSrc[self._sf_rIntA-1] == ':': self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'PDH', True, True
                            else: self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'PDW', True, True
                        else: rtrn = -5
                    elif (self._sf_rStrB == ':' and mviSrc[self._sf_rIntA+1] == ';') or (self._sf_rStrB == ';' and mviSrc[self._sf_rIntA+1] == ':'):
                        if self._sf_rStrB == ':' and mviSrc[self._sf_rIntA+1] == ';': self._sf_rBoolC = True 
                        else: self._sf_rBoolC = False
                        self._sf_sLstX = re.search(r'<.*?>', mviSrc[self._sf_rIntA+1:])
                        if self._sf_sLstX:
                            if self._sf_rBoolC: self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'LCH', True, True
                            else: self._sf_rStrC, self._sf_rBoolD, self._sf_rBoolE = 'RCH', True, True
                        else: rtrn = -6
                    if not self._sf_rBoolE:
                        self._sf_rIntB = len(self._sf_rLstD)
                        if self._sf_rIntB > 2 and self._sf_rIntB < 5:
                            self._sf_rStrA = ''.join(self._sf_rLstD)
                            if self._sf_rStrA.find('map') > -1:
                                self._sf_sLstX = re.search(r'<.*?>', mviSrc[self._sf_rIntA+1:])
                                if self._sf_sLstX: self._sf_rStrC, self._sf_rBoolD = 'MAP', True
                                else: rtrn = -8
                            elif self._sf_rStrA.find('lock') > -1:
                                self._sf_sLstX = re.search(r'<.*?>', mviSrc[self._sf_rIntA+1:])
                                if self._sf_sLstX: self._sf_rStrC, self._sf_rBoolD = 'LCK', True
                                else: rtrn = -9
                        else:
                            self._sf_rStrA = ''.join(self._sf_rLstD)
                            if self._sf_rStrA.find('menorah') > -1:
                                self._sf_sLstX = re.search(r'<.*?>', mviSrc[self._sf_rIntA+1:])
                                if self._sf_sLstX: self._sf_rStrC, self._sf_rBoolD = 'MNH', True
                                else: rtrn = -7
                    if self._sf_rBoolD:
                        self._sf_rBoolD = False
                        self.sqtpp_ntr_mvi8_intrpt_core(self._sf_rStrC, True, True, None, None)
                else:
                    self._sf_sIntX-=1
                    if self._sf_sIntX < 1:
                        self._sf_rLstD = []
                        self._sf_sBoolX = False
                if rtrn < 0 or self._sf_rStrB == '#':
                    break
        else: rtrn -1
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_mvi8_intrpt_core(self, ins: str, sbx: bool, grp: bool, ix: int, apd: str):
        # <<<
        # returns:
        try:
            if sbx: self._sf_sBoolX = True
            if grp:
                self._sf_sLstX = self._sf_sLstX.group(0)
                self._sf_sIntX = len(self._sf_sLstX)
                if ins == 'SLC' or ins == 'SCR': self._sf_sLstX = self._sf_sLstX.replace('=','').replace('/','').replace('^','').replace(';','')
                elif ins == 'LCH' or ins == 'RCH': self._sf_sLstX = self._sf_sLstX.replace(':','').replace(';','').replace('<','').replace('>','')
                elif ins == 'PDW' or ins == 'PDH':
                    self._sf_sLstX = self._sf_sLstX.replace('{','').replace('}','')
                    self._sf_rLstE = self._sf_sLstX.split(',')
                    if ins == 'PDH': self.sqtpp_ntr_mvi8_intrpt_core_ext_pdh()
                    else: self._sf_rLstI = [str(plndrm) for plndrm in self._sf_rLstE]
                elif ins == 'MNH' or ins == 'MAP' or ins == 'LCK':
                    self._sf_sLstX = self._sf_sLstX.replace('<','').replace('>','')
                    if ins == 'LCK': self.sqtpp_ntr_mvi8_intrpt_core_ext_lck()
                self._sf_rLstC.append(f'{ins}%{self._sf_sLstX}')
            if not grp:
                self._sf_sIntX = ix
                self._sf_rLstC.append(apd)
        except Exception as err_sqtpp_ntr_mvi8_intrpt_core:
            raise Exception(f'[NTR / MVI8] - a direct MVI8 run error has occured: {err_sqtpp_ntr_mvi8_intrpt_core}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_mvi8_intrpt_core_ext_lck(self):
        # <<<
        # returns:
        self._sf_rLstE = self._sf_sLstX.split('<')
        self._rg_rLstA = self._sf_rLstE[0].split(',')
        #--------------------------------------------
        print(self._rg_rLstA)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_mvi8_intrpt_core_ext_pdh(self):
        # FNC_ID=ST12-15885479069535
        # SqtppFncs slots in use: (_sf_rBoolF, _sf_rIntC, _sf_rIntD, _sf_rIntE, _sf_rIntF, _sf_rLstE, _sf_rLstF, _sf_rLstG, _sf_rLstI, _sf_rStrD)
        # returns: (none)
        self._sf_rIntD = len(self._sf_rLstE)
        for self._sf_rIntC in range(self._sf_rIntD):
            self._sf_rIntE = 1
            self._sf_rLstF = set()
            for self._sf_rStrD in self._sf_rLstE[self._sf_rIntC]:
                if self._sf_rStrD == '0': self._sf_rIntF = 9
                else: self._sf_rIntF = int(self._sf_rStrD)
                self._sf_rIntE = math.floor((math.tan((((self._sf_rIntE*int(self._sf_rIntF))+1)/2))-1)+self._sf_rIntF)
                self._sf_rLstF.add(self._sf_rIntE)
            self._sf_rLstF = list(self._sf_rLstF)
            self._sf_rIntE = len(self._sf_rLstF)
            self._sf_rBoolF = False
            self._sf_rLstG = [1,1]
            self._sf_rIntD = 0
            while self._sf_rIntD < self._sf_rIntE:
                if self._sf_rLstF[self._sf_rIntD] > 9:
                    if self._sf_rLstG[0] <= self._sf_rLstG[1] and not self._sf_rBoolF: self.sqtpp_ntr_mvi8_intrpt_core_ext_pdh_gif(True, False)
                    else: self.sqtpp_ntr_mvi8_intrpt_core_ext_pdh_gif(False, True)
                else:
                    if self._sf_rLstG[0] >= self._sf_rLstG[1] and self._sf_rBoolF: self.sqtpp_ntr_mvi8_intrpt_core_ext_pdh_gif(False, True)
                    else: self.sqtpp_ntr_mvi8_intrpt_core_ext_pdh_gif(True, False)
                self._sf_rIntD+=1
            if self._sf_rBoolF and self._sf_rLstG[1] > self._sf_rLstG[0]: self._sf_rLstI.append(int(f'{self._sf_rLstE[self._sf_rIntC]}1{self._sf_rLstE[self._sf_rIntC][::-1]}'))
            else: self._sf_rLstI.append(int(f'{self._sf_rLstE[self._sf_rIntC]}5{self._sf_rLstE[self._sf_rIntC][::-1]}'))
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_mvi8_intrpt_core_ext_pdh_gif(self, pdhG: bool, pdhF: bool):
        # FNC_ID=ST12-97847763790534
        # SqtppFncs slots in use: (_sf_rBoolF, _sf_rLstG)
        # return: (none)
        if pdhG: self._sf_rLstG[0]+=1
        else: self._sf_rLstG[0]-=1
        if pdhF: self._sf_rBoolF = True
        else: self._sf_rBoolF = False
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_tree_cycle_prime_mcr(self, nrTlmA: int, nrTlmB: int, nrKlmA: int, nrKlmB: int) -> list:
        # <<<
        # returns: (list)
        self._rg_rIntA = lambda x, y: (x[0] * y[1] - x[1] * y[0], x[0] * y[0] + x[1] * y[1], x[0] + y[1] - x[1] * y[0], x[0] * y[0] + x[1] * y[1])
        self._rg_rIntB = lambda x, y: (x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[1] * y[1], x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[1] * y[1])
        self._rg_rIntC = lambda x, y: (math.floor((math.pi * (x[0] * y[1] - x[1] * y[0]) - 1) / y[0]), math.floor((math.atan(x[0] * y[0] + x[1] * y[1]) * y[1]) / x[1]))
        self._rg_rIntD = lambda x, y: (math.ceil((x[0] / y[0])), math.floor((1 + y[1] + (math.pi * (math.sqrt(x[0]) / (x[1] / y[1]))))))
        self._rg_rLstA = self._rg_rIntA((nrTlmA,nrTlmB), (nrKlmA,nrKlmB))
        self._rg_rLstB = self._rg_rIntB(self._rg_rLstA, self._rg_rLstA)
        self._rg_rLstC = self._rg_rIntC(self._rg_rLstA, self._rg_rLstB)
        self._rg_rLstD = self._rg_rIntD(self._rg_rLstB, self._rg_rLstC)
        if self._rg_rLstC[1] > self._rg_rLstD[1]: self._rg_rStrA = 'G'
        elif self._rg_rLstC[1] == self._rg_rLstD[1]: self._rg_rStrA = 'E'
        else: self._rg_rStrA = 'L'
        return [self._rg_rStrA, self._rg_rLstD[0], self._rg_rLstD[1]]
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_ntr_tree_bmh(self, ptrn: str, src: str) -> list:
        # FNC_ID=ST12-75802967891415
        # SqtppFncs slots in use: (_sf_rStrD)
        # returns: (!slots _sf_rStrD is the string source!)
        self._rg_rIntC = len(ptrn)
        self._rg_rLstA = [self._rg_rIntC for self._rg_rIntB in range(256)]
        self._rg_rIntD = self._rg_rIntC-1
        for self._rg_rIntA in range(self._rg_rIntD): self._rg_rLstA[ord(ptrn[self._rg_rIntA])] = self._rg_rIntC-self._rg_rIntA-1
        self._rg_rLstB = []
        self._rg_rIntA = 0
        self._rg_rIntD = len(src)
        while self._rg_rIntA < self._rg_rIntD:
            self._rg_rIntB = 0
            while self._rg_rIntB < self._rg_rIntC and src[self._rg_rIntA-self._rg_rIntB] == ptrn[self._rg_rIntC - 1 - self._rg_rIntB]:
                self._rg_rIntB+=1
            if self._rg_rIntB == self._rg_rIntC:
                self._rg_rLstB.append(self._rg_rIntA-1)
                self._rg_rIntA+=1
            else: self._rg_rIntA+=max(self._rg_rLstA[ord(src[self._rg_rIntA])], self._rg_rIntB)
        return self._rg_rLstB
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
#                                                                      •
#//////////           .          .                                      •
#/////////                    .            .                  /\•.•.•    \       .
#////////         .                                          /  \    \    \
#///////              .           / //__|__\\ \       .     /.   \    \    \     .
#//////   .         .            / //___|___\\ \           /      \____\    \   . _____
#•••••••••••••••••••••••••••••••••••\•••••••/•••__________/.•.•.•./    /_____.•.•.
#//////                   .      / //___|___\\ \          \      /    /       .   \
#///////    .      .              / //_   _\\ \        .   \    /    /   •   .     \
#////////       .                  / //_ _\\ \     .        \  /    /            .  \
#/////////               __________/ //___\\ \_________      \/____/   .             \
#//////////      .     __________________________________                             •
#                                                                                      
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer(self, regKyRd: bool, regKyNm: str, regKyDt, schm: str):
        # FNC_ID=ST12-27309548944050
        # SqtppFncs slots in use: (non-local)
        # returns:
        rtrn = None
        if not regKyRd:
            if schm != None:
                if isinstance(schm, str):
                    if schm.find('/') > -1:
                        if not os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py'): rtrn = self.sqtpp_registry_homer_build(False, None, None, schm)
                        else:
                            with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'r') as flObjRegRdA: self._rg_rStrA = flObjRegRdA.read()
                            rtrn = self.sqtpp_registry_homer_add_schema(schm)
                        if rtrn == 1:
                            return True
                    else:
                        if isinstance(regKyNm, str):
                            if regKyDt != None:
                                if not os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py'): rtrn = self.sqtpp_registry_homer_build(True, regKyNm, regKyDt, schm)
                                else:
                                    with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'r') as flObjRegRdB: self._rg_rStrA = flObjRegRdB.read()
                                    rtrn = self.sqtpp_registry_homer_add_key(regKyNm, regKyDt, schm)
                                if rtrn == 1:
                                    return True
                                else:
                                    if rtrn == -1:
                                        raise Exception('[sqtpp-reg >> registry] (add registry key) - invalid chars @keyName or/and @harpSchema as a schema name, valid chars: _ a-z A-Z 0-9')
                                    elif rtrn == -2:
                                        raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyData cannot be a nested list, currently unsupported')
                                    elif rtrn == -3:
                                        raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyData cannot be bytes or a bytearray type, currently unsupported')
                                    elif rtrn == -4:
                                        raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyData is an invalid type, unknown or unsupported type')
                                    elif rtrn == -5:
                                        raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyData has found use of char " in string(s) declarings, not supported')
                                    elif rtrn == -6:
                                        raise Exception(f'[sqtpp-reg >> registry] (add registry key) - @harpSchema as a schema name "{schm}" for adding a registry key, no such harp-schema found in registry; all registry keys must have a valid assigned schema')
                            else:
                                raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyData cannot be None for add/edit of a registry key, not supported')
                        else:
                            raise Exception('[sqtpp-reg >> registry] (add registry key) - @keyName must be a str type for add or edit of a registry key')
                else:
                    raise Exception('[sqtpp-reg >> registry] - @harpSchema must be a str type if @isRead=False, either a file path to a schema file or a schema name if adding a registry key')
            else:
                raise Exception('[sqtpp-reg >> registry] - @harpSchema is None, must be either a file path or a schema name if @isRead=False')
        else:
            if isinstance(regKyNm, str):
                if regKyDt != None:
                    if len(regKyDt) > 0:
                        rtrn = self.sqtpp_registry_homer_read(regKyNm, regKyDt)
                    else:
                        raise Exception('[sqtpp-reg >> registry] (read registry key) - @keyData use for a comparison key on read state must have a length')
                else:
                    rtrn = self.sqtpp_registry_homer_read(regKyNm, None)
                if isinstance(rtrn, str):
                    if rtrn.find('(.>>!:!<<.)') > -1:
                        rtrn = rtrn.split('=')
                        rtrn = int(rtrn[1])
                        if rtrn == 1:
                            raise Exception(f'[sqtpp-reg >> registry] (read registry key) - registry key "{regKyNm}" was not found')
                        elif rtrn == 2:
                            raise Exception('[sqtpp-reg >> registry] (read registry key) - invalid registry key header declaring discovered')
                        elif rtrn == 3:
                            raise Exception('[sqtpp-reg >> registry] (read registry key) - invalid registry key data declaring discovered')
                        elif rtrn == 4:
                            raise Exception(f'[sqtpp-reg >> registry] (read registry key) - registry key "{regKyNm}" assigned harp-schema was not found')
                        elif rtrn == 5:
                            raise Exception('[sqtpp-reg >> registry] (read registry key) - invalid harp-schema header declaring')
                        elif rtrn == 6:
                            raise Exception('[sqtpp-reg >> registry] (read registry key) - invalid harp-schema data declaring')
                        elif rtrn == 7:
                            raise Exception(f'[sqtpp-reg >> registry] (read registry key) - ast conversion error of registry key "{regKyNm}" value')
                    else:
                        return rtrn
                return rtrn
            else:
                raise Exception('[sqtpp-reg >> registry] (read registry key) - @keyName must be a str type for return read of a registry key')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_read(self, kyNm: str, kyDt):
        # FNC_ID=ST12-52552189378799
        # SqtppFncs slots in use: (hidden)
        # returns: (reloads sqtpp1_2_REG.py if changed, properly and from here only)
        if not self._rg_sMdlTrg:
            self._rg_sMdlTrg = True
            self._rg_sMdlEdt = False
            import sqtpp1_2_REG
        else:
            if 'sqtpp1_2_REG' in sys.modules:
                if self._rg_sMdlEdt:
                    self._rg_sMdlEdt = False
                    importlib.reload(sqtpp1_2_REG)
                    sys.modules.pop('sqtpp1_2_REG', None)
            else:
                self._rg_sMdlEdt = False
                import sqtpp1_2_REG
        if set(kyNm).issubset(SQTPP_SET_VARS):
            return sqtpp1_2_REG.sqtpp_reg_lll_run(kyNm, kyDt)
        else:
            raise Exception('[sqtpp-reg >> registry] (read registry key) - @keyName is not a valid staqtapp registry key name, has invalid char(s) valid chars: _ a-z A-Z 0-9')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_build(self, addRegKy: bool, regKyNm: str, regKyDt, schm: str):
        # FNC_ID=ST12-29710212262687
        # SqtppFncs slots in use: (non-local)
        # returns: (none)
        self._rg_rLstA = []
        self._rg_rStrA = '\n'
        self._rg_rLstA.append(f"# This py-module is auto-generated by the Staqtapp1.2 vfs env-var library for registry functions use. Edit at your own risk.{self._rg_rStrA}")
        self._rg_rLstA.append(f"{self._rg_rStrA}from collections import deque{self._rg_rStrA}{self._rg_rStrA}import math{self._rg_rStrA}import ast{self._rg_rStrA}import re{self._rg_rStrA}")
        self._rg_rLstA.append(f"{self._rg_rStrA}class SqtppRegLLL():{self._rg_rStrA}{self._rg_rStrA}    __slots__ = (){self._rg_rStrA}{self._rg_rStrA}    def __init__(self):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        pass{self._rg_rStrA}{self._rg_rStrA}{self._rg_rStrA}class SqtppRegLLL_Fncs(SqtppRegLLL):{self._rg_rStrA}{self._rg_rStrA}    __slots__ = ('_lll_sRdrRtrn', '_lll_sSpdrRtrn', '_lll_sThemas', '_lll_sTharpe', '_lll_sKyHdr', '_lll_sKyDat', '_lll_sKyStDat', '_lll_sKyBln', '_lll_sKyCmx', '_lll_sKySet', '_lll_sHarpErr', '_lll_sPrsErr', '_lll_sPrsRtrn', '_lll_sTyp1', '_lll_sNmId', '_lll_sLmb', '_lll_sLstA', '_lll_sBlnSw', '_lll_rStrA', '_lll_rStrB', '_lll_rStrC', '_lll_rStrD', '_lll_rLstA', '_lll_rLstB', '_lll_rLstC', '_lll_rLstD', '_lll_rLstE', '_lll_rLstF', '_lll_rIntA', '_lll_rIntB', '_lll_rIntC', '_lll_rIntD', '_lll_rIntE', '_lll_rBoolA', '_lll_rBoolB', '_lll_rBoolC', '_lll_rBoolD'){self._rg_rStrA}")
        self._rg_rLstA.append(f"{self._rg_rStrA}    def __init__(self):{self._rg_rStrA}{self._rg_rStrA}        self._lll_sThemas = deque([{self._rg_rStrA}            'SQTPP_REG_KEY:8888888888:__LTLKV1:88||88||8888||88||88||88||AM:8888:8888:9S8:____SQTPP_REG_STGS_KEY____:____SQTPP_REG_STGS_SCHM____=[~||/LRK:default~||/]:|.||.|:'{self._rg_rStrA}")
        self._rg_rLstA.append(f"        ]){self._rg_rStrA}#|:>|<:|_______________________________________________________________________________{self._rg_rStrA}        self._lll_sTharpe = deque([{self._rg_rStrA}")
        self._rg_rLstA.append(f"            'SQTPP_REG_HARP_SCHEMA:88||88||8888||88||88||88||AM:8888888888:008S9:____SQTPP_REG_STGS_SCHM____=>!<:|.||.|:'{self._rg_rStrA}        ]){self._rg_rStrA}")
        self._rg_rLstA.append(f"#|.<:>.|_______________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_key_rdr(self, keyNm: str, keyDt):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        try:{self._rg_rStrA}            if keyDt != None: self._lll_sKyStDat = keyDt{self._rg_rStrA}            else: self._lll_sKyStDat = None{self._rg_rStrA}")
        self._rg_rLstA.append(f"            self._lll_rIntA = 0{self._rg_rStrA}            self._lll_sKyBln = False{self._rg_rStrA}            self._lll_sKyCmx = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"            self._lll_sKySet = False{self._rg_rStrA}            self._lll_rBoolA = False{self._rg_rStrA}            self._lll_sRdrRtrn = None{self._rg_rStrA}")
        self._rg_rLstA.append(f"            self._lll_rStrA = ':9S8:' + keyNm  + ':'{self._rg_rStrA}            self._lll_rIntB = len(self._lll_sThemas){self._rg_rStrA}            while self._lll_rIntA < self._lll_rIntB:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                if self._lll_sThemas[self._lll_rIntA].find(self._lll_rStrA) > -1:{self._rg_rStrA}                    self._lll_rBoolA = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    break{self._rg_rStrA}                self._lll_rIntA+=1{self._rg_rStrA}            if self._lll_rBoolA:{self._rg_rStrA}                self._lll_sKyHdr = re.findall(r'SQTPP_REG_KEY\:.*?\:9S8\:' + re.escape(keyNm) + '.*?=', self._lll_sThemas[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                if len(self._lll_sKyHdr) > 0:{self._rg_rStrA}                    self._lll_sKyHdr[0] = self._lll_sKyHdr[0].replace('=', ''){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    self._lll_sKyHdr = self._lll_sKyHdr[0].split(':'){self._rg_rStrA}                    self._lll_sKyHdr.pop(0){self._rg_rStrA}                    self._lll_sKyDat = re.findall(r'=.*?:\|\.\|\|\.\|:', self._lll_sThemas[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    if len(self._lll_sKyDat) > 0:{self._rg_rStrA}                        self._lll_sKyDat = self._lll_sKyDat[0].replace(':|.||.|:', ''){self._rg_rStrA}")
        self._rg_rLstA.append(f"                        self._lll_sKyDat = self._lll_sKyDat[1:len(self._lll_sKyDat)]{self._rg_rStrA}                        if self._lll_sKyDat.lower() == 'false' or self._lll_sKyDat.lower() == 'true': self._lll_sKyBln = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        if self._lll_sKyDat.find('complex(') > -1: self._lll_sKyCmx = True{self._rg_rStrA}                        if self._lll_sKyDat.find('set(') > -1: self._lll_sKySet = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        self._lll_sRdrRtrn = self.sqtpp_reg_harp_key(){self._rg_rStrA}                        if self._lll_sHarpErr:{self._rg_rStrA}                            if self._lll_sRdrRtrn == -1: self._lll_sRdrRtrn = '(.>>!:!<<.)=4'{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            elif self._lll_sRdrRtrn == -2: self._lll_sRdrRtrn = '(.>>!:!<<.)=5'{self._rg_rStrA}                            elif self._lll_sRdrRtrn == -3: self._lll_sRdrRtrn = '(.>>!:!<<.)=6'{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            elif self._lll_sRdrRtrn == -4: self._lll_sRdrRtrn = '(.>>!:!<<.)=7'{self._rg_rStrA}                        else:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            self.sqtpp_reg_harp_prc(){self._rg_rStrA}                            if self._lll_sKyStDat != None:{self._rg_rStrA}                                try:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                                    if self._lll_sKyDat == self._lll_sKyStDat:{self._rg_rStrA}                                        return True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                                    else:{self._rg_rStrA}                                        return False{self._rg_rStrA}                                except Exception as reg_typ_cmp_err:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                                    return False{self._rg_rStrA}                            else:{self._rg_rStrA}                                return self._lll_sKyDat{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else: self._lll_sRdrRtrn = '(.>>!:!<<.)=3'{self._rg_rStrA}                else: self._lll_sRdrRtrn = '(.>>!:!<<.)=2'{self._rg_rStrA}")
        self._rg_rLstA.append(f"            else: self._lll_sRdrRtrn = '(.>>!:!<<.)=1'{self._rg_rStrA}            return self._lll_sRdrRtrn{self._rg_rStrA}        except Exception as sqtpp_registry_err:{self._rg_rStrA}")
        self._rg_rLstA.append(f"            raise Exception('[sqtpp-reg >> registry] direct registry module key reader exception ~sqtpp1_2_REG.py~ ' + sqtpp_registry_err){self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_key(self):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rIntA = 0{self._rg_rStrA}        self._lll_sSpdrRtrn = 1{self._rg_rStrA}        self._lll_rBoolA = False{self._rg_rStrA}        self._lll_sHarpErr = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rIntB = len(self._lll_sTharpe){self._rg_rStrA}        self._lll_rStrA = ':008S9:' + self._lll_sKyHdr[7] + '='{self._rg_rStrA}        while self._lll_rIntA < self._lll_rIntB:{self._rg_rStrA}")
        self._rg_rLstA.append(f"            if self._lll_sTharpe[self._lll_rIntA].find(self._lll_rStrA) > -1:{self._rg_rStrA}                self._lll_rBoolA = True{self._rg_rStrA}                break{self._rg_rStrA}")
        self._rg_rLstA.append(f"            self._lll_rIntA+=1{self._rg_rStrA}        if self._lll_rBoolA:{self._rg_rStrA}            self._lll_rLstA = re.findall(r'SQTPP_REG_HARP_SCHEMA\:.*?\:008S9\:' + re.escape(self._lll_sKyHdr[7]) + '.*?=', self._lll_sTharpe[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"            if len(self._lll_rLstA) > 0:{self._rg_rStrA}                self._lll_rLstA[0] = self._lll_rLstA[0].replace('=', ''){self._rg_rStrA}                self._lll_rLstA = self._lll_rLstA[0].split(':'){self._rg_rStrA}")
        self._rg_rLstA.append(f"                self._lll_rLstA.pop(0){self._rg_rStrA}                self._lll_rLstB = re.findall(r'=.*?:\|\.\|\|\.\|:', self._lll_sTharpe[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                if len(self._lll_rLstB) > 0:{self._rg_rStrA}                    self._lll_rLstB = self._lll_rLstB[0].replace(':|.||.|:', ''){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    self._lll_rLstB = self._lll_rLstB[1:len(self._lll_rLstB)]{self._rg_rStrA}                    self._lll_sSpdrRtrn = self.sqtpp_reg_harp_pre_prc(){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    if not self._lll_sPrsErr:{self._rg_rStrA}                        return self._lll_sSpdrRtrn{self._rg_rStrA}                    else:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        if self._lll_sSpdrRtrn == -1:{self._rg_rStrA}                            self._lll_sHarpErr = True{self._rg_rStrA}                            self._lll_sSpdrRtrn = -4{self._rg_rStrA}")
        self._rg_rLstA.append(f"                else:{self._rg_rStrA}                    self._lll_sHarpErr = True{self._rg_rStrA}                    self._lll_sSpdrRtrn = -3{self._rg_rStrA}")
        self._rg_rLstA.append(f"            else:{self._rg_rStrA}                self._lll_sHarpErr = True{self._rg_rStrA}                self._lll_sSpdrRtrn = -2{self._rg_rStrA}        else:{self._rg_rStrA}")
        self._rg_rLstA.append(f"            self._lll_sHarpErr = True{self._rg_rStrA}            self._lll_sSpdrRtrn = -1{self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}")
        self._rg_rLstA.append(f"    def sqtpp_reg_harp_pre_prc(self):{self._rg_rStrA}        self._lll_sPrsErr = False{self._rg_rStrA}        self._lll_sKyDat = self._lll_sKyDat.replace('~||/', '\u0027'){self._rg_rStrA}")
        self._rg_rLstA.append(f"        if not self._lll_sKyCmx and not self._lll_sKySet:{self._rg_rStrA}            try:{self._rg_rStrA}                self._lll_sKyDat = ast.literal_eval(self._lll_sKyDat)   {self._rg_rStrA}")
        self._rg_rLstA.append(f"            except Exception as err_key_data_ast:{self._rg_rStrA}                self._lll_sPrsErr = True{self._rg_rStrA}                return -1{self._rg_rStrA}")
        self._rg_rLstA.append(f"        else:{self._rg_rStrA}            if self._lll_sKyCmx:{self._rg_rStrA}                self._lll_rLstA = self._lll_sKyDat.split('('){self._rg_rStrA}")
        self._rg_rLstA.append(f"                self._lll_rLstA[1] = self._lll_rLstA[1].replace(' ', '').replace(')', ''){self._rg_rStrA}                self._lll_rLstA = self._lll_rLstA[1].split(','){self._rg_rStrA}")
        self._rg_rLstA.append(f"                if self._lll_rLstA[0].find('.') > -1: self._lll_rIntA = float(self._lll_rLstA[0]){self._rg_rStrA}                else: self._lll_rIntA = int(self._lll_rLstA[0]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                if self._lll_rLstA[1].find('.') > -1: self._lll_rIntB = float(self._lll_rLstA[1]){self._rg_rStrA}                else: self._lll_rIntB = int(self._lll_rLstA[1]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                self._lll_sKyDat = complex(self._lll_rIntA, self._lll_rIntB){self._rg_rStrA}            else:{self._rg_rStrA}                self._lll_rLstA = self._lll_sKyDat.split('('){self._rg_rStrA}")
        self._rg_rLstA.append(f"                self._lll_rLstA[1] = self._lll_rLstA[1].replace(' ', '').replace(')', ''){self._rg_rStrA}                if self._lll_rLstA[1].find(',') > -1: self._lll_rLstA = self._lll_rLstA[1].split(','){self._rg_rStrA}")
        self._rg_rLstA.append(f"                else: self._lll_rLstA = [self._lll_rLstA[1]]{self._rg_rStrA}                self._lll_rLstD = []{self._rg_rStrA}                self._lll_sNmId = set('.1234567890'){self._rg_rStrA}")
        self._rg_rLstA.append(f"                self._lll_rIntB = len(self._lll_rLstA){self._rg_rStrA}                for self._lll_rIntA in range(self._lll_rIntB):{self._rg_rStrA}                    if set(self._lll_rLstA[self._lll_rIntA]).issubset(self._lll_sNmId) > 1:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        if self._lll_rLstA[self._lll_rIntA].find('.') > -1: self._lll_rLstD.append(float(self._lll_rLstA[self._lll_rIntA])){self._rg_rStrA}")
        self._rg_rLstA.append(f"                        else: self._lll_rLstD.append(int(self._lll_rLstA[self._lll_rIntA])){self._rg_rStrA}                    elif self._lll_rLstA[self._lll_rIntA].lower() == 'true': self._lll_rLstD.append(bool(1)){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    elif self._lll_rLstA[self._lll_rIntA].lower() == 'false': self._lll_rLstD.append(bool(0)){self._rg_rStrA}                    else: self._lll_rLstD.append(self._lll_rLstA[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    self._lll_sKyDat = set(self._lll_rLstD){self._rg_rStrA}        if any(isinstance(_, list) for _ in self._lll_sKyDat):{self._rg_rStrA}")
        self._rg_rLstA.append(f"            raise Exception('[sqtpp-reg >> registry] - registry key cannot be evaluated, has nested list from non-supported edit of module sqtpp1_2_REG.py'){self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rLstB = self._lll_rLstB.split('|./^.'){self._rg_rStrA}        self._lll_sLstA = [')']{self._rg_rStrA}        self._lll_rLstB = [_ for _ in self._lll_rLstB if _ not in self._lll_sLstA]{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rLstD = []{self._rg_rStrA}        self._lll_rLstE = []{self._rg_rStrA}        self._lll_rLstF = []{self._rg_rStrA}        self._lll_rIntB = len(self._lll_rLstB){self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rBoolA = True{self._rg_rStrA}        self._lll_rBoolB = False{self._rg_rStrA}        self._lll_rBoolC = False{self._rg_rStrA}        self._lll_rBoolD = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"        for self._lll_rIntA in range(1, self._lll_rIntB):{self._rg_rStrA}            self._lll_rStrA = self._lll_rLstB[self._lll_rIntA]{self._rg_rStrA}")
        self._rg_rLstA.append(f"            if self._lll_rBoolA:{self._rg_rStrA}                self._lll_rBoolA = False{self._rg_rStrA}                self._lll_rLstC = [self._lll_rStrA.replace(':(', '')]{self._rg_rStrA}")
        self._rg_rLstA.append(f"            else:{self._rg_rStrA}                if self._lll_rBoolB or self._lll_rStrA == '.|.//^.':{self._rg_rStrA}                    if not self._lll_rBoolB: self._lll_rBoolB = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else:{self._rg_rStrA}                        self._lll_rBoolB = False{self._rg_rStrA}                        self._lll_rLstC.append(self._lll_rStrA.replace(':(', '')){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif not self._lll_rBoolC and self._lll_rStrA.find('type:(') > -1: self._lll_rLstD.append(self._lll_rStrA.replace('type:(', '')){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif self._lll_rBoolC or self._lll_rStrA == 'item:(':{self._rg_rStrA}                    if not self._lll_rBoolC: self._lll_rBoolC = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else:{self._rg_rStrA}                        if self._lll_rStrA.find('%inherit=') > -1:{self._rg_rStrA}                            self._lll_sLstA = self._lll_rStrA.split('='){self._rg_rStrA}")
        self._rg_rLstA.append(f"                            self._lll_rLstE.append('>>' + self._lll_rLstC[len(self._lll_rLstC)-1] + ':' + self._lll_sLstA[1]){self._rg_rStrA}                        if self._lll_rStrA.find('%type:(') > -1:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            self._lll_rStrA = self._lll_rStrA.replace('%type:(', ''){self._rg_rStrA}                            self._lll_rLstE[len(self._lll_rLstE)-1] = self._lll_rLstE[len(self._lll_rLstE)-1] + ':' + self._lll_rStrA{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        if self._lll_rLstB[self._lll_rIntA+1][0] != '%': self._lll_rBoolC = False{self._rg_rStrA}                elif self._lll_rBoolD or self._lll_rStrA.find('validator[') > -1:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    if not self._lll_rBoolD: self._lll_rBoolD = True{self._rg_rStrA}                    else:{self._rg_rStrA}                        if self._lll_rStrA == ']': self._lll_rBoolD = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        else:{self._rg_rStrA}                            self._lll_rStrA = self._lll_rStrA.replace('~||/', '\u0027'){self._rg_rStrA}                            self._lll_rLstF.append(self._lll_rLstC[len(self._lll_rLstC)-1] + ':' + self._lll_rLstD[len(self._lll_rLstD)-1] + '<' + self._lll_rStrA + ':|/>'){self._rg_rStrA}")
        self._rg_rLstA.append(f"        return 1{self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc(self):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        try:{self._rg_rStrA}            self._lll_rBoolA = True{self._rg_rStrA}            self._lll_sBlnSw = False{self._rg_rStrA}            self._lll_rIntB = len(self._lll_rLstF){self._rg_rStrA}")
        self._rg_rLstA.append(f"            for self._lll_rIntA in range(self._lll_rIntB):{self._rg_rStrA}                self._lll_rBoolB = False{self._rg_rStrA}                self._lll_rLstA = re.findall(r'.*?<', self._lll_rLstF[self._lll_rIntA]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                if not self._lll_rBoolA:{self._rg_rStrA}                    if self._lll_rStrA == self._lll_rLstA[0]: self.sqtpp_reg_harp_prc_profile(True){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else: self.sqtpp_reg_harp_prc_profile(self._lll_rBoolA)     {self._rg_rStrA}                else:{self._rg_rStrA}                    self._lll_rBoolA = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    self.sqtpp_reg_harp_prc_profile(self._lll_rBoolA){self._rg_rStrA}        except Exception as sqtpp_registry_key_validator_prc_err:{self._rg_rStrA}")
        self._rg_rLstA.append(f"            raise Exception('[sqtpp-reg >> registry] direct registry module key validator process exception ~sqtpp1_2_REG.py~ ' + sqtpp_registry_key_validator_prc_err){self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc_profile(self, bypAsgn: bool):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        if not bypAsgn:{self._rg_rStrA}            self._lll_rBoolB = True{self._rg_rStrA}            self._lll_rStrA = self._lll_rLstA[0]{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rStrB = self._lll_rLstF[self._lll_rIntA].split('<'){self._rg_rStrA}        self._lll_rStrC = self._lll_rStrB[0].replace('<', ''){self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rStrC = self._lll_rStrC.split(':'){self._rg_rStrA}        self._lll_rStrB = self._lll_rStrB[1].replace(':|/>', ''){self._rg_rStrA}        self._lll_rLstB = re.findall(r'lambda.*?\:', self._lll_rStrB){self._rg_rStrA}")
        self._rg_rLstA.append(f"        if self._lll_rLstB[0].find(',') < 0:{self._rg_rStrA}            if not self._lll_sBlnSw and self._lll_sKyBln:{self._rg_rStrA}                self._lll_sBlnSw = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                self.sqtpp_reg_harp_prc_core('b'){self._rg_rStrA}            elif isinstance(self._lll_sKyDat, bool): self.sqtpp_reg_harp_prc_core('b'){self._rg_rStrA}")
        self._rg_rLstA.append(f"            elif isinstance(self._lll_sKyDat, list): self.sqtpp_reg_harp_prc_core('l'){self._rg_rStrA}            elif isinstance(self._lll_sKyDat, str): self.sqtpp_reg_harp_prc_core('sr'){self._rg_rStrA}")
        self._rg_rLstA.append(f"            elif isinstance(self._lll_sKyDat, int): self.sqtpp_reg_harp_prc_core('i'){self._rg_rStrA}            elif isinstance(self._lll_sKyDat, float): self.sqtpp_reg_harp_prc_core('f'){self._rg_rStrA}")
        self._rg_rLstA.append(f"            elif isinstance(self._lll_sKyDat, complex): self.sqtpp_reg_harp_prc_core('c'){self._rg_rStrA}            elif isinstance(self._lll_sKyDat, set): self.sqtpp_reg_harp_prc_core('st'){self._rg_rStrA}")
        self._rg_rLstA.append(f"            else:{self._rg_rStrA}                raise Exception('[sqtpp-reg >> registry] - registry key (' + self._lll_sKyHdr[6] + ') is a unknown/non-supported type for a registry key value, see REGISTRY_CALLS.TXT'){self._rg_rStrA}")
        self._rg_rLstA.append(f"        else:{self._rg_rStrA}            raise Exception('[sqtpp-reg >> registry] - registry schema (' + self._lll_sKyHdr[7] + ') has lambda function(s) with more than one parameter, see REGISTRY_CALLS.TXT'){self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc_core(self, typDsg: str):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        crProcTyp = None{self._rg_rStrA}        crProcTypLst = False{self._rg_rStrA}        crProcTypSet = False{self._rg_rStrA}        crProcTypStr = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"        try:{self._rg_rStrA}            self._lll_rBoolC = True{self._rg_rStrA}            if not isinstance(self._lll_sKyDat, self.sqtpp_reg_harp_prc_core_cnvrt_styp_to_ctyp()):{self._rg_rStrA}")
        self._rg_rLstA.append(f"                if typDsg == 'l': crProcTypLst = True{self._rg_rStrA}                if not crProcTypLst and typDsg == 'st': crProcTypSet = True{self._rg_rStrA}")
        self._rg_rLstA.append(f"                if not crProcTypLst and not crProcTypSet and typDsg == 'sr': crProcTypStr = True{self._rg_rStrA}                if self._lll_sTyp1 == 'list':{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    if not crProcTypSet:{self._rg_rStrA}                        if not crProcTypStr: self._lll_sKyDat = [self._lll_sKyDat]{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        else: self.sqtpp_reg_harp_prc_core_cnvrt_str_to_lst(){self._rg_rStrA}                    else: self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif self._lll_sTyp1 == 'string':{self._rg_rStrA}                    if not crProcTypSet:{self._rg_rStrA}                        if not crProcTypLst:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            if typDsg == 'f': self._lll_sKyDat = str(self._lll_sKyDat){self._rg_rStrA}                            elif typDsg == 'c': self._lll_sKyDat = str(self._lll_sKyDat.real){self._rg_rStrA}")
        self._rg_rLstA.append(f"                            else: self._lll_sKyDat = str(self._lll_sKyDat){self._rg_rStrA}                        else: self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_str(){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else:{self._rg_rStrA}                        self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}                        self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_str(){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif self._lll_sTyp1 == 'integer': self. sqtpp_reg_harp_prc_core_int_flt_map(typDsg, True, crProcTypSet, crProcTypLst, crProcTypStr){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif self._lll_sTyp1 == 'float': self.sqtpp_reg_harp_prc_core_int_flt_map(typDsg, False, crProcTypSet, crProcTypLst, crProcTypStr){self._rg_rStrA}")
        self._rg_rLstA.append(f"                elif self._lll_sTyp1 == 'complex':{self._rg_rStrA}                    if not crProcTypSet:{self._rg_rStrA}                        if not crProcTypLst:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            if not crProcTypStr:{self._rg_rStrA}                                if typDsg == 'f' or typDsg == 'i': self._lll_sKyDat = complex(self._lll_sKyDat, 0){self._rg_rStrA}")
        self._rg_rLstA.append(f"                                elif typDsg == 'b':{self._rg_rStrA}                                    if self._lll_sKyDat: self._lll_sKyDat = complex(1, 0){self._rg_rStrA}")
        self._rg_rLstA.append(f"                                    else: self._lll_sKyDat = complex(0, 0){self._rg_rStrA}                            else:{self._rg_rStrA}                                self.sqtpp_reg_harp_prc_core_cnvrt_str_to_lst(){self._rg_rStrA}")
        self._rg_rLstA.append(f"                                self.sqtpp_reg_harp_prc_core_cnvrt_lst_set_to_cmx(False){self._rg_rStrA}                        else: self.sqtpp_reg_harp_prc_core_cnvrt_lst_set_to_cmx(False){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else: self.sqtpp_reg_harp_prc_core_cnvrt_lst_set_to_cmx(True){self._rg_rStrA}                elif self._lll_sTyp1 == 'boolean':{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    if not crProcTypSet:{self._rg_rStrA}                        if not crProcTypLst:{self._rg_rStrA}                            if not crProcTypStr:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                                if typDsg == 'f': self._lll_sKyDat = bool(int(self._lll_sKyDat)){self._rg_rStrA}                                elif typDsg == 'i': self._lll_sKyDat = bool(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"                                elif typDsg == 'c': self._lll_sKyDat = bool(int(self._lll_sKyDat.real)){self._rg_rStrA}                            else:{self._rg_rStrA}")
        self._rg_rLstA.append(f"                                self._lll_sKyDat = self._lll_sKyDat.lower(){self._rg_rStrA}                                if self._lll_sKyDat == 'true': self._lll_sKyDat = bool(1){self._rg_rStrA}")
        self._rg_rLstA.append(f"                                else: self._lll_sKyDat = bool(0){self._rg_rStrA}                        else:{self._rg_rStrA}                            self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(True){self._rg_rStrA}")
        self._rg_rLstA.append("                            self._lll_sKyDat = {bool(self._lll_sKyDat)}\n                    else:\n                        self._lll_sKyDat = list(self._lll_sKyDat)\n")
        self._rg_rLstA.append("                        self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(True)\n                        self._lll_sKyDat = {bool(self._lll_sKyDat)}\n")
        self._rg_rLstA.append("                elif self._lll_sTyp1 == 'set':\n                    if not crProcTypLst:\n                        if not crProcTypStr: self._lll_sKyDat = {self._lll_sKyDat}\n")
        self._rg_rLstA.append(f"                        else:{self._rg_rStrA}                            self.sqtpp_reg_harp_prc_core_cnvrt_str_to_lst(){self._rg_rStrA}                            self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    else: self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}        except Exception as converter_prc_core_err:{self._rg_rStrA}            self._lll_rBoolC = False{self._rg_rStrA}")
        self._rg_rLstA.append(f"        if self._lll_rBoolC:{self._rg_rStrA}            try:{self._rg_rStrA}                self._lll_rStrD = eval(self._lll_rStrB){self._rg_rStrA}                self._lll_sLmb = self._lll_rStrD(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"            except Exception as validator_prc_core_err:{self._rg_rStrA}                self._lll_rBoolC = False{self._rg_rStrA}            if self._lll_rBoolC: self._lll_sKyDat = self._lll_sLmb{self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc_core_int_flt_map(self, typDsg: str, isInt: bool, pSet: bool, pLst: bool, pStr: bool):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        if not pSet:{self._rg_rStrA}            if not pLst:{self._rg_rStrA}                if not pStr:{self._rg_rStrA}                    if isInt and typDsg == 'f': self._lll_sKyDat = math.floor(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    elif not isInt and typDsg == 'i': self._lll_sKyDat = float(self._lll_sKyDat){self._rg_rStrA}                    elif typDsg == 'c':{self._rg_rStrA}")
        self._rg_rLstA.append(f"                        if isInt: self._lll_sKyDat = math.floor(self._lll_sKyDat.real){self._rg_rStrA}                        else: self._lll_sKyDat = self._lll_sKyDat.real{self._rg_rStrA}")
        self._rg_rLstA.append(f"                    elif typDsg == 'b':{self._rg_rStrA}                        if isInt:{self._rg_rStrA}                            if self._lll_sKyDat: self._lll_sKyDat = 1{self._rg_rStrA}")
        self._rg_rLstA.append(f"                            else: self._lll_sKyDat = 0{self._rg_rStrA}                        else:{self._rg_rStrA}                            if self._lll_sKyDat: self._lll_sKyDat = float(1){self._rg_rStrA}")
        self._rg_rLstA.append(f"                            else: self._lll_sKyDat = float(0){self._rg_rStrA}                else:{self._rg_rStrA}                    self.sqtpp_reg_harp_prc_core_cnvrt_str_to_lst(){self._rg_rStrA}")
        self._rg_rLstA.append(f"                    self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(isInt){self._rg_rStrA}            else: self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(isInt){self._rg_rStrA}")
        self._rg_rLstA.append(f"        else:{self._rg_rStrA}            self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}            self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(isInt){self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc_core_cnvrt_lst_elm(self):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self._lll_rIntD = len(self._lll_sKyDat){self._rg_rStrA}        for self._lll_rIntC in range(self._lll_rIntD):{self._rg_rStrA}            if set(self._lll_sKyDat[self._lll_rIntC]).issubset(self._lll_sNmId):{self._rg_rStrA}")
        self._rg_rLstA.append(f"                if self._lll_sKyDat[self._lll_rIntC].find('.') > -1: self._lll_sKyDat[self._lll_rIntC] = float(self._lll_sKyDat[self._lll_rIntC]){self._rg_rStrA}")
        self._rg_rLstA.append(f"                else: self._lll_sKyDat[self._lll_rIntC] = int(self._lll_sKyDat[self._lll_rIntC]){self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}")
        self._rg_rLstA.append(f"    def sqtpp_reg_harp_prc_core_cnvrt_lst_to_str(self):{self._rg_rStrA}        self._lll_rIntD = len(self._lll_sKyDat){self._rg_rStrA}        for self._lll_rIntC in range(self._lll_rIntD):{self._rg_rStrA}")
        self._rg_rLstA.append(f"            if not isinstance(self._lll_sKyDat[self._lll_rIntC], str): self._lll_sKyDat[self._lll_rIntC] = str(self._lll_sKyDat[self._lll_rIntC]){self._rg_rStrA}")
        self._rg_rLstA.append(f"        if len(self._lll_sKyDat) > 1: self._lll_sKyDat = ','.join(self._lll_sKyDat){self._rg_rStrA}        else: self._lll_sKyDat = self._lll_sKyDat[0]{self._rg_rStrA}")
        self._rg_rLstA.append(f"#|______________________________________________________________________________________{self._rg_rStrA}    def sqtpp_reg_harp_prc_core_cnvrt_str_to_lst(self):{self._rg_rStrA}")
        self._rg_rLstA.append(f"        if self._lll_sKyDat.find(',') > -1: self._lll_sKyDat = self._lll_sKyDat.split(','){self._rg_rStrA}        else: self._lll_sKyDat = [self._lll_sKyDat]{self._rg_rStrA}")
        self._rg_rLstA.append(f"        self.sqtpp_reg_harp_prc_core_cnvrt_lst_elm(){self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}")
        self._rg_rLstA.append(f"    def sqtpp_reg_harp_prc_core_cnvrt_lst_set_to_cmx(self, isLstCnvr: bool):{self._rg_rStrA}        if isLstCnvr: self._lll_sKyDat = list(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"        self.sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(False){self._rg_rStrA}        self._lll_sKyDat = complex(self._lll_sKyDat, 0){self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}")
        self._rg_rLstA.append(f"    def sqtpp_reg_harp_prc_core_cnvrt_lst_to_num(self, isInt: bool):{self._rg_rStrA}        self._lll_rIntE = 0{self._rg_rStrA}        self._lll_rIntD = len(self._lll_sKyDat){self._rg_rStrA}")
        self._rg_rLstA.append(f"        for self._lll_rIntC in range(self._lll_rIntD):{self._rg_rStrA}            if isinstance(self._lll_sKyDat[self._lll_rIntC], int) or isinstance(self._lll_sKyDat[self._lll_rIntC], float): self._lll_rIntE = self._lll_rIntE + self._lll_sKyDat[self._lll_rIntC]{self._rg_rStrA}")
        self._rg_rLstA.append(f"            elif isinstance(self._lll_sKyDat[self._lll_rIntC], complex): self._lll_rIntE = self._lll_rIntE + self._lll_sKyDat[self._lll_rIntC].real{self._rg_rStrA}")
        self._rg_rLstA.append(f"            elif isinstance(self._lll_sKyDat[self._lll_rIntC], bool):{self._rg_rStrA}                if self._lll_sKyDat[self._lll_rIntC]: self._lll_rIntE+=1{self._rg_rStrA}")
        self._rg_rLstA.append(f"        if isInt: self._lll_sKyDat = math.floor(self._lll_rIntE){self._rg_rStrA}        else: self._lll_sKyDat = self._lll_rIntE{self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}")
        self._rg_rLstA.append(f"    def sqtpp_reg_harp_prc_core_cnvrt_styp_to_ctyp(self):{self._rg_rStrA}        if self._lll_sTyp1 == 'string':{self._rg_rStrA}            return str{self._rg_rStrA}")
        self._rg_rLstA.append(f"        elif self._lll_sTyp1 == 'integer':{self._rg_rStrA}            return int{self._rg_rStrA}        elif self._lll_sTyp1 == 'boolean':{self._rg_rStrA}")
        self._rg_rLstA.append(f"            return bool{self._rg_rStrA}        elif self._lll_sTyp1 == 'complex':{self._rg_rStrA}            return complex{self._rg_rStrA}        elif self._lll_sTyp1 == 'set':{self._rg_rStrA}")
        self._rg_rLstA.append(f"            return set{self._rg_rStrA}        elif self._lll_sTyp1 == 'float':{self._rg_rStrA}            return float{self._rg_rStrA}        elif self._lll_sTyp1 == 'list':{self._rg_rStrA}")
        self._rg_rLstA.append(f"            return list{self._rg_rStrA}#|______________________________________________________________________________________{self._rg_rStrA}#| 'WAR!!! WHAT IS IT GOOD FOR? ABSOLUTELY ----> NOTHING!' - EDWIN STARR{self._rg_rStrA}")
        self._rg_rLstA.append(f"{self._rg_rStrA}def sqtpp_reg_lll_run(lName: str, lData):{self._rg_rStrA}    lllCls = SqtppRegLLL_Fncs(){self._rg_rStrA}    return lllCls.sqtpp_reg_key_rdr(lName, lData)")
        self._rg_rLstA = ''.join(self._rg_rLstA)
        self._rg_rLstA = self._rg_rLstA.replace(".replace('~||/', '\u0027')", ".replace('~||/', '\\u0027')")
        with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'w') as flObjRegWrt: flObjRegWrt.write(self._rg_rLstA)
        self._rg_rStrA = None
        self._rg_rLstA = None
        if os.path.isfile(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py'):
            with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'r') as flObjReg: self._rg_rStrA = flObjReg.read()
        else:
            raise Exception(f"[sqtpp-reg >> registry] - could not write the registry module sqtpp1_2_REG.py to Staqtapp's current working directory '{SQTPP_MDL_DIR}'")
        if addRegKy:
            return self.sqtpp_registry_homer_add_key(regKyNm, regKyDt, schm)
        else:
            return self.sqtpp_registry_homer_add_schema(schm)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_add_key(self, regKyNm: str, regKyDt, schNm: str):
        # FNC_ID=ST12-51515326608349
        # SqtppFncs slots in use: (hidden)
        # returns: (all added registry keys must have an assigned harp-schema name)
        # -1=invalid chars @ key name or/and schema name
        # -2=unsupported nested list registry key value
        # -3=unsupported bytes or bytearray type...
        # -4=unsupported registry value type, unknown
        # -5=unsupported " char(s) to a string value
        # -6=schema not found
        try:
            if self._rg_rStrA.find(f':008S9:{schNm}={schNm}=(') > -1:
                rtrn = 1
                lstL = None
                self._rg_rBoolA = False
                if set(regKyNm).issubset(SQTPP_SET_VARS) and set(schNm).issubset(SQTPP_SET_VARS):
                    if isinstance(regKyDt, list):
                        self._rg_rLstA = []
                        self._rg_rBoolA = True
                        self._rg_rIntB = len(regKyDt)
                        for self._rg_rIntA in range(self._rg_rIntB):
                            if isinstance(regKyDt[self._rg_rIntA], str):
                                if regKyDt[self._rg_rIntA].find('"') > -1:
                                    return -5
                                else:
                                    regKyDt[self._rg_rIntA] = regKyDt[self._rg_rIntA].replace('\n','|./^.')
                                    self._rg_rLstA.append(f'~||/{regKyDt[self._rg_rIntA]}~||/')
                            elif isinstance(regKyDt[self._rg_rIntA], (int,float,complex)): self._rg_rLstA.append(str(regKyDt[self._rg_rIntA]))
                            elif isinstance(regKyDt[self._rg_rIntA], bool): 
                                if not regKyDt[self._rg_rIntA]: self._rg_rLstA.append('False')
                                else: self._rg_rLstA.append('True')
                            elif isinstance(regKyDt[self._rg_rIntA], list):
                                return -2
                            elif isinstance(regKyDt[self._rg_rIntA], (bytes,bytearray)):
                                return -3
                            else:
                                return -4
                        lstL = f'__LTLKV{len(self._rg_rLstA)}'
                        self._rg_rLstA = f'=[{",".join(self._rg_rLstA)}]:|.||.|:'
                    elif isinstance(regKyDt, str):
                        if regKyDt.find('"') > -1:
                            return -5
                        else:
                            regKyDt = regKyDt.replace('\n', '|./^.')
                            self._rg_rLstA = f'=~||/{regKyDt}~||/:|.||.|:'
                    elif isinstance(regKyDt, bool):
                        if not regKyDt: self._rg_rLstA = '=False:|.||.|:'
                        else: self._rg_rLstA = '=True:|.||.|:'
                    elif isinstance(regKyDt, (int,float,complex)): self._rg_rLstA = f'={regKyDt}:|.||.|:'
                else:
                    return -1
                dttm = datetime.now()
                if not self._rg_rBoolA: lstL = "__LTLKVNAL"
                if self._rg_rStrA.find(f':9S8:{regKyNm}') > -1:
                    self._rg_rLstB = re.findall(r'SQTPP_REG_KEY\:.*?\:9\S8\:' + re.escape(regKyNm) + r'\:.*?\:\|\.\|\|\.\|\:', self._rg_rStrA)
                    self._rg_rLstC = self._rg_rLstB[0].split(':')
                    self._rg_rStrC = f'SQTPP_REG_KEY:{self._rg_rLstC[1]}:{lstL}:{dttm.strftime("%m||%d||%Y||%I||%M||%S||%p")}:{self._rg_rLstC[4]}:{self._rg_rLstC[5]}:9S8:{self._rg_rLstC[7]}:{schNm}{self._rg_rLstA}'
                    self._rg_rStrA = self._rg_rStrA.replace(self._rg_rLstB[0], self._rg_rStrC)
                else: self.sqtpp_registry_homer_apnd_deq_ext('self._lll_sThemas = deque([', '#|:>|<:|', f'SQTPP_REG_KEY:{random.randint(1000000000,9999999999)}:{lstL}:{dttm.strftime("%m||%d||%Y||%I||%M||%S||%p")}:{random.randint(1000,9999)}:{random.randint(1000,9999)}:9S8:{regKyNm}:{schNm}{self._rg_rLstA}')
                self._rg_rStrB = None
                self._rg_rStrC = None
                with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'w') as flObjRegWrt: flObjRegWrt.write(self._rg_rStrA)
                self._rg_sMdlEdt = True
                self._rg_rStrA = None
                return 1
            else:
                return -6
        except Exception as sqtpp_registry_homer_add_key_err:
            raise Exception(f'[sqtpp-reg >> registry] - (sqtpp_registry_homer_add_key) direct exception: {sqtpp_registry_homer_add_key_err}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_add_schema(self, schmPth: str):
        # FNC_ID=ST12-59061838804103
        # SqtppFncs slots in use: (hidden)
        # returns: (all added registry keys must have an assigned harp-schema name)
        try:
            if os.path.isfile(schmPth):
                with open(schmPth, 'r') as flObjRegSchm: self._rg_rStrB = flObjRegSchm.read()
                rtrnDcs = None
                schmNm = schmPth.split('/')
                schmNm = schmNm[len(schmNm)-1]
                schmNm = schmNm.split('.')
                schmNm = schmNm[0]
                rtrn = self.sqtpp_registry_homer_schema_spdr(schmNm)
                if rtrn[0] == '!':
                    rtrn = rtrn.split('÷')
                    if rtrn[2].find(':') > -1:
                        rtrnDcs = rtrn[2].split(':')
                        if rtrnDcs[0] == '3':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - invalid type declaration "{rtrnDcs[1]}", schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrnDcs[0] == '4':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - registry schema name "{rtrnDcs[1]}" does not match filename "{schmNm}", schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrnDcs[0] == '5':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - registry schema name "{rtrnDcs[1]}" has invalid chars; valid chars _ a-z A-Z 0-9, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrnDcs[0] == '7':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - category type name "{rtrnDcs[1]}" has invalid chars; valid chars _ a-z A-Z 0-9, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrnDcs[0] == '14':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - category type "{rtrnDcs[1]}" not present in registry schema or is not already visible for an inherit assignment, schema code line ({rtrn[1]}) in "{schmPth}"')
                    else:
                        if rtrn[2] == '1':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - missing type declaration, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '2':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - missing EOL comma for type declaration(s), schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '6':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - expected a category type naming declaration, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '8':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - no category type naming set for any type(s) validation, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '9':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - lambda function for validator sequence is not well defined, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '10':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - unexpected "]" end of a lambda validator sequence before any lambda function(s) added, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '11':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - dual use of single & double quotes found in a lambda function, not supported, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '12':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - no found inherit assignment after a item declaration or not a proper item declaration, schema code line ({rtrn[1]}) in "{schmPth}"')
                        elif rtrn[2] == '13':
                            raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - no found category type for assignment with a inherit category type, schema code line ({rtrn[1]}) in "{schmPth}"')
                elif rtrn == '@1':
                    dttm = datetime.now()
                    if self._rg_rStrA.find(f':008S9:{schmNm}') > -1:
                        self._rg_rLstB = re.findall(r'SQTPP_REG_HARP_SCHEMA\:.*?\:008S9\:' + re.escape(schmNm) + r'=.*?\:\|\.\|\|\.\|\:', self._rg_rStrA)
                        self._rg_rLstC = self._rg_rLstB[0].split(':')
                        self._rg_rStrB = f'SQTPP_REG_HARP_SCHEMA:{dttm.strftime("%m||%d||%Y||%I||%M||%S||%p")}:{self._rg_rLstC[2]}:008S9:{schmNm}={"|./^.".join(self._rg_sSchm)}:|.||.|:'
                        self._rg_rStrA = self._rg_rStrA.replace(self._rg_rLstB[0], self._rg_rStrB)
                    else:
                        self._rg_sSchm = "|./^.".join(self._rg_sSchm)
                        self.sqtpp_registry_homer_apnd_deq_ext('self._lll_sTharpe = deque([', '#|.<:>.|', f'SQTPP_REG_HARP_SCHEMA:{dttm.strftime("%m||%d||%Y||%I||%M||%S||%p")}:{random.randint(1000000000,9999999999)}:008S9:{schmNm}={self._rg_sSchm}:|.||.|:')
                    self._rg_sSchm = None
                    self._rg_rStrB = None
                    self._rg_rStrC = None
                    with open(f'{SQTPP_MDL_DIR}/sqtpp1_2_REG.py', 'w') as flObjRegWrt: flObjRegWrt.write(self._rg_rStrA)
                    self._rg_sMdlEdt = True
                    self._rg_rStrA = None
                    return 1
            else:
                raise Exception(f'[sqtpp-reg >> registry] (add registry schema) - directory path "{schmPth}" is not a valid file path, registry harp-schema code file not found')
        except Exception as sqtpp_registry_homer_add_schema_err:
            raise Exception(f'[sqtpp-reg >> registry] - (sqtpp_registry_homer_add_schema) direct exception: {sqtpp_registry_homer_add_schema_err}')
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_apnd_deq_ext(self, sFnd: str, eFnd: str, apnd: str):
        # FNC_ID=ST12-74601895900751
        # SqtppFncs slots in use: (hidden)
        # returns: (none)
        self._rg_rIntA = self._rg_rStrA.find(sFnd)
        self._rg_rIntB = self._rg_rStrA.find(eFnd)
        self._rg_rStrB = self._rg_rStrA[self._rg_rIntA:self._rg_rIntB-12]
        self._rg_rStrC = self._rg_rStrB
        self._rg_rStrD = '\n'
        self._rg_rStrB = f"{self._rg_rStrB},{self._rg_rStrD}            '{apnd}'"
        self._rg_rStrA = self._rg_rStrA.replace(self._rg_rStrC, self._rg_rStrB)
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~
    def sqtpp_registry_homer_schema_spdr(self, schmNm: str):
        # FNC_ID=ST12-43731682241907
        # SqtppFncs slots in use: (hidden)
        # returns:
        # !÷line#÷1=type declaration(s), missing any type declaration
        # !÷line#÷2=type declaration(s), missing proper comma for EOL
        # !÷line#÷3:wrong type=type declaration not a valid one
        # !÷line#÷4:wrong schema name=schema name does not match the filename
        # !÷line#÷5:invalid chars schema name=schema name has invalid chars
        # !÷line#÷6=expected a type category name declaration...
        # !÷line#÷7:invalid chars category name type=category name type has invalid chars
        # !÷line#÷8=no category type name assigned for any type validations
        # !÷line#÷9=lambda function is not well defined
        # !÷line#÷10=unexpected end of a lambda validator seq before any lambda added...
        # !÷line#÷11=lambda function has dual use of string declarations ' & "
        # !÷line#÷12=no found inherit assignment after an item declaration
        # !÷line#÷13=no found category type for assignment with a inherit category type
        # !÷line#÷14:invalid category type=category type for inherit assignment not found
        lstA = ['bool','complex','float','integer','set','list','string','*']
        self._rg_rLstA = self._rg_rStrB.split('\n')
        self._rg_rLstA[:] = [l for l in self._rg_rLstA if '#' not in l and not l.isspace()]
        self._rg_rLstA = list(filter(None, self._rg_rLstA))
        self._rg_rIntB = len(self._rg_rLstA)
        self._rg_rBoolA = True
        vldLm = False
        typSw = False
        typAg = False
        typAd = False
        typEt = False
        typIn = 0
        typTrk = []
        self._rg_sSchm = []
        rtrn = '@1'
        for self._rg_rIntA in range(self._rg_rIntB):
            self._rg_rBoolB = False
            if self._rg_rLstA[self._rg_rIntA].find(']') > -1:
                if vldLm:
                    vldLm = False
                    self._rg_sSchm.append(']')
                else:
                    return f'!÷{self._rg_rIntA+1}÷10'
            self._rg_rLstB = re.findall(r'lambd.*?\:', self._rg_rLstA[self._rg_rIntA])
            if len(self._rg_rLstB) > 0: self._rg_rBoolB = True
            else: self._rg_rLstA[self._rg_rIntA] = self._rg_rLstA[self._rg_rIntA].replace(' ','')
            if self._rg_rBoolA:
                self._rg_rBoolA = False
                self._rg_rLstA[self._rg_rIntA] = self._rg_rLstA[self._rg_rIntA].replace('=(','')
                if not set(self._rg_rLstA[self._rg_rIntA]).issubset(SQTPP_SET_VARS):
                    return f'!÷{self._rg_rIntA+1}÷5:{self._rg_rLstA[self._rg_rIntA]}'
                if self._rg_rLstA[self._rg_rIntA] == schmNm: self._rg_sSchm.append(f'{self._rg_rLstA[self._rg_rIntA]}=(')
                else:
                    return f'!÷{self._rg_rIntA+1}÷4:{self._rg_rLstA[self._rg_rIntA]}'
                typSw = True
            else:
                if self._rg_rLstA[self._rg_rIntA] == 'item:(':
                    self._rg_rLstB = re.findall(r'inherit\=.*?\,', self._rg_rLstA[self._rg_rIntA+1])
                    if len(self._rg_rLstB) > 0:
                        self._rg_sSchm.append('item:(')
                        if len(typTrk) > 0:
                            self._rg_rLstB = self._rg_rLstB[0].split('=')
                            self._rg_rLstB = self._rg_rLstB[1].replace(',','')
                            self._rg_rIntC = 0
                            self._rg_rBoolC = False
                            self._rg_rIntD = len(typTrk)
                            while self._rg_rIntC < self._rg_rIntD:
                                if typTrk[self._rg_rIntC] == self._rg_rLstB:
                                    self._rg_rBoolC = True
                                    break
                                self._rg_rIntC+=1
                            if self._rg_rBoolC:
                                typIn = self._rg_rIntA+2
                                self._rg_sSchm.append(f'%inherit={self._rg_rLstB}')
                            else:
                                return f'!÷{self._rg_rIntA+2}÷14:{self._rg_rLstB}'
                        else:
                            return f'!÷{self._rg_rIntA+2}÷13'
                    else:
                        return f'!÷{self._rg_rIntA+2}÷12'
                if self._rg_rLstA[self._rg_rIntA] != '),':
                    if not self._rg_rBoolB and not typSw:
                        if not typAd:
                            if typAg:
                                if self._rg_rLstA[self._rg_rIntA].find('type:(') > -1 and self._rg_rLstA[self._rg_rIntA].find(',') > -1:
                                    self._rg_rLstA[self._rg_rIntA] = self._rg_rLstA[self._rg_rIntA].replace('type:(','')
                                    self._rg_rLstB = self._rg_rLstA[self._rg_rIntA].split(',')
                                    if len(self._rg_rLstB) > 1:
                                        if self._rg_rLstB[len(self._rg_rLstB)-1] == '':
                                            self._rg_rLstB.pop(len(self._rg_rLstB)-1)
                                            self._rg_rIntD = len(self._rg_rLstB)
                                            self._rg_rIntF = len(lstA)
                                            for self._rg_rIntC in range(self._rg_rIntD):
                                                self._rg_rIntE = 0
                                                self._rg_rBoolC = False
                                                while self._rg_rIntE < self._rg_rIntF:
                                                    if self._rg_rLstB[self._rg_rIntC] == lstA[self._rg_rIntE]:
                                                        self._rg_rBoolC = True
                                                        break
                                                    self._rg_rIntE+=1
                                                if not self._rg_rBoolC:
                                                    return f'!÷{self._rg_rIntA+1}÷3:{self._rg_rLstB[self._rg_rIntC]}'
                                            if typIn == self._rg_rIntA: typIn = '%type:('
                                            else: typIn = 'type:('
                                            if len(self._rg_rLstB) > 1: self._rg_sSchm.append(f'{typIn}{",".join(self._rg_rLstB)}')
                                            else: self._rg_sSchm.append(f'{typIn}{self._rg_rLstB[0]}')
                                            typIn = 0
                                        else:
                                            return f'!÷{self._rg_rIntA+1}÷2'
                                    else:
                                        return f'!÷{self._rg_rIntA+1}÷1'
                                    typAd = True
                            else:
                                if not typEt:
                                    return f'!÷{self._rg_rIntA+1}÷8'
                                else:
                                    return f'!÷{self._rg_rIntA}÷8'
                        else:
                            typAd = False
                            if self._rg_rLstA[self._rg_rIntA] == 'validator[': self._rg_sSchm.append('validator[')
                    else:
                        if self._rg_rBoolB:
                            self._rg_rLstB = re.findall(r'lambda(?:\s*[a-zA-Z_][a-zA-Z_0-9]*(?:\s*,\s*[a-zA-Z_][a-zA-Z_0-9]*)*)?\s*:\s*.+', self._rg_rLstA[self._rg_rIntA])
                            if len(self._rg_rLstB) > 0:
                                vldLm = True
                                self._rg_rLstB = self._rg_rLstB[0]
                                if self._rg_rLstB.find("'") > -1 and self._rg_rLstB.find('"') > -1:
                                    return f'!÷{self._rg_rIntA}÷11'
                                else:
                                    if self._rg_rLstB.find("'") > -1: self._rg_rLstB = self._rg_rLstB.replace("'", '~||/')
                                    if self._rg_rLstB.find('"') > -1: self._rg_rLstB = self._rg_rLstB.replace('"', '~||/')
                                if self._rg_rLstB[len(self._rg_rLstB)-1] == ',': self._rg_rLstB = self._rg_rLstB[0:len(self._rg_rLstB)-1]
                                self._rg_sSchm.append(self._rg_rLstB)
                            else:
                                return f'!÷{self._rg_rIntA}÷9'
                        else:
                            typSw = False
                            if self._rg_rLstA[self._rg_rIntA].find(':(') > -1:
                                self._rg_rLstB = self._rg_rLstA[self._rg_rIntA].split(':(')
                                self._rg_rLstA[self._rg_rIntA] = self._rg_rLstA[self._rg_rIntA].replace(':(','')
                                if self._rg_rLstB[0] == 'type' or self._rg_rLstB[0] == 'item':
                                    typAg = False
                                    typEt = True
                                else: typAg = True
                                if typAg:
                                    if not set(self._rg_rLstA[self._rg_rIntA]).issubset(SQTPP_SET_VARS):
                                        return f'!÷{self._rg_rIntA+1}÷7:{self._rg_rLstA[self._rg_rIntA]}'
                                    else:
                                        typTrk.append(self._rg_rLstA[self._rg_rIntA])
                                        self._rg_sSchm.append(f'{self._rg_rLstA[self._rg_rIntA]}:(')
                            else:
                                return f'!÷{self._rg_rIntA+1}÷6'
                else:
                    typSw = True
                    self._rg_sSchm.append('.|.//^.')
        return rtrn
#___________________________________________AHS/////////////////////////////////////////
#///////////////////////////////////////////______________________________________||~.~


#_______________________________________________________________________________________

#                         .|IMPORTABLE FRONT FUNCTIONS|.

#_______________________________________________________________________________________
def sqtpp_rd1(src):
    # **** For testing purposes only ****
    sqtppCls = Sqtpp()
    sqtppCls.mcf_sqtpp_rd1(src)
#_______________________________________________________________________________________
#_______________________________________________________________________________________
#_______________________________________________________________________________________
def makevfs(vfsFileName: str, directoryName: str, folderName:str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_makevfs(vfsFileName, directoryName, folderName)
#_______________________________________________________________________________________
def setpath(vfsFileName: str, directoryName: str, folderName: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_setpath(vfsFileName, directoryName, folderName)
#_______________________________________________________________________________________
def corevar(mode: int, varName: str, booleanList: list):
    sqtppCls = Sqtpp()
    rtrn = sqtppCls.mcf_corevar(mode, varName, booleanList)
    if rtrn != None:
        return rtrn
#_______________________________________________________________________________________
def addvar(varName: str, varData: str):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_addvar(varName, varData)
#_______________________________________________________________________________________
def appvar(varNames: list, varDatas: list, varLocks):
    sqtppCls = Sqtpp()
    sqtppCls.mcf_appvar(varNames, varDatas, varLocks)
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
def listfiles():
    sqtppCls = Sqtpp()
    sqtppCls.mcf_list_files()
#_______________________________________________________________________________________
def lambdalist(asComplete: bool):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_lambdalist(asComplete)
#_______________________________________________________________________________________
def genicvar(mode: str, varName, varData, varId: list):
    sqtppCls = Sqtpp()
    return sqtppCls.mcf_genicvar(mode, varName, varData, varId)
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
def registry(isRead: bool, keyName: str, keyData, harpSchema: str):
    sqtppCls = Sqtpp()
    # @keyData can be string, list, bool, int, float or complex but not a nested list
    # @harpSchema string only, is either a schema .../dir/file path or schema's name
    return sqtppCls.mcf_lll_registry(isRead, keyName, keyData, harpSchema)
#_______________________________________________________________________________________
def pojishon(mode: str, varData, varName, dirList: list):
    sqtppCls = Sqtpp()
    # @varData & @varName can both be list type or str type pairing
    return sqtppCls.mcf_pojishon(mode, varData, varName, dirList)
#_______________________________________________________________________________________
