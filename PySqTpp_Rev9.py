# Code File: StaqTapp-1.02 [PySqTpp_Rev9.py] main utility rev9 general functions use




# Staqtapp 1.02.353

# For global variables file use and other lords' global variables fork bending


# ***These modules part of the SolaceXn AI software package as is for all lords***


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import PySqTpp_Rev9Interface

import mmap
import os
import re
#______________________________________________________________________________________

class Rev9Setup(PySqTpp_Rev9Interface.PySqTppRev9Interface):
    # - settled functions for rev9 build module methods -
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