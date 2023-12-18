# Code File: StaqTapp-1.02 [stpx.py] StaqTapp gzip methods & module calls


# Staqtapp 1.02.458

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


from PySqTpp_Stpx import StpxSrvc as __stsrC
import stpp
import stpu
import os
import re

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

# [ x_getlist_vars(isSort) ] - returns (str) list of all glb var names associated to
# file currently set in gzip path to/from after a @x_addlist_vars() call, does not
# get all glb var names directly from the .tqpt variable source file, this of use to
# multi-processing encodings or other procedures involving backup tracing, also very
# useful to ai-sys that would call ×_findvar() & ×_renamevar() in secure cycles

# (not yet a fully implemented stpx method)
# [ x_menorahvar(isGreater, isSar, varName) ] - returns a specialized compressed
# palindrome encoded int of any number, multi-processing should be considered

# [ x_makesource(isStatic, isMakeFolder, isEraseSource) ] - calls main stpp function

# [ x_addvar(varName, varData) ] - calls main stpp function

# [ x_removevar(isBackup, varNames) ] - deletes glb variable(s) from set path .tqpt source
# if @isBackup=True then creates a .gz compressed backup file of the .tqpt source file in
# the .../stpx folder directory; @varNames can be a single str or str-list of variable name(s)
# this function returns True if performed any .tqpt glb variable(s) removal(s) or False if not

# [ x_renamevar(varName, newVarName) ] - calls main stpp function

# [ x_loadvar_str(varName) ] - calls main stpp function

# [ x_loadvar_deque(isNumbers, varName) ] - calls main stpp function

# [ x_loadsar_remap(isPrmExc, catPin) ] - calls main stpp function

# [ x_changevar(varName, newVarData) ] - calls main stpp function

# [ x_findvar(allSources, varName) ] - calls main stpp function

# [ x_finddata(isRegx, varNames, search) ] -  if @varNames(str-list) is not given
# then will read the .tqpt variables source file line by line, this method returns list
# type result as ['var_name', 'found_data'] @isRegx=True expects compiled pattern
# expression @search, otherwise uses str.find() to locate any match, @search
# can be compiled regular expression, str or numbers as a fine parameter choice;
# if compiled regex pattern on line-by-line find, pattern compiled must be rb'' or b''

# [ x_splitsource(newFileName) ] - splits a .tqpt and/or connected .tpqt lock source 
# in half for new staqtapp source file(s) -- min. var stack length must be 42 or more;
# returns True if done, False if not, or None if detected a .tqpt source corruption

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
    # then created stpx folder/file will be in path of this module's current running directory
    __stsrC.stpx_set_path(fldrPth, fleNm)
#______________________________________________________________________________________

def x_getpath(pth: str):
    # returns @:pth<...> and @:fle<...> stpx gz listings as a (str)list
    return __stsrC.stpx_get_path(pth)
#______________________________________________________________________________________

def x_addlist_vars():
    # sets all global variable names listed in a .tqpt file to a listed stack in the gzip
    # [/x_stpx.gz] made from x_setpath() call---gzip to be present & valid .tqpt set path
    # currently from set path .tqpt source file; method allows var name listing any tqpt:
    # var names added to gzip stack are listed as ':var<@tqpt_file_name:@var_name>'
    # returns replace count int if gzip of prior listed variable name(s) set of .tqpt name
    # of has then fully replaced that prior set wether changes or not to the .tqpt file
    # otherwise returns None ***all x viewable: var, sar and sar pointer type namings***
    return __stsrC.stpx_add_list_vars()
#______________________________________________________________________________________

def x_getlist_vars(isSort: bool):
    # returns a (str) list of all glb variable names associated with set .tqpt file name
    # from x_stpx.gz after a @x_addlist_vars() call with gzip set path .tqpt file name
    return __stsrC.stpx_get_list_vars(isSort)
#______________________________________________________________________________________

def x_menorahvar(isGreater, src):
    # THIS METHOD NOT FULLY IMPLEMENTED YET
    # @src is any str of seq numbers wether negative or not, this method is for and
    # will compress number to a menorah palindrome return equality responsible
    
    # https://ibb.co/C12Qbr4
    # the kindness of a child no man made, no man can give and no man above
    
    #stpxXq = StpxSrvc()
    #return stpxXq.stpx_get_menorah_palindrome_encoding(isGreater, src)
    pass
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

def x_removevar(isBackup: bool, varNames):
    # see x_removevar() function uses explained @ top of this module
    return __stsrC.stpx_remove_vars(isBackup, varNames)
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

def x_finddata(isRegx: bool, varNames: list, search):
    # see x_finddata() function uses explained @ top of this module
    return __stsrC.stpx_find_data(isRegx, varNames, search)
#______________________________________________________________________________________

def x_splitsource(newFileName: str):
    # see x_splitsource() function uses explained @ top of this module
    return __stsrC.stpx_split_source(newFileName)
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

def test():
    
    #x_changevar('seq_212_M34nor', '@qp(0987654321,0123456789,2.7,8.1,9.3):')
    
    #x_setpath('/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test')
    
    x_removevar(False, 'variableDequeTest6')
    
    #x_addlist_vars()

    #print(x_getlist_vars(True))
    
    #print(x_findvar(False, 'seq_111'))
    
    #print(x_finddata(True, None, re.compile(rb'5678')))

test()


