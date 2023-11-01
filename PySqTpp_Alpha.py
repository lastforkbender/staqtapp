# Code File: StaqTapp-1.02 [PySqTpp_Alpha.py] S.A.R. main functions use




# Staqtapp 1.02.337

# For global variables file use and other lords' global variables fork bending


# ***These modules part of the SolaceXn AI software package as is for all lords***


# email: 5deg.blk.blt.cecil(@)gmail
# github: https://github.com/lastforkbender/staqtapp
# contact: https://pastebin.com/eumqiBAx


import PySqTpp_SarInterface

import mmap
import os
import re

from time import time, ctime
#______________________________________________________________________________________

class SarAlpha(PySqTpp_SarInterface.PySqTppSarInterface):
    # - settled functions for sar intelligence -
#______________________________________________________________________________________

    def extr_load_sar_remap(self, is_prm_exchng: bool, cat_pin: str, dir_path: str, source_name: str) -> int:
        # @override PySqTppSarInterface.extr_load_sar_remap()
        
        # FUNCTION RETURN-CODES
            
        # ------------------------------------------------------------------------
        # return  -1 : invalid file path, not there
        # return -2  : no sar variable names found of category pin given
        
        vrNmrLst = []
        rvmLst = []
        nmrStrA = None
        nmrStrB = None
        abcStr = ''
        abrStr = ''
        tmplVar = ''
        rngLst = None
        swSepr = None
        idx = None
        
        try:
            if os.path.isfile(dir_path + '/' + source_name + '.tqpt'):
                ptrnStr = re.compile(rb'<'+re.escape(str.encode(cat_pin))+rb'_sar_[0-9]{10}_[0-9]{1}=')
                with open(dir_path + '/' + source_name + '.tqpt', mode='r') as fObjLsr:
                    with mmap.mmap(fObjLsr.fileno(), length=0, access=mmap.ACCESS_READ) as mObjLsr:
                        for sVnm in ptrnStr.findall(mObjLsr):
                            # place all found sar variable category, the variable's main number into a list
                            rngLst = bytes.decode(sVnm, 'utf-8').split('_')
                            if len(rngLst[2]) == 10:
                                vrNmrLst.append(rngLst[2])
                        mObjLsr.close()
                    mObjLsr = None
                nLen = len(vrNmrLst)
                if nLen > 0:
                    rngLst = []
                    # How to make a temple variable/multi-loop quantum like pointer?
                    for nmr in range(nLen):
                        # First, get the number 4 to 4 as integers, with 1rst number of each(LtoR, 0&5) as
                        # the toroidal-reg parity for the concluded made temple variable's LtoR or RtoL;
                        # is Menorah-Base 1:6 of the first numbers, each 4 placeholds folded to non-zero
                        # as of same looking at a Menorah, 4 left in or 4 right in always to center 1 divide,
                        # same number system on your hands but pairing 1 thumbs however is this case
                        # in how the temple variable is constructed of the sar address intersections/adds
                        rvmLst = []
                        nmrStrA = ''
                        swSepr = False
                        idx = 0
                        for currChr in vrNmrLst[nmr]:
                            if idx == 0 or idx == 5:
                                if currChr == '0':
                                    # ummm.. no. nothing is impossible, not possible
                                    currChr = '1'
                                rngLst.append(currChr)
                                swSepr = True
                            else:
                                if swSepr == True and currChr == '0':
                                    # again again just plain no, nothing cannot begin anything, even zero
                                    # that has never escaped a placeholding of one, inescapable is one
                                    currChr = '1'
                                    swSepr = False
                                if idx == 4 or idx == 9:
                                    nmrStrA += currChr
                                    rvmLst.append(nmrStrA)
                                    swSepr = False
                                    nmrStrA = ''
                                else:
                                    nmrStrA += currChr
                                    swSepr = False
                            idx+=1
                        # now 5 steps of greater or lesser comparisons, first reducing each 4 digit number
                        # by thousandths, hundredths and then tenths, in that < or > stored as a grid corner
                        # abstract, relevant to each numbers grid a same in matching persistent curvature,
                        # ancient technique of comparison cornering any number system but not obsolete;
                        # symbols & meaning of < or > in Menorah-Base would be much different, however
                        # a same principle of pairing both numbers to LtoR or RtoL retains in 5 abstracts; a
                        # rule consistency as seen above also applies, 0 cannot escape a 1 placeholding
                        # of a temple variable type dimensional length and parity address joining LtoR/RtoL
                        
                        # reduce each by it's thousandths to hundreths etc. of the same retained numbers,
                        # these first 3 < or > added to abcStr are all horizontal m specific-----example grids:
                        
                        # 7>2, 70<82 and 709>182 all horizontal comparison abstracts a same grids; notice
                        # there is a blank [ ] center after vertical abstracts, horizontal vs vertical in Menorah-
                        # Base has two very different distinct definitions rather than xy being on a same loop,
                        # this universe having deep external mirroring quantum fields not made by Base10
                        # [7] [<] [>] [>]*     *[>] [>] [<] [2]
                        # [7] [0] [ ] [<]*     *[<] [ ] [8] [2]
                        # [7] [0] [9] [>]*     *[>] [1] [8] [2]
                        # [7] [0] [9] [4]       [1] [1] [8] [2]
                        
                        # like a large rotor interlink sensor, comparing all pulls but
                        # no final pull compare needed; inner stability is always more
                        # powerful than a outer obscurity any expansion mirrored
                        rvmChrLstB = list(rvmLst[1])
                        idx = 0
                        # the above done because as the example grids.. inverted compared;
                        # all temple variable types are palindrome seeking to even from odd,
                        # or absolute quantum reality of something not spinning but is
                        for currNmrA in rvmLst[0]:
                            idx+=1
                            if swSepr == False:
                                nmrStrA += currNmrA
                            else:
                                abcStr += '.'
                                break
                            if idx == 1:
                                nmrStrB = rvmChrLstB[3]
                            elif idx == 2:
                                nmrStrB = rvmChrLstB[2]+rvmChrLstB[3]
                            elif idx == 3:
                                nmrStrB = rvmChrLstB[1]+rvmChrLstB[2]+rvmChrLstB[3]
                                swSepr = True
                            if int(nmrStrA) > int(nmrStrB):
                            # below a illusive construct, if fold both example grids above into each other
                            # is exact same of all < or > however is also at the same time not the same;
                            # why temple(ont'ago) variable types make great pointers of many addresses
                            # at once using the further corner analog separations LtoR both RtoL to evens
                                abcStr += '>'
                            elif int(nmrStrA) < int(nmrStrB):
                                abcStr += '<'
                        # the next two; the vertical corner abstracts all palindrome compares.. in fact could be
                        # reverse, having 3 vertical palindrome compares and 2 horizontal compares, however 
                        # as commented above, the computer you are using doesn't understand the illusion
                        # would all be the same < or > complete pattern for both grids regardless, which
                        # brings the equal topic in focus more; if the <> comparison checks above are equal
                        # then no < or > is added to abcStr and since temple variables seek palindrome
                        # compression, a same the previous < or > as then << or >> but if this .. is in the abcStr
                        # string of all three checks were equal.. then is true Menorah-Base multi-looping
                        # understood; first retain the very simple compares at the known palindrome columns,
                        # appended to a abrStr for pairs if paired, the *void-equal* is more probable now
                        rvmChrLstA = list(rvmLst[0])
                        if int(rvmChrLstA[1]) > int(rvmChrLstB[2]):
                            abrStr += '>'
                        elif int(rvmChrLstA[1]) < int(rvmChrLstB[2]):
                            abrStr += '<'
                        if int(rvmChrLstA[2]) > int(rvmChrLstB[1]):
                            abrStr += '>'
                        elif int(rvmChrLstA[2]) < int(rvmChrLstB[1]):
                            abrStr += '<'
                        abrStr += '.'
                    # finally we have both magic strings needed for a temple variable pointer make,
                    # if you print out abcStr and abrStr on top of each other, you will see the curved
                    # difference progression length getting larger @abcStr abstracts compared of
                    # @abrStr, this both disadvantage and advantage to several addresses pointed
                    # to at same moment, temple variables use a probable notation rather than a
                    # direct correct normal parallel pointer, however advantage being can point to
                    # many more memory addresses at once with accepted accuracy in focus of
                    # using temple variables in parallel; such things as a dense metal rod dropped
                    # from a very high place into a then departed mountain on impact would require
                    # very many very parallel COG trajectory calculations, or more swedishly speaking
                    # a small bio make computer that is otherwise slow of it's virtual bus structures
                        
                    # some more Menorah-Base explaining is needed now of these two strings, that
                    # will be embedded of the temple variable mapping pointer: first a Menorah is a
                    # wave of 3 semi-circles or 3 triangles if you have it, from small to large or the
                    # inverted large to small, each 7 candleholders are known palindrome multi-loop
                    # count lined; arrange of all three semi-circles as a wave, each end(candleholder)
                    # is open, the other 2 closed/joined with both facing opposite of the open 2, in
                    # technical computing terms of the abcStr compared of abrStr and relative 4 to 4
                    # addressing of the sar variable's main address number, the rngLst numbers are
                    # both open-joined to any of these 4 grouped compares, 2 joined/2open of any
                    # wave abstract, multi-loop toroidal-reg parity mentioned at begin of this method
                    # is just all and what is now needed is to intract both strings(waves) to the whole
                    # accumlate of the vrNmrLst via this parallel open/join LtoR or RtoL outer loops
                        
                    # though this embedding is commented of the next codings, cannot be fully under-
                    # stood until is known how this temple variable will be loaded in a list string type
                    # from a staqtapp tqpt variable source file that requires probable compares only,
                    # not direct comparing as seen of the all above coding constructs, and this also
                    # why very secure global variables outside a program is not impossible
                        
                    # .....a final temple variable/pointer is in a format of [n:n-mc-vn:hn] the first two
                    # n's(0&5) being the rngLst numbers added from the top 2nd parse loop, these
                    # will exact match any further stacked sar memory addressing of a sar variable;
                    # of any nesting, can be otherwise infinite by multi-looping these two numbers if
                    # you are understanding this as *remap of mirrored pointers, not single loop(zero)
                    ve = 0
                    idx = 0
                    idxLen = 0
                    tLenR = 0
                    tLenL = 0
                    for cnrAb in abcStr:
                        # most common < or > for then addressed sar, other functions in
                        # connection with this type addressing will know the decipher probable
                        # by the last static -vn:hn, 2(vertical): 3(horizontal), or how many palindrome
                        # rotations to do of a best probable linking correction pointed to further
                        # addr of sar variables in parallel added to sub-interlink of the original sar
                        if cnrAb == '>':
                            nmrStrA = '>'
                            tLenR+=1
                            idx+=1
                        elif cnrAb == '<':
                            nmrStrA = '<'
                            tLenL+=1
                            idx+=1
                        else:
                            # is a dot separator, what is the count?
                            idxLen+=1
                            if idxLen < 9:
                                if idx == 2:
                                    if nmrStrA == '>':
                                        tLenR+=1
                                    else:
                                        tLenL+=1
                                elif idx == 1:
                                    if nmrStrA == '>':
                                        tLenR+=2
                                    else:
                                        tLenL+=2
                                elif idx == 0:
                                    # and this is why two separate loops for counting abcStr & abrStr
                                    # are needed, for now keep count of this as occured, a void=equal;
                                    # the random shuffle function in the PySqTpp_Parser module that
                                    # assigns sar variable id's, mirror timed convex sorting, pretty good
                                    # at preventing this but of course can/will happen
                                    ve+=1
                                idx = 0
                                nmrStrA = None
                            else:
                                break
                    # now counting of abrStr and main reason cannot just do this type
                    # counts from the other codes above in one go; also, the void-equal..
                    # circumstance comparison is more likely to be in this string, abrStr
                    # is from all palindromes <|> comparisons and needed strict order,
                    # if this out of order, everything up to this point was out of order; this
                    # can be thought of as a quantum observation or the void-equal, whereof
                    # the previous constants very important to positions after a before next
                    # that spans this entire remap of every sar variable id being category new
                    idx = 0
                    idxLen = 0
                    for pCnrAb in abrStr:
                        if pCnrAb == '>':
                            nmrStrA == '>'
                            tLenR+=1
                            idx+=1
                        elif pCnrAb == '<':
                            nmrStrA == '<'
                            tLenL+=1
                            idx+=1
                        else:
                            # is the dot char separator, if went with 3 vertical & 2 horizontal grid
                            # compares at begin would be much more complex to count now
                            idxLen+=1
                            if idxLen < 9:
                                if ve > 0 and idx == 0:
                                    tLenR-=1
                                    tLenL-=1
                                    ve-=1
                                else:
                                    if ve > 0 and idx > 0 and idx < 3:
                                        if nmrStrA == '>' and tLenR > len(vrNmrLst):
                                            tLenR-=1
                                            ve-=1
                                        elif nmrStrA == '<' and tLenL < len(vrNmrLst):
                                            tLenL+=1
                                            ve-=1
                                        else:
                                            if nmrStrA == '>':
                                                tLenR-=1
                                            else:
                                                tLenL-=1
                                            ve-=1
                                    elif ve == 0 and idx > 0 and idx < 3:
                                        if nmrStrA == '>':
                                            tLenR+=1
                                        else:
                                            tLenL+=1
                                    else:
                                        # is a inverted multi-loop abstract! ve & idx both totally hidden, a
                                        # real grid to grid situation of your guess is as good as mine, this
                                        # would translate into a impossible 3d object if did all the math
                                        tLenR+=1
                                        tLenL+=1
                                idx = 0
                                nmrStrA = None
                            else:
                                break
                    # time to add the variable/pointers for special write into tqpt source file, count finished;
                    # temple variable added to tqpt source file cannot be found or updated from functions
                    # outside sar specific functions of this global variables library uses
                    idx = 0
                    idxLen = len(vrNmrLst)
                    rvmLst = [0]*idxLen
                    while idx < idxLen:
                        rvmLst[idx] = rngLst[idx] + ':' + rngLst[idx+1] + '-' + str(tLenL) + ':' + str(tLenR) + '-' + '2:3'
                        idx+=1
                    newSarAlpha = SarAlpha()
                    newSarAlpha.write_extension_source('wb_sar_remap', ",".join(rvmLst), dir_path, source_name)
                else:
                    # no found sar category(cat_pin) variable names
                    return -2
            else:
                # staqtapp tqpt source file was not found
                return -1
                
        except Exception as e:
            print("staqtapp error: ",e)
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

    def sar_map(self, is_read: bool, dsg_fnc: str, full_path: str):
        # @override PySqTppSarInterface.sar_map()
        return True
        


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
            elif ext_pnt == 'wb_sar_remap':
                with open(dir_path + '/' + source_name + '.tqpt', 'r+b') as fObjWsr:
                    with mmap.mmap(fObjWsr.fileno(), length=0, prot=mmap.PROT_READ) as mmapObjWsr:
                        wrdx = mmapObjWsr.read()
                        mmapObjWsr.close()
                    mmapObjWsr = None
                tm = time()
                jnLst = [wrdx.replace(b"\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!",b""), str.encode('\n<' + "**SAR**__MAP___" + ctime(tm) + '=' + source + '>\n!!!END_TQPT_FILE(-DO-NOT-EDIT-OR-REMOVE-)!!!')]
                with open(dir_path + '/' + source_name + '.tqpt', 'wb') as fObjWsr2x:
                    fObjWsr2x.write(b"".join(jnLst))
                    fObjWsr2x.close()
                fObjWsr2x = None
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





























