# Code File: StaqTapp-1.02 PySqTpp_Rev9Interface.py] StaqTapp rev9 utility interface class


# Staqtapp 1.02.441

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
#__________________________________________________________________________________________

class PySqTppRev9Interface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'rev9_craft_interface') and callable(subclass.rev9_craft_interface) and hasattr(subclass, 'rev9_craft_main') and callable(subclass.rev9_craft_main) and hasattr(subclass, 'rev9_craft_parser') and callable(subclass.rev9_craft_parser) and hasattr(subclass, 'rev9_craft_utility') and callable(subclass.rev9_craft_utility) and hasattr(subclass, 'rev9_craft_net') and callable(subclass.rev9_craft_net) and hasattr(subclass, 'rev9_concentrated_naming') and callable(subclass.rev9_concentrated_naming) and hasattr(subclass, 'rev9_preform_priority_tree') and callable(subclass.rev9_preform_priority_tree) and hasattr(subclass, 'rev9_map') and callable(subclass.rev9_map) and hasattr(subclass, 'rev9_get_header') and callable(subclass.rev9_get_header) and hasattr(subclass, 'rev9_ocudlr') and callable(subclass.rev9_ocudlr) and hasattr(subclass, 'rev9_cleanup_directory') and callable(subclass.rev9_cleanup_directory) or NotImplemented)
        
        
    @abc.abstractmethod
    def rev9_craft_interface(self, is_exist: bool, py_name: str, build_folder: str):
        # builds rev9 interfacing self-encoded modules
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_craft_main(self, is_exist: bool, py_name: str, py_names: list, build_folder: str):
        # builds rev9 main self-encoded modules
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_craft_parser(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # builds rev9 parser self-encoded modules
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_craft_utility(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # builds rev9 utility self-encoded modules
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_craft_net(self, is_exist: bool, py_name: str, py_intrfc_name: str, py_names: list, build_folder: str):
        # builds rev9 bluetooth/internet self-encoded modules
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_concentrated_naming(self, fle_ext: str, lib_nm: str, folder_path):
        # applies naming aspects to modules, interfaces, classes, functions and variables
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_preform_priority_tree(self, is_bypass_route_dsg: bool, build_folder: str):
        # creates a read/write capable branched structured file for abstract reasoning of encoded templates in the rev zip file
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_map(self, is_read: bool, is_backup: bool, dsg: str, source:str, dir_path: str) -> int:
        # does all read and/or write of rev9 source files
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_get_header(self, mdl_dsg: str, py_name:str, py_intrfc_name: str, py_imports: list) -> str:
        # returns header text for a py module
        raise NotImplementedError
        
    @abc.abstractmethod
    def rev9_ocudlr(self, ltr: str) -> str:
        # returns path indicators for console prints
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def rev9_cleanup_directory(self, folder_path):
        # removes build structure files used for modules creations
        raise NotImplementedError