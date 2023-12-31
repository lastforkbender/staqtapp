# Code File: StaqTapp-1.02 [PySqTpp_Parser.py] main functions use


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


import PySqTpp_Interface

from collections import deque
from decimal import Decimal as dcml
from random import randrange as rrng
from datetime import date as dttm

import mmap
import glob
import stps
import sys
import os
import re
#______________________________________________________________________________________

class TqptParser(PySqTpp_Interface.PySqTppInterface):
    # - settled functions for .tqpt variables file -
#______________________________________________________________________________________

    def make_variables_source(self, is_static: bool, make_dir: bool, overwrite_source: bool, dir_path: str, make_source_name: str) -> int:
        # @override PySqTppInterface.make_variables_source()
        
        # FUNCTION RETURN-CODES
            
        # ****if both make_dir and overwrite_source true then seeks overwrite****
        
        # --------------------------make_dir==true--------------------------------
        # return 1  : new folder new variables source file to current module's dir
        # return -1 : both folder & variables source file already there...
        # return 2  : folder already there however made new variables source file
        # return -2 : current module's directory is of no length..........
        
        # -------------------overwrite_source==true|false-------------------------
        # return 3  : overwrite=false, dir exist, made new variables source file
        # return -3 : overwrite=false, variables source file already exist...
        # return 4  : overwrite=true, file exist or not, overwrite was done
        # return -4 : overwrite=true|false, dir path given is not there...
        
        try:
        
            # get directory path of current module's use
            currMdlDir = os.path.dirname(os.path.abspath(__file__)) + '/'
        
            if make_dir==True and overwrite_source==False:
            
                if len(currMdlDir) > 0:
                    # check if to be made folder is not already there
                    if not os.path.isdir(currMdlDir + make_source_name):
                        # make new folder from source file name given and new
                        # empty variables source file a same name
                        os.makedirs(currMdlDir + make_source_name)
                        if not is_static:
                            with open(currMdlDir + make_source_name + '/' + make_source_name + '.tqpt', mode='w') as vsa: vsa.write('<RESERVED_DO_NOT_EDIT=||||:_>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                            return 1
                        else:
                            with open(currMdlDir + make_source_name + '/' + make_source_name + '.tqpt', mode='w') as vsa: vsa.write('<RESERVED_DO_NOT_EDIT=||||:*>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                            return 1
                    else:
                        # folder is already there... is source file also there?
                        if not os.path.isfile(currMdlDir + make_source_name + '/' + make_source_name + '.tqpt'):
                            # false, make the new empty variables source file
                            if not is_static:
                                with open(currMdlDir + make_source_name + '/' + make_source_name + '.tqpt', mode='w') as vsb: vsb.write('<RESERVED_DO_NOT_EDIT=||||:_>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 2
                            else:
                                with open(currMdlDir + make_source_name + '/' + make_source_name + '.tqpt', mode='w') as vsb: vsb.write('<RESERVED_DO_NOT_EDIT=||||:*>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 2
                        else:
                            # ! both folder and variables source file already exist !
                            return -1
                else:
                    # ! current module's directory is of no length !
                    return -2
            else:
                # either make new variables source file with given directory path
                # or the overwrite existing variables source file to blank
                if not overwrite_source:
                    # does variables source file already exist?
                    if os.path.isfile(dir_path + '/' + make_source_name + '.tqpt'):
                        # ! overwrite = false and the variables source file exist !
                        return -3
                    else:
                        # create a new variables source file, first check dir exist
                        if os.path.isdir(dir_path):
                            if not is_static:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vsc: vsc.write('<RESERVED_DO_NOT_EDIT=||||:_>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 3
                            else:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vsc: vsc.write('<RESERVED_DO_NOT_EDIT=||||:*>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 3
                        else:
                            # ! dir_path is not found !
                            return -4
                else:
                    # checking if dir path is there, overwrite=true
                    if os.path.isdir(dir_path):
                        # overwrite=true, does variables source file exist? regardless
                        # makes empty variables source file anyways via overwrite call
                        if os.path.isfile(dir_path + '/' + make_source_name + '.tqpt'):
                            # (open variables source file to overwrite to empty)
                            if not is_static:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vsd: vsd.write('<RESERVED_DO_NOT_EDIT=||||:_>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 4
                            else:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vsd: vsd.write('<RESERVED_DO_NOT_EDIT=||||:*>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 4
                        else:
                            if not is_static:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vse: vse.write('<RESERVED_DO_NOT_EDIT=||||:_>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 4
                            else:
                                with open(dir_path + '/' + make_source_name + '.tqpt', mode='w') as vse: vse.write('<RESERVED_DO_NOT_EDIT=||||:*>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')
                                return 4
                    else:
                        # ! dir path given is not there !
                        return -4
                        
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________
        
    def add_variables_source(self, var_name: str, var_data: str, dir_path: str, source_name: str) -> int:
        # @override PySqTppInterface.add_variables_source()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return 1  : finished write to tqpt source file
        # return -1 : directory path given is not valid
        # return -2 : filename given is not valid
        # return -3 : variable name invalid, already exist in tqpt source file
        # return -4 : no write to a static set variables tqpt source file
        # return -5 : invalid settings to tqpt source file, not read
        # return -6 : newline char found in variable's data
        # return -7 : no proper @qp(...): data declaring found
        # return -8 : missing closing ): of a data declare
        
        otRslt = None
        nrRslt = None
        rslt = None
        
        try:
            
            if os.path.isdir(dir_path):
                # valid folder directory, is variables source filename correct?
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    # both folder path & source file exist, search if the
                    # given var_name is already in the .tqpt file or not
                    newTqptParser = TqptParser()
                    # check variable data of proper formatting
                    otRslt = newTqptParser.char_regularity(True, False, 'avs', var_data)
                    if otRslt == 2:
                        rslt = newTqptParser.tqpt_map(True, False, 'avs', False, var_name, '', dir_path, source_name)
                        if rslt == 2:
                            # add new global variable to tqpt source file, variable name was not found
                            nrRslt == newTqptParser.tqpt_map(False, True, 'avs', False, var_name, var_data, dir_path, source_name)
                            if nrRslt == -1:
                                # source file is static locked variables, no write allowed
                                return -4
                            elif nrRslt == -2:
                                # bad settings to tqpt file, no read
                                return -5
                        elif rslt == 1:
                            # variable already exist, no overwrite to this function operation
                            return -3
                    elif otRslt == -1:
                        # newline char found
                        return -6
                    elif otRslt == -3:
                        # no @qp tags found
                        return -7
                    elif otRslt == -4:
                        # missing @qp closing of data tag
                        return -8
                else:
                    # source filename is not valid from a valid directory
                    return -2
            else:
                # invalid directory
                return -1
            
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def change_variable_name(self, var_name: str, new_var_name: str, dir_path: str, source_name: str) -> int:
        # @override PySqTppInterface.change_variable_name()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid tqpt folder path
        # return -2  : invalid tqpt file name
        # return -3  : tqpt source file is static locked
        # return -4  : @var_name not found
        # return -5  : @new_var_name is invalid chars
        
        src = None
        
        try:
            if os.path.isdir(dir_path):
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    newTqptParser = TqptParser()
                    if newTqptParser.check_tqpt_settings(True, dir_path + '/' + source_name + '.tqpt') == -1:
                        with open(dir_path + '/' + source_name + '.tqpt', mode='r') as fileObjCvn:
                            with mmap.mmap(fileObjCvn.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjCvn:
                                src = mmapObjCvn.read()
                                mmapObjCvn.close()
                            mmapObjCvn = None
                        if src.find(b'\n<' + str.encode(var_name) + b'=') > -1:
                            if newTqptParser.check_parameter_string(True, new_var_name, False) == True:
                                with open(dir_path + '/' + source_name + '.tqpt', 'wb') as fCvnWrt:
                                    fCvnWrt.write(src.replace(b'\n<' + str.encode(var_name) + b'=', b'\n<' + str.encode(new_var_name) + b'='))
                                    fCvnWrt.close()
                                fCvnWrt = None
                                # change tpqt lock file if attached to this now changed tqpt source
                                try:
                                    with open(dir_path + '/' + source_name + '.tpqt', 'r') as fCvnPq:
                                        src = fCvnPq.read()
                                        fCvnPq.close()
                                    fCvnPq = None
                                    if src.find('<:' + var_name + '=') > -1:
                                        with open(dir_path + '/' + source_name + '.tpqt', 'w') as fCvnPqWrt:
                                            fCvnPqWrt.write(src.replace('<:' + var_name + '=', '<:' + new_var_name + '='))
                                            fCvnPqWrt.close()
                                        fCvnPqWrt = None
                                except Exception:
                                    pass
                            else:
                                return -5
                        else:
                            # variable name not found
                            return -4
                    else:
                        # tqpt source is static locked variables source
                        return -3
                else:
                    return -2
            else:
                return -1
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def update_variables_source(self, var_name: str, var_data: str, dir_path: str, source_name: str) -> int:
        # @override PySqTppInterface.update_variables_source()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid directory path
        # return -2  : invalid tqpt variables source file name
        # return -3  : newline char found
        # return -4  : no proper @qp data tagging found
        # return -5  : missing ): closing for @qp( tag
        # return -6  : variable name was not found
        
        rslt = None
        otRslt = None
        nrRslt = None
        ptrnStr = None
        joinStr = None
        
        try:
            if os.path.isdir(dir_path):
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    newTqptParser = TqptParser()
                    # is the new variable data of proper formatting?
                    otRslt = newTqptParser.char_regularity(True, False, 'uvs', var_data)
                    if otRslt == 2:
                        ptrnStr = re.compile(rb'<'+re.escape(str.encode(var_name))+rb'=')
                        with open(dir_path + '/' + source_name + '.tqpt', mode='r') as fileObjUv:
                            with mmap.mmap(fileObjUv.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjUv:
                                try:
                                    nrRslt = re.search(rb'<'+re.escape(str.encode(var_name))+rb'=', mmapObjUv.read()).span(0)
                                except Exception:
                                    # .span() tuple error throw, pattern was not found
                                    return -6
                                rslt = mmapObjUv.find(b'\n', nrRslt[1])
                                if rslt != -1:
                                    ptrnStr = mmapObjUv[0:nrRslt[0]-1]
                                    joinStr = mmapObjUv[rslt:len(mmapObjUv)]
                                else:
                                    return -6
                                mmapObjUv.close()
                            mmapObjUv = None
                        with open(dir_path + '/' + source_name + '.tqpt', 'wb') as fObjWrtVn:
                            fObjWrtVn.write(ptrnStr + b'\n<' + str.encode(var_name) + b'=' + str.encode(var_data) + b'>' + joinStr)
                            fObjWrtVn.close()
                        fObjWrtVn = None
                    elif otRslt == -1:
                        # newline char found
                        return -3
                    elif otRslt == -3:
                        # no @qp tags found
                        return -4
                    elif otRslt == -4:
                        # missing @qp closing of data tag
                        return -5
                else:
                    return -2
            else:
                return -1
            
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def self_assign_variable_name(self, prepin_cat_dsg: str, var_data: str, dir_path: str, source_name: str) -> int:
        # @override PySqTppInterface.self_assign_variable_name()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid folder path
        # return -2  : invalid file name
        # return -3  : found newline char in variable data
        # return -4  : no proper @qp(...) tag formatting found
        # return -5  : missing closing ): for variable data @qp(
        # return -6  : invalid category pin chars
        
        otRslt = None
        nrRslt = None
        fndCms = None
        vrNm = None
        
        try:
            if os.path.isdir(dir_path):
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    newTqptParser = TqptParser()
                    # parameter data, variable's data proper @qp(... tag format(s)?
                    otRslt = newTqptParser.char_regularity(True, False, 'savn', var_data)
                    if otRslt == 2:
                        # checks out, no comma use found in variable data
                        fndCms = False
                    elif otRslt == 22:
                        # found comma use in variable data
                        fndCms = True
                    elif otRslt == -1:
                        return -3
                    elif otRslt == -3:
                        return -4
                    elif otRslt == -4:
                        return -5
                    # check prepin_cat_dsg variable name id is of valid chars
                    if newTqptParser.check_parameter_string(True, prepin_cat_dsg, False):
                        # parameter checks all ok, build the random variable name, p_fnc_nnnnnnnnnn_b
                        syncLst = [str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10)), str(rrng(0,10))]
                        vrNm = prepin_cat_dsg.replace("_", "") + "_sar_" + ''.join(newTqptParser.rand_shuffle(syncLst)) + "_"
                        if fndCms == True:
                            vrNm += '1'
                        else:
                            vrNm += '0'
                        # add variable and variable's data to the chosen tqpt variable source file
                        nrRslt = newTqptParser.tqpt_map(False, True, 'sar', False, vrNm, var_data, dir_path, source_name)
                        # add collect new sar data
                        stps.newsaradd('savn', vrNm, var_data, dir_path, source_name)
                    else:
                        return -6
                else:
                    return -2
            else:
                return -1
       
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def load_variables_source_str(self, var_name, dir_path, source_name):
        # @override PySqTppInterface.load_variables_source_str()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1   : invalid folder path
        # return -2   : invalid filename path
        # return -3   : variable name was not found @dir_path/source_name
        # return -4   : newline chars found........
        # return -5   : false all numbers...
        # return -6   : missing @qp(...): taggings or invalid
        # return -7   : missing closing ): of qp( data declare
        # return -8   : non-supported variable type @var_name
        # return -9   : no finds from a variable list get
        # return -10 : no valid data return from result list finds
        
        rslt = None
        fncRtrn = None
        
        try:
            if os.path.isdir(dir_path):
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    newTqptParser = TqptParser()
                    # check is a str type or a list type
                    if isinstance(var_name, str) == True:
                        rslt = newTqptParser.tqpt_map(True, False, 'lvss', False, var_name, None, dir_path, source_name)
                        if rslt == '...':
                            return -3
                        else:
                            fncRtrn = newTqptParser.char_regularity(False, False, 'lvss', rslt)
                            if fncRtrn == -1:
                                return -4
                            elif fncRtrn == -2:
                                return -5
                            elif fncRtrn == -3:
                                return -6
                            elif fncRtrn == -4:
                                return -7
                            else:
                                if len(fncRtrn) > 1:
                                    return fncRtrn
                                else:
                                    return fncRtrn[0]
                    elif isinstance(var_name, list) == True:
                        # is a variables names list, get all variables' data lines in a list, lvss_lr call
                        rslt = newTqptParser.tqpt_map(True, False, 'lvss_lr', False, var_name, None, dir_path, source_name)
                        if rslt[0] == "_@qp!(!_!!_!)!":
                            # no variables in the list we're found!
                            return -9
                        else:
                            rtrnLst = []
                            lenLst = len(rslt)
                            for vrn in range(lenLst):
                                fncRtrn = newTqptParser.char_regularity(False, False, 'lvss', rslt[vrn])
                                if isinstance(fncRtrn, list) == True and len(fncRtrn) > 0:
                                    rtrnLst.append(fncRtrn)
                            lenLst = len(rtrnLst)
                            if lenLst == 0:
                                return -10
                            else:
                                if lenLst > 1:
                                    return rtrnLst
                                else:
                                    return rtrnLst[0]
                    else:
                        return -8
                else:
                    # invalid filename
                    return -2
            else:
                # no valid directory folder
                return -1
                
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def load_variables_source_deque(self, is_numbers: bool, var_name: str, dir_path: str, source_name: str):
        # @override PySqTppInterface.load_variables_source_list()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1 : invalid folder path given
        # return -2 : invalid filename
        # return -3 : invalid variable name, not found
        # return -4 : has newline chars
        # return -5 : false for is_all_numbers
        # return -6 : no found @qp data declare tags
        # return -7 : missing closing qp ): ending
        
        rslt = None
        fncRtrn = None
        
        try:
        
            if os.path.isdir(dir_path):
                # valid directory
                if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                    # valid .tqpt variables source file
                    newTqptParser = TqptParser()
                    rslt = newTqptParser.tqpt_map(True, False, 'lvsd', False, var_name, None, dir_path, source_name)
                    if rslt == '...':
                        # variable name was not found in the tqpt source file
                        return -3
                    else:
                        # check variable's data is proper format for a tqpt source file,
                        # parse it and return the deque list as is
                        fncRtrn = newTqptParser.char_regularity(False, is_numbers, 'lvsd', rslt)
                        if fncRtrn == -1:
                            return -4
                        elif fncRtrn == -2:
                            return -5
                        elif fncRtrn == -3:
                            return -6
                        elif fncRtrn == -4:
                            return -7
                        else:
                            return fncRtrn
                else:
                    # invalid file name
                    return -2
            else:
                # invalid folder path
                return -1
                
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def search_variable(self, all_tqpt_sources: bool, var_name: str, dir_path: str, source_name: str):
        # @override PySqTppInterface.search_variable()
        
        # FUNCTION RETURN-CODES
            
        # -------------------all_tqpt_sources=False-------------------------------
        # return True  : found variable at given path & tqpt file name
        # return False : no found variable at given path & tqpt file name
        
        # -------------------all_tqpt_sources=True--------------------------------
        # return -1 : invalid directory path
        # return -2 : variable source file not found
        # return -3 : no found tqpt files for dir_path
        
        ptrnStr = None
        lnNmr = None
        dqLst = []
        
        try:
            if os.path.isdir(dir_path):
                if all_tqpt_sources == True:
                    # source_name is ignored as a specific parameter string for tqpt file
                    # get string list of all tqpt source files at the given directory
                    flLst = glob.glob(dir_path + '/' + "*.tqpt")
                    if len(flLst) > 0:
                        ptrnStr = str.encode('<'+var_name+'=')
                        for fl in range(len(flLst)):
                            lnNmr = 0
                            with open(flLst[fl], mode='r+b') as mFlObj:
                                with mmap.mmap(mFlObj.fileno(), length=0, prot=mmap.PROT_READ) as mMpObj:
                                    for fLn in iter(mMpObj.readline, b''):
                                        lnNmr+=1
                                        # found; add dir, var name and line number :via
                                        if fLn.find(ptrnStr) != -1:
                                            dqLst.append(flLst[fl] + ':' + var_name + ':' + str(lnNmr))
                                            break
                                    mMpObj.close()
                                mMpObj = None
                        return dqLst
                    else:
                        # no found tqpt source files........
                        return -3
                else:
                    # search on given file name only
                    if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                        newTqptParser = TqptParser()
                        rslt = newTqptParser.tqpt_map(True, False, 'sv', False, var_name, '', dir_path, source_name)
                        if rslt == 1:
                            return True
                        else:
                            return False
                    else:
                        # tqpt source file is not found
                        return -2
            else:
                # invalid folder path
                return -1
                
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def tqpt_map(self, is_read, is_write, dsg_fnc, is_overwrite, glb_var, glb_var_data, folder_path, tqpt_name):
        # @override PySqTppInterface.tqpt_map()
    
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1 : tried write on a static set tqpt source file
        # return 1  : variable was found in tqpt source file
        # return 2  : variable not found in tqpt source file
        # return -2 : is bad tqpt file settings...
        # return 3  : finished write to tqpt source file
    
        tqptLn = ''
        ptrnStr = ''
        lnsCnt = None
        nrRslt = None
        rslt = None
        vrblFnd = False
        
        # -------- READ TQPT VARIABLES SOURCE FILES -------------------------------
        if is_read == True and is_write == False:
            if dsg_fnc == 'lvss_lr':
                # - OPTIMIZED -
                dtLst = []
                with open(folder_path + '/' + tqpt_name + '.tqpt', mode='r') as fObjLlr:
                    with mmap.mmap(fObjLlr.fileno(), length=0, access=mmap.ACCESS_READ) as mObjLlr:
                        lnsCnt = len(glb_var)
                        nrlStr = mObjLlr.read()
                        for lr in range(lnsCnt):
                            try:
                                nrRslt = re.search(rb'<'+re.escape(str.encode(glb_var[lr]))+rb'=', nrlStr).span(0)
                            except Exception as e:
                                nrRslt = None
                            if nrRslt != None:
                                vrblFnd = True
                                rslt = mObjLlr.find(b'\n', nrRslt[1])
                                if rslt != -1:
                                    tqptLn = mObjLlr[nrRslt[1]:rslt-1]
                                    dtLst.append(bytes.decode(tqptLn, 'utf-8'))
                        mObjLlr.close()
                    mObjLlr = None
                if vrblFnd == True:
                    return dtLst
                else:
                    dtLst.append('_@qp!(!_!!_!)!')
                    return dtLst
            #--------------------------------------------------------------------------------------------------------------------------------------------
            elif dsg_fnc == 'avs' or dsg_fnc == "uvs":
                ptrnStr = re.compile(rb'<'+re.escape(str.encode(glb_var))+rb'=')
                with open(folder_path + '/' + tqpt_name + '.tqpt', mode='r') as fileObjTm1:
                    with mmap.mmap(fileObjTm1.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjTm1:
                        if re.search(ptrnStr, mmapObjTm1.read()):
                            vrblFnd = True
                        mmapObjTm1.close()
                    mmapObjTm1 = None
                    if vrblFnd == False:
                        return 2
                    else:
                        return 1
            #--------------------------------------------------------------------------------------------------------------------------------------------
            elif dsg_fnc == 'lvsd' or dsg_fnc == 'lvss' or dsg_fnc == 'sv':
                with open(folder_path + '/' + tqpt_name + '.tqpt', mode='r') as fileObjPf:
                    with mmap.mmap(fileObjPf.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjPf:
                        try:
                            nrRslt = re.search(rb'<'+re.escape(str.encode(glb_var))+rb'=', mmapObjPf.read()).span(0)
                        except Exception:
                            nrRslt = None
                        if nrRslt != None:
                            vrblFnd = True
                            if dsg_fnc == 'lvss' or dsg_fnc == 'lvsd':
                                rslt = mmapObjPf.find(b'\n', nrRslt[1])
                            else:
                                rslt = 1
                            if rslt != -1:
                                if dsg_fnc == 'lvss' or dsg_fnc == 'lvsd':
                                    tqptLn = mmapObjPf[nrRslt[1]:rslt-1]
                            else:
                                vrblFnd = False
                        mmapObjPf.close()
                    mmapObjPf = None
                    if vrblFnd == True:
                        if dsg_fnc == 'lvss' or dsg_fnc == 'lvsd':
                            return bytes.decode(tqptLn, 'utf-8')
                        else:
                            return 1
                    else:
                        if dsg_fnc == 'lvss' or dsg_fnc == 'lvsd':
                            return '...'
                        else:
                            return -1
                                   
        # -------- WRITE TQPT VARIABLES SOURCE FILES -------------------------------      
        elif is_read == False and is_write == True:
            # is write to .tqpt source file, check first if the source file
            # can be written to, e.g. is not a static made .tqpt source file
            newTqptParser = TqptParser()
            if dsg_fnc != 'sar':
                rslt = newTqptParser.check_tqpt_settings(True, folder_path + '/' + tqpt_name + ".tqpt")
            else:
                rslt = -1
            if rslt == -1:
                # not a static locked variables source file, get/write variables & datas
                if dsg_fnc == 'avs' or dsg_fnc == 'sar':
                    with open(folder_path + '/' + tqpt_name + '.tqpt', 'r+b') as fileObjTm2:
                        with mmap.mmap(fileObjTm2.fileno(), length=0, prot=mmap.PROT_READ) as mmapObjTm2:
                            tqptLn = mmapObjTm2.read()
                            mmapObjTm2.close()
                        mmapObjTm2 = None
                    ptrnStr = [tqptLn.replace(b"\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!",b""), str.encode('\n<' + glb_var + '=' + glb_var_data + '>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')]
                    with open(folder_path + '/' + tqpt_name + '.tqpt', 'wb') as fileObjTm2X:
                        fileObjTm2X.write(b''.join(ptrnStr))
                        fileObjTm2X.close()
                    fileObjTm2X = None
                    return 3
            elif rslt == 1:
                # no write, is a static locked .tqpt variables source!
                return -1
            elif rslt == -2:
                # no readable settings to the .tqpt source file...
                return -2
#______________________________________________________________________________________

    def check_tqpt_settings(self, is_static: bool, full_path: str) -> int:
        # @override PySqTppInterface.check_tqpt_settings()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return 1  : true for the setting in question
        # return -1 : false for the setting in question
        # return -2 : empty settings line from tqpt source file read
        
        tqptLn = None
                
        with open(full_path, 'r') as fileObjCts:
            # get the first reserved .tqpt file settings line, line 1
            tqptLn = fileObjCts.readline()
            fileObjCts.close()
            fileObjCts = None
            if len(tqptLn) > 0:
                if is_static:
                    # non-static tqpt file setting is =||||:_
                    if tqptLn.find('=||||:*') > -1:
                        return 1
                    else:
                        return -1
            else:
                # not a legit staqtapp .tqpt variables source file
                return -2
#______________________________________________________________________________________

    def check_parameter_string(self, is_variable, parameter, is_list):
        # @override PySqTppInterface.check_parameter_string()
        
        # check if a string parameter is of valid chars
        try:
            if is_variable == True:
                alwdChrsVars = set("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                if is_list == False:
                    if set(parameter).issubset(alwdChrsVars) == True:
                        return True
                    else:
                        return False
                else:
                    lenLst = len(parameter)
                    for prm in range(lenLst):
                        if set(parameter[prm]).issubset(alwdChrsVars) == False:
                            return False
                    return True
            else:
                alwdChrsFlnm = set("._-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                if set(parameter).issubset(alwdChrsFlnm):
                    return True
                else:
                    return False
        except Exception as e:
            print("staqtapp error: ",e)
#______________________________________________________________________________________

    def char_regularity(self, is_read_only: bool, is_all_numbers: bool, calling_function: str, source: str):
        # @override PySqTppInterface.char_regularity()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return  1   : yah is all numbers
        # return -1   : new line in data is not allowed of staqtapp global variables
        # return  2   : is proper @qp(...): char staqtapp tag(s) observe find(s)
        # return  22 : proper tag check return with found comma use in variable data
        # return -2   : false check for is_all_numbers however
        # return -3   : no proper @qp(...): variables' data tags found
        # return -4   : missing a closing ): for data declare @qp(
        
        dqRtn = deque()
        lstRtn = []
        dqLst = None
        qdLst = None
        cptDatStr = ''
        qpPrvChr = None
        nmbrChrs = set('.-, 0123456789')
        srcLen = len(source)
        srcIdx = 0
        ttlQp = 0
        qpCnt = None
        qpPrgPrhL = False
        qpPrgPrhR = False
        qpPrgRstT = False
        qpOpnVdSw = False
        qpCmsVdSw = False
        qpCmrFncr = False
        qpDcmVdSw = False
        qpNmrVdSw = False
        qpNmrDcSw = False
        
        for currChr in source:
            srcIdx+=1
            # @qp( checks """"""""""""""""""""""""""""""""""""""""""""""""""""""
            if qpOpnVdSw == False:
                if qpPrgRstT == True:
                    qpPrgRstT = False
                    qpPrgPrhL = False
                    qpPrgPrhR = False
                if currChr == '@':
                    qpPrvChr = currChr
                elif qpPrvChr == '@' and currChr == 'q':
                    qpPrvChr = currChr
                elif qpPrvChr == 'q' and currChr == 'p':
                    qpPrvChr = currChr
                elif qpPrvChr == 'p' and currChr == '(':
                    qpPrgPrhL = True
                    qpOpnVdSw = True
            # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            else:
                if currChr == '.':
                    qpDcmVdSw = True
                    if is_read_only == False:
                        cptDatStr += currChr
                elif currChr == ',':
                    qpCmsVdSw = True
                    if is_read_only == False:
                        cptDatStr += currChr
                elif currChr == '\n':
                    # no newline chars allowed, exit out
                    return -1
                elif currChr == ')':
                    # end of @qp( tag for a variable's data?):?
                    qpPrvChr = currChr
                elif currChr == ':' and qpPrvChr == ')':
                    # is end of a tqpt source file data declare
                    ttlQp+=1
                    qpPrgPrhR = True
                    qpOpnVdSw = False
                    if is_read_only == False and is_all_numbers == True:
                        if qpCmsVdSw == True and qpDcmVdSw == True:
                            dqLst = cptDatStr.split(',')
                            if calling_function == 'lvsd':
                                qdLst = [dcml(x.strip(' ')) for x in dqLst]
                                dqRtn.append(qdLst)
                            elif calling_function == 'lvss':
                                lstRtn.append(dqLst)
                        elif qpCmsVdSw == False and qpDcmVdSw == True:
                            if calling_function == 'lvsd':
                                dqRtn.append(dcml(cptDatStr.strip(' ')))
                            elif calling_function == 'lvss':
                                lstRtn.append(cptDatStr)
                        elif qpCmsVdSw == True and qpDcmVdSw == False:
                            dqLst = cptDatStr.split(',')
                            if calling_function == 'lvsd':
                                qdLst = [int(x.strip(' ')) for x in dqLst]
                                dqRtn.append(qdLst)
                            elif calling_function == 'lvss':
                                lstRtn.append(dqLst)
                        elif qpCmsVdSw == False and qpDcmVdSw == False:
                            if calling_function == 'lvsd':
                                dqRtn.append(int(cptDatStr.strip(' ')))
                            elif calling_function == 'lvss':
                                lstRtn.append(cptDatStr)
                    elif is_read_only == False and is_all_numbers == False:
                        if qpCmsVdSw == True:
                            # has comma adding to data declare string
                            dqLst = cptDatStr.split(',')
                            for ds in range(len(dqLst)):
                                qpNmrVdSw = False
                                qpNmrDcSw = False
                                for dChr in dqLst[ds]:
                                    if set(dChr).issubset(nmbrChrs) == True:
                                        qpNmrVdSw = True
                                    else:
                                        qpNmrVdSw = False
                                        break
                                    if dChr == '.':
                                        qpNmrDcSw = True
                                if qpNmrVdSw == True and qpNmrDcSw == True:
                                    if calling_function == 'lvsd':
                                        dqRtn.append(dcml(dqLst[ds].strip(' ')))
                                    elif calling_function == 'lvss':
                                        lstRtn.append(dqLst[ds])
                                elif qpNmrVdSw == True and qpNmrDcSw == False:
                                    if calling_function == 'lvsd':
                                        dqRtn.append(int(dqLst[ds].strip(' ')))
                                    elif calling_function == 'lvss':
                                        lstRtn.append(dqLst[ds])
                                elif qpNmrVdSw == False:
                                    if calling_function == 'lvsd':
                                        dqRtn.append(dqLst[ds])
                                    elif calling_function == 'lvss':
                                        lstRtn.append(dqLst[ds])
                        else:
                            # has no comma addings to data declare string
                            qpNmrVdSw = False
                            qpNmrDcSw = False
                            for sChr in cptDatStr:
                                if set(sChr).issubset(nmbrChrs) == True:
                                    qpNmrVdSw = True
                                else:
                                    qpNmrVdSw = False
                                    break
                                if sChr == '.':
                                    qpNmrDcSw = True
                            if qpNmrVdSw == True and qpNmrDcSw == True:
                                if calling_function == 'lvsd':
                                    dqRtn.append(dcml(cptDatStr.strip(' ')))
                                elif calling_function == 'lvss':
                                    lstRtn.append(cptDatStr)
                            elif qpNmrVdSw == True and qpNmrDcSw == False:
                                if calling_function == 'lvsd':
                                    dqRtn.append(int(cptDatStr.strip(' ')))
                                elif calling_function == 'lvss':
                                    lstRtn.append(cptDatStr)
                            elif qpNmrVdSw == False:
                                if calling_function == 'lvsd':
                                    dqRtn.append(cptDatStr)
                                elif calling_function == 'lvss':
                                    lstRtn.append(cptDatStr)
                    qpPrgRstT = True
                    if qpCmsVdSw == True:
                        qpCmrFncr = True
                    qpCmsVdSw = False
                    qpDcmVdSw = False
                    if is_read_only == False:
                        cptDatStr = ''
                elif currChr != ')' and currChr != ':' and currChr != '.' and currChr != ',':
                    if is_all_numbers == True:
                        if set(currChr).issubset(nmbrChrs) == False:
                            return -2
                    if is_read_only == False:
                        cptDatStr += currChr
                        
        if qpPrgPrhL == True and qpPrgPrhR == False:
            return -4
        else:
            if is_read_only == False:
                if calling_function == 'lvsd':
                    return dqRtn
                elif calling_function == 'lvss':
                    return lstRtn
            else:
                if is_all_numbers == True:
                    return 1
                else:
                    if ttlQp > 0:
                        if calling_function != 'savn':
                            return 2
                        else:
                            if qpCmrFncr == True:
                                return 22
                            else:
                                return 2
                    else:
                        return -3                                     
#______________________________________________________________________________________

    def rand_shuffle(self, particles: list) -> list:
        # @override PySqTppInterface.rand_shuffle()
        
        rtn = None
        amx = None
        bmx = 2
        lenP = len(particles)
        lenM = lenP+1
        mirror = [False for i in range(lenM)]
        
        for z in range(lenP):
            mirror[z] = False
            for y in range(lenP):
                amx = rrng(0, lenP)
                if not mirror[amx]:
                    mirror[amx] = True
                    rtn = particles[amx]
                    particles[amx] = particles[y]
                    particles[y] = rtn
                else:
                    mirror[lenM-1] = True
                    while mirror[lenM-1]:
                        if mirror[bmx]:
                            mirror[lenM-1] = False
                            if amx+bmx > lenP-1:
                                bmx = amx+bmx-lenP
                            else:
                                bmx = amx+bmx
                                rtn = particles[bmx]
                                particles[bmx] = particles[y]
                                particles[y] = rtn
                        else:
                            if bmx < lenP-1:
                                bmx+=1
                            else:
                                bmx = rrng(0, lenP)
        return particles
#______________________________________________________________________________________
