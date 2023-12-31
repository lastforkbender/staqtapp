# Code File: StaqTapp-1.02 [PySqTpp_SarInterface.py] StaqTapp S.A.R. main interface class


# Staqtapp 1.02.460

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

class PySqTppSarInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'extr_load_sar_remap') and callable(subclass.extr_load_sar_remap) and hasattr(subclass, 'sar_map') and callable(subclass.sar_map) and hasattr(subclass, 'acquired_tqpt_source') and callable(subclass.acquired_tqpt_source) and hasattr(subclass, 'write_extension_source') and callable(subclass.write_extension_source) and hasattr(subclass, 'char_bridge') and callable(subclass.char_bridge) and hasattr(subclass, 'word_bridge') and callable(subclass.word_bridge) or NotImplemented)
    
    
    @abc.abstractmethod
    def extr_load_sar_remap(self, is_prm_exchng: bool, cat_pin: str, dir_path: str) -> int:
        # determines pattern cluster & assemble instructions rotations to grouped category pin variables
        # returns a str list of the instructions in sequence order via set branching & r-temple %attrs/%xn's
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def sar_map(self, is_read: bool, dsg_fnc: str, full_path: str):
        # read or write instructions with sar methods
        raise NotImplementedError
        
    
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
