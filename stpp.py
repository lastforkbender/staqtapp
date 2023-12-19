# Code File: StaqTapp-1.02 [stpp.py] StaqTapp main functional calls module


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


from PySqTpp_Parser import TqptParser
from collections import deque
from stps import extrloadsarremap
import stpu
#______________________________________________________________________________________

# STAQTAPP'S  PILOT - stpp.methods()

# [.makesource] - creates a new empty staqtapp tqpt variables source file

# [.addvar] - writes new variable and it's data to chosen staqtapp tqpt source file

# [.renamevar] - changes to new variable name @ .tqpt and .tpqt source files if any
# use at your own risk, normally not recommended on glb vars safe or unsafe

# [.addsar] - adds sar variables to tqpt source files with collection extensions, see
# sar_remap, sar_demap, loadsar_temple

# [.changevar] - writes new data to chosen variable/staqtapp tqpt source file

# [.findvar] - returns true/false of chosen staqtapp source file or a multi-detailed find list

# [.loadvar_str] - returns str or list(strings) type from staqtapp tqpt source files variable(s)

# [.loadvar_deque] - returns a deque type list of variable's current stored data

# [.loadsar_temple] - [TO-DO] front end access @ de-entaglement of common global
# variable entaglements & security issues, hidden obscured access

# [.sar_remap] - see PySqTppSarAlpha, adds temple variable/sar variables multi-pointer
# type to tqpt sources

# [.sar_demap] - [TO-DO] assigns front keys(natural) & back keys(non-natural) to temple
# variables/pointers secure wrapped/obfuscated and/or locked
#______________________________________________________________________________________

# UTILITY - calling stpp.methods()

# [.lockvar] - creates tpqt lock function call files for global variable(s) domain restrictions

# [.keyvar] - searches a tpqt function lock file, giving feedback conditional on the global
# variable allowed to be changed by listed functions in pairing of the tqpt source file

# [.searchkeys] - returns a list of function name(s) from a global variable search in a tpqt file

# [.viewkeys] - prints a tpqt global variable keys/functions locks sublist file to console

# [.lockvar_edit] - a parallel/helper function to lockvar; does not add new function name(s)
# sublist to a new variable name to add, rather new function name(s) sublist to a already
# existing .tpqt file with a already variable name listed, useful for multi-processing needs

# [.unlockvar] - (TO-DO) inverts a tpqt function lock file for a given number of instructions,
# useful on mathematical intense operations; is only a temporary cache of tpqt file inverted
# @ which entry/exit of variables/functions locks listed that the programmer decides on;
# is unsecure in that it allows parallel tqpt entanglement in parallel of open global variables

# [.scanvar] - searches a py module for potential global variable conflicts with a provided
# global variable name, returns suggested smart str global variable name or wanted var
# name as given; does not use regex and very accurate scan of all classes, functions and
# variables names, including all variable naming inside any function's parameters

# [.viewsource] - prints a tqpt variables source file's contents to console in readable slots
#______________________________________________________________________________________

# SELF-REPLICATION GLOBAL VARIABLES LIBRARY BUILD - calling stpp.methods()

# [.rev9build] - builds a custom global variables i/o library using an assortment of different options
# including __slots__ and/or sars enabled variables programming to made py modules builds, 15
# parameter settings are of this method call to begin a rev9 global variables resource library build
#______________________________________________________________________________________

def makesource(isStatic, isMakeFolder, isEraseSource, folderPath, fileName):
    
    # isMakeFolder=bool, isEraseSource=bool, folderPath=str, fileName=str
    
    # **this function only makes a new folder when isMakeFolder=true and isEraseSource
    # ==false for the current working module's path found**
    	
    	# if tqpt source file is made as a static read, no write, the setting for this
    	# is ||||:* at top of file or ||||:_ for non-static read/write tqpt files
    	
    	
    	# Boolean arguments use for <makesource>
    
    # ((isMakeSource==True and isEraseSource==True)) seeks overwrite of source file or
    # make new empty source file from path/name given, will overwrite a existing
    # variables source file to empty
    
    # ((isMakeSource==False and isEraseSource==True)) seeks overwrite of source file or
    # make new empty source file, will overwrite a existing source file to empty
    
    # ((isMakeSource==False and isEraseSource==False)) seeks make of a new empty source
    # file from path/name given, no overwrite of source file to empty
    
    # ((isMakeSource==True and isEraseSource==False)) seeks new folder; new source file
    # made at current module's directory use, will not overwrite a existing source file
    # to empty of current module's directory, no overwrites regardless of isEraseSource
    # set to true or false of the arguments conditionals use together, fileName is used
    # and must be valid to ._-, aA-zZ and 0-9 string argument given, both folder & file
    
    
    rslt = None
    
    if isinstance(isMakeFolder, bool) and isinstance(isEraseSource, bool):
        newTqptParser = TqptParser()
        ##################################################################
        if isEraseSource == True:
        ##################################################################
        # overwrite any .tqpt variables source file to empty is true
        
            if len(folderPath) > 0 and len(fileName) > 0:
                if newTqptParser.check_parameter_string(False, fileName, False):
                    # is a valid filename
                    rslt = newTqptParser.make_variables_source(isStatic, False, True, folderPath, fileName)
                    if rslt == -4:
                        # folderPath is not there
                        raise Exception("staqtapp<makesource> invalid folderpath @" + folderPath)
                else:
                    # not a valid filename
                    raise Exception("staqtapp<makesource> invalid filename, allowed chars ._- aA-zZ 0-9")
            else:
                # folderPath and/or fileName not of any string length
                raise Exception("staqtapp<makesource> null folderpath and/or null filename")
        ##################################################################
        elif isMakeFolder == False and isEraseSource == False:
        ##################################################################
        # any overwrites is false, however can make new .tqpt source file
        
            if len(folderPath) > 0 and len(fileName) > 0:
                if newTqptParser.check_parameter_string(False, fileName, False):
                    rslt = newTqptParser.make_variables_source(isStatic, False, False, folderPath, fileName)
                    if rslt == -3:
                        # source file already exist, no overwrite
                        raise Exception("staqtapp<makesource> source file '" + fileName + "' already exist, no overwrite")
                    elif rslt == -4:
                        raise Exception("staqtapp<makesource> invalid folderpath @" + folderPath)
                else:
                    # filename of not allowed chars...
                    raise Exception("staqtapp<makesource> invalid filename, allowed chars ._- aA-zZ 0-9")
            else:
                raise Exception("staqtapp<makesource> null folderpath and/or null filename")
        ##################################################################
        elif isMakeFolder == True and isEraseSource == False:
        ##################################################################
        # make new folder & source file of a current module's directory
        
            if len(fileName) > 0:
                if newTqptParser.check_parameter_string(False, fileName, False):
                    rslt = newTqptParser.make_variables_source(isStatic, True, False, folderPath, fileName)
                    if rslt == -1:
                        raise Exception("staqtapp<makesource> folder & source file already exist")
                    elif rslt == -2:
                        raise Exception("staqtapp<makesource> current module's directory not found...")
                else:
                    raise Exception("staqtapp<makesource> invalid filename, allowed chars ._- aA-zZ 0-9")
            else:
                # file name length is null...
                raise Exception("staqtapp<makesource> null filename")
    else:
        # as boolean parameter(s) needed was not a matched type
        raise Exception("staqtapp<makesource> invalid arguments for bool types")
  
#______________________________________________________________________________________

def addvar(varName, varData, folderPath, fileName):
    
    # varName=str, varData=str, folderPath=str, fileName=str
    
    # *varData parameter must be of '@qp(data):' or '@qp(data,...):' tag declarings
    # and also have no newline chars, if other chars are in between the data declarings
    # is ignored; if comma adds inside varData declares, will be read as a array/list
    # return for loadvar functions and other, more than one data tag declaring is array
    # considered; if needed string explict with numbers, like ip addrs etc. include
    # quote marks normal use string declare; nesting of @qp tagging is not supported
    
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(True, varName, False):
            rslt = newTqptParser.add_variables_source(varName, varData, folderPath, fileName)
            # check for any of the exception returns, otherwise silent finished
            if rslt == -1:
                raise Exception("staqtapp<addvar> invalid folderpath @" + folderPath)
            elif rslt == -2:
                raise Exception("staqtapp<addvar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -3:
                raise Exception("staqtapp<addvar> variable name '" + varName + "' already exist @" + folderPath + "/" + fileName + ".tqpt")
            elif rslt == -4:
                raise Exception("staqtapp<addvar> cannot write to a static locked tqpt source file")
            elif rslt == -5:
                raise Exception("staqtapp<addvar> bad .tqpt source file, could not read settings")
            elif rslt == -6:
                raise Exception("staqtapp<addvar> newline chars not allowed in variable sources")
            elif rslt == -7:
                raise Exception("staqtapp<addvar> no proper data declare(s) '@qp(data):' found")
            elif rslt == -8:
                raise Exception("staqtapp<addvar> missing data declare closing '):' ")
        else:
            raise Exception("staqtapp<addvar> invalid variable name, allowed chars _ aA-zZ 0-9")
    else:
        raise Exception("staqtapp<addvar> null folderpath and/or null filename")
#______________________________________________________________________________________

def renamevar(varName, newVarName, folderPath, fileName):
    
    # varName=str, newVarName=str, folderPath=str, fileName=str
    
    # renames an existing variable name in a .tqpt variables source to @newVarName;
    # if suceeds then checks if any .tpqt files and makes variable name change also
    
    rslt = None
    
    if len(folderPath) > 0 and len(fileName) > 0:
        newTqptParser = TqptParser()
        rslt = newTqptParser.change_variable_name(varName, newVarName, folderPath, fileName)
        if rslt == -1:
            raise Exception("staqtapp<renamevar> invalid folderpath @" + folderPath)
        elif rslt == -2:
            raise Exception("staqtapp<renamevar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
        elif rslt == -3:
            raise Exception("staqtapp<renamevar> variables source file '" + fileName + ".tqpt' is a static source")
        elif rslt == -4:
            raise Exception("staqtapp<renamevar> variable name '" + varName + "' not found @" + folderPath + "/" + fileName + ".tqpt")
        elif rslt == -5:
            raise Exception("staqtapp<renamevar> invalid variable name @newVarName, allowed chars _ aA-zZ 0-9")
    else:
        raise Exception("staqtapp<renamevar> null folderpath and/or null filename")
#______________________________________________________________________________________

def loadvar_str(varName, folderPath, fileName):
    
    # varName=str | list, folderPath=str, fileName=str
    
    # @varName can be str or list and as a same return as str or list, if list as a
    # parameter then appends to the return list what it can, ignoring variable -----
    # names not found in the selected tqpt source file folderPath/fileName; is to
    # be noted list return from a list parameter given returns lists nested in a list
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(True, varName, True):
            rslt = newTqptParser.load_variables_source_str(varName, folderPath, fileName)
            if rslt == -3:
                # variable was not found in tqpt source file
                raise Exception("staqtapp<loadvar_str> variable name '" + varName + "' not found @" + folderPath + "/" + fileName + ".tqpt")
            elif rslt == -2:
                # invalid fileName given
                raise Exception("staqtapp<loadvar_str> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -1:
                # invalid folderPath given
                raise Exception("staqtapp<loadvar_str> invalid folderpath @" + folderPath)
            elif rslt == -4:
                # newline chars found
                raise Exception("staqtapp<loadvar_str> newline char found in variable's data, no parse")
            elif rslt == -5:
                # false is_all_numbers, no parse; no load
                raise Exception("staqtapp<loadvar_str> not all numbers, no parse")
            elif rslt == -6:
                # no @qp( data declaring tags found
                raise Exception("staqtapp<loadvar_str> no found @qp(data): declarings")
            elif rslt == -7:
                raise Exception("staqtapp<loadvar_str> missing closing ): for variable data declare")
            elif rslt == -8:
                raise Exception("staqtapp<loadvar_str> invalid type @varName, must be str or list")
            elif rslt == -9:
                raise Exception("staqtapp<loadvar_str> no found variable names @varName as list")
            elif rslt == -10:
                raise Exception("staqtapp<loadvar_str> no valid data returns from @varName as list")
            else:
                return rslt
        else:
            raise Exception("staqtapp<loadvar_str> invalid variable name, allowed chars _ aA-zZ 0-9")
    else:
        raise Exception("staqtapp<loadvar_str> null folderpath and/or null filename")
#______________________________________________________________________________________

def loadvar_deque(isNumbers, varName, folderPath, fileName):
    
    # isNumbers=bool, varName=str, folderPath=str, fileName=str
    
    # this function returns decimal or int for numbers in a array or else, nested
    # variable data @qp( tagging is not yet supported of this version, see addvar
    	    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(True, varName, False):
            rslt = newTqptParser.load_variables_source_deque(isNumbers, varName, folderPath, fileName)
            if rslt == -3:
                # variable was not found in tqpt source file
                raise Exception("staqtapp<loadvar_deque> variable name '" + varName + "' not found @" + folderPath + "/" + fileName + ".tqpt")
            elif rslt == -2:
                # invalid fileName given
                raise Exception("staqtapp<loadvar_deque> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -1:
                # invalid folderPath given
                raise Exception("staqtapp<loadvar_deque> invalid folderpath @" + folderPath)
            elif rslt == -4:
                # newline chars found
                raise Exception("staqtapp<loadvar_deque> newline char found in variable's data, no parse")
            elif rslt == -5:
                # false is_all_numbers, no parse; no load
                raise Exception("staqtapp<loadvar_deque> not all numbers, no parse")
            elif rslt == -6:
                # no @qp( data declaring tags found
                raise Exception("staqtapp<loadvar_deque> no found @qp(data): declarings")
            elif rslt == -7:
                # missing closing ): of a @qp( data declaring...
                raise Exception("staqtapp<loadvar_deque> missing closing ): for variable data declare")
            else:
                return rslt
        else:
            # bad variable name chars...
            raise Exception("staqtapp<loadvar_deque> invalid variable name, allowed chars _ aA-zZ 0-9")
    else:
        raise Exception("staqtapp<loadvar_deque> null folderpath and/or null filename")
    
#______________________________________________________________________________________

def loadsar_remap(isPrmExc, catPin, folderPath, fileName):
        
    # isPrmExc=bool, catPin=str, folderPath=str, fileName=str
    
    # adds temple variable/sar variables multi-pointer type to tqpt
    # variable source file that already has sar variables added to it,
    # the category pin must be a parameter for what sar variables
    # will the temple variable be connected to when added to file; can
    # have multiple remaps applied of a single source file, however
    # staqtapp only load temple variables of a most recent date/time
        
    extrloadsarremap(isPrmExc, catPin, folderPath, fileName)
#______________________________________________________________________________________

def changevar(varName, newVarData, folderPath, fileName):
    
    # varName=str, newVarData=str, folderPath=str, fileName=str
    
    # renews variable data @ existing variable listed from chosen tqpt source file, folder+file
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(False, fileName, False):
            rslt = newTqptParser.update_variables_source(varName, newVarData, folderPath, fileName)
            if rslt == -1:
                raise Exception("staqtapp<changevar> invalid folderpath @" + folderPath)
            elif rslt == -2:
                raise Exception("staqtapp<changevar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -3:
                raise Exception("staqtapp<changevar> newline chars not allowed in variable sources")
            elif rslt == -4:
                raise Exception("staqtapp<changevar> no proper data declare(s) '@qp(data):' found")
            elif rslt == -5:
                raise Exception("staqtapp<changevar> missing data declare closing '):' ")
            elif rslt == -6:
                raise Exception("staqtapp<changevar> variable name '" + varName + "' not found @" + folderPath + "/" + fileName + ".tqpt")
        else:
            raise Exception("staqtapp<changevar> invalid filename, allowed chars ._- aA-zZ 0-9")
    else:
        raise Exception("staqtapp<changevar> null folderpath and/or null filename")
#______________________________________________________________________________________

def findvar(allSources, varName, folderPath, fileName):
    
    # allSources=bool, varName=str, folderPath=str, fileName=str
    
    # parameter allSources of True, then finds all tqpt files of given folderPath
    # and returns a list type in format 'fullpath:varname:linenumber' str @indices
    # if variable find(s) else returns a empty list; allSources=False returns true
    # or false for variable found or not found from given dir & file name combined
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(False, fileName, False):
            rslt = newTqptParser.search_variable(allSources, varName, folderPath, fileName)
            if rslt == -3:
                raise Exception("staqtapp<findvar> no found tqpt variable source files @" + folderPath)
            elif rslt == -2:
                raise Exception("staqtapp<findvar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -1:
                raise Exception("staqtapp<findvar> invalid folderpath @" + folderPath)
            else:
                return rslt
        else:
            raise Exception("staqtapp<findvar> invalid filename, allowed chars ._- aA-zZ 0-9")
    else:
        raise Exception("staqtapp<findvar> null folderpath and/or null filename")

#______________________________________________________________________________________

def addsar(catPin, varData, folderPath, fileName):
    
    # catPin=str, varData=str, folderPath=str, fileName=str
    
    # works the same as a staqtapp addvar function however the variable name is assigned to
    # a random ten digit number, also allows data collection of any words used in the data for
    # the variable, created in a dat extension file of the tqpt variable source's directory;
    # catPin str parameter is intened for tracking purposes of any grouped type data use and is
    # a string included of the variable's random assigned number both; due to complexity
    # of larger word files and needed parsing of not adding duplicates should be considered for
    # multi processing, addvar_sar is of the PySqTppSarInterface's methods separated and
    # does not add duplicate words to the created extension file of that tqpt source directory
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(False, fileName, False):
            rslt = newTqptParser.self_assign_variable_name(catPin, varData, folderPath, fileName)
            if rslt == -1:
                raise Exception("staqtapp<addsar> invalid folderpath @" + folderPath)
            elif rslt == -2:
                raise Exception("staqtapp<addsar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -3:
                raise Exception("staqtapp<addsar> newline chars not allowed in variable sources")
            elif rslt == -4:
                raise Exception("staqtapp<addsar> no proper data declare(s) '@qp(data):' found")
            elif rslt == -5:
                raise Exception("staqtapp<addsar> missing data declare closing '):' ")
            elif rslt == -6:
                raise Exception("staqtapp<addsar> invalid category pin, allowed chars _ aA-zZ 0-9")
        else:
            raise Exception("staqtapp<addsar> invalid filename, allowed chars ._- aA-zZ 0-9")
    else:
        raise Exception("staqtapp<addsar> null folderpath and/or null filename")
#______________________________________________________________________________________

def lockvar(varName, fncName, fullPath):
    
    # UTILITY FUNCTION: [used with keyvar()]
        
    # varName=str, fncName=str | list, fullPath=str
    
    # lockvar adds to or creates tpqt files, position-quanity rather than quanity-position;
    # a tpqt file is made at same directory of a tqpt global variable data file, is a lock
    # file for global variables usage in parallel of allowed functions of a variable, to be
    # used with the pairing utility function keyvar; @fncName can be a single allowed
    # function name or a list of allowed function namings, restricts global variable edits
    # via which function is allowed to edit it dependent upon programmer's usage, @full-
    # path is always the file path of the .tqpt variables source file, not a .tpqt lock file
    
    # tpqt file structure:
        
    # <:varName=
    # fncName
    # fncName:>
    # <:varName=
    # fncName:>
    
    stpu.ult_limit_outer_domain(varName, fncName, fullPath)
#______________________________________________________________________________________

def keyvar(isLogF, varName, fncName, fullPath):
    
    # UTILITY FUNCTION: [used with lockvar()]
        
    # isLogF=bool, varName=str, fncName=str, fullPath=str
    
    # ** @fullPath is full file path of the .tqpt variable source file, not .tpqt file path **
    
    # searches a .tpqt function lock file for listed @varName and sub-listed allowed
    # function(s) name(s), if @fncName is found will return True or False not found;
    # @isLogF=True then adds to a .logf file in directory of the .tqpt & .tpqt files if a
    # True found return, in the log format as single line entries repeated:
        
    # >> var: <@varName>, fnc: <@fncName>, time: <date-time>
    
    return stpu.ult_fnc_var_request(isLogF, varName, fncName, fullPath)
#______________________________________________________________________________________

def searchkeys(varName, fullPath):
    
    # UTILITY FUNCTION:
        
    # varName=str, fullPath=str
    
    # important stpp.function that returns the sublist of functions allowed to change
    # a global variable, listed in a tpqt lock file -- @fullPath is the tqpt source path; if
    # no search results found then returns a None type rather than a list type
    
    return stpu.ult_return_function_keys(varName, fullPath)
#______________________________________________________________________________________

def lockvar_edit(varName, fncName, fullPath):
    
    # UTILITY FUNCTION:
        
    # varName=str, fncName= str | list, fullPath=str
    
    # parallel/helper function to lockvar; does not add new function name(s) sublist to a new
    # variable name to add, rather new function name(s) sublist to a already existing .tpqt file
    # with a already @varName listed ----useful for multi-processing needs or import needs in
    # testing a global variable's stranger reactions recorded; @fncName can be str or a str list
    
    stpu.ult_edit_fnc_lock(varName, fncName, fullPath)
#______________________________________________________________________________________

def scanvar(varName, fullPath):
    
    # UTILITY FUNCTION:
        
    # varName=str, fullPath=str
    
    # scans/search of entire py module's text - function names, function parameters,
    # class names and all variable declared names @fullPath given for a py module,
    # returns suggested safe glb variable name by comparison checks of the py module
    # and this function's parameter @varName, returns wanted variable name or a
    # suggested smart glb variable name as str
    
    return stpu.ult_varname(varName, fullPath)
#______________________________________________________________________________________

def viewsource(fullPath):
    
    # UTILITY FUNCTION:
        
    # fullPath=str
    
    # prints to console the selected tqpt source file in a readable form:
    
    # ----- <variable name here>
    # Data:
    # <variables's data here>
    
    stpu.ult_show_tqpt_contents(fullPath)
#______________________________________________________________________________________

def viewkeys(fullPath):
    
    # UTILITY FUNCTION:
        
    # fullPath=str
    
    # prints to console a tpqt lock file contents from given tqpt source file path @fullPath
    
    stpu.ult_show_tpqt_contents(fullPath)

#______________________________________________________________________________________

def rev9build(slotsEncoding, sarsEncoding, multiStability, multiExtractable, applyObfuscation, contentDependent, staticShifting, sortingTolerate, counterIntuitiveVariables, superPalindromePointers, variablesLengthMuting, variablesTopographyLearning, globalVariablesFileExtension, globalVariablesLibraryName, buildFolderPath):
    
    # SPECIALIZED FUNCTION(r.e.v. re-inverted environment variables):
        
    # **all parameters of this function are in required; this specialized feature of staqtapp creates
    # a custom, instant callable global variables by file py library work, that may include bluetooth
    # protocol outer expressions for communication of other rev9 self-encoded modules builds**
    
    
    # REV9 BEGIN IN-BUILD ENTRY METHOD PARAMETERS:
                
        # (1)    <slotsEncoding=bool>,  applies abstract __slots__ py module class/function programming to the in-build global variables library rev9 decisions, this can effect performance and the overall built size of the library finalized
                
        # (2)    <sarsEncoding=bool>,  applies global sar variables type/global sar temple variables pointer type programming to finalized library build, see PySqTpp_Alpha or stpp module's sar functions descriptions usage
                
        # (3)    <multiStability=bool>,  applies complete finalized directional error checking within interface/class/functions to class/functions usage inner and/or outer; if False, does not apply it's code writting for more strict type error feedbacks
                
        # (4)    <multiExtractable=bool>,  applies approximate global variables data @is_variables_topography_learning, or if False makes choice of indicated performance clauses by any found constants in parameters changes
               # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
        # (5)    <applyObfuscation=bool>,  applies obfuscated variables naming to the in-build coding of the custom global variables library, does not obfuscate the finalized callable function names or their parameters
                
        # (6)    <contentDependent=bool>,  applies formulation strict observes to global variables data type interactions chosen; a basic read/write functional argument, however does effect overall performance in a finalized library build
               # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
        # (7)    <staticShifting=bool>,  applies any chosen shifting mechanics to the global variables file type format chosen via static bound declaring in coding builds; can take longer of it's decision build loops but more tighter coding finalized of library builds
                
        # (8)    <sortingTolerate=bool>,  applies & determines position inter-changes to global variables file formats, function direction flowings and read/write mapping of global variables scope communication to outer parameters options made
                
        # (9)    <counterIntuitiveVariables=bool>,  from above almost opposite but not, applies non-traditional means of callable function flows inner to global variables file format overall library builds; can make the function encoding difficult to read
                
        # (10)  <superPalindromePointers=bool>,  uses superbranching rotational variables mapping to the applied coding in-build resolves, in the global variables file read/write regions of library made; can effect reading performances if using __slots__
               # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
        # (11)  <variablesLengthMuting=bool>,  uses strict lock-offs to finalized functions' parameters usages built; the rev9 model determines this scope and can also effect performance timing and can make very unreadable function encodings also
                
        # (12)  <variablesTopographyLearning=bool>,  rev9 model build decision based exclusive only, joins property scopes of any found constants to combine/compress for other file types associated & written for any outer data gathering usage
               # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
        # (13)  <globalVariablesFileExtension: str>,  global variables source file extension to use for the finalized rev9 global variables library build
                
        # (14)  <globalVariablesLibraryName: str>,  overall library name of the global variables read/write library to be built by the rev9 model; rev9 build library model uses this to name on all other files, classes, functions, variables, slots and etc.
        
        # (15) <buildFolderPath: str>,  folder path where global variables rev9 type library will be built
        
    stpu.ult_call_rev9_service(slotsEncoding, sarsEncoding, multiStability, multiExtractable, applyObfuscation, contentDependent, staticShifting, sortingTolerate, counterIntuitiveVariables, superPalindromePointers, variablesLengthMuting, variablesTopographyLearning, globalVariablesFileExtension, globalVariablesLibraryName, buildFolderPath)
#______________________________________________________________________________________

#def test():
    
    #tqpt = ['/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test', '/storage/emulated/0/qpython/scripts3/staqtapp-test/staqtapp-test.tqpt',]
    
    #addvar("swTest1", "@qp(swTest1Data):", tqpt[0], tqpt[1])
    
    #lockvar('swTest1', 'someMethod1', tqpt[2])
        
    #viewkeys(tqpt[2])
    
    #renamevar("swTest1", "new_swTest1", tqpt[0], tqpt[1])
    
    #viewkeys(tqpt[2])
    
    #rev9build(True, True, True, False, False, True, True, False, False, True, True, False, "rttl", "RevTestLib", "/storage/emulated/0/rev9")
    
#______________________________________________________________________________________
    
#test()



