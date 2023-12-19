# Code File: StaqTapp-1.02 [stpr.py] StaqTapp __main__ rev9 functional calls module


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


from PySqTpp_Rev9 import Rev9Setup

import multiprocessing
import collections
import sys

__rev9__prc = None

#______________________________________________________________________________________

def _rev9_r9cp(r9cp_lst):
    try:
        for pdx in range(len(r9cp_lst)):
            print(r9cp_lst[pdx])
    except Exception:
        pass
#______________________________________________________________________________________

def _rev9_proc(pr9cn_lst):
    global __rev9__prc
    __rev9__prc = None
    __rev9__prc = multiprocessing.Process(target = _rev9_r9cp, args = (pr9cn_lst,), daemon = True)
#______________________________________________________________________________________

def _rev9_updt_cp(pr9cx_lst):
    _rev9_proc(pr9cx_lst)
    __rev9__prc.start()
    __rev9__prc.join()
    
#______________________________________________________________________________________
#______________________________________________________________________________________
# - - - - - - - - - - - - - - - - - - - - - REV9 CUSTOM GLOBAL VARIABLES MODULES BUILDING .□ .■
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 
#
#
# staqtapp-rev9 flow-chart drawing link: https://ibb.co/s3MS9Jd
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________
#______________________________________________________________________________________

def rev9_update_write_abstract_settings(is_slots_encoding, is_sars_encoding, is_multi_stability, is_multi_extractable, is_obfuscated, is_content_dependent, is_static_shifting, is_sorting_tolerate, is_counterintuitive_variables, is_superpalindrome_pointers, is_variables_length_muting, is_variables_topography_learning, folder_path):
    
    r9s = Rev9Setup()
    
    tLst = []
    mStr = None
    
    msSw = False
    meSw = False
    
    # all this very crucial for narrowing the writing code paths rev9 model takes on encoding differences;
    # having a one time config file the programmer edits outside this is considered but not implemented
    tLst.append("\n\n]" + r9s.rev9_ocudlr('o') + "<[>>  STAQTAPP-REV9 LIBRARY MODULES BUILDER IS RUNNING")
    tLst.append("\n]" + r9s.rev9_ocudlr('o') + "<[>>  .....starting sort of assigned initial build-in settings")
    mStr = '//./ STAQTAPP-REV9 STRUCTURE~REACTION SETTINGS FILE //./ (!!!DO NOT EDIT OR REMOVE!!!)\n\n<:PhaseUnificationMediumAccords=\n'
    # what level of phase medium encoding are we looking at first?
    if is_slots_encoding == True and is_sars_encoding == True:
        tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  p.u.m.a. setting build will be __slots__ & sars variables programming composed")
        mStr += 'hybrid:>\n'
    elif is_slots_encoding == True and is_sars_encoding == False:
        tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  p.u.m.a. setting build will be __slots__ variables programming composed")
        mStr += 'slots:>\n'
    elif is_slots_encoding == False and is_sars_encoding == True:
        tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  p.u.m.a. setting build will be sars variables programming composed")
        mStr += 'sars:>\n'
    elif is_slots_encoding == False and is_sars_encoding == False:
        tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  p.u.m.a. setting build will be general variables programming composed")
        mStr += 'general:>\n'
    tLst.append("]" + r9s.rev9_ocudlr('o') + "<[>>  .....sorting linked property scopes(i.p.c.d.) to secondary rev9 self-encoding settings")
    mStr += '<:IsolatedPositionCodeDepths=\n'
    if is_multi_stability == True and is_multi_extractable == True:
        msSw = True
        meSw = True
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  multi-stability & multi-extractable are present rev9 settings found")
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  most likely to spawn bluetooth optional modules encoding mapped")
        if is_variables_length_muting == True and is_static_shifting == True:
            tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  strict parameter variables encoding will be used @static-shifts")
            mStr += 'mmvs-1'
        # this can be override to use static shifting regardless of settings already passed in
        elif is_variables_length_muting == True and is_sorting_tolerate == True:
            tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  strict parameter variables encoding will be used")
            mStr += 'mmvs-2'
        elif is_variables_length_muting == False and is_static_shifting == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  strict parameter variables encoding will not be used @static-shifts")
            mStr += 'mmss'
        # !!!cannot be a override to use static shifting encodings!!!
        elif is_variables_length_muting == False and is_sorting_tolerate == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  strict parameter variables encoding will not be used")
            mStr += 'mmst'
        else:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  neither @static-shifting or a sortable encodings tolerate will be used")
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  if any topography encoded learning enabled will be less core present")
            mStr += 'mm?'
        if len(tLst) > 0:
            _rev9_updt_cp(tLst)
            tLst = []
    elif is_multi_stability == True and is_multi_extractable == False:
        msSw = True
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  multi-extractable is not a present rev9 build code-core setting")
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  can likely spawn bluetooth options if is a content dependent build...")
        if is_counterintuitive_variables == True and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  counterintuitive-vars & content dependent glb-vars type will be used")
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  rev9 encoding model will not use parallel probables to code finalized @static-shifts")
            mStr += 'msvd-1'
        elif is_counterintuitive_variables == True and is_content_dependent == False:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  glb-vars content dependent is not a enabled rev9 encode setting")
            tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  rev9 encoding model will use parallel probables to code finalized @static-shifts")
            mStr += 'msvd-2'
        elif is_counterintuitive_variables == False and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('r') + "<[>>  content dependent interactions will be applied @multi-stability error checking")
            mStr += 'mscd'
        elif is_counterintuitive_variables == False and is_content_dependent == False:
            mStr += 'ms_rsrv-0'
        else:
            mStr += 'ms_rsrv-?'
    elif is_multi_stability == False and is_multi_extractable == True:
        meSw = True
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  @multi-extractable setting on, found with @multi-stability off")
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  this can cause a override setting @sorting-tolerate option(s)")
        mStr += '-mmse?'
    elif is_multi_stability == False and is_multi_extractable == False:
        r9s.rev9_cleanup_directory(folder_path)
        raise Exception("staqtapp-rev9 build error: either multi-extractable and/or multi-stability initial setting(s) must be True")
    mStr +=':>\n'
    if len(tLst) > 0:
        _rev9_updt_cp(tLst)
        tLst = []
    tLst.append("]" + r9s.rev9_ocudlr('o') + "<[>>  ...sorting parallel connected @identity-states for bluetooth descriptors")
    mStr += '<:ParallelConnectedIdentityStates=\n'
    if msSw == True and is_superpalindrome_pointers == True and is_sorting_tolerate == True:
        if is_variables_topograhy_learning == True and is_counterintuitive_variables == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. connect states are superpalindrome builds with counter topography")
            mStr += 'mst_vtcv'
        elif is_variables_topography_learning == True and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. connect states are superpalindrome builds with content dependencies")
            mStr += 'mst_cd'
        elif is_variables_topography_learning == True and is_static_shifting == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. connect states are superpalindrome builds with static shifts")
            mStr += 'mst_ss'
        elif is_variables_topography_learning == True and is_static_shifting == False:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. connect states are superpalindrome builds with no static shifts")
            mStr += 'mst_??'
        else:
            mStr += 'mst_!!!'
    if msSw == True and is_superpalindrome_pointers == True and is_sorting_tolerate == False:
        if is_variables_topography_learning == True and is_counterintuitive_variables == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is non-sort tolerate superpalindrome builds with counter topography")
            mStr += 'ms_vtcv'
        elif is_variables_topography_learning == True and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is non-sort tolerate superpalindrome builds with content dependencies")
            mStr += 'ms_cd'
        elif is_variables_topography_learning == True and is_static_shifting == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is non-sort tolerate superpalindrome builds with static shifts")
            mStr += 'ms_ss'
        elif is_variables_topography_learning == True and is_static_shifting == False:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is non-sort tolerate superpalindrome builds with no static shifts")
            mStr += 'ms_??'
        else:
            mStr += 'ms_!!!'
    if msSw == True and is_superpalindrome_pointers == False and is_sorting_tolerate == True:
        if meSw == True and is_variables_length_muting == True and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is sort tolerate build with dependent variables length muting")
            mStr += 'ms-me_vlcd'
        elif meSw == True and is_variables_length_muting == True and is_content_dependent == False:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is sort tolerate build with variables length muting")
            mStr += 'ms-me_vl'
        elif meSw == True and is_variables_length_muting == False and is_content_dependent == True:
            tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  p.c.i.s. is sort tolerate build with content dependencies")
            mStr += 'ms-me_cd'
        else:
            mStr += 'msst_?'
    else:
        if msSw == True and meSw == True:
            mStr += 'ms-me_?'
        elif msSw == True and meSw == False:
            mStr += 'ms-?'
        elif msSw == False and meSw == True:
            mStr += 'me-?'
    mStr += ':>\n'
    if len(tLst) > 0:
        _rev9_updt_cp(tLst)
        tLst = []
    if is_obfuscated == True:
        mStr += '<:ObfuscateEncodings=\ny:>'
    else:
        mStr += '<:ObfuscateEncodings=\nn:>'
    rslt = r9s.rev9_map(False, False, 'wisf', mStr, folder_path)
    if rslt == -1:
        r9s.rev9_cleanup_directory(folder_path)
        raise Exception("staqtapp rev9 build error: build folder path cannot be nothing")
    elif rslt == -2:
        r9s.rev9_cleanup_directory(folder_path)
        raise Exception("staqtapp rev9 build error: build folder path was not found @" + folder_path)
    elif rslt == -3:
        r9s.rev9_cleanup_directory(folder_path)
        raise Exception("staqtapp rev9 build error: unknown source error happened...")
#______________________________________________________________________________________

def rev9_model_service(is_slots_encoding, is_sars_encoding, is_multi_stability, is_multi_extractable, is_obfuscated, is_content_dependent, is_static_shifting, is_sorting_tolerate, is_counterintuitive_variables, is_superpalindrome_pointers, is_variables_length_muting, is_variables_topography_learning, global_variables_file_extension, global_variables_library_name, build_folder_path):
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                                      / VARIABLES OF ABBA \ 
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    # REV9 IN-BUILD METHOD PARAMETERS:
                
    # (1)    <is_slots_encoding=bool>,  applies abstract __slots__ py module class/function programming to the in-build global variables library rev9 decisions, this can effect performance and the overall built size of the library finalized
                
    # (2)    <is_sars_encoding=bool>,  applies global sar variables type/global sar temple variables pointer type programming to finalized library build, see PySqTpp_Alpha or stpp module's sar functions descriptions usage
                
    # (3)    <is_multi_stability=bool>,  applies complete finalized directional error checking within interface/class/functions to class/functions usage inner and/or outer; if False, does not apply it's code writting for more strict type error feedbacks
                
    # (4)    <is_multi_extractable=bool>,  applies approximate global variables data @is_variables_topography_learning, or if False makes choice of indicated performance clauses by any found constants in parameters changes
         # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
    # (5)    <is_obfuscated=bool>,  applies obfuscated variables naming to the in-build coding of the custom global variables library, does not obfuscate the finalized callable function names or their parameters
                
    # (6)    <is_content_dependent=bool>,  applies formulation strict observes to global variables data type interactions chosen; a basic read/write functional argument, however does effect overall performance in a finalized library build
         # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
    # (7)    <is_static_shifting=bool>,  applies any chosen shifting mechanics to the global variables file type format chosen via static bound declaring in coding builds; can take longer of it's decision build loops but more tighter coding finalized of library builds
                
    # (8)    <is_sorting_tolerate=bool>,  applies & determines position inter-changes to global variables file formats, function direction flowings and read/write mapping of global variables scope communication to outer parameters options made
                
    # (9)    <is_counterintuitive_variables=bool>,  from above almost opposite but not, applies non-traditional means of callable function flows inner to global variables file format overall library builds; can make the function encoding difficult to read
                
    # (10)  <is_superpalindrome_pointers=bool>,  uses superbranching rotational variables mapping to the applied coding in-build resolves, in the global variables file read/write regions of library made; can effect reading performances if using __slots__
         # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
    # (11)  <is_variables_length_muting=bool>,  uses strict lock-offs to finalized functions' parameters usages built; the rev9 model determines this scope and can also effect performance timing and can make very unreadable function encodings also
                
    # (12)  <is_variables_topography_learning=bool>,  rev9 model build decision based exclusive only, joins property scopes of any found constants to combine/compress for other file types associated & written for any outer data gathering usage
         # *****can build bluetooth functional file extension matters//custom normals or customs invertable to sars enabled self-network expressions interconnected e.g. android os*****
                
    # (13)  <global_variables_file_extension: str>,  global variables source file extension to use for the finalized rev9 global variables library build
                
    # (14)  <global_variables_library_name: str>,  overall library name of the global variables read/write library to be built by the rev9 model; rev9 build library model uses this to name on all other files, classes, functions, variables, slots and etc.
                
    # (15)  <build_folder_path: str>, folder path chosen for rev9 global variables files modules built
               
    r9s = Rev9Setup()
    
    rslt = None
    
    tLst = []
    nLst = None
    
    try: 
        # determine the general abstract encoding paths/options & write as the initial settings file
        rev9_update_write_abstract_settings(is_slots_encoding, is_sars_encoding, is_multi_stability, is_multi_extractable, is_obfuscated, is_content_dependent, is_static_shifting, is_sorting_tolerate, is_counterintuitive_variables, is_superpalindrome_pointers, is_variables_length_muting, is_variables_topography_learning, build_folder_path)
        # write begin priority rev9 tree decision file; this connected to encoded zip file templates direct,
        # created from source written above and saves a backup file of this in build directory a same
        tLst.append("]" + r9s.rev9_ocudlr('o') + "<[>>  assembling priority tree decision file @ build folder directory")
        r9s.rev9_preform_priority_tree(False, build_folder_path)
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  finished assembling a beginning priority tree file")
        tLst.append("]" + r9s.rev9_ocudlr('o') + "<[>>  applying concentrated naming pattern & basic format module saves")
        rslt = r9s.rev9_concentrated_naming(global_variables_file_extension, global_variables_library_name, build_folder_path)
        if rslt == -1:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_file_extension parameter must be more than 3 chars")
        elif rslt == -2:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_library_name parameter must be more than 5 chars")
        elif rslt == -3:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_file_extension parameter cannot be more than 7 chars")
        elif rslt == -4:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_library_name parameter cannot be more than 14 chars")
        elif rslt == -5:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_library_name parameter has invalid chars, allowed chars: a-z A-Z")
        elif rslt == -6:
            r9s.rev9_cleanup_directory(build_folder_path)
            raise Exception("staqtapp rev9 build error: @global_variables_file_extension parameter has invalid chars, allowed chars: a-z A-Z")
        else:
            nLst = rslt
        tLst.append("]" + r9s.rev9_ocudlr('c') + "<[>>  concentrated naming patterns applied to modules")
        if len(tLst) > 0:
            _rev9_updt_cp(tLst)
            tLst = []
            # begin rev9 self-replicate encode engine setup tuples & the overall module scope checks for priority tree
            
    except Exception as e:
        r9s.rev9_cleanup_directory(build_folder_path)
        raise Exception("staqtapp rev9 build error: ",e)
#______________________________________________________________________________________

def main(args):
    sRt = 1
    try:
        if len(args) == 15:
            s = 0
            while s < 15:
                if s < 12:
                    if not isinstance(args[s], bool):
                        sRt = -1
                        break
                else:
                    if not isinstance(args[s], str):
                        sRt = -2
                        break
                s+=1
        else:
            raise Exception("staqtapp rev9 build error: missing initial rev9 settings parameters")
    except Exception as e:
        raise Exception("staqtapp rev9 build error: ",e)
    if sRt > 0:
        rev9_model_service(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10], args[11], args[12], args[13], args[14])
    else:
        raise Exception("staqtapp rev9 build error: initial parameter settings must be proper placement of boolean type and string type arguments only")
    
#______________________________________________________________________________________

if __name__ == '__main__':
    main(sys.argv[1:])
#______________________________________________________________________________________
