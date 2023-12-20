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

