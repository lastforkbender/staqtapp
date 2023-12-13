# Code File: StaqTapp-1.02 [PySqTpp_Stpx.py] stpx functions abs/ext module


# Staqtapp 1.02.431

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
                with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpW:
                    gzObjXtpW.write(b':pth<' + str.encode(dir_path) + b'>\n:fle<' + str.encode(source_name) + b'>')
                gzObjXtpW = None
            else:
                gzSrc = None
                pthLst = None
                with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'rb') as gzObjXtpR:
                    gzSrc = gzObjXtpR.read()
                    pthLst = re.findall(rb':pth<.*?>\n:fle<.*?>', gzSrc)
                gzObjXtpR = None
                with gzip.open(mdlPthX + '/stpx/x_stpx.gz', 'wb') as gzObjXtpN:
                    gzObjXtpN.write(gzSrc.replace(pthLst[0], b':pth<' + str.encode(dir_path) + b'>\n:fle<' + str.encode(source_name) + b'>'))
                gzObjXtpN = None
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
            pth = StpxSrvc.stpx_get_path(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
            gzSrc = None
            with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'rb') as gzObjSlvR:
                gzSrc = gzObjSlvR.read()
            gzObjSlvR = None
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
                        with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjASlvW:
                            gzObjASlvW.write(gzStrA + b''.join(varNmLst))
                        gzObjASlvW = None
                    else:
                        gzStrB = gzSrc[px[1]:len(gzSrc)]
                        with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjBSlvW:
                            gzObjBSlvW.write(gzStrA + b''.join(varNmLst) + gzStrB)
                        gzObjBSlvW = None
                    return cnt
                else:
                    with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'wb') as gzObjCSlvW:
                        gzObjCSlvW.write(gzSrc + b''.join(varNmLst))
                    gzObjCSlvW = None
                    return None
            else:
                return None
        except Exception as e:
            print("staqtapp stpx error: ", e)
#______________________________________________________________________________________

    def stpx_get_list_vars(is_sorted: bool) -> list:
        try:
            pth = StpxSrvc.stpx_get_path(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz')
            ptrn = re.compile(r':var<' + re.escape(pth[1]) + r':.*?>')
            varNmLst = []
            with gzip.open(os.path.dirname(os.path.abspath(__file__)) + '/stpx/x_stpx.gz', 'rb') as gzObjGlvR:
                gzSrc = bytes.decode(gzObjGlvR.read(), 'utf-8')
                for mtch in ptrn.findall(gzSrc):
                    varNmLst.append(mtch.replace(':var<' + pth[1] + ':', "").strip('>'))
                gzSrc = None
            gzObjGlvR = None
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













