# Code File: StaqTapp-1.01 [PySqTpp_SarInterface.py] StaqTapp S.A.R. main interface class




# Staqtapp 1.01.722

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(@)gmail


import abc

#__________________________________________________________________________________________

class PySqTppSarInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'acquired_tqpt_source') and callable(subclass.acquired_tqpt_source) and hasattr(subclass, 'write_extension_source') and callable(subclass.write_extension_source) and hasattr(subclass, 'char_bridge') and callable(subclass.char_bridge) and hasattr(subclass, 'word_bridge') and callable(subclass.word_bridge) or NotImplemented)
    
    
    @abc.abstractmethod
    def acquired_tqpt_source(self, dsg_fnc: str, item_name: str, item_data: str, dir_path: str, source_name: str):
        # grants sar access to a tqpt variable source for pattern learning
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def write_extension_source(self, ext_pnt: str, source: str, dir_path: str, source_name: str) -> bool:
        # writes specific data extensions to a sar extension file type in same directory of tqpt source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def char_bridge(self, source: str) -> str:
        # char string analysis for separated word string return
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def word_bridge(self, source: str, dir_path: str) -> bool:
        # logging of words found for sar
        raise NotImplementedError
        
        
        
        
        
        
        
        
        
        
        
        
        