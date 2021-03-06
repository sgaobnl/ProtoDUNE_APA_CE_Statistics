# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Mon Dec  9 13:37:50 2019
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
from Abnormals import Abnormals

#t_pat = "Test001"
#             [  "09_23_2018_run03rms_run03fpg_run01asi.csv",\ #200mV
#                "09_23_2018_run03rms_run02fpg_run01asi.csv",\ #900mV
#                "09_23_2018_run02rms_run01fpg_run01asi.csv",\ #200mV, 0xFF0xFF
#                "09_17_2018_run01rms_run01fpg_run01asi.csv",\ #200mV, 0xFF0xFF
#                "09_17_2018_run02rms_run02fpg_run01asi.csv",\ #900mV, 0xFF0xFF
#                ] 

#runfpgs = [["09_23_2018", "03" ],  ["09_23_2018", "02" ],  ["09_23_2018", "01" ],  ["09_17_2018", "01" ],  ["09_17_2018", "02" ]] #date, run_fpg_no
runfpgs = [["1l_06_2019", "01" ],  ] #date, run_fpg_no
BadFEs, BadADCs = Abnormals()
#rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/statistics_csv/"
rpath = '''/Users/shanshangao/Documents/tmp/PD/'''

index_f = "tests_index.csv"
tindexs = []
with open(rpath + index_f, 'r') as fp:
    for cl in fp:
        tmp = cl.split(",")
        x = []
        for i in tmp:
            x.append(i.replace(" ", ""))
        x = x[:-1]
        tindexs.append(x)
tindexs = tindexs [1:]

tmp = []
for y in tindexs:
#    if ( (int(y[13][0]) > 0) and (int(y[14][0]) > 0) and (int(y[15][0]) > 0) and \
#         (int(y[16][0]) > 0) and (int(y[17][0]) > 0) and (int(y[18][0]) > 0)  ) and (y[0] == "#39"):
    if  (y[0] == "#39"):
        t_pat = "Test" + format( int(y[0][1:]), "03d")
        if "200" in y[9]:
            bad_fe_flg = True
        else:
            bad_fe_flg = False
        if "0xFF" in y[12]:
            bad_adc_flg = True
        else:
            bad_adc_flg = False
        tmp.append ([t_pat, bad_fe_flg, bad_adc_flg])
validtests = tmp
print validtests

for validtest in validtests:
#for validtest in [["Test004", True, True]]:
    print validtest
    t_pat = validtest[0]
    print t_pat + " is running"
    bad_fe_flg = validtest[1]
    bad_adc_flg = validtest[1]

    for root, dirs, files in os.walk(rpath):
        break
    
    csvfs = []
    for f in files:
        if ("results.csv" in f) and ( "Test" in f):
            csvfs.append(f)
    tfs = []
    for f in csvfs:
        if (t_pat in f):
            tfs.append(rpath+f)
    
    pd_chns = []
    for f in tfs:
        with open(f, 'r') as cf:
            l = 0
            for cl in cf:
                tmp = cl.split(",") 
                chp = []
                for i in tmp:
                    chp.append(i.replace(" ", ""))
                chp = chp[:-1]
     
                if (len(chp) > 20 ):
                    if (l >0):
                        pd_chns.append ( chp )
                    else:
                        pd_title = chp
                l = l+1
    
    gainfs = []
    for f in files:
        if ("run01asi.csv" in f) and ( "rms" in f) and ( "fpg" in f):
            gainfs.append(f)
    g_chns = []
    for f in gainfs:
        gf = rpath+ f
        with open(gf, 'r') as gfp:
            apano = int(f[3])
            gdate = f[5:15]
            grmsno = f[f.find("rms")-2: f.find("rms")]
            gfpgno = f[f.find("fpg")-2: f.find("fpg")]
            
            l = 0
            for gl in gfp:
                tmp = gl.split(",") 
                chp = []
                for i in tmp:
                    chp.append(i.replace(" ", ""))
     
                chp = chp[:-1]
     
                if (len(chp) > 5 ):
                    if (l >0):
                        g_chns.append ( [apano, gdate, grmsno, gfpgno, ] + chp )
                    else:
                        g_title = ["APA_No", "Date", "RMS no", "FPGA-DAC no", ] + chp
                l = l+1
    
    goft = 4
    ccs = []
    ccs_title = pd_title
    ccs_title = ccs_title  + ["FE_Valid", "ADC_Valid"]
    for runfpg in runfpgs:
        ccs_title = ccs_title + ["Date", "FPGADAC no"] + g_title[goft+8: goft+16] 
    
    i_g = 0
    for cc in pd_chns:
        apaloc = cc[0]
        wibno = int(cc[6])
        fembno = int(cc[7])
        fembchn = int(cc[3])
        asicno = int(cc[8])

        if (bad_fe_flg):
            z = "APA" + apaloc[1] + "WIB" + format(wibno, "1d") + "FEMB" + format(fembno, "1d") + "FE" + format(asicno, "1d") 
            if ( z in BadFEs ):
                if ( (float(cc[17]) - float(cc[10])) > 800 ) and ( abs(float(cc[18]) - float(cc[10])) > 300 ) :
                    fe_valid = True
                else:
                    fe_valid = False
            else:
                fe_valid = True
        else:
            fe_valid = True
        if (bad_adc_flg):
            z = "APA" + apaloc[1] + "WIB" + format(wibno, "1d") + "FEMB" + format(fembno, "1d") + "ADC" + format(asicno, "1d") 
            if ( z in BadADCs ):
                adc_valid = False
            else:
                adc_valid = True
        else:
            adc_valid = True
        cc = cc  + [fe_valid, adc_valid]

        for runfpg in runfpgs:
            for gc in g_chns:
                if (gc[goft+0] == apaloc):
                    if (int(gc[goft+5]) == fembchn ):
                        if (int(gc[goft+1]) == wibno ) and (int(gc[goft+2]) == fembno ) and (runfpg[0] == gc[1]) and (runfpg[1] == gc[3]) :
                            i_g = i_g + 1
                            cc = cc + runfpg + gc[goft+8:goft+16] 
                            if (runfpg == runfpgs[-1] ):
                                z = "APA" + apaloc[1] + "WIB" + format(wibno, "1d") + "FEMB" + format(fembno, "1d") + "FE" + format(asicno, "1d") 
                                if ( z in BadFEs )  :
                                    cc[24+2] = cc[34+2]
                                    cc[25+2] = cc[35+2]
                                    cc[26+2] = cc[36+2]
                                    cc[27+2] = cc[37+2]
                                    cc[28+2] = cc[38+2]
                                    cc[29+2] = cc[39+2]
                                    cc[30+2] = cc[40+2]
                                    cc[31+2] = cc[41+2]
                                    cc[32+2] = cc[42+2]
                                    cc[33+2] = cc[43+2]
                                ccs.append(cc)
    
    PCE = t_pat + "_ProtoDUNE_CE_characterization" + ".csv"
    with open (rpath+PCE, 'w') as fp:
        fp.write(",".join(str(i) for i in ccs_title) +  "," + "\n")
        for x in ccs:
            fp.write(",".join(str(i) for i in x) +  "," + "\n")
    print PCE
    print "Wait for next..."
print "Done"
