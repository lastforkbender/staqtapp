# Code File: StaqTapp-1.02 [PySqTpp_Rev9.py] main utility rev9 general functions use




# Staqtapp 1.02.342

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
    # - settled functions for rev9 general build module methods -
#______________________________________________________________________________________

    def rev9_map(self, is_read: bool, dsg: str, source:str, dir_path: str) -> int:
        # @override PySqTppRev9Interface.rev9_map()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return -1  : folder path is empty
        # return -2  : folder path is not there
        # return -3  : is a empty source...
        
        if len(dir_path) > 0:
            if os.path.isdir(dir_path):
                if is_read == True:
                    # -------- READ REV9 SOURCE FILES --------------------------------------------
                    if len(source) > 0:
                        pass
                    else:
                        return -3
                else:
                    # -------- READ+WRITE REV9 SOURCE FILES -------------------------------
                    if len(source) > 0:
                        if dsg == 'wisf':
                            with open(dir_path + '/__sqtpp_rev9.stgs', 'w')as fWisf: fWisf.write(source)
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




