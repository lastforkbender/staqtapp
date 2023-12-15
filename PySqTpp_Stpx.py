# Code File: StaqTapp-1.02 [PySqTpp_Stpx.py] stpx functions abs/ext module


# Staqtapp 1.02.439

# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import PySqTpp_StpxInterface
import random
import mmap
import stpp
import gzip
import os
import re
import io

#______________________________________________________________________________________

class StpxSrvc(PySqTpp_StpxInterface.PySqTppStpxInterface):
    # - settled functions for stpx abs/ext methods -
#______________________________________________________________________________________

    def stpx_set_path(dir_path: str, source_name: str):
        try:
            mdlPthX = os.path.dirname(os.path.abspath(__file__))
            stpxNw = False
            if os.path.isdir(mdlPthX + '/stpx') == False:
                os.makedirs(mdlPthX + '/stpx')
                stpxNw = True
            if os.path.isfile(mdlPthX + '/stpx/x_stpx.gz') == False or stpxNw == True:
                StpxSrvc.stpx_map('gzw', mdlPthX + '/stpx/x_stpx.gz', b':pth<' + str.encode(dir_path) + b'>\n:fle<' + str.encode(source_name) + b'>')
            else:
                gzSrc = StpxSrvc.stpx_map('gzr', mdlPthX + '/stpx/x_stpx.gz', None)
                pthLst = re.findall(rb':pth<.*?>\n:fle<.*?>', gzSrc)
                gzSrc = gzSrc.replace(pthLst[0], b':pth<' + str.encode(dir_path) + b'>\n:fle<' + str.encode(source_name) + b'>')
                StpxSrvc.stpx_map('gzw', mdlPthX + '/stpx/x_stpx.gz', gzSrc)
                gzSrc = None
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_get_path(full_curr_path: str) -> list:
        try:
            ptrn = re.compile(rb':pth<.*?\n:fle<.*?>')
            with gzip.open(full_curr_path, 'rb') as gzObjGp:
                for mtch in ptrn.findall(gzObjGp.read()):
                    mtch = mtch.split(b'\n')
                    mtch[0] = bytes.decode(mtch[0].replace(b':pth<', b"").strip(b'>'), 'utf-8')
                    mtch[1] = bytes.decode(mtch[1].replace(b':fle<', b"").strip(b'>'), 'utf-8')
                    return mtch
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_add_list_vars() -> int:
        try:
            mdlPthX = os.path.dirname(os.path.abspath(__file__))
            pth = StpxSrvc.stpx_get_path(mdlPthX + '/stpx/x_stpx.gz')
            gzSrc = StpxSrvc.stpx_map('gzr', mdlPthX + '/stpx/x_stpx.gz', None)
            ptrn = re.compile(rb'<.*?=')
            varNmLst = []
            with open(pth[0] + '/' + pth[1] + '.tqpt', mode='r', encoding='utf-8') as fObjSlvR:
                with mmap.mmap(fObjSlvR.fileno(), length=0, access=mmap.ACCESS_READ) as fMpObjSlvR:
                    for mtch in ptrn.findall(fMpObjSlvR):
                       if len(mtch) >= 3:
                           varNmLst.append(b'\n:var<' + str.encode(pth[1]) + b':' + mtch.strip(b'<=') + b'>')
                    fMpObjSlvR.close()
                fMpObjSlvR = None
            if len(varNmLst) > 1:
                varNmLst.pop(0)
                if gzSrc.find(b':var<' + str.encode(pth[1]) + b':') > -1:
                    cnt = 0
                    px = [0,0]
                    pStrt = True
                    ptrn = re.compile(rb':var<' + re.escape(str.encode(pth[1])) + rb':.*?>')
                    for fnd in ptrn.finditer(gzSrc):
                        if pStrt == True:
                            pStrt = False
                            px[0] = fnd.start()-1
                        px[1] = fnd.end()
                        cnt+=1
                    gzStrA = gzSrc[0:px[0]]
                    if px[1] == len(gzSrc):
                        StpxSrvc.stpx_map('gzw', mdlPthX + '/stpx/x_stpx.gz', gzStrA + b''.join(varNmLst))
                    else:
                        gzStrB = gzSrc[px[1]:len(gzSrc)]
                        StpxSrvc.stpx_map('gzw', mdlPthX + '/stpx/x_stpx.gz', gzStrA + b''.join(varNmLst) + gzStrB)
                    return cnt
                else:
                    StpxSrvc.stpx_map('gzw', mdlPthX + '/stpx/x_stpx.gz', gzSrc + b''.join(varNmLst))
                    return None
            else:
                return None
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_get_list_vars(is_sorted: bool) -> list:
        try:
            mdlPthX = os.path.dirname(os.path.abspath(__file__))
            pth = StpxSrvc.stpx_get_path(mdlPthX + '/stpx/x_stpx.gz')
            ptrn = re.compile(r':var<' + re.escape(pth[1]) + r':.*?>')
            varNmLst = []
            gzSrc = bytes.decode(StpxSrvc.stpx_map('gzr', mdlPthX + '/stpx/x_stpx.gz', None), 'utf-8')
            for mtch in ptrn.findall(gzSrc):
                varNmLst.append(mtch.replace(':var<' + pth[1] + ':', "").strip('>'))
            gzSrc = None
            if len(varNmLst) > 0:
                if is_sorted == False:
                    return varNmLst
                else:
                    if len(varNmLst) == 1:
                        return varNmLst
                    else:
                        varNmLst.sort()
                        return varNmLst
            else:
                return None
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_find_data(isRegx: bool, varNames: list, search):
        try:
            pth = StpxSrvc.stpx_get_path(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
            vnLen = None
            varSrc = None
            srchRslt = None
            rtrnLst = []
            if isinstance(varNames, list) == True and len(varNames) > 0:
                vnLen = len(varNames)
                if isRegx == False: search = str(search)
                for x in range(vnLen):
                    if stpp.findvar(False, varNames[x], pth[0], pth[1]) == True: 
                        varSrc = stpp.loadvar_str(varNames[x], pth[0], pth[1])
                        if isinstance(varSrc, str):
                            if isRegx == True:
                                srchRslt = re.findall(search, varSrc)
                                if len(srchRslt) > 0:
                                    rtrnLst.append(varNames[x])
                                    rtrnLst.append(srchRslt[0])
                            else:
                                if varSrc.find(search) > -1:
                                    rtrnLst.append(varNames[x])
                                    rtrnLst.append(search)
                        else:
                            vpLen = len(varSrc)
                            for lx in range(vpLen):
                                if isRegx == True:
                                    srchRslt = re.findall(search, varSrc[lx])
                                    if len(srchRslt) > 0:
                                        rtrnLst.append(varNames[x] + '[' + str(lx) + ']')
                                        rtrnLst.append(srchRslt[0])
                                else:
                                    if varSrc[lx].find(search) > -1:
                                        rtrnLst.append(varNames[x] + '[' + str(lx) + ']')
                                        rtrnLst.append(search)
                if len(rtrnLst) > 1:
                    return rtrnLst
                else:
                    return None
            else:
                xCnt = 0
                if isRegx == False: search = str(search)
                with open(pth[0] + '/' + pth[1] + '.tqpt', 'r+b') as fObjFdt:
                    mObjFdt = mmap.mmap(fObjFdt.fileno(), 0, prot=mmap.PROT_READ)
                    for ln in iter(mObjFdt.readline, b''):
                        if isRegx == True:
                            srchRslt = re.findall(search, ln)
                            if len(srchRslt) > 0:
                                xCnt+=1
                                rtrnLst.append(None)
                                rtrnLst.append(bytes.decode(srchRslt[0]))
                                srchRslt = re.findall(rb'^<.*?=', ln)
                                rtrnLst[xCnt-1] = bytes.decode(srchRslt[0]).strip('<=')
                                xCnt+=1
                        else:
                            if ln.find(str.encode(search)) > -1:
                                xCnt+=1
                                rtrnLst.append(None)
                                rtrnLst.append(search)
                                srchRslt = re.findall(rb'^<.*?=', ln)
                                rtrnLst[xCnt-1] = bytes.decode(srchRslt[0]).strip('<=')
                                xCnt+=1
                    if len(rtrnLst) > 1:
                        return rtrnLst
                    else:
                        return None
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_remove_vars(is_backup: bool, var_names) -> bool:
        # optimized fri, dec 15-23 ---- now correctly removes any associated .tpqt entries also;
        # of stranger things required here... seeks delete of any .tpqt entries regardless if there
        # was no removes @ .tqpt source file pre, for file error precautions or any outside edits...
        try:
            pth = StpxSrvc.stpx_get_path(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
            vrNmsLen = None
            vrSrc = None
            src = None
            rplc = False
            if isinstance(var_names, str) == True:
                vrSrc = var_names
                var_names = [vrSrc]
            if is_backup == True:
                StpxSrvc.stpx_backups(True, 'tqpt', pth)
            src = StpxSrvc.stpx_map('tmr', pth, None)
            vrNmsLen = len(var_names)
            for x in range(vrNmsLen):
                vrSrc = re.findall(rb'\n<' + re.escape(str.encode(var_names[x])) + rb'=.*?>', src)
                if len(vrSrc[0]) > len(var_names[x])+5:
                    src = src.replace(vrSrc[0], b'')
                    if rplc == False: rplc = True
            if rplc == True:
                StpxSrvc.stpx_map('twb', pth, src)
            if os.path.isfile(pth[0] + '/' + pth[1] + '.tpqt') == True:
                src = StpxSrvc.stpx_map('lmr', pth, None)
                rplcLck = False
                for lx in range(vrNmsLen):
                    vrSrc = re.findall(rb'\n<:' + re.escape(var_names[lx]) + rb'=(?s:.*?).*:>', src)
                    if len(vrSrc[0]) > len(var_names[lx])+5:
                        src = src.replace(vrSrc[0], b'')
                        if rplcLck == False: rplcLck = True
                    else:
                        vrSrc = re.findall(rb'<:' + re.escape(var_names[lx]) + rb'=(?s:.*?).*:>', src)
                        if len(vrSrc[0]) > len(var_names[lx])+5:
                            # found @ top entry block of the .tpqt lock file
                            src = src.replace(vrSrc[0], b'')
                            if rplcLck == False: rplcLck = True
                if rplcLck == True:
                    StpxSrvc.stpx_map('lwb', pth, src)
            return rplc
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_map(dsg, pth, src):
        fPth = None
        if dsg == 'tmr' or dsg == 'lmr':
            rtrnSrc = None
            if dsg == 'tmr': fPth = pth[0] + '/' + pth[1] + '.tqpt'
            elif dsg == 'lmr': fPth = pth[0] + '/' + pth[1] + '.tpqt'
            with open(fPth, mode='r') as fObjTmr:
                with mmap.mmap(fObjTmr.fileno(), length=0, access=mmap.ACCESS_READ) as mpObjTmr:
                    rtrnSrc = mpObjTmr.read()
                    mpObjTmr.close()
                mpObjTmr = None
            return rtrnSrc
        elif dsg == 'twb' or dsg == 'lwb':
            if dsg == 'twb': fPth = pth[0] + '/' + pth[1] + '.tqpt'
            elif dsg == 'lwb': fPth = pth[0] + '/' + pth[1] + '.tpqt'
            with open(fPth, mode='wb') as fObjTwb:
                fObjTwb.write(src)
                fObjTwb.close()
            fObjTwb = None
        elif dsg == 'gzr':
            rtrnGzSrc = None
            with gzip.open(pth, 'rb') as gzObjR:
                rtrnGzSrc = gzObjR.read()
            gzObjR = None
            return rtrnGzSrc
        elif dsg == 'gzw':
            with gzip.open(pth, 'wb') as gzObjW:
                gzObjW.write(src)
            gzObjW = None
#______________________________________________________________________________________

    def stpx_backups(is_write: bool, dsg: str, pthLst: list):
        if is_write == True:
            if dsg == 'tqpt':
                src = StpxSrvc.stpx_map('tmr', pthLst, None)
                StpxSrvc.stpx_map('gzw', os.path.dirname(os.path.abspath(__file__)) + '/stpx/tqpt_bck_' + pthLst[1] + '.gz', src)
                src = None
        else:
            pass
#______________________________________________________________________________________

    def stpx_get_menorah_palindrome_encoding(isGreater: bool, src: str) -> int:
        # THIS METHOD NOT FULLY IMPLEMENTED YET
        
        nSt = set('-0123456789')
        stLst = []
        dtLst = []
        rtrnStr = ''
        prvX = '1'
        lStCnt = 1
        rStCnt = 1
        ix = None
        rx = None
        cg = None
        cgPl = None
        cgRl = False
        cgHld = False
    
        src = src.replace('-', '')
        for x in src:
            ix = int(x)
            rx = int(prvX)
            if ix == rx-1: lStCnt+=1
            elif ix == rx+1: lStCnt-=1
            elif ix-1 == rx: rStCnt+=1
            elif ix+1 == rx: rStCnt-=1
            elif ix == rx:
                if lStCnt > rStCnt: lStCnt-=1
                elif lStCnt < rStCnt: rStCnt-=1
                else:
                    if lStCnt < 0:
                        lStCnt+=1
                        cgPl = True
                    if rStCnt < 0:
                        rStCnt+=1
                        cgPl = True
                    if lStCnt > 0:
                        lStCnt-=1
                        cgRl = True
                    if rStCnt > 0: 
                        rStCnt-=1
                        cgRl = True
            if lStCnt == rStCnt: cgHld = True
            if x == prvX: stLst.append(x)
            else: dtLst.append(x)
            if cgPl == True and cgRl == True and cgHld == True:
                lStCnt = 1
                rStCnt = 1
            cgPl = False
            cgRl = False
            cgHld = False
            prvX = x
        prvX = 'q'
        cgPl = 0
        if lStCnt == rStCnt: cgPl = 1
        elif len(src) == 1: cgPl = 1
        else:
            cgHld = True
            cg = 1
            for y in src:
                ix = int(y)
                if ix < lStCnt and cg >= rStCnt: lStCnt = ix
                if ix > rStCnt and cg <= lStCnt: rStCnt = ix
                cg+=1
            if lStCnt == 0: lStCnt = 1
            if rStCnt == 0: rStCnt = 1
            if lStCnt == rStCnt: cgPl = 1
            else:
                if isGreater == True:
                    if lStCnt > rStCnt: prvX = 'l'
                    else: prvX = 'r'
                else:
                    if lStCnt < rStCnt: prvX = 'l'
                    else: prvX = 'r'
        lens = [len(stLst), len(dtLst)]
        ix = []
        rx = []
        cgRl = None
        cgNb = None
        cgNx = False
        kr_kn = 1
        if lens[0] > 0:
            for n in range(lens[0]):
                if stLst[n] == cgRl:
                    ix.append(stLst[n])
                    for nas in range(len(ix)):
                        if lens[0] == len(ix): break
                        else:
                            if ix[nas] == '1' or ix[nas] == '3' or ix[nas] == '5' or ix[nas] == '7' or ix[nas] == '9': kr_kn+=1
                cgRl = stLst[n]
        else:
            if cgHld == True: cgNb = True
            else: cgNb = False
        if lens[1] > 2:
            if cgPl != None:
                if rStCnt > 1:
                    for a in range(len(dtLst)):
                        if lStCnt >= 1:
                            if prvX == 'q':
                                if kr_kn > 1 and cgNb == False:
                                    if cgRl == dtLst[a]:
                                        if len(dtLst) > 1: dtLst.pop(a)
                                        else:
                                            lens.append(len(dtLst))
                                            cgNx = True
                                            break
                                    kr_kn-=1
                                else:
                                    if cgNb == True:
                                        if cgRl == dtLst[a]:
                                            if len(dtLst) > 1: dtLst.pop(a)
                                            else:
                                                lens.append(len(dtLst))
                                                cgNx = True
                                                break
                                        kr_kn-=2
                                    else:
                                        if cgRl == dtLst[a]:
                                            if len(dtLst) > 1:
                                                stLst.append(dtLst[a])
                                                dtLst.pop(a)
                                            else:
                                                lens.append(len(dtLst))
                                                cgNx = True
                                                break
                                            kr_kn+=2
                            elif prvX == 'l':
                                if cgNb == True and lStCnt > 3:
                                    if len(dtLst) > 1:
                                        if cgRl == dtLst[a]:
                                            dtLst.pop(a)
                                            kr_kn-=1
                                        else:
                                            kr_kn+=1
                                    else:
                                        lens.append(len(dtLst))
                                        cgNx = True
                                        break
                                else:
                                    if cgRl == dtLst[a] and len(dtLst) > 1 and cgNb == False:
                                        dtLst.pop(a)
                                        kr_kn-=2
                                    else: pass
                            elif prvX == 'r':
                                if cgRl == dtLst[a] and len(dtLst) > 1:
                                    dtLst.pop(a)
                                    kr_kn+=1
                                else:
                                    if len(dtLst) == 1:
                                        cgNx = True
                                        break
                                    if cgNb == True: kr_kn-=1
                                    else: kr_kn+=1
                        else:
                            # lStCnt is less than 1
                            if prvX == 'q': pass
                            elif prvX == 'l': pass
                            elif prvX == 'r': pass
                        cgRl = dtLst[a]
                else:
                    # rStCnt is less than 1
                    #for b in range(lens[1]):
                    pass                        
            else:
                #cgPl=1
                pass
        else:
            # lens[1]<3
            pass
        
        print(dtLst)
        print(stLst)
        print(ix)
        print(lens)
        print('lStCnt: ' + str(lStCnt))
        print('rStCnt: ' + str(rStCnt))
        print(prvX)
        print(kr_kn)
#______________________________________________________________________________________













