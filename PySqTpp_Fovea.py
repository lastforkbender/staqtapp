# Code File: StaqTapp-1.02 [PySqTpp_Fovea.py] StaqTapp's scripting lang parser/stpx interpreter


# Staqtapp 1.02.460

# Staqtapp is a full global variables stack feature rich library, covering all solid
# i/o functions calls from the stpp.py module or stpx.py pro module. Features
# included are precise parsings, interchangable & dynamic .tpqt lock files for
# avoiding entanglements, mmap responsive reads-writes-edits across all it's
# functional calls & much more like the scanning of any py module for potential
# global variables conflicts. Staqtapp uses only in-built python libraries and has
# no current package release, until it's scope exceeds any expected relations or
# utterly bypass any formatted opinions of filed global variables uses. With q-bit
# computing very near. A long-term goal of Staqtapp is to provide alt simulations
# of such circumstances in the future, where global variables use by concentrated
# files using hybrid computing desolves the long bad opinions of global variables.

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


#______________________________________________________________________________________



# ---------------------------------------------- FOVEA SCRIPT KEYWORDS ---------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# DEVELOPER NOTE: all of staqtapp's fovea scripting instruction parameters are y or n
# for boolean conditions, or yn; or ny if previous instruction is nested call of set path to
# a temp directory before change, this will set magic interpreter string to XKGT after
# set to XKTG, of will not change to XKTG again but is of a same read focus sought; at
# any time a parameter use of yn or ny, then the specific @fovea_mantis type methods
# can change the source to a expanded clause or compressed clause of execute | loop
# all other parameters follow the same guidelines described in the stpp or stpx module


# ---------- PREFIX-INTERPRETER-G | G-TYPE KEYWORDS(only stpx methods related):
#
# SPH:
# [set path] --> sph, folderPath, tqptFileName;
#
# GPH:
# [get path] --> gph (has no parameters);
#
# AVL:
# [add var list] --> avl (has no parameters);
#
# GVL: !has boolean parameters!
# [get var list] --> gvl, isSorted;


# ---------- PREFIX-INTERPRETER-T | T-TYPE KEYWORDS(only stpx methods related):
#
# FDD: !has boolean parameters!
# [find data] --> fdd, isRegex, variableNames, search;
#
# SSC:
# [split source] --> ssc, newTqptFileName;


# ---------- PREFIX-INTERPRETER-X | X-TYPE KEYWORDS:
#
# AVR:
# [add var] --> avr, variableName, variableData;
#
# LDV:
# [load var str] --> ldv, variableName;
#
# CHV:
# [change var] --> chv, variableName, newVariableData;
#
# RNV:
# [rename var] --> rnv, variableName, newVariableName;
#
# FND: !has boolean parameters!
# [find var] --> fnd, isAllSources, variableName;
#
# RVR: !has boolean parameters!
# [remove var] --> rvr, isBackup, variableNames;
#
# ASR: !can manifest boolean parameter options!
# [add sar] --> asr, categoryPin, variableData;
#
# LSR: !can manifest boolean parameter options!
# [load sar remap] --> lsr, categoryPin;


# ---------- PREFIX-INTERPRETER-K | K-TYPE KEYWORDS:
#
# LKV:
# [lock var] --> lkv, variableName, functionName;
#
# KYV:
# [key var] --> kyv, variableName, functionName;
#
# SRK:
# [search keys] --> srk, variableName;

#______________________________________________________________________________________
#______________________________________________________________________________________

import PySqTpp_FoveaInterface
import PySqTpp_Rev9 as r9
import mmap
import stps
import stpx
import gzip
import os
import re
import io

#______________________________________________________________________________________

class FoveaStpx(PySqTpp_FoveaInterface.PySqTppFoveaInterface):
    # - settled functions for fovea instruction parsing methods -
#______________________________________________________________________________________

    def fovea_mantis_absorb(x_src, fPth: str) -> bool:
        
        # first, determine the abstract of XKTG or XKGT via represented occurences;
        # of XK then either XXK or XKK, and of KX then either KKX or KXX, these two
        # different aspects of each associated with X to K, X is the 8 main instruction
        # calls: avr, ldv, chv, rnv, fnd, rvr, asr and lsr -- of these 8 core abstracts, of very
        # high probable call in pair of another in same category(XXK or KXX) mirrors
        # same lesser/higher probable of a dual K prefix-interpreter calls(XKK or KKX)
        
        # K prefix-interpreter calls are all refrence to lock var(LKV), key var(KYV) and
        # search keys(SRK) of which known to be of more higher probable paired calls
        # in concentrated grouping of the script's instructions, making this view of the
        # script four dimensional to a dual copy represent -Lto+R or -Rto+L both; from
        # a biological speaking aspect, which is included of my education level these
        # global variable encodings to the magic string XKTG or/and XKGT are all env
        # effects by choice of the total instructions to place effect on the interpreter
        
        # NOTE: Not about tokens or credits, about abstract ----- credit or token is flaw,
        # flawed judgement in mathematical expansions often and judged irrelevant
        # because it often leads to more complex encoding suspect of redundancies
        
        # ☆love your neighbor, not judge them by circumstances of credit or tokens
        # often in use for a foundation of trust in usury and lies written in legal-trash
        
        if len(x_src) > 0:
            fstx = FoveaStpx()
            mtch = None
            # 1=field, 2=file, 3=fuzz
            dsg = None
            hdr = None
            hxr = None
            ins = None
            if isinstance(x_src, str) == True:
                if x_src.find('dsg=field') > -1:
                    dsg = 1
                    # is a direct combined string joined by new line chars, doesn't need endings--> ';'
                    # split it stripping the header info and if any comments in the new ins list also
                    x_src = x_src.split('\n')
                    if len(x_src) > 1:
                        hdr = ins[0]
                        x_src = fstx.fovea_mantis_list_edits('fma', x_src)
                    else:
                        return False
                elif x_src.find('dsg=file') > -1:
                    dsg = 2
                    # is '\n's after each char end ';' instructions, a staqtapp fovea .qpsx script file..?
                    # this way of running script can have added options @x_src as the twin header
                    # that can also have numerous math options &| other refrences to other scripts
                    ins = bytes.decode(fstx.fovea_mantis_map('rfm', fPth))
                    ins = ins.split('\n')
                    if len(ins) > 1:
                        hdr = ins[0]
                        hxr = x_src
                        x_src = fstx.fovea_mantis_list_edits('fma', ins)
                        ins = None
                    else:
                        return False
                else:
                    return False
            elif isinstance(x_src, list) == True:
                dsg = 3
                # passing a list to @x_src is considered fuzzy logic, can include custom made
                # descriptions in the header line; and pointing to certain options in this module
                # or purposes escaping the magic string XKGT's pointings of other descriptors
                # this type script run produce very expected results or very unexpected results
                # [ [normally, magic string is set to XKTG with no unknown descriptor(s) calls] ]
                if len(x_src) > 1:
                    hdr = x_src[0]
                    x_src = fstx.fovea_mantis_list_edits('fma', x_src)
                else:
                    return False
            else:
                return False
            # remove @x_src elements of ';'/space and count how many X, K, T and G -----------
            # prefix-interpreter instructions there are in this script run; also remove any blanks
            xktgLst = [0,0,0,0]
            for x in range(len(x_src)):
                try:
                    x_src[x] = x_src[x].replace(' ;', '')
                    if x_src[x].find('avr') > -1 or x_src[x].find('ldv') > -1 or x_src[x].find('chv') > -1 or x_src[x].find('rnv') > -1:
                        xktgLst[0]+=1
                    elif x_src[x].find('fnd') > -1 or x_src[x].find('rvr') > -1 or x_src[x].find('asr') > -1 or x_src[x].find('lsr') > -1:
                        xktgLst[0]+=1
                    elif x_src[x].find('lkv') > -1 or x_src[x].find('kyv') > -1 or x_src[x].find('srk') > -1:
                        xktgLst[1]+=1
                    elif x_src[x].find('fdd') > -1 or x_src[x].find('ssc') > -1:
                        xktgLst[2]+=1
                    elif x_src[x].find('sph') > -1 or x_src[x].find('gph') > -1 or x_src[x].find('avl') > -1 or x_src[x].find('gvl') > -1:
                        xktgLst[3]+=1
                    else:
                        if len(x_src) > 1:
                            x_src.pop(x)
                        else:
                            return False
                except Exception as e:
                    if len(x_src) > 1:
                        x_src.pop(x)
                    else:
                        return False
            # call upon @fovea_mantis_algo() to set magic string XKTG as initial startings
            return True
        else:
            return False
#______________________________________________________________________________________

    def fovea_mantis_echo(x_src: list):
        # TODO - does several things including security & extraction of any nested parameters
        pass
#______________________________________________________________________________________

    def fovea_mantis_algo(isLoop: bool, dsg: int, prefix: list, currDrvr: list) -> list:
        # TODO - determines the magic string XKTG | XKGT depends, order and/or change
        pass
#______________________________________________________________________________________

    def fovea_mantis_list_edits(dsg: str, lstSrc: list) -> list:
        # specific edits of list for source instruction sets and other needed list structuring
        lstLen = len(lstSrc)
        xf = 0
        if dsg == 'fma':
            lstSrc.pop(0)
            while xf < lstLen:
                if lstSrc[xf].find('☆') > -1:
                    lstSrc.pop(xf)
                xf+=1
            return lstSrc
#______________________________________________________________________________________

    def fovea_mantis_map(dsg: str, pth: str):
        # handles all read, search, write or replace methods for this module's parsings
        if dsg == 'rfm':
            with open(pth, mode='r') as fObjRfma:
                with mmap.mmap(fObjRfma.fileno(), length=0, access=mmap.ACCESS_READ) as mpObjRfma:
                    rtrn = mpObjRfma.read()
                    mpObjRfma.close()
                mpObjRfma = None
            return rtrn
        