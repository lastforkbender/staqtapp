# Code File: StaqTapp-1.01 [PySqTpp_UltInterface.py] StaqTapp utility interface class




# Staqtapp 1.01.913

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(@)gmail


import abc
#__________________________________________________________________________________________

class PySqTppUltInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'scan_py_module') and callable(subclass.scan_py_module) or NotImplemented)
    
    
    @abc.abstractmethod
    def scan_py_module(self, var_name: str, full_path: str) -> str:
        # complete search a py module for global variable name conflicts, return suggested smart variable name str or None
        raise NotImplementedError
        
        
        
        