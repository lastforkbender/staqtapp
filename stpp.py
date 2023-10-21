# Code File: StaqTapp-1.01 [stpp.py] StaqTapp main functional calls module




# Staqtapp 1.02.073

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


from PySqTpp_Parser import TqptParser
from collections import deque
from stps import extrloadsarremap
from stpu import ult_varname, ult_show_tqpt_contents
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________

# STAQTAPP'S  PILOT - stpp.methods()


# [.makesource] - creates a new empty staqtapp tqpt variables source file

# [.addvar] - writes new variable and it's data to chosen staqtapp tqpt source file

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


# UTILITY:


# [.scanvar] - searches a py module for potential global variable conflicts with a provided
# global variable name, returns suggested smart str global variable name or wanted var
# name as given; does not use regex and very accurate scan of all classes, functions and
# variables names, including all variable naming inside any function's parameters

# [.viewsource] - prints a tqpt variables source file's contents to console

#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
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

def sar_remap(isPrmExc, catPin, folderPath, fileName):
        
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

def scanvar(varName, fullPath):
    
    # UTILITY FUNCTION:
        
    # varName=str, fullPath=str
    
    # scans/search of entire py module's text - function names, function parameters,
    # class names and all variable declared names @fullPath given for a py module,
    # returns suggested safe glb variable name by comparison checks of the py module
    # and this function's parameter @varName, returns wanted variable name or a
    # suggested smart glb variable name as str
    
    return ult_varname(varName, fullPath)
#______________________________________________________________________________________

def viewsource(fullPath):
    
    # UTILITY FUNCTION:
        
    # fullPath=str
    
    # prints to console the selected tqpt source file in readable form:
    
    # ----- <variable name here>
    # Data:
    # <variables's data here>
    
    ult_show_tqpt_contents(fullPath)
#______________________________________________________________________________________

def test():
    
    #newTqptParser = TqptParser()
    
    #makesource(False, False, False, '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #addvar("vrnm_1000", "@qp(7.8,9.8,10.000001,turtle7):", '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #dequeTest = loadvar_deque(False, "vrnm_1000", '/storage/emulated/0/qpython/scripts3/staqtapp-test', "staqtapp-test2")
    
    #lst = findvar(True, 'variable99', '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #addvar_sar("tiger", "@qp(9000):", '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #changevar('variableDequeTest4001', '@qp(y+z(i/r)c+1, 9.99999999,no errors please):', '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test')
    
    #loadsar_remap(False, "tiger", '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #scanvar("someVar", '/storage/emulated/0/qpython/scripts3/ynos.py')
    
    #tmpLst = ['variableDequeTest1', 'variableDequeTest2', 'variableDequeTest3']
    
    #rtrnStr = loadvar_str(tmpLst, '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test')
    
    #viewsource("/storage/emulated/0/qpython/scripts3/staqtapp-test/staqtapp-test2.tqpt")
    
    #print(rtrnStr)
    
#______________________________________________________________________________________
    
#test()



