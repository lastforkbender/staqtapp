# Code File: StaqTapp-1.01 [PySqTpp_Alpha.py] S.A.R. main functions use




# Staqtapp 1.01.722

# For global variables file use and other global variables magic;
# these modules part of SolaceXn AI software packages as updated.


# Email: 5deg.blk.blt.cecil(at)gmail


import PySqTpp_SarInterface

import mmap
import os
#______________________________________________________________________________________

class SarAlpha(PySqTpp_SarInterface.PySqTppSarInterface):
    # - settled functions for sar intelligence -
#______________________________________________________________________________________

    def acquired_tqpt_source(self, dsg_fnc: str, item_name: str, item_data: str, dir_path: str, source_name: str):
        # @override PySqTppSarInterface.acquired_tqpt_source()
        
        wrdStr = None
        
        newSarAlpha = SarAlpha()
        if dsg_fnc == 'savn':
            wrdStr = newSarAlpha.char_bridge(item_data)
            if wrdStr != None:
                newSarAlpha.word_bridge(wrdStr, dir_path)
            
#______________________________________________________________________________________

    def write_extension_source(self, ext_pnt: str, source: str, dir_path: str, source_name: str) -> bool:
        # @override PySqTppSarInterface.write_extension_source()
        
        jnLst = None
        wrdx = None
        
        try:
            if ext_pnt == 'wb_new':
                with open(dir_path + '/' + source_name + '.dat', mode='w') as wb_new:
                    wb_new.write(source)
            elif ext_pnt == 'wb_wrdx':
                with open(dir_path + '/' + source_name + '.dat', 'r+b') as fileObjEwr:
                    with mmap.mmap(fileObjEwr.fileno(), length=0, prot=mmap.PROT_READ) as mmapObjEwr:
                        wrdx = mmapObjEwr.read()
                        mmapObjEwr.close()
                    mmapObjEwr = None
                jnLst = [wrdx, str.encode(source)]
                with open(dir_path + '/' + source_name + '.dat', 'wb') as wb_wrdx:
                    wb_wrdx.write(b''.join(jnLst))
            return True
        except Exception:
            return False
#______________________________________________________________________________________

    def char_bridge(self, source: str) -> str:
        # @override PySqTppSarInterface.char_bridge()
        
        sChrsSepr = set(' ,;:"()<>.!?')
        sChrsLtrs = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        swLtrs = False
        swJnp = False
        swAdd = False
        swRst = False
        prvChr = None
        wrdx = ''
        chcWrdx = ''
        
        try:
            for currChr in source:
                if set(currChr).issubset(sChrsSepr) and swJnp == False:
                    if swLtrs == True:
                        swLtrs = False
                        if wrdx.find(chcWrdx) == -1:
                            wrdx += chcWrdx.lower() + ':'
                            swAdd = True
                        chcWrdx = ''
                else:
                    if currChr == '-' and swLtrs == True:
                        if currChr == '-' and prvChr == '-':
                            swRst = True
                            swLtrs = False
                            swJnp = False
                            chcWrdx = ''
                            prvChr = ''
                        else:
                            swJnp = True
                            prvChr = currChr
                            chcWrdx += currChr
                    elif set(currChr).issubset(sChrsLtrs):
                        swLtrs = True
                        swJnp = False
                        chcWrdx += currChr
                    else:
                        swRst = True
                        swLtrs = False
                        swJnp = False
            if swAdd == False and swRst == False:
                if wrdx.find(chcWrdx) == -1:
                    wrdx += chcWrdx.lower() + ':'
                else:
                    return None
            return wrdx
        except Exception:
            return None
#______________________________________________________________________________________

    def word_bridge(self, source: str, dir_path: str) -> bool:
        # @override PySqTppSarInterface.word_bridge()
        
        wrdLst = None
        wrdIdx = None
        rtrnRslt = True
        swNew = False
        ptrnStr = None
        srcLen = None
        
        newSarAlpha = SarAlpha()
        try:
            if not os.path.isfile(dir_path + '/sq__tpp1_sar___wrdx.dat'):
                rtrnRslt = newSarAlpha.write_extension_source('wb_new', "SQTPP1-SAR-WRD-LST -----DO----NOT----EDIT-----\n:", dir_path, "sq__tpp1_sar___wrdx")
                swNew = True
            if rtrnRslt == True and swNew == False:
                wrdLst = source.split(':')
                wrdLst.pop()
                srcLen = len(wrdLst)
                with open(dir_path + '/sq__tpp1_sar___wrdx.dat', mode='r') as fileObjRd:
                    with mmap.mmap(fileObjRd.fileno(), length=0, access=mmap.ACCESS_READ) as mmapObjRd:
                        wrdIdx = 0
                        while wrdIdx < srcLen:
                            ptrnStr = str.encode(':'+wrdLst[wrdIdx]+':')
                            if mmapObjRd.find(ptrnStr) > -1:
                                if wrdIdx == srcLen-1:
                                    wrdLst.pop(wrdIdx)
                                    srcLen-=1
                                    break
                                else:
                                    wrdLst.pop(wrdIdx)
                                    srcLen-=1
                            else:
                                wrdIdx+=1
                        mmapObjRd.close()
                    mmapObjRd = None
            # write new word list data
            if rtrnRslt == True:
                if swNew == False and srcLen > 0:
                    ptrnStr = ''
                    for i in range(srcLen):
                        ptrnStr += wrdLst[i] + ':'
                if swNew == True:
                    newSarAlpha.write_extension_source('wb_wrdx', source, dir_path, 'sq__tpp1_sar___wrdx')
                else:
                    if srcLen > 0:
                        newSarAlpha.write_extension_source('wb_wrdx', ptrnStr, dir_path, 'sq__tpp1_sar___wrdx')
            else:
                return False
        except Exception:
            return False
#______________________________________________________________________________________





























