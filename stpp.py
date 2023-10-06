# Code File: StaqTapp-1.01 [stpp.py] StaqTapp main functional calls module




# Staqtapp 1.01.493

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(at)gmail


from PySqTpp_Parser import TqptParser
from collections import deque


#______________________________________________________________________________________



#______________________________________________________________________________________



#______________________________________________________________________________________

def makesource(isStatic, isMakeFolder, isEraseSource, folderPath, fileName):
    
    # isMakeFolder=bool, isEraseSource=bool, folderPath=str, fileName=str
    
    # **this function only makes a new folder when isMakeFolder=true and isEraseSource
    # ==false for the current working module's path found**
    	
    	# if tqpt source file is made as a static read, no write, the setting for this
    	# is ||||:* at top of file or ||||:_ for non-static read/write tqpt files
    	
    	
    	# Boolean arguments use for <makesource> :)
    
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
                if newTqptParser.check_parameter_string(False, fileName):
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
                if newTqptParser.check_parameter_string(False, fileName):
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
                if newTqptParser.check_parameter_string(False, fileName):
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
        if newTqptParser.check_parameter_string(True, varName):
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

def loadvar_deque(isNumbers, varName, folderPath, fileName):
    
    # isNumbers=bool, varName=str, folderPath=str, fileName=str
    
    # this function returns decimal or int for numbers in a array or else, nested
    # variable data @qp( tagging is not yet supported of this version, see addvar
    	    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(True, varName):
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

def findvar(allSources, varName, folderPath, fileName):
    
    # allSources=bool, varName=str, folderPath=str, fileName=str
    
    # parameter allSources of True, then finds all tqpt files of given folderPath
    # and returns a list type in format 'fullpath:varname:linenumber' str @indices
    # if variable find(s) else returns a empty list; allSources=False returns true
    # or false for variable found or not found from given dir & file name combined
    
    rslt = None
    
    newTqptParser = TqptParser()
    if len(folderPath) > 0 and len(fileName) > 0:
        if newTqptParser.check_parameter_string(False, fileName):
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

def addvar_sar(catPin, varData, folderPath, fileName):
    
    # closeAsStatic=bool, catPin=str, varData=str, folderPath=str, fileName=str
    
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
        if newTqptParser.check_parameter_string(False, fileName):
            rslt = newTqptParser.self_assign_variable_name(closeAsStatic, catPin, varData, folderPath, fileName)
            if rslt == -1:
                raise Exception("staqtapp<addvar_sar> invalid folderpath @" + folderPath)
            elif rslt == -2:
                raise Exception("staqtapp<addvar_sar> variables source file '" + fileName + ".tqpt' was not found @" + folderPath)
            elif rslt == -3:
                raise Exception("staqtapp<addvar_sar> newline chars not allowed in variable sources")
            elif rslt == -4:
                raise Exception("staqtapp<addvar_sar> no proper data declare(s) '@qp(data):' found")
            elif rslt == -5:
                raise Exception("staqtapp<addvar_sar> missing data declare closing '):' ")
            elif rslt == -6:
                raise Exception("staqtapp<addvar_sar> invalid category pin, allowed chars _ aA-zZ 0-9")
        else:
            raise Exception("staqtapp<addvar_sar> invalid filename, allowed chars ._- aA-zZ 0-9")
    else:
        raise Exception("staqtapp<addvar_sar> null folderpath and/or null filename")
    



#______________________________________________________________________________________

def test():
    
    #newTqptParser = TqptParser()
    
    #makesource(False, False, False, '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #addvar("variable99", "@qp(99999999999999999999999):", '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #dequeTest = loadvar_deque(False, "variableDequeTest4001", '/storage/emulated/0/qpython/scripts3/staqtapp-test', "staqtapp-test")
    
    #lst = findvar(True, 'variable1', '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    addvar_sar(False, "sarTest2", "@qp(---Solely, passwords are unsecure):@qp(A great password begins with kat:):", '/storage/emulated/0/qpython/scripts3/staqtapp-test', 'staqtapp-test2')
    
    #print(testLst)
    
#______________________________________________________________________________________
    
test()







































