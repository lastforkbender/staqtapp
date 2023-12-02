# Code File: StaqTapp-1.02 [PySqTpp_Rev9.py] main utility rev9 general functions use


# Staqtapp 1.02.385

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import PySqTpp_Rev9Interface

import collections
import os
import re

#______________________________________________________________________________________

class Rev9Setup(PySqTpp_Rev9Interface.PySqTppRev9Interface):
    # - settled functions for rev9 build module methods -
#______________________________________________________________________________________

    def rev9_craft_interface(self, is_exist: bool, py_name: str, build_folder: str):
        # @override PySqTppRev9Interface.rev9_craft_interface()
        
        r9s = Rev9Setup()
        cStr = None
        cLst = []
        
        if is_exist == True:
            pass
        else:
            cLst.append('import abc')
            cStr = r9s.rev9_get_header('intrfc', py_name, None, cLst)
            cStr += "class " + py_name.replace('_', '') + "(metaclass=abc.ABCMeta):\n\n\n    @classmethod\n    def __subclasshook__(cls, subclass):\n"
            with open(build_folder + '/' + py_name + '.txt', 'w') as fRev: fRev.write(cStr)
#______________________________________________________________________________________

    def rev9_craft_main(self, is_exist: bool, py_name: str, py_names: list, build_folder: str):
        # @override PySqTppRev9Interface.rev9_craft_main()
        
        r9s = Rev9Setup()
        cStr = None
        
        if is_exist == True:
            pass
        else:
            cStr = r9s.rev9_get_header('main', py_name, None, py_names)
            with open(build_folder + '/' + py_name + '.txt', 'w') as fRev: fRev.write(cStr)
#______________________________________________________________________________________

    def rev9_craft_parser(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # @override PySqTppRev9Interface.rev9_craft_parser()
        
        r9s = Rev9Setup()
        cStr = None
        
        if is_exist == True:
            pass
        else:
            cStr = r9s.rev9_get_header('prsr', py_name, py_intrfc_name, py_names)
            cStr += 'class ' + py_name.replace('_', '') + '(' + py_intrfc_name + '.' + py_intrfc_name.replace('_', '') + '):\n#______________________________________________________________________________________\n\n'
            with open(build_folder + '/' + py_name + '.txt', 'w') as fRev: fRev.write(cStr)
#______________________________________________________________________________________

    def rev9_craft_utility(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # @override PySqTppRev9Interface.rev9_craft_utility()
        
        r9s = Rev9Setup()
        cStr = None
        
        if is_exist == True:
            pass
        else:
            cStr = r9s.rev9_get_header('prsr', py_name, py_intrfc_name, py_names)
            cStr += 'class ' + py_name.replace('_', '') + '(' + py_intrfc_name + '.' + py_intrfc_name.replace('_', '') + '):\n#______________________________________________________________________________________\n\n'
            with open(build_folder + '/' + py_name + '.txt', 'w') as fRev: fRev.write(cStr)
#______________________________________________________________________________________

    def rev9_craft_net(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # @override PySqTppRev9Interface.rev9_craft_net()
        
        r9s = Rev9Setup()
        cStr = None
        
        if is_exist == True:
            pass
        else:
            cStr = r9s.rev9_get_header('prsr', py_name, py_intrfc_name, py_names)
            cStr += 'class ' + py_name.replace('_', '') + '(' + py_intrfc_name + '.' + py_intrfc_name.replace('_', '') + '):\n#______________________________________________________________________________________\n\n'
            with open(build_folder + '/' + py_name + '.txt', 'w') as fRev: fRev.write(cStr)
#______________________________________________________________________________________

    def rev9_concentrated_naming(self, fle_ext: str, lib_nm: str, folder_path: str):
        # @override PySqTppRev9Interface.rev9_concentrated_naming()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : invalid file extension str length less than 4 chars
        # return -2  : invalid library name str length less than 6 chars
        # return -3  : invalid file extension str length greater than 7 chars
        # return -4  : invalid library name str length greater than 14 chars
        # return -5  : invalid chars found in library naming
        # return -6  : invalid chars found in file extension
        
        cCnt = None
        cLen = None
        cStr = None
        prvChr = None
        cptlLtrs = None
        rtrnLst = None
        
        vldChrs = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        r9s = Rev9Setup()
        if len(fle_ext) > 3:
            if len(lib_nm) > 5:
                if len(fle_ext) > 7:
                    return -3
                else:
                    if len(lib_nm) > 14:
                        return -4
                    else:
                        # check is proper chars usage @ lib_nm + fle_ext
                        if set(lib_nm).issubset(vldChrs) == True:
                            if set(fle_ext).issubset(vldChrs) == True:
                                # setup all the modules' namings
                                cCnt = 0
                                cLen = len(lib_nm)-1
                                cStr = ''
                                prvChr = '@'
                                cptlLtrs = False
                                for curChr in lib_nm:
                                    if cCnt != 0 and cLen != cCnt and prvChr.isupper() == False and curChr.isupper() == True:
                                        cStr += '_'
                                        if cptlLtrs == False:
                                            cptlLtrs = True
                                    cStr += curChr
                                    prvChr = curChr
                                    cCnt+=1
                                if cptlLtrs == True:
                                    rtrnLst = [cStr + '_Rev9_Main', cStr + '_Rev9_Interface', cStr + '_Rev9_Parser', cStr + '_Rev9_Utility_Interface', cStr + '_Rev9_Utility', cStr + '_Rev9Net_Interface', cStr + '_Rev9Net']
                                else:
                                    rtrnLst = [cStr + '_rev9_main', cStr + '_rev9_interface', cStr + '_rev9_parser', cStr + '_rev9_utility_interface', cStr + '_rev9_utility', cStr + '_rev9net_interface', cStr + '_rev9net']
                                # craft the begin interface files and save as py modules in build folder
                                r9s.rev9_craft_interface(False, rtrnLst[1], folder_path)
                                r9s.rev9_craft_interface(False, rtrnLst[3], folder_path)
                                r9s.rev9_craft_interface(False, rtrnLst[5], folder_path)
                                # craft the begin main py module to build directory
                                ioLst = [rtrnLst[2], rtrnLst[4], rtrnLst[6]]
                                r9s.rev9_craft_main(False, rtrnLst[0], ioLst, folder_path)
                                # craft the begin parser py module to build directory
                                ioLst = [rtrnLst[4]]
                                r9s.rev9_craft_parser(False, rtrnLst[2], rtrnLst[1], ioLst, folder_path)
                                # craft the begin utility py module to build directory
                                ioLst = [rtrnLst[2]]
                                r9s.rev9_craft_utility(False, rtrnLst[4], rtrnLst[3], ioLst, folder_path)
                                # craft the begin net py module to build directory
                                ioLst = [rtrnLst[4]]
                                r9s.rev9_craft_net(False, rtrnLst[6], rtrnLst[5], ioLst, folder_path)
                                return rtrnLst
                            else:
                                return -6
                        else:
                            return -5
            else:
                return -2
        else:
            return -1
#______________________________________________________________________________________

    def rev9_preform_priority_tree(self, is_bypass_route_dsg: bool, build_folder: str):
        # @override PySqTppRev9Interface.rev9_preform_priority_tree()
        
        r9s = Rev9Setup()
        rStr = r9s.rev9_map(True, False, "rd_stgs", None, build_folder)
        ptrnStr = None
        stgsLst = []
        fnd = None
        rl = 0
        while rl < 4:
            if rl == 0: ptrnStr = re.compile(r'<:'+re.escape(r"PhaseUnificationMediumAccords")+r'=(?s:.*?).*:>')
            elif rl == 1: ptrnStr = re.compile(r'<:'+re.escape(r"IsolatedPositionCodeDepths")+r'=(?s:.*?).*:>')
            elif rl == 2: ptrnStr = re.compile(r'<:'+re.escape(r"ParallelConnectedIdentityStates")+r'=(?s:.*?).*:>')
            else: ptrnStr = re.compile(r'<:'+re.escape(r"ObfuscateEncodings")+r'=(?s:.*?).*:>')
            fnd = False
            for stgsMtc in ptrnStr.findall(rStr):
                if len(stgsMtc) > 0:
                    stgsLst.append(stgsMtc)
                    stgsLst[rl] = stgsLst[rl].strip('\n <:>')
                    fnd = True
                    break
            if fnd == True:
                rl+=1
            else:
                r9s.rev9_cleanup_directory(build_folder)
                raise Exception("staqtapp rev9 build error: missing configuration settings for priority tree")
        ptrnStr = ''
        rl = 0
        while rl < 4:
            rStr = stgsLst[rl].split('=')
            if len(rStr) == 2 and is_bypass_route_dsg == False:
                ptrnStr += "<" + rStr[0] + "\n  :" + rStr[1] + ">\n    ::rev_fnc_dsg=)...(>\n      ::rev_zip_tmplt_addr=)...(>\n        ::rev_emc1=)...(>\n        ::rev_emc2=)...(>\n        ::rev_emc3=)...(>\n        ::rev_emc4=)...(>\n        ::rev_emc5=)...(>\n        ::rev_emc6=)...(>\n        ::rev_emc7=)...(>\n        ::rev_emc8=)...(>\n        ::rev_emc9=)...(>"
            else:
                ptrnStr += "<" + rStr[0] + "\n  :routn_dsg>\n    ::rev_fnc_dsg=)...(>\n      ::rev_zip_tmplt_addr=)...(>\n        ::rev_emc1=)...(>\n        ::rev_emc2=)...(>\n        ::rev_emc3=)...(>\n        ::rev_emc4=)...(>\n        ::rev_emc5=)...(>\n        ::rev_emc6=)...(>\n        ::rev_emc7=)...(>\n        ::rev_emc8=)...(>\n        ::rev_emc9=)...(>"
            if rl < 3:
                rl+=1
                ptrnStr += "\n"
            else:
                rl+=1
        r9s.rev9_map(False, True, 'wpt', ptrnStr, build_folder)
#______________________________________________________________________________________

    def rev9_map(self, is_read: bool, is_backup: bool, dsg: str, source:str, dir_path: str) -> int:
        # @override PySqTppRev9Interface.rev9_map()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : folder path is empty
        # return -2  : folder path is not there
        # return -3  : is a empty source...
        
        rStr = None
        
        if len(dir_path) > 0:
            if os.path.isdir(dir_path):
                if is_read == True:
                    # -------- READ REV9 SOURCE FILES --------------------------------------------
                    if dsg == 'rd_stgs':
                        with open(dir_path + '/__sqtpp_rev9.stgs', 'r') as fRdStgs:
                            rStr = fRdStgs.read()
                            return rStr
                else:
                    # -------- READ+WRITE REV9 SOURCE FILES -------------------------------
                    if len(source) > 0:
                        if dsg == 'wisf':
                            with open(dir_path + '/__sqtpp_rev9.stgs', 'w') as fWisf: fWisf.write(source)
                        elif dsg == 'wpt':
                            with open(dir_path + '/__sqtpp_rev9.tree', 'w') as fWpt: fWpt.write(source)
                            if is_backup == True:
                                with open(dir_path + '/__sqtpp_rev9.tree.bck', 'w') as fWpt: fWpt.write(source)
                    else:
                        return -3
            else:
                return -2
        else:
            return -1
#______________________________________________________________________________________

    def rev9_get_header(self, mdl_dsg: str, py_name: str, py_intrfc_name: str, py_imports: list) -> str:
        # @override PySqTppRev9Interface.rev9_get_header()
        
        rtrnStr = "# StaqTapp-Rev9 Global Variables Library [" + py_name + ".py]\n# https://github.com/lastforkbender/staqtapp\n\n# These encoded files are self-replicated functional global variables py modules by the staqtapp library\n\n\n\n"
        if mdl_dsg == 'intrfc':
            for hdrA in range(len(py_imports)):
                rtrnStr += py_imports[hdrA] + '\n'
        elif mdl_dsg == 'main':
            for hdrB in range(len(py_imports)):
                rtrnStr += 'from ' + py_imports[hdrB] + ' import ' + py_imports[hdrB].replace('_', "") + '\n'
        elif mdl_dsg == 'prsr':
            rtrnStr += 'import ' + py_intrfc_name + '\n\n'
            for hdrC in range(len(py_imports)):
                rtrnStr += 'from ' + py_imports[hdrC] + ' import ' + py_imports[hdrC].replace('_', "") + '\n'
            rtrnStr += '\nimport mmap\nimport glob\nimport os\nimport re\n'
        rtrnStr += "#______________________________________________________________________________________\n\n"
        return rtrnStr
#______________________________________________________________________________________

    def rev9_ocudlr(self, ltr: str) -> str:
        # @override PySqTppRev9Interface.rev9_ocudlr()
        
        if ltr == 'o':
            return '○'
        elif ltr == 'c':
            return '●'
        elif ltr == 'u':
            return '◒'
        elif ltr == 'd':
            return '◓'
        elif ltr == 'l':
            return '◑'
        elif ltr == 'r':
            return '◐'
#______________________________________________________________________________________

    def rev9_cleanup_directory(self, folder_path):
        # @override PySqTppRev9Interface.rev9_cleanup_directory()
        
        try:
            if os.path.isfile(folder_path + "/__sqtpp_rev9.stgs"):
                os.remove(folder_path + "/__sqtpp_rev9.stgs")
            if os.path.isfile(folder_path + "/__sqtpp_rev9.tree"):
                os.remove(folder_path + "/__sqtpp_rev9.tree")
            if os.path.isfile(folder_path + "/__sqtpp_rev9.tree.bck"):
                os.remove(folder_path + "/__sqtpp_rev9.tree.bck")
        except Exception:
            pass
#______________________________________________________________________________________