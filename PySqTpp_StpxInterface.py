# Code File: StaqTapp-1.02 PySqTpp_StpxInterface.py] StaqTapp stpx interface class


# Staqtapp 1.02.445

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

class PySqTppStpxInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'stpx_set_path') and callable(subclass.stpx_set_path) and hasattr(subclass, 'stpx_get_path') and callable(subclass.stpx_get_path) and hasattr(subclass, 'stpx_add_list_vars') and callable(subclass.stpx_add_list_vars) and hasattr(subclass, 'stpx_get_list_vars') and callable(subclass.stpx_get_list_vars) and hasattr(subclass, 'stpx_find_data') and callable(subclass.stpx_find_data) and hasattr(subclass, 'stpx_remove_vars') and callable(subclass.stpx_remove_vars) and hasattr(subclass, 'stpx_backups') and callable(subclass.stpx_backups) and hasattr(subclass, 'stpx_get_menorah_palindrome_encoding') and callable(subclass.stpx_get_menorah_palindrome_encoding) or NotImplemented)
        
        
    @abc.abstractmethod
    def stpx_set_path(dir_path: str, source_name: str):
        # creates gzip stpx folder/file if not present, sets directory/file path for all stpx functions
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_get_path(full_curr_path: str) -> list:
        # returns the path list from read gzip stack to all stpx's module function call
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_add_list_vars() -> int:
        # adds glb var names @ gzip file from current set .tqpt file path, returns replaced total if present
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_get_list_vars(is_sorted: bool) -> list:
        # returns var names list from gzip file from the set .tqpt file path
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_find_data(isRegx: bool, varNames: list, search):
        # returns list of var_name + var_data sequences of searched .tqpt set path source
        raise NotImplementedError
        
    
    @abc.abstractmethod
    def stpx_remove_vars(is_backup: bool, var_names) -> bool:
        # deletes any valid glb .tqpt variable(s) found from @var_names, returns true if did remove(s)
        # also removes any glb variables connected to a .tpqt lock source file if any during remove(s)
        # performs a backup of the .tqpt source file to a gzip file in .../stpx folder if @is_backup=True
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_backups(is_write: bool, dsg: str, pthLst: list):
        # performs staqtapp-stpx pro related backup procedures
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def stpx_get_menorah_palindrome_encoding(isGreater: bool, src: str):
        # compressed unique int return from a menorah palindrome equality rendered
        # using rotational variable multi-loop counts & other non-nothing abstracts
        raise NotImplementedError
        
        
        
        
        