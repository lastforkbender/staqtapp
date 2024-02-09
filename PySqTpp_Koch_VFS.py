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
import random
import secrets
import os
import re

# Imported PySqTpp_Koch module(s) for this module's objectives.
import PySqTpp_Koch_Immersion as immr
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
    #  6  = crtfl finished without error
    
    # ERRORS:
    # -1  = missing sqtpp-koch folder
    # -2  = write new .envfs file error
    # -3  = .envfs file read error
    # -4  = mkdir parameter path error
    # -5  = mkdir parameter path already exist
    # -6  = could not perform mkdir
    # -7  = rsv change error
    # -8  = crtfl parameter path not found
    # -9  = could not perform crtfl
    # -10 = encdir parameter path not found
    # -11 = encdir seten module addr not found
    
# __________________________________________________________________________________

class VFS():
      
    def __init__(self, fn: str):
        self._cf = crr_pth = f'{os.path.dirname(os.path.abspath(__file__))}/sqtpp-koch'
        self._fn = fn
        self._fc = self._vfs_flchk()
        self._fs = self._vfs_adrsec('Seten')
        self._fl = None
        self._fx = False
        self._fsx = False
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

    def _vfs_adrsec(self, w):
        fLst = list(os.listdir(os.path.dirname(os.path.abspath(__file__))))
        fLst = list(filter(lambda x: w in x, fLst))
        cLst = None
        f = 0
        while f < len(fLst):
            if len(fLst[f]) == 42:
                cLst = fLst[f].replace('.py',"").split('_')
                fLst[f] = cLst[3]
            else:
                fLst.pop(f)
                f-=1
            f+=1
        self._fsx = True
        return fLst
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
        if not self._fx:
            if self._vfs_opnfl() < 0:
                return -3
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
        sPrt = bytes('\◇\/\/','utf-8')
        rltLst = re.findall(sPrt+re.escape(str.encode(dirPth,'utf-8'))+b'\/.*?\/',self._fl)
        for x in range(len(rltLst)): rltLst[x] = bytes.decode(rltLst[x],'utf-8')
        return rltLst
# __________________________________________________________________________________

    def _vfs_mkdir(self,__) -> int:
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_opnfl()==2:
                        __=__.split('/')
                        ______=False
                        ___=len(__)-1
                        ____=None
                        _____=None
                        _______=None
                        if ___==2 and __[0]=='v' and __[1]=='sk':
                            _____=self._vfs_lstdir('sk')
                            if len(_____)>0:______=True
                            if ______:____=['●-□','v/sk/',_____[0]]
                            else:____=['●-□','v/sk/','---◇-sk-']
                        elif ___==3 and __[0]=='v' and __[1]=='sk' and __[2]=='sys':
                            _____=self._vfs_lstdir('sys')
                            if len(_____)>0:______=True
                            if ______:____=['○-■','v/sk/sys/',_____[0]]
                            else:____=['○-■','v/sk/sys/','---◇-sys-']
                        elif ___==4 and __[0]=='v' and __[1]=='sk' and __[2]=='sys' and __[3]=='env':
                            _____=self._vfs_lstdir('env')
                            if len(_____)>0:______=True
                            if ______:____=['●-■','v/sk/sys/env/',_____[0]]
                            else: ____=['●-■','v/sk/sys/env/','---◇-env-']
                        else:
                            return -4
                        if self._fl.find(bytes(f'◇//{__[len(__)-2]}/{__[len(__)-1]}/','utf-8'))>-1:
                            return -5
                        else:
                            _______=self._vfs_dirslc(______,bytes(f'{____[0]}{____[1]}','utf-8'),bytes(____[2],'utf-8'))
                            if _______[1]==b'...':_______[1]=bytes(f'◇//{__[len(__)-2]}/{__[len(__)-1]}/\n...\n---◇-{__[len(__)-1]}-','utf-8')
                            else: _______[1]=bytes(f'{_______[1]}\n◇//{__[len(__)-2]}/{__[len(__)-1]}/\n...\n---◇-{__[len(__)-1]}-','utf-8')
                            with open(f'{self._cf}/{self._fn}',mode='wb') as fMkDirObj:fMkDirObj.write(b'\n'.join(_______))
                            _______=None
                            if self._vfs_opnfl()<0:
                                return -3
                            else:
                                return 3
                    else:
                        return -3
            else:
                return -1
        except Exception as err_vfs_mkdir:
            return -6
# __________________________________________________________________________________

    def _vfs_encdir(self, pth, islobe, dsg, xnrA, xnrB, xnrC, stnAdr):
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_opnfl() < 0:
                        return -3
                pthLst = pth.split('/')
                if self._fl.find(bytes(f'◇//{pthLst[0]}/{pthLst[1]}/','utf-8')) > -1:
                    xnr = None
                    encStn = None
                    if islobe > 0:
                        if dsg == 'xnr':
                            xnr = immr.sqtpp_koch_get_addr_xnr_lst(xnrA,xnrB,xnrC,random.randint(32,64))
                            for x in range(len(xnr)): xnr[x] = str(xnr[x])
                            xnr = ''.join(xnr)
                            self._fl = self._fl.replace(bytes(f'◇//{pthLst[0]}/{pthLst[1]}/','utf-8'),bytes(f'◇//{pthLst[0]}/{xnr}/','utf-8'))
                            self._fl = self._fl.replace(bytes(f'---◇-{pthLst[1]}-','utf-8'),bytes('---◇-!!!-','utf-8'))
                        elif dsg == 'seten':
                            if not self._fsx: self._fs = self._vfs_adrsec('Seten')
                            vld = False
                            for sa in range(len(self._fs)):
                                if stnAdr == self._fs[sa]:
                                    vld = True
                                    break
                            if vld:
                                encStnAddr = lambda a,k1,k2,k3: ''.join(''.join(chr(ord(c)^ord(k1)^ord(k2)^ord(k3)) for c,k1,k2,k3 in zip(blk.ljust(8,'!'),k1,k2,k3)) for blk in (a[i:i+8] for i in range(0,len(a),8)))
                                encStn = encStnAddr(stnAdr,xnrA,xnrB,xnrC)
                                self._fl = self._fl.replace(bytes(f'◇//{pthLst[0]}/{pthLst[1]}/','utf-8'),bytes(f'◇//{pthLst[0]}/{encStn}/','utf-8'))
                                self._fl = self._fl.replace(bytes(f'---◇-{pthLst[1]}-','utf-8'),bytes('---◇-!!!-','utf-8'))
                            else:
                                return -11
                    else:
                        # A super complex joined vfs directory, XNR-XOR retained for DRL decipher stacking.
                        # Any env-var having same name in another file, set assigned added cat id to each.
                        pass
                    with open(f'{self._cf}/{self._fn}',mode='wb') as fEncDirObj: fEncDirObj.write(self._fl)
                    if dsg == 'drl-hv':
                        return 'drl-hv not yet implemented'
                    elif dsg == 'xnr':
                        return xnr
                    elif dsg == 'seten':
                        return encStn
                else:
                    return -10
            else:
                return -1 
        except Exception as err_vfs_encdir:
            print(err_vfs_encdir)
            #return -12
# __________________________________________________________________________________

    def _vfs_crtfl(self,____,______) -> int:
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_opnfl()<0:
                        return -3
                __=[0,self._fl.find(bytes(f'◇//{____}/','utf-8'))]
                if __[1]>-1:
                    __[1]=__[1]+len(____)+6
                    ___=____.split('/')
                    __.append(self._fl.find(bytes(f'---◇-{___[len(___)-1]}-','utf-8')))
                    if __[2]>-1:
                        __.append(len(self._fl))
                        _______=lambda ________,_________,__________,___________,____________:(________[_________:__________],________[___________:____________])
                        _____________=_______(self._fl,__[0],__[1],__[2],__[3])
                        with open(f'{self._cf}/{self._fn}',mode='wb') as fNwFlObj:
                            fNwFlObj.write(_____________[0]+b'\n'+______+b'\n'+_____________[1])
                        _____________=None
                        if self._vfs_opnfl()<0:
                            return -3
                        else:
                            return 6
                    else:
                        return -8
                else:
                    return -8
            else:
                return -1
        except Exception as err_vfs_crtfl:
            return -9
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

    def _vfs_rsv(self,__,_______,_____,___________,___,_________,________,_) -> int:
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_opnfl()<0:
                        return -3
                _______________=aes.sqtpp_koch_aes_encode_data(__,_______,_____,___________)
                ______________=bytes(___,'utf-8')
                ____=bytearray()
                for rsv in range(len(_______________)):____.append(_______________[rsv]^______________[rsv%len(______________)])
                _______________=_
                _________________=bytes(aes.sqtpp_koch_aes_encode_data(______________,_________,________,_))
                ______________=___________
                self._vfs_wrtstg('RSV<.*?>','RSV<',_________________)
                if self._vfs_opnfl() == -3:
                    return -3
                else:
                    return 4
            else:
                return -1
        except Exception as err_vfs_rsv:
            print -7
# __________________________________________________________________________________

    def _vfs_lck(self,______,____,________,_______):
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_opnfl()<0:
                        return -3
                ______=xortl.sqtpp_koch_xortl(True,______,____,________,_______)
                self._vfs_wrtstg('LCK<.*?>','LCK<',______)
            else:
                return -1
        except Exception as err_vfs_lck:
            self._vfs_wrtstg('LCK<.*?>','LCK<',b'TIMELOCK')
        if self._vfs_opnfl() == -3:
            return -3
        else:
            return 5
# __________________________________________________________________________________

    def _vfs_pntbrk(self, cmd: list, bExt: list):
        cmds = None
        nmsc = None
        rtrn = None
        for s in range(len(cmd)):
            # _______________LSTDIR__________________________________________
            # _______________________________________________________________
            if cmd[s].find('lstdir(') > -1:
                cmds = cmd[s].replace('lstdir(','').strip(')')
                rtrn = self._vfs_lstdir(cmds)
            # _______________MKDIR___________________________________________
            # _______________________________________________________________
            elif cmd[s].find('mkdir(') > -1:
                cmds = cmd[s].replace('mkdir(','').strip(')')
                rtrn = self._vfs_mkdir(cmds)
            # _______________ENCDIR__________________________________________
            # _______________________________________________________________
            elif cmd[s].find('encdir(') > -1:
                cmds = cmd[s].replace('encdir(','').strip(')').split(',')
                nmsc = int(cmds[1])
                if nmsc == 1 and cmds[2] == 'xnr':
                    rtrn = self._vfs_encdir(cmds[0],nmsc,cmds[2],int(cmds[3]),int(cmds[4]),int(cmds[5]),cmds[6])
                elif nmsc == 1 and cmds[2] == 'seten':
                    rtrn = self._vfs_encdir(cmds[0],nmsc,cmds[2],cmds[3],cmds[4],cmds[5],cmds[6])
                else:
                    pass
            # _______________CRTFL___________________________________________
            # _______________________________________________________________
            elif cmd[s].find('crtfl(') > -1:
                cmds = cmd[s].replace('crtfl(','').strip(')')
                rtrn = self._vfs_crtfl(cmds,bExt[0])
            # _______________CFG_____________________________________________
            # _______________________________________________________________
            elif cmd[s].find('cfg(') > -1:
                pass
            # _______________RSV_____________________________________________
            # _______________________________________________________________
            elif cmd[s].find('rsv(') > -1:
                cmds = cmd[s].replace('rsv(','').strip(')').split(',')
                rtrn = self._vfs_rsv(bExt[0],bExt[1],bExt[2],int(cmds[0]),cmds[1],bExt[3],bExt[4],int(cmds[2]))
            # _______________LCK_____________________________________________
            # _______________________________________________________________
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
    
#print(sqtpp_koch_vfs('sk-vfs-0001.envfs',['encdir(sk/middle_dir,1,seten,uE!8%1F5*45?8Z#7,53#9@7h2C5/3%5R2,*&7!32&j6X%2Q+43,rViHqtAinoZarvltksmR)'],[None]))

