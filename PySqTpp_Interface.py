# Code File: StaqTapp-1.02 [PySqTpp_Interface.py] StaqTapp main interface class

# Staqtapp 1.02.450

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


import abc
#from collections import deque

#__________________________________________________________________________________________

class PySqTppInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'make_variables_source') and callable(subclass.make_variables_source) and hasattr(subclass, 'add_variables_source') and callable(subclass.add_variables_source) and hasattr(subclass, 'change_variable_name') and callable(subclass.change_variable_name) and hasattr(subclass, 'update_variables_source') and callable(subclass.update_variables_source) and hasattr(subclass, 'self_assign_variable_name') and callable(subclass.self_assign_variable_name) and hasattr(subclass, 'load_variables_source_str') and callable(subclass.load_variables_source_str) and hasattr(subclass, 'load_variables_source_deque') and callable(subclass.load_variables_source_deque) and hasattr(subclass, 'search_variable') and callable(subclass.search_variable) and hasattr(subclass, 'tqpt_map') and callable(subclass.tqpt_map) and hasattr(subclass, 'check_tqpt_settings') and callable(subclass.check_tqpt_settings) and hasattr(subclass, 'check_parameter_string') and callable(subclass.check_parameter_string) and hasattr(subclass, 'char_regularity') and callable(subclass.char_regularity) and hasattr(subclass, 'rand_shuffle') and callable(subclass.rand_shuffle) or NotImplemented)
    
    
    @abc.abstractmethod
    def make_variables_source(self, is_static: bool, make_dir: bool, overwrite_source: bool, dir_path: str, make_source_name: str) -> int:
        # create new variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def add_variables_source(self, var_name: str, var_data: str, dir_path: str, source_name: str) -> int:
        # add variables to a variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def change_variable_name(self, var_name: str, new_var_name: str, dir_path: str, source_name: str) -> int:
        # renames a stored global variable's name
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def update_variables_source(self, var_name: str, var_data: str, dir_path: str, source_name: str) -> int:
        # updates new variable data changes
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def self_assign_variable_name(self, prepin_cat_dsg: str, var_data: str, dir_path: str, source_name: str) -> int:
        # auto assigns random variable name connected to a given begin/prepin category id
        # writes the variable's data with option to flip static setting off->on for write->read i/o/t
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def load_variables_source_str(self, var_name, dir_path, source_name):
        # extracts variable(s) data from variables source file as a str or a multi str list type return
        raise NotImplementedError
    
    
    @abc.abstractmethod
    def load_variables_source_deque(self, is_numbers: bool, var_name: str, dir_path: str, source_name: str):
        # extract variable's data from variables source file as a deque type return only
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def search_variable(self, all_tqpt_sources: bool, var_name: str, dir_path: str, source_name: str):
        # search and find any variable in any tqpt variable source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def tqpt_map(self, is_read, is_write, dsg_fnc, is_overwrite, glb_var, glb_var_data, folder_path, tqpt_name):
        # mmap operations on .tqpt global variables source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def check_tqpt_settings(self, is_static: bool, full_path: str) -> int:
        # returns settings checks or other for a tqpt variables source file settings
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def check_parameter_string(self, is_variable, parameter, is_list):
        # check parameter string is valid chars
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def char_regularity(self, is_read_only: bool, is_all_numbers: bool, calling_function: str, source: str):
        # strict parsing of a variable's data from chosen source file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rand_shuffle(self, particles: list) -> list:
        # random shuffle of the given list
        raise NotImplementedError