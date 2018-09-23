# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Sep 23 01:44:11 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import os.path
import math
import copy

def bad_adc_ana ( ccs ):
    bad_adc_ccs = []
    for cc in ccs:
        if cc[25] == "False" :
            bad_adc_ccs.append(cc)
    return bad_adc_ccs

def fe900_ana ( ccs ):
    fe900_ccs = []
    for cc in ccs:
        if cc[24] == "False" :
            fe900_ccs.append(cc)
    return fe900_ccs

def stuck_ana ( ccs ):
    stuck_ccs = []
    for cc in ccs:
        if float(cc[16]) > 0.95 :
            continue
        else:
            ped = float(cc[10])
            pedmod64 = ped%64
            rms = float(cc[11])
            sfrms = float(cc[14])
            encratio = (rms/sfrms)  
            fpg1 = cc[34] 
            fpg2 = cc[44] 
            if fpg1 != "None":
                egain = float(fpg1) 
                if ( egain >= 100 ) and (egain<= 180 ):
                    pass
                elif fpg2 != "None":
                    egain = float(fpg2) 
                    if ( egain >= 100 ) and (egain<= 180 ):
                        pass
                    else:
                        egain = 135
                else:
                    egain = 135
            else:
                egain = 135
            enc = rms * float(egain)
            sfenc = sfrms * egain
            #if ( sfenc > 400) and (( encratio > 1.5) or ( encratio < 0.5)) and ((pedmod64<60) or (pedmod64>15)):
            if ( sfenc > 400) and (( encratio > 1.5) or ( encratio < 0.5)) :
                stuck_ccs.append(cc)
    return stuck_ccs

def inactive_ana ( ccs ):
    inact_fe_ccs = []
    for cc in ccs:
        ped = float(cc[10])
        pp  = float(cc[17])
        pn  = float(cc[18])
        ppa = pp - ped
        pna = ped-pn
        if ( ppa < 800 ) and (pna < 300):
            inact_fe_ccs.append(cc) 
    return inact_fe_ccs

def open_ana ( ccs, enc_thr = 350 ):
    open_ccs = []
    for cc in ccs:
        rms = float(cc[11])
        fpg1 = cc[34] 
        fpg2 = cc[44] 
        if fpg1 != "None":
            egain = float(fpg1) 
            if ( egain >= 100 ) and (egain<= 180 ):
                pass
            elif fpg2 != "None":
                egain = float(fpg2) 
                if ( egain >= 100 ) and (egain<= 180 ):
                    pass
                else:
                    egain = 135
            else:
                egain = 135
        else:
            egain = 135
        enc = rms * float(egain)
        if (enc < enc_thr) :
            open_ccs.append(cc) 
    return open_ccs  

def noisechn_ana ( ccs, enc_thr = 1000 ):
    noisechn_ccs = []
    for cc in ccs:
        rms = float(cc[11])
        fpg1 = cc[34] 
        fpg2 = cc[44] 
        if fpg1 != "None":
            egain = float(fpg1) 
            if ( egain >= 100 ) and (egain<= 180 ):
                pass
            elif fpg2 != "None":
                egain = float(fpg2) 
                if ( egain >= 100 ) and (egain<= 180 ):
                    pass
                else:
                    egain = 135
            else:
                egain = 135
        else:
            egain = 135
        enc = rms * float(egain)
        if (enc > enc_thr) :
            noisechn_ccs.append(cc) 
    return noisechn_ccs  

def wires_ana ( ccs, wire = "U" ):
    wires_ccs = []
    for cc in ccs:
        if (cc[2][0] == wire):
            wires_ccs.append(cc) 
    return wires_ccs  

def apa_ana ( ccs, apa = 1 ):
    apa_ccs = []
    for cc in ccs:
        if (int(cc[0][1]) == apa):
            apa_ccs.append(cc) 
    return apa_ccs  

def wib_ana ( apa_ccs, wib = 0 ):
    wib_ccs = []
    for cc in ccs:
        if (int(cc[6]) == wib):
            wib_ccs.append(cc) 
    return wib_ccs  

def femb_ana ( wib_ccs, femb = 0 ):
    femb_ccs = []
    for cc in ccs:
        if (int(cc[7]) == femb):
            femb_ccs.append(cc) 
    return femb_ccs  

def classify_ana (ccs):
    bad_adc_ccs = bad_adc_ana(ccs)
    for i in bad_adc_ccs:
        ccs.remove(i)
    
    fe900_ccs = fe900_ana(ccs)
    for i in fe900_ccs:
        ccs.remove(i)
    
    stuck_ccs = stuck_ana ( ccs )
    for i in stuck_ccs:
        ccs.remove(i)
                
    inact_fe_ccs = inactive_ana(ccs)
    for i in inact_fe_ccs:
        ccs.remove(i)
    
    open_ccs = open_ana ( ccs, enc_thr = 350)
    for i in open_ccs:
        ccs.remove(i)
    
    good_ccs = ccs
    return good_ccs, bad_adc_ccs, fe900_ccs, stuck_ccs, inact_fe_ccs, open_ccs

def pnum_ana ( ccs, pnum = 0 ): #for number parameter only
    tmp = []
    for cc in ccs:
        tmp.append(cc[pnum])
    tmp = map(float, tmp)
    return  tmp 

def paras_ana (ccs):
    peds =np.array( pnum_ana(ccs, pnum=10) )
    rmss =np.array( pnum_ana(ccs, pnum=11) )
    sfrmss =np.array( pnum_ana(ccs, pnum=14) )
    pps =np.array( pnum_ana(ccs, pnum=17) ) - peds
    pns =np.array( pnum_ana(ccs, pnum=18) ) - peds
    fpgs =np.array( pnum_ana(ccs, pnum=32) )
    inls =np.array( pnum_ana(ccs, pnum=33) )
    encs = rmss * fpgs
    sfencs = sfrmss * fpgs
#    fpg2s = pnum_ana(ccs, pnum=42)
#    inl2s = pnum_ana(ccs, pnum=43)
#    fpg3s = pnum_ana(ccs, pnum=32)
#    inl3s = pnum_ana(ccs, pnum=33)
#    fpg4s = pnum_ana(ccs, pnum=42)
#    inl4s = pnum_ana(ccs, pnum=43)
    return peds, encs, sfencs, fpgs, inls, pps, pns 



rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/statistics_csv/"
t_pat = "Test004"
PCE = t_pat + "_ProtoDUNE_CE_characterization" + ".csv"
ppath = rpath + PCE
ccs = []
with open(ppath, 'r') as fp:
    for cl in fp:
        tmp = cl.split(",")
        x = []
        for i in tmp:
            x.append(i.replace(" ", ""))
        x = x[:-1]
        ccs.append(x)
ccs_title = ccs[0]
ccs = ccs[1:]
print len(ccs)
good_ccs, bad_adc_ccs, fe900_ccs, stuck_ccs, inact_fe_ccs, open_ccs = classify_ana (ccs)

noisechn_css =  noisechn_ana( good_ccs, enc_thr = 1000 )

uwire_ccs =  wires_ana ( good_ccs, wire = "U" )
uparas =  paras_ana (uwire_ccs)
for i in uparas:
    print np.mean(i), np.std(i)

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
vwire_ccs =  wires_ana ( good_ccs, wire = "V" )
vparas =  paras_ana (vwire_ccs)
for i in vparas:
    print np.mean(i), np.std(i)

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
xwire_ccs =  wires_ana ( good_ccs, wire = "X" )
xparas =  paras_ana (xwire_ccs)
for i in xparas:
    print np.mean(i), np.std(i)


print len(uwire_ccs), len(vwire_ccs), len(xwire_ccs)
print len(noisechn_css)
print len(ccs)



