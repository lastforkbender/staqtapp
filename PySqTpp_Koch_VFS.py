# __________________________________________________________________________________

# Staqtapp-Koch: Hybrid Env-Vars Lib (https://github.com/lastforkbender/staqtapp)

# Version: 2.01.079
# __________________________________________________________________________________


# ●■ Staqtapp-Koch Module Name: PySqTpp_Koch_VFS.py


# ● ■  Description of this module's purpose:
    
#       This module is the virtual file system for Staqtapp-Koch library:
#       An diamond grade vfs, obfuscation/multi-encryption addr routing;
#       includes XORTL time-lock settings for all modules' addr-locks. At
#       runtime .envfs file will have hundreds of deep decoy sub-dirs----
#       rendering future ai comprehension useless in cracking it's routing.


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
import os
import re

# Imported PySqTpp_Koch module(s) for this module's objectives.
import PySqTpp_Koch_Immersion as immr
import PySqTpp_Koch_XORTL as xortl
import PySqTpp_Koch_AES as aes
# __________________________________________________________________________________

# VFS FUNCTIONS' INT RETURNS:
    
    # NO ERRORS: 
    #  1  = -----------------------------------------------
    #  2  = -----------------------------------------------
    #  3  = -----------------------------------------------
    #  4  = -----------------------------------------------
    #  5  = -----------------------------------------------
    #  6  = -----------------------------------------------
    
    # ERRORS:
    # -1  = -----------------------------------------------
    # -2  = -----------------------------------------------
    # -3  = -----------------------------------------------
    # -4  = -----------------------------------------------
    # -5  = -----------------------------------------------
    # -6  = -----------------------------------------------
    # -7  = -----------------------------------------------
    # -8  = -----------------------------------------------
    # -9  = -----------------------------------------------
    # -10 = -----------------------------------------------
    # -11 = -----------------------------------------------
    # -12 = -----------------------------------------------
    # -13 = -----------------------------------------------
    # -14 = -----------------------------------------------
    # -15 = -----------------------------------------------
    # -16 = -----------------------------------------------
    # -17 = -----------------------------------------------
    # -18 = -----------------------------------------------
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
            if os.path.isfile(f'{self._cf}/{self._fn}'):
                if self._vfs_opnfl() < 0:
                    return -3
                else:
                    return 1
            else:
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

    def _vfs_adrsec(self, w: str) -> list:
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

    def _vfs_chkfx(self, isFx: bool) -> int:
        rtrn = True
        if isFx:
            if not self._fx:
                if self._vfs_opnfl() < 0: rtrn = False
        else:
            if self._vfs_opnfl() < 0: rtrn = False
        return rtrn
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
            self._fl = fWrObj.read()
            ptrn = re.findall(bytes(ptrn,'utf-8'),self._fl)
            fWrObj.seek(0,0)
            self._fl = self._fl.replace(ptrn[0],bytes(stg,'utf-8')+src+b'>')
            fWrObj.write(self._fl)
# __________________________________________________________________________________

    def _vfs_lstdir(self, dirPth: str) -> list:
        if not self._vfs_chkfx(True):
            return -3
        sPrt = bytes('\◇\/\/','utf-8')
        rltLst = re.findall(sPrt+re.escape(str.encode(dirPth,'utf-8'))+b'\/.*?\/',self._fl)
        for x in range(len(rltLst)): rltLst[x] = bytes.decode(rltLst[x],'utf-8')
        return rltLst
# __________________________________________________________________________________

    def _vfs_gtflnm(self,_____):
        if not self._vfs_chkfx(True):
            return -3
        try:
            ________=[]
            __=bytes('\◇\/\/','utf-8')
            _____=re.search(__+re.escape(_____)+b'\/',self._fl)
            ________.append(_____.span()[1])
            __________=_____.group().split(b'/')
            __=bytes('---◇-','utf-8')
            _____=re.search(__+re.escape(__________[len(__________)-2])+b'-',self._fl)
            ________.append(_____.span()[0])
            _________=re.findall(rb'\[(.*?)\]',self._fl[________[0]:________[1]])
            if len(_________)>0:
                return _________[0].replace(b'[',b'').strip(b']')
            else:
                return None
        except Exception as err_vfs_gtflnm:
            return None
# __________________________________________________________________________________

    def _vfs_mkdir(self,__):
        try:
            if self._fc==1:
                if not self._fx:
                    if self._vfs_chkfx(False):
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
                            self._fl = b'\n'.join(_______)
                            with open(f'{self._cf}/{self._fn}',mode='wb') as fMkDirObj:fMkDirObj.write(self._fl)
                            _______=None
                            return 3
                    else:
                        return -3
            else:
                return -1
        except Exception as err_vfs_mkdir:
            return -6
# __________________________________________________________________________________

    def _vfs_encdir(self,_____,____,______,_,__,___,_________):
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
                    return -3
                _____=_____.split('/')
                if self._fl.find(bytes(f'◇//{_____[0]}/{_____[1]}/','utf-8'))>-1:
                    ___________=None
                    _______________=None
                    if ____>0:
                        if ______=='xnr':
                            ___________=immr.sqtpp_koch_get_addr_xnr_lst(_,__,___,random.randint(32,64))
                            for ____________________ in range(len(___________)):___________[____________________]=str(___________[____________________])
                            ___________=''.join(___________)
                            self._fl = self._fl.replace(bytes(f'◇//{_____[0]}/{_____[1]}/','utf-8'),bytes(f'◇//{_____[0]}/{___________}/','utf-8'))
                            self._fl = self._fl.replace(bytes(f'---◇-{_____[1]}-','utf-8'),bytes(f'---◇-{___________}-','utf-8'))
                        elif ______=='seten':
                            if not self._fsx: self._fs=self._vfs_adrsec('Seten')
                            ________________=False
                            for ______________________ in range(len(self._fs)):
                                if _________==self._fs[______________________]:
                                    ________________=True
                                    break
                            if ________________:
                                __________________=lambda a,k1,k2,k3: ''.join(''.join(chr(ord(c)^ord(k1)^ord(k2)^ord(k3)) for c,k1,k2,k3 in zip(blk.ljust(8,'!'),k1,k2,k3)) for blk in (a[i:i+8] for i in range(0,len(a),8)))
                                _______________=__________________(_________,_,__,___)
                                self._fl = self._fl.replace(bytes(f'◇//{_____[0]}/{_____[1]}/','utf-8'),bytes(f'◇//{_____[0]}/{_______________}/','utf-8'))
                                self._fl = self._fl.replace(bytes(f'---◇-{_____[1]}-','utf-8'),bytes(f'---◇-{_______________}-','utf-8'))
                            else:
                                return -11
                    else:
                        return '_!_'
                    with open(f'{self._cf}/{self._fn}',mode='wb') as fEncDirObj: fEncDirObj.write(self._fl)
                    if ______=='xnr':
                        return ___________
                    elif ______=='seten':
                        return _______________
                else:
                    return -10
            else:
                return -1 
        except Exception as err_vfs_encdir:
            return -12
# __________________________________________________________________________________

    def _vfs_crtfl(self,____,______):
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
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
                        self._fl = _____________[0]+b'\n'+______+b'\n'+_____________[1]
                        with open(f'{self._cf}/{self._fn}',mode='wb') as fNwFlObj: fNwFlObj.write(self._fl)
                        _____________=None
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

    def _vfs_gtfl(self,_____,____):
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
                    return -3
                ______=self._fl.find(bytes(f'◇//{_____}/','utf-8'))
                if ______>-1:
                    ________=self._fl.find(bytes(f']{____}[','utf-8'),______)
                    __=None
                    if ________>-1:
                        ________=________+len(____)
                        __=self._fl.find(bytes(f'[{____}]','utf-8'),________)
                        return self._fl[________+3:__-1]
                    else:
                        return -14
                else:
                    return -13
            else:
                return -1
        except Exception as err_vfs_gtfl:
            return -15
# __________________________________________________________________________________

    def _vfs_gtvr(self,____,_____,______,_______,________):
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
                    return -3
                _____=self._fl.find(bytes(f'◇//{____}/{_____}/','utf-8'))
                _______=None
                if _____>-1:
                    ________=None
                    ___________=str.encode('[\□|\■|\○|\●]')
                    __________=re.findall(___________+re.escape(str.encode(______))+b'<(?s:.*?).*><.*?><.*?>',self._fl)
                    if len(__________)>0:
                        __________[0]=__________[0].replace(b'>',b'')
                        __________=__________[0].split(b'<')
                        ________=re.findall(b'[\xa1|\xa0|\x8b|\x8f]',__________[0])
                        ________=________[0]
                        __________[0]=__________[0].replace(________,b'')
                        __________.append(________)
                        return __________
                    else:
                        return -17
                else:
                    return -16
            else:
                return -1
        except Exception as err_vfs_getvar:
            return -18
# __________________________________________________________________________________

    def _vfs_rsv(self,__,_______,_____,___________,___,_________,________,_) -> int:
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
                    return -3
                _______________=aes.sqtpp_koch_aes_encode_data(__,_______,_____,___________)
                ______________=bytes(___,'utf-8')
                ____=bytearray()
                for rsv in range(len(_______________)):____.append(_______________[rsv]^______________[rsv%len(______________)])
                _______________=_
                _________________=bytes(aes.sqtpp_koch_aes_encode_data(______________,_________,________,_))
                ______________=___________
                self._vfs_wrtstg('RSV<.*?>','RSV<',_________________)
                return 4
            else:
                return -1
        except Exception as err_vfs_rsv:
            print -7
# __________________________________________________________________________________

    def _vfs_lck(self,______,____,________,_______) -> int:
        try:
            if self._fc==1:
                if not self._vfs_chkfx(True):
                    return -3
                ______=xortl.sqtpp_koch_xortl(True,______,____,________,_______)
                self._vfs_wrtstg('LCK<.*?>','LCK<',______)
                return 5
            else:
                return -1
        except Exception as err_vfs_lck:
            self._vfs_wrtstg('LCK<.*?>','LCK<',b'TIMELOCK')
            return 5
# __________________________________________________________________________________

    def _vfs_pntbrk(self, cmd: list, bExt: list):
        cmds = None
        nmsc = None
        rtrn = None
        for s in range(len(cmd)):
            if cmd[s].find('lstdir(') > -1:
                cmds = cmd[s].replace('lstdir(','').strip(')')
                rtrn = self._vfs_lstdir(cmds)
            elif cmd[s].find('mkdir(') > -1:
                cmds = cmd[s].replace('mkdir(','').strip(')')
                rtrn = self._vfs_mkdir(cmds)
            elif cmd[s].find('encdir(') > -1:
                cmds = cmd[s].replace('encdir(','').strip(')').split(',')
                nmsc = int(cmds[1])
                if nmsc == 1 and cmds[2] == 'xnr':
                    rtrn = self._vfs_encdir(cmds[0],nmsc,cmds[2],int(cmds[3]),int(cmds[4]),int(cmds[5]),cmds[6])
                elif nmsc == 1 and cmds[2] == 'seten':
                    rtrn = self._vfs_encdir(cmds[0],nmsc,cmds[2],cmds[3],cmds[4],cmds[5],cmds[6])
                else:
                    return '_!_'
            elif cmd[s].find('crtfl(') > -1:
                cmds = cmd[s].replace('crtfl(','').strip(')')
                rtrn = self._vfs_crtfl(cmds,bExt[0])
            elif cmd[s].find('gtflnm') > -1:
                cmds = cmd[s].replace('gtflnm(','').strip(')')
                rtrn = self._vfs_gtflnm(bExt[0])
            elif cmd[s].find('gtfl(') > -1:
                cmds = cmd[s].replace('gtfl(','').strip(')').split(',')
                rtrn = self._vfs_gtfl(cmds[0],cmds[1])
            elif cmd[s].find('gtvr(') > -1:
                cmds = cmd[s].replace('gtvr(','').strip(')').split(',')
                rtrn = self._vfs_gtvr(cmds[0],bExt[0],cmds[1],int(cmds[2]),cmds[3])
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

