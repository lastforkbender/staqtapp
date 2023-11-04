# Code File: StaqTapp-1.02 PySqTpp_Rev9Interface.py] StaqTapp rev9 utility interface class




# Staqtapp 1.02.353

# For global variables file use and other lords' global variables fork bending


# ***These modules part of the SolaceXn AI software package as is for all lords***


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import abc
#__________________________________________________________________________________________

class PySqTppRev9Interface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'rev9_preform_priority_tree') and callable(subclass.rev9_preform_priority_tree) and hasattr(subclass, 'rev9_map') and callable(subclass.rev9_map) and hasattr(subclass, 'rev9_ocudlr') and callable(subclass.rev9_ocudlr) or NotImplemented)
        
        
    @abc.abstractmethod
    def rev9_preform_priority_tree(self, is_bypass_route_dsg: bool, build_folder: str):
        # creates a read/write capable branched structured file for abstract reasoning of encoded templates in the rev zip file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_map(self, is_read: bool, is_backup: bool, dsg: str, source:str, dir_path: str) -> int:
        # does all read and/or write of rev9 source files
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_ocudlr(self, ltr: str) -> str:
        # returns path indicators for console prints
        raise NotImplementedError
        
        

        
        
        