# Code File: StaqTapp-1.01 [PySqTpp_Interface.py] StaqTapp main interface class




# Staqtapp 1.01.493

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(@)gmail


import abc
#from collections import deque

#__________________________________________________________________________________________

class PySqTppInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'make_variables_source') and callable(subclass.make_variables_source) and hasattr(subclass, 'add_variables_source') and callable(subclass.add_variables_source) and hasattr(subclass, 'load_variables_source_deque') and callable(subclass.load_variables_source_deque) and hasattr(subclass, 'search_variable') and callable(subclass.search_variable) and hasattr(subclass, 'tqpt_map') and callable(subclass.tqpt_map) and hasattr(subclass, 'check_tqpt_settings') and callable(subclass.check_tqpt_settings) and hasattr(subclass, 'check_parameter_string') and callable(subclass.check_parameter_string) and hasattr(subclass, 'char_regularity') and callable(subclass.char_regularity) or NotImplemented)
    
    
    @abc.abstractmethod
    def make_variables_source(self, is_static: bool, make_dir: bool, overwrite_source: bool, dir_path: str, make_source_name: str) -> int:
        # create new variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def add_variables_source(self, var_name: str, var_data: str, dir_path: str, source_name: str) -> int:
        # add variables to a variables source file
        raise NotImplementedError
    
    
    @abc.abstractmethod
    def load_variables_source_deque(self, is_numbers: bool, var_name: str, dir_path: str, source_name: str):
        # extract variable's data from variables source file as list type
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def search_variable(self, all_tqpt_sources: bool, var_name: str, dir_path: str, source_name: str):
        # search and find any variable in any tqpt variable source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def tqpt_map(self, is_read: bool, is_write: bool, dsg_fnc: str, is_overwrite: bool, glb_var: str, glb_var_data: str, folder_path: str, tqpt_name: str):
        # mmap operations on .tqpt global variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def check_tqpt_settings(self, is_static: bool, full_path: str) -> int:
        # returns settings checks or other for a tqpt variables source file settings
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def check_parameter_string(self, is_variable: bool, parameter: str) -> bool:
        # check parameter string is valid chars
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def char_regularity(self, is_read_only: bool, is_all_numbers: bool, calling_function: str, source: str):
        # strict parsing of a variable's data from chosen source file
        raise NotImplementedError
#__________________________________________________________________________________________











