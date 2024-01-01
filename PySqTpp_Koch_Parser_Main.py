# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.024
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_Parser_Main.py


# ● ■  Description of this module's purpose:
    
#       This module is the main parsing unit for all .stkv env-var files.
#       Integrated for __slots__ performances and handling of specialized
#       features that are included of this version of Staqtapp throughout.
#       Discrete before-error validations implemented as original version.


# ● ■  Staqtapp-Koch Env-Vars Library Overview:

#       The scope of this env-vars system is routine focused upon env-var
#       security via obfuscated addresses inter-connected to env-vars own
#       obfuscation of it's data, using tor like circumstances, procedural
#       generation of env-var keys/spacing and one-way shared descriptors.

#       Having limited made keys outside this env-var system for access of
#       advanced security issue... if chosen of a needed env-vars solution.
#       Of then a email response will be given for a phone number to call,
#       involving a signature and purchase after agreed terms are met, then
#       custom built Staqtapp-Koch full package library for your key sent.
#       Pricing terms for single package is $318 U.S. dollars, however ---
#       is variable to the conditions of use.(This public version does not
#       include those strong fractal-palindrome based security modules.)

    
# Contact: rcttcr5@gmail.com
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________


# Imported core python module(s) for this module's objectives.
from collections import deque
import mmap
import os
import re
# __________________________________________________________________________________
# __________________________________________________________________________________

class PySqTpKhMnPr:
    
    __slots__ = ('varname', 'vardata')

    # The two-way parameter for env-var formats.
    def __init__(self, varname, vardata):
        self.varname = varname
        self.vardata = vardata

    # Define __slots__ return handle as string property returns.
    def __str__(self):
        return f'{self.varname}={self.vardata}'

    def rename(self, newvarname):
        self.varname = newvarname

    def changedata(self, newvardata):
        self.vardata = newvardata
# __________________________________________________________________________________
# __________________________________________________________________________________

class PySqTpKhMnPr_Accs:
    
    def __init__(self, filepath, source):
        self.filepath = filepath
        self.source = source
        self.envvars = deque()
        self.sqtpp_koch_set_stkv_file(filepath, source)
# __________________________________________________________________________________

    def sqtpp_koch_set_stkv_file(self, pth: str, src: list):
        
        #**To be called first before any env-var interactions**
        
        # Makes proper checks & creates new file if any, then
        # calls @sqtpp_koch_parse_stkv_content() for appending.
        # This is main difference from original staqtapp; this
        # version loads all variables @ file on first read ---
        # making it true __slots__ environment variable system.
        try:
            if isinstance(pth, str):
                # Check if given filepath already exist...
                if os.path.isfile(pth):
                    # Is valid, initialize the envvars/access manage complete.
                    self.sqtpp_koch_parse_stkv_content()
                else:
                    # Env-var file is not present, check folder
                    # path is valid by split and a rejoin find.
                    if pth.find('/') > -1:
                        pth = pth.split('/')
                        fLn = len(pth)
                        fNm = None
                        if fLn > 1:
                            fNm = pth[fLn-1]
                            pth.pop(fLn-1)
                            pth = '/'.join(pth)
                            if os.path.isdir(pth):
                                # Check if @fNm is of valid chars for a filename.
                                if self.sqtpp_koch_validate_str(fNm):
                                    # Is there env-vars to add of this new file @src,
                                    # if so check if is a list and in proper formats.
                                    if len(src) > 0:
                                        if isinstance(src, list):
                                            pass
                                        else:
                                            raise Exception("staqtapp-koch error<set_file>: @source for new env-vars file not of a list type")
                                    else:
                                        # Make the new file with a temp variable add.
                                        pass
                                else:
                                    raise Exception("staqtapp-koch error<set_file>: filename has invalid chars, valid chars _- aA-zZ 0-9")
                            else:
                                raise Exception("staqtapp-koch error<set_file>: file path is not valid")
                        else:
                            raise Exception("staqtapp-koch error<set_file>: file path is not valid")
                    else:
                        raise Exception("staqtapp-koch error<set_file>: file path is not valid")
                    self.sqtpp_koch_parse_stkv_content()
            else:
                raise Exception("staqtapp-koch error<set_file>: file path must be of a str type")
        except Exception as mnpr_sksf_err:
            print("staqtapp-koch error<set_file>: ", mnpr_skrf_err)
# __________________________________________________________________________________

    def sqtpp_koch_parse_stkv_content(self):
        
        # Is the manage class set filepath a valid file?
        if os.path.isfile(self.filepath):
            try:
                envVrLst = None
                # Get the mmap'd file object to a non-byte list converted reading.
                with open(self.filepath, mode='r') as flObjRf:
                    with mmap.mmap(flObjRf.fileno(), length=0, access=mmap.ACCESS_READ) as mpObjRf:
                        envVrLst = bytes.decode(mpObjRf.read(), 'utf-8').split('\n')
                        mpObjRf.close()
                    # Eradicate the mmap file object.
                    mpObjRf = None
                envVrLstLen = len(envVrLst)
                if envVrLstLen > 1:
                    if envVrLst[0].find('POS:') and envVrLst[0].find('CLP:'):
                        # Parse header data/settings/formulas/etc. to koch gzip file.
                        self.sqtpp_koch_parse_special_content(True, envVrLst[0])
                    envVrLst.pop(0)
                    # Finds & appends all valid env-vars to deque @ __slots__ involved.
                    ptrn = r'^(?P<varname>\w+)=(?P<vardata>.*)$'
                    vrFnd = False
                    mtch = None
                    for v in range(envVrLstLen):
                        mtch = re.match(ptrn, envVrLst[v])
                        if mtch:
                            if not vrFnd: vrFnd = True
                            self.envvars.append(PySqTpKhMnPr(mtch.group('varname'), mtch.group('vardata')))
                else:
                    # File's content is of no sound order to parse.
                    raise Exception("staqtapp-koch error<read_file>: file is a non-reachable content or is corrupted")
            except Exception as mnpr_skrf_err:
                print("staqtapp-koch error<read_file>: ", mnpr_skrf_err)
        else:
            raise Exception("staqtapp-koch error<read_file>: file path was not found")
# __________________________________________________________________________________

    def sqtpp_koch_parse_special_content(self, isHdr, src):
        
        if isHdr:
            # Below are the 12 possible header types for .stkv staqtapp-koch
            # file. All U* regions are decimal record; IA and WR as int type
            # record further, also a same for POS & CLP. The last three ----
            # ORDER, METHOD and EXPIRE are all equation pairings if applied.
            
            # UY:d,UR:d,UM:d,UL:d,IA:i,WR:i,POS:i,CLP:i,ORDER:f,METHOD:f,EXPIRE:f
            
            src = src.replace(':', "").strip(' ').split(',')
            
# __________________________________________________________________________________

    def sqtpp_koch_stkv_add_var(self, var):
        self.envvars.append(var)
# __________________________________________________________________________________

    def sqtpp_koch_stkv_remove_var(self, var):
        self.envvars.remove(var)
# __________________________________________________________________________________

    def sqtpp_koch_save_stkv_file(self):
        
        # Saves the entire set of env-vars to file
        with open(self.file_path, mode='w', encoding='utf-8') as flObjSf:
            for envvar in self.envvars:
                flObjSf.write(f'{envvar.varname}={envvar.vardata}\n')
            flObjSf.close()
        flObjSf = None
# __________________________________________________________________________________

    def sqtpp_koch_validate_str(self, src):
        
        # Checks if @src is of valid chars by a subset deduction.
        alwdChrs = set("_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        if set(src).issubset(alwdChrs):
            return True
        else:
            return False
# __________________________________________________________________________________




