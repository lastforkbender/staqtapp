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
import secrets
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
# __________________________________________________________________________________

class VFS():
      
    def __init__(self, fn: str):
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
            self._fx = False
            return -3
        self._fx = True
        return 2
# __________________________________________________________________________________

    def _vfs_dirslc(self, stk: bool, fndS, fndE) -> list:
        lenS = len(fndS)
        pntLst = [self._fl.find(fndS),self._fl.find(fndE)]
        if not stk:
            return [self._fl[0:pntLst[0]+lenS],self._fl[pntLst[0]+lenS+1:pntLst[1]-1],self._fl[pntLst[1]:len(self._fl)]]
        else:
            return [self._fl[0:pntLst[0]+lenS],b'...',self._fl[pntLst[1]:len(self._fl)]]
# __________________________________________________________________________________

    def _vfs_wrtstg(self, ptrn: str, stg: str, src):
        with open(f'{self._cf}/{self._fn}',mode='r+b') as fWrObj:
            cnts = fWrObj.read()
            ptrn = re.findall(bytes(ptrn,'utf-8'),cnts)
            fWrObj.seek(0,0)
            fWrObj.write(cnts.replace(ptrn[0],bytes(stg,'utf-8')+src+b'>'))
# __________________________________________________________________________________

    def _vfs_lstdir(self, dirPth: str) -> list:
        if not self._fx:
            if self._vfs_opnfl() < 0:
                return -3
        lstDir = []
        rltLst = re.findall(b'\/\/'+re.escape(str.encode(dirPth,'utf-8'))+b'\/.*?\/',self._fl)
        for x in range(len(rltLst)): lstDir.append(rltLst[x])
        return lstDir
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
                        dirLst = None
                        dirStk = False
                        slcLst = None
                        if cLen==2 and nwPth[0]=='v' and nwPth[1]=='sk':
                            dirLst = self._vfs_lstdir('sk')
                            if len(dirLst) > 0: dirStk = True
                            if dirStk:
                                dirType = ['●-□','v/sk/',f'◇{bytes.decode(dirLst[0],"utf-8")}']
                            else: dirType = ['●-□','v/sk/','---◇-sk-']
                        elif cLen==3 and nwPth[0]=='v' and nwPth[1]=='sk' and nwPth[2]=='sys':
                            dirLst = self._vfs_lstdir('sys')
                            if len(dirLst) > 0: dirStk = True
                            if dirStk:
                                dirType = ['○-■','v/sk/sys/',f'◇{bytes.decode(dirLst[0],"utf-8")}']
                            else: dirType = ['○-■','v/sk/sys/','---◇-sys-']
                        elif cLen==4 and nwPth[0]=='v' and nwPth[1]=='sk' and nwPth[2]=='sys' and nwPth[3]=='env':
                            dirLst = self._vfs_lstdir('env')
                            if len(dirLst) > 0: dirStk = True
                            if dirStk:
                                dirType = ['●-■','v/sk/sys/env/',f'◇{bytes.decode(dirLst[0],"utf-8")}']
                            else: dirType = ['●-■','v/sk/sys/env/','---◇-env-']
                        else:
                            return -4
                        if self._fl.find(bytes(f'◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/','utf-8')) > -1:
                            return -5
                        else:
                            slcLst = self._vfs_dirslc(dirStk,bytes(f'{dirType[0]}{dirType[1]}','utf-8'),bytes(dirType[2],'utf-8'))
                            if slcLst[1] == b'...':
                                slcLst[1] = bytes(f'◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/\n...\n---◇-{nwPth[len(nwPth)-1]}-','utf-8')
                            else:
                                slcLst[1] = bytes(f'{slcLst[1]}\n◇//{nwPth[len(nwPth)-2]}/{nwPth[len(nwPth)-1]}/\n...\n---◇-{nwPth[len(nwPth)-1]}-','utf-8')
                            with open(f'{self._cf}/{self._fn}',mode='wb') as fMkDirObj: fMkDirObj.write(b'\n'.join(slcLst))
                            slcLst = None
                            if self._vfs_opnfl() < 0:
                                return -3
                            else:
                                return 3
                    else:
                        return -3
            else:
                return -1
        except Exception as err_vfs_mkdir:
            print(err_vfs_mkdir)
# __________________________________________________________________________________

    def _vfs_crtfl(self, pth, src) -> int:
        pass

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

    def _vfs_rsv(self, pD, pK1, pV1, pL1, pK2, pK3, pV2, pL2) -> int:
        try:
            rsv = aes.sqtpp_koch_aes_encode_data(pD,pK1,pV1,pL1)
            xrk = bytes(pK2,'utf-8')
            bRy = bytearray()
            for x in range(len(rsv)):bRy.append(rsv[x]^xrk[x%len(xrk)])
            rsv = pL2
            xrk = bytes(aes.sqtpp_koch_aes_encode_data(bRy,pK3,pV2,pL2))
            bRy = pL1
            self._vfs_wrtstg('RSV<.*?>','RSV<',xrk)
            if self._vfs_opnfl() == -3:
                return -3
            else:
                return 4
        except Exception as err_vfs_rsv:
            print -7
# __________________________________________________________________________________

    def _vfs_lck(self, src, ky, iv, blkSz: int):
        try:
            src = xortl.sqtpp_koch_xortl(True,src,ky,iv,blkSz)
            self._vfs_wrtstg('LCK<.*?>','LCK<',src)
        except Exception as err_vfs_lck:
            self._vfs_wrtstg('LCK<.*?>','LCK<',b'TIMELOCK')
        if self._vfs_opnfl() == -3:
            return -3
        else:
            return 5
# __________________________________________________________________________________

    def _vfs_pntbrk(self, cmd: list, bExt: list):
        cmds = None
        rtrn = None
        for s in range(len(cmd)):
            if cmd[s].find('ltdir(') > -1:
                cmds = cmd[s].replace('lstdir(','').strip(')')
                rtrn = self._vfs_ltdir(cmds)
            elif cmd[s].find('mkdir(') > -1:
                cmds = cmd[s].replace('mkdir(','').strip(')')
                rtrn = self._vfs_mkdir(cmds)
            elif cmd[s].find('cfg(') > -1:
                pass
            elif cmd[s].find('rsv(') > -1:
                cmds = cmd[s].replace('rsv(','').strip(')').split(',')
                rtrn = self._vfs_rsv(bExt[0],bExt[1],bExt[2],int(cmds[0]),cmds[1],bExt[3],bExt[4],int(cmds[2]))
            elif cmd[s].find('lck(') > -1:
                cmds = cmd[s].replace('lck(','').strip(')')
                rtrn = self._vfs_lck(bExt[0],bExt[1],bExt[2],int(cmds))
            if isinstance(rtrn,int):
                if rtrn < 0:
                    break
        return rtrn
# __________________________________________________________________________________

def sqtpp_koch_vfs(fn: str, cmnds: list, btsExt: list):
    cls = VFS(fn)
    return cls._vfs_pntbrk(cmnds,btsExt)


#print(sqtpp_koch_vfs('sk-vfs-0001.envfs',['mkdir(v/sk/sys/top_path)'],[None]))
















