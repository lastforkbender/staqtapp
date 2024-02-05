# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_VFS.py


# ● ■  Description of this module's purpose:
    
#       This module is the virtual file system for Staqtapp-Koch library.


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
import os
import re

# Imported PySqTpp_Koch module(s) for this module's objectives.
import PySqTpp_Koch_XORTL as xortl
import PySqTpp_Koch_AES as aes
# __________________________________________________________________________________

# VFS FUNCTIONS' INT RETURNS:
    
    # NO ERRORS: 
    #  1  = .envfs file is there
    #  2  = .envfs file was read without error
    #  3  = mkdir finished without error
    #  4  = rsv number change finished without error
    #  5  = lck sequence change finished without error
    
    # ERRORS:
    # -1  = missing sqtpp-koch folder
    # -2  = write new .envfs file error
    # -3  = .envfs file read error
    # -4  = mkdir parameter path error
    # -5  = mkdir parameter path already exist
    # -6  = could not perform mkdir
    # -7  = rsv change error
    # -8  = lck change error
# __________________________________________________________________________________

class VFS():
      
    def __init__(self, fn):
        self._cf = crr_pth = f'{os.path.dirname(os.path.abspath(__file__))}/sqtpp-koch'
        self._fn = fn
        self._fc = self._vfs_flchk()
        self._fl = None
        self._fx = False
# __________________________________________________________________________________

    def _vfs_flchk(self) -> int:
        if os.path.isdir(self._cf):
            # VFS file naming, sk-vfs-####.envfs
            if os.path.isfile(f'{self._cf}/{self._fn}'):
                return 1
            else:
                # Make new .envfs file.
                structLst =['● ■ Staqtapp-Koch V.F.S.(v2.01.079)\n']
                structLst.append('____________________________________________________________\n○-◇CFG<UY:?,UR:?,UM:?,UL:?,IA:?,WR:?,POS:?,CLP:?,ORDER:?,METHOD:?,EXPIRE:?>\n')
                structLst.append('____________________________________________________________\n○-◇RSV<...>\n')
                structLst.append('____________________________________________________________\n○-◇LCK<...>\n\n')
                structLst.append('○-□v/\n...\n---◇-v-\n●-□v/sk/\n...\n---◇-sk-\n○-■v/sk/sys/\n...\n---◇-sys-\n●-■v/sk/sys/env/\n...\n---◇-env-\n')
                try:
                    with open(f'{self._cf}/{self._fn}',mode='w',encoding='utf-8') as fNwEnvFsObj:
                        fNwEnvFsObj.write(''.join(structLst))
                except Exception as err_vfs_flchk:
                    return -2
                return 1
        else:
            return -1
# __________________________________________________________________________________

    def _vfs_opnfl(self) -> int:
        try:
            with open(f'{self._cf}/{self._fn}',mode='rb') as fVfsObj:
                self._fl = fVfsObj.read()
        except Exception as err_vfs_opnfl:
            return -3
        self._fx = True
        return 2
# __________________________________________________________________________________

    def _vfs_dirsc(self, s, e) -> list:
        pntLst = [self._fl.find(s),self._fl.find(e)]
        return [self._fl[0:pntLst[0]+len(s)],self._fl[pntLst[0]+len(s)+1:pntLst[1]-1],self._fl[pntLst[1]:len(self._fl)]]
# __________________________________________________________________________________

    def _vfs_wrtstg(self, ptrn: str, stg: str, src):
        with open(f'{self._cf}/{self._fn}',mode='r+b') as fWrObj:
            cnts = fWrObj.read()
            ptrn = re.findall(bytes(ptrn,'utf-8'),cnts)
            fWrObj.seek(0,0)
            fWrObj.write(cnts.replace(ptrn[0],bytes(stg,'utf-8')+src+b'>'))
# __________________________________________________________________________________

    def _vfs_mkdir(self, nwPth: str) -> int:
        # Allowed add dir: v/sk/<nwPth> or v/sk/sys/<nwPth> or v/sk/sys/env/<nwPth>
        try:
            if self._fc == 1:
                if not self._fx:
                    if self._vfs_opnfl() == 2:
                        nwPth = nwPth.split('/')
                        cLen = len(nwPth)-1
                        dirTyp = None
                        slcLst = None
                        if cLen==2 and nwPth[0]=='v' and nwPth[1]=='sk':
                            dirType = ['●-□','v/sk/','---◇-sk-']
                        elif cLen==3 and nwPth[0]=='v' and nwPth[1]=='sk' and nwPth[2]=='sys':
                            dirType = ['○-■','v/sk/sys/','---◇-sys-']
                        elif cLen==4 and nwPth[0]=='v' and nwPth[1]=='sk' and nwPth[2]=='sys' and nwPth[3]=='env':
                            dirType = ['●-■','v/sk/sys/env/','---◇-env-']
                        else:
                            return -4
                        if self._fl.find(bytes(f'◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/','utf-8')) > -1:
                            return -5
                        else:
                            slcLst = self._vfs_dirsc(bytes(f'{dirType[0]}{dirType[1]}','utf-8'),bytes(dirType[2],'utf-8'))
                            if slcLst[1] == b'...':
                                slcLst[1] = bytes(f'◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/\n...\n---◇-{nwPth[len(nwPth)-1]}-','utf-8')
                            else:
                                slcLst[1] = bytes(f'{slcLst[1]}\n◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/\n...\n---◇-{nwPth[len(nwPth)-1]}-','utf-8')
                            with open(f'{self._cf}/{self._fn}',mode='wb') as fMkDirObj: fMkDirObj.write(b'\n'.join(slcLst))
                            slcLst = None
                            return 3
                    else:
                        return -3
            else:
                return -1
        except Exception as err_vfs_mkdir:
            return -6
# __________________________________________________________________________________

    def _vfs_cfg(self, rst: bool, dsg: str, vls: list) -> int:
        # vls/UY:d,UR:d,UM:d,UL:d,IA:i,WR:i,POS:i,CLP:i,ORDER:f,METHOD:f,EXPIRE:f
        if not rst:
            if dsg == 'yrml':
                pass
            elif dsg == 'iwpc':
                pass
            elif dsg == 'order':
                pass
            elif dsg == 'method':
                pass
            elif dsg == 'expire':
                pass
        else:
            pass
# __________________________________________________________________________________

    def _vfs_rsv(self, rsvNum: list) -> int:
        try:
            rsv = aes.sqtpp_koch_aes_encode_data(rsvNum[0],rsvNum[1],rsvNum[2],rsvNum[3])
            xrk = bytes(rsvNum[4],'utf-8')
            bRy = bytearray()
            for x in range(len(rsv)):bRy.append(rsv[x]^xrk[x%len(xrk)])
            rsvNum = bytes(aes.sqtpp_koch_aes_encode_data(bRy,rsvNum[5],rsvNum[6],rsvNum[7]))
            self._vfs_wrtstg('RSV<.*?>','RSV<',rsvNum)
            if self._vfs_opnfl() == -3:
                return -3
            else:
                return 4
        except Exception as err_vfs_rsv:
            return -7
# __________________________________________________________________________________

    def _vfs_lck(self, src, ky, iv, blkSz):
        try:
            xrtl = xortl.sqtpp_koch_xortl(True,src,ky,iv,blkSz)
            self._vfs_wrtstg('LCK<.*?>','LCK<',xrtl)
        except Exception as err_vfs_lck:
            self._vfs_wrtstg('LCK<.*?>','LCK<',b'TIMELOCK')
        if self._vfs_opnfl() == -3:
            return -3
        else:
            return 5
# __________________________________________________________________________________

#def test():
    #cls = VFS('sk-vfs-0001.envfs')
    #import secrets
    #print(cls._vfs_lck(bytes('500438202228711904238550','utf-8'),secrets.token_bytes(256),secrets.token_bytes(16),16))
#test()

