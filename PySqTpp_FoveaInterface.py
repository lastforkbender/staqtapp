# Code File: StaqTapp-1.02 [PySqTpp_FoveaInterface.py] StaqTapp's Stpx Fovea Interpreter Interface


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

class PySqTppFoveaInterface(metaclass=abc.ABCMeta):
    
    
    @classmethod
    def __subclasshook__(cls, subclass):
        # subclasshook for the abstract methods defines
        return (hasattr(subclass, 'fovea_mantis_absorb') and callable(subclass.fovea_mantis_absorb) and hasattr(subclass, 'fovea_mantis_echo') and callable(subclass.fovea_mantis_echo) and hasattr(subclass, 'fovea_mantis_algo') and callable(subclass.fovea_mantis_algo) and hasattr(subclass, 'fovea_mantis_list_edits') and callable(subclass.fovea_mantis_list_edits) and hasattr(subclass, 'fovea_mantis_map') and callable(subclass.fovea_mantis_map) or NotImplemented)
        
        
    @abc.abstractmethod
    def fovea_mantis_absorb(x_src, fPth: str) -> bool:
        # determines view/direction of the instruction set; and create of a .qpsx script file of
        # the file's header data & XKTG magic string -- if source is not a .qpsx script file path
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def fovea_mantis_echo(x_src: list):
        # determines any nest type scripting use of g-prefix-keywords(sph, gph or avl, gvl)
        # params & routines of calling the correct functions in sequence to [XKTG | XKGT]
        raise NotImplementedError
        
    
    @abc.abstractmethod
    def fovea_mantis_algo(isLoop: bool, dsg: int, prefix: list, currDrvr: list) -> list:
        # determines the magic string XKTG | XKGT depends, order and/or change
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def fovea_mantis_list_edits(dsg: str, lstSrc: list) -> list:
        # specific edits of list for source instruction sets and other needed list structuring
        raise NotImplementedError
        
        
    @abc.abstractmethod
    def fovea_mantis_map(dsg: str, pth: str):
        # # handles all read, search, write or replace methods for this module's parsings
        raise NotImplementedError
        