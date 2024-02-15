# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_DCY.py


# ● ■  Description of this module's purpose:
    
#       This module makes decoy/dummy vfs directories & files. This is the
#       public version of this feature, contained in this module only. The
#       more secure version of Staqtapp-Koch uses ml and urls for this. Is
#       for protecting the .envfs file upfront; the code is commented here.
#       However the more secure version of this library is not freeware.


# ● ■  Staqtapp-Koch Env-Vars Library Overview:

#       The current project status is critical to implementing security
#       values of env-var use not seen before or done before. In focus
#       of forthcoming advances, this env-var library is being built of
#       a proposed system that forms a basis of complex abstractions to
#       isolate those security values. Whereof any considerations into
#       env-var security that would involve other discrete methods inact
#       to placements of env-var use, those outer models of access or no.
#       This library using fractal based rotational palindrome settings
#       of env-var use and of extreme cut-off for modern ai comprehension
#       if applied correctly as a modular sub-system approach.

    
# Contact: rcttcr5@gmail.com
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________
# __________________________________________________________________________________


# Imported core python module(s) for this module's objectives.
import secrets as scs
import random as rdm
import string as srg

# Imported PySqTpp_Koch module(s) for this module's objectives.
from PySqTpp_Koch_VFS import sqtpp_koch_vfs
# __________________________________________________________________________________

def _vfs_mkdcy(vfsFlnm: str, isDF: bool, src: str, vfsPth: str) -> bool:
    # ::PUBLIC VERSION::
    
    # PARAMETERS:
    # Either is a empty decoy directory, decoy directory and
    # a empty file or decoy directory and decoy file(@isDF)
    # (@src str is used for the file's contents if as given)
    # This ver. does not do any encryption of @src input; or
    # use any type machine learning of this feature further.
    # (..if a @src str, must be bytes string for vfs writes)
        
    # Random select of a main vfs directory .../sk/, .../sys/ or .../env/
    # ..or optional parameter vfsPth is set to 'sk', 'sys' or 'env'
    try:
        pth = None
        pthSwA = False
        if len(vfsPth) > 0:
            if vfsPth == 'sk':
                pth = 'v/sk/'
                pthSwA = True
            elif vfsPth == 'sys':
                pth = 'v/sk/sys/'
                pthSwA = True
            elif vfsPth == 'env':
                pth = 'v/sk/sys/env/'
                pthSwA = True
        if not pthSwA:
            if rdm.randint(1,99)>=61 and rdm.randint(1,99)<=83:
                pth = 'v/sk/'
                vfsPth = 'sk'
            elif rdm.randint(1,99)<=51 and rdm.randint(1,99)>=73:
                pth = 'v/sk/sys/'
                vfsPth = 'sys'
            elif rdm.randint(1,99)>=41 and rdm.randint(1,99)<=63:
                pth = 'v/sk/sys/env/'
                vfsPth = 'env'
            else:
                if rdm.randint(1,99)<=41 and rdm.randint(1,99)>=63:
                    pth = 'v/sk/'
                    vfsPth = 'sk'
                elif rdm.randint(1,99)>=51 and rdm.randint(1,99)<=73:
                    pth = 'v/sk/sys/'
                    vfsPth = 'sys'
                elif rdm.randint(1,99)<=61 and rdm.randint(1,99)>=83:
                    pth = 'v/sk/sys/env/'
                    vfsPth = 'env'
                else:
                    if rdm.randint(1,99)>=41:
                        pth = 'v/sk/sys/env/'
                        vfsPth = 'env'
                    else:
                        pth = 'v/sk/sys/'
                        vfsPth = 'sys'
        rdm_sub_dir = lambda s,e: ''.join(rdm.choice(rdm.sample(srg.ascii_letters,k=10)+['_']) for _ in range(rdm.randint(s,e)))
        # A dummy vfs sub-directory of random letters + random placed underscores.
        dcyDir = rdm_sub_dir(17,rdm.randint(18,42))
        # Fake directory will get seten-addr klp-length XOR encryption, three keys.
        # The seten-addr XOR type encryption has padding & block ciphering shifting.
        # Is not a multiple layered AES encryption routing as done on env-var data,
        # however is prone to adding multiple newlines---making the taking apart of
        # the vfs file for analysis useless if many of these vfs decoy directories.
        # Reverse parsing tools will fail on the encoded padding lengths separated,
        # similar to space-shift encryption seen in embedded firmware protections.
        kChrs = 'abcdefghijklmnopqrstuvwxyz0123456789?$&#*%!'
        kLst = []
        for x in range(3): kLst.append(''.join(scs.choice(kChrs) for ___ in range(16)))
        if isDF:
            # A decoy vfs encrypted directory and a decoy file via @src is expected.
            # Call vfs mdl-cmds to make dir and encrypt it. Return will be enc-dir.
            # A parameter can be added to this method for a seten-addr, other than
            # the one used for this set of vfs commands. Must be a valid seten-addr.
            dcyDir = sqtpp_koch_vfs(vfsFlnm,[f'mkdir({pth}{dcyDir})',f'encdir({vfsPth}/{dcyDir},1,seten,{kLst[0]},{kLst[1]},{kLst[2]},rViHqtAinoZarvltksmR'],[None])
            sqtpp_koch_vfs(vfsFlnm,[f'crtfl({vfsPth}/{dcyDir})'],[src])
            return dcyDir
        else:
            # A empty directory or not, encrypted.
            pass
    except Exception as err_vfs_mkdcy:
        return err_vfs_mkdcy
         
                
#def test():  
     #print(_vfs_mkdcy('sk-vfs-0001.envfs', True, str.encode(']aaaaa-bbbbb-ccccc-0001-enc[\nThis fake files contents.\n---[aaaaa-bbbbb-ccccc-0001-enc]-'),'sys'))    
#test()















