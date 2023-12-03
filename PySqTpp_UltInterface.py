# Code File: StaqTapp-1.02 [PySqTpp_UltInterface.py] StaqTapp utility interface class


# Staqtapp 1.02.387

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import abc
#__________________________________________________________________________________________

class PySqTppUltInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'limit_outer_domain') and callable(subclass.limit_outer_domain) and hasattr(subclass, 'asguard_variable_domain') and callable(subclass.asguard_variable_domain) and hasattr(subclass, 'search_key_lock') and callable(subclass.search_key_lock) and hasattr(subclass, 'overwrite_fnc_lock') and callable(subclass.overwrite_fnc_lock) and hasattr(subclass, 'scan_py_module') and callable(subclass.scan_py_module) and hasattr(subclass, 'print_tqpt_file') and callable(subclass.print_tqpt_file) and hasattr(subclass, 'print_tpqt_file') and callable(subclass.print_tpqt_file) and hasattr(subclass, 'tpqt_map') and callable(subclass.tpqt_map) or NotImplemented)
    
    
    @abc.abstractmethod
    def limit_outer_domain(self, var_name, func_name, full_path) -> int:
        # adds a variable name & function name(s) to a .tpqt functions lock extension file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def asguard_variable_domain(self, inact_logf: bool, var_name: str, func_name: str, full_path: str):
        # allows control of what functions can change a global variable via .tpqt extension file lookups
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def search_key_lock(self, var_name: str, full_path: str):
        # finds a listed variable name in a tpqt function lock file and returns a list type of function names associated with the variable
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def overwrite_fnc_lock(self, var_name, func_name, full_path):
        # overwrites a function lock list entry within a existing tpqt file of chosen variable listed
        raise NotImplementedError
    
    
    @abc.abstractmethod
    def scan_py_module(self, var_name: str, full_path: str) -> str:
        # complete search a py module for global variable name conflicts, return suggested smart variable name str or None
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def print_tqpt_file(self, full_path: str):
        # prints to console the contents of a tqpt variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def print_tpqt_file(self, full_path):
        # prints to console the contents of a tpqt functions lock file
        raise NotImplementedError
        
    @abc.abstractmethod
    def tpqt_map(self, is_read, is_exist, dsg_fnc, var_name, func_name, full_path):
        # performs read & write of tpqt files
        raise NotImplementedError   