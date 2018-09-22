# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sat Sep 22 17:49:13 2018
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
runfpgs = [["09_17_2018", "01" ],  ["09_17_2018", "02" ]] #date, run_fpg_no
BadFEs, BadADCs = Abnormals()
rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/statistics_csv/"

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
    if ( (int(y[13][0]) > 0) and (int(y[14][0]) > 0) and (int(y[15][0]) > 0) and \
         (int(y[16][0]) > 0) and (int(y[17][0]) > 0) and (int(y[18][0]) > 0)  ):
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

for validtest in validtests:
    print validtest
#for validtest in [["Test027", False, False]]:
    t_pat = validtest[0]
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
    for runfpg in runfpgs:
        ccs_title = ccs_title + ["Date", "FPGADAC no"] + g_title[goft+8: goft+16] + ["FE_Valid", "ADC_Valid"]
    
    i_g = 0
    for cc in pd_chns:
        apaloc = cc[0]
        wibno = int(cc[6])
        fembno = int(cc[7])
        fembchn = int(cc[3])
        asicno = int(cc[4])
        for runfpg in runfpgs:
            for gc in g_chns:
                if (gc[goft+0] == apaloc):
                    if (int(gc[goft+5]) == fembchn ):
                        if (int(gc[goft+1]) == wibno ) and (int(gc[goft+2]) == fembno ) and (runfpg[0] == gc[1]) and (runfpg[1] == gc[3]) :
                            i_g = i_g + 1

                            if (bad_fe_flg):
                                z = "APA" + apaloc[1] + "WIB" + format(wibno, "1d") + "FEMB" + format(fembno, "1d") + "FE" + format(asicno, "1d") 
                                if ( z in BadFEs ):
                                    #if ( (cc[17] - cc[10]) > 800 ) and ( (cc[18] - cc[10]) < -500 ) :
                                    if ( (float(cc[17]) - float(cc[10])) < 800 ) and ( (float(cc[18]) - float(cc[10])) > -500 ) :
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

                            cc = cc + runfpg + gc[goft+8:goft+16]  + [fe_valid, adc_valid]
                            if (runfpg == runfpgs[-1] ):
                                ccs.append(cc)
    

                            print len(cc)
                            for k in range(len(cc)):
                                print ccs_title[k], cc[k]
                            exit()
#                    print cc
#                    print gc

#print i_g/2, len(cc)

#
#    if f == "femb_config_wr_v323_rms.cfg":
#        v323_cfgs = []
#        with open(root_path + f, 'r') as cf:
#            for cl in cf:
#                v323_cfgs.append ( cl.split(",")[0:5])
#    if f == "femb_config_wr_v325c_rms.cfg":
#        v325c_cfgs = []
#        with open(root_path + f, 'r') as cf:
#            for cl in cf:
#                v325c_cfgs.append ( cl.split(",")[0:5])
#
#precfgs_rd = []
#for idir in sorted(dirs):
#    if (idir.find("APA") >= 0 ):
#        apano = int(idir[3])
#        cfp = root_path + idir + "/" 
#        for subroot, subdirs, subfiles in os.walk(cfp):
#            break
#        for cff in sorted(subfiles):
#            cffp = cfp + cff
#            if (cffp.find("step11") > 0 ) and (cffp.find("ped_FE_ADC.txt") >=0 ) and (cffp.find("ped_FE_ADC.txt.swp") <0 ): #for rms
#                fembcfgs = []
#                with open(cffp, 'r') as cf:
#                    for cl in cf:
#                        fembcfgs.append(cl) 
#
#                if ( fembcfgs[1].find("step11")>= 0):
#                    wibno  = int (fembcfgs[1][3:5])
#                    fembno = int (fembcfgs[1][16])
#                    hexphase0 = hex(int(fembcfgs[2].split("=")[1][0:-1], 16))
#                    hexphase1 = hex(int(fembcfgs[3].split("=")[1][0:-1], 16))
#                    if (int(hexphase0,16) != 0xBF) or (int(hexphase1,16) != 0xBF) :
#                        print "ERROR ADC SYNC, not 0xBF, please check"
#                        exit()
#                    feadc_spi = []
#                    for i in range(72):
#                        feadc_spi.append(hex( int(fembcfgs[i+4][0:-1], 16) ))
#                    precfgs_rd.append([apano, wibno, fembno, hexphase0, hexphase1, feadc_spi])
#                else:
#                    print "ERROR Gain and Tp setting, quit, please check"
#                    exit()
#
##V325C_FEMBs = ["APA3WIB3FEMB1"]
##
#femb_cfgs = [["APA no (1-6)", "WIB no (0-4)", "FEMB no (0-3)", "FW Version", "WR Sequence", "WR ADDR (HEX)", "WR VALUE (HEX)", "RDBK VALUE (HEX)", "Note"]            , ]
#
#
#for ai in range(1,7,1):
#    for wi in range(0,5,1):
#        for fi in range(0,4,1):
#            if (ai == 3) and (wi==3) and (fi ==1) :
#                fw_ver = "V325C"
#                cfgs = copy.deepcopy(v325c_cfgs)
#            else:
#                fw_ver = "V0323"
#                cfgs = copy.deepcopy(v323_cfgs)
#            for precfg in precfgs_rd:
#                if (precfg[0] == ai) and (precfg[1] == wi) and (precfg[2] == fi) :
#                    femb_precfgs = precfg
#                    break
#
#            for i in range(len(cfgs)):
#                if (i >0):
#                    wr_addr = int(cfgs[i][1],16)
#                    if (wr_addr == 0x06 ):
#                        cfgs[i][2] = femb_precfgs[3]
#                        cfgs[i][3] = " NA "  
#                    #elif (wr_addr == 0x0F ):
#                    #    cfgs[i][2] = femb_precfgs[4]
#                    #    cfgs[i][3] = "  "  
#                    elif ( wr_addr in range(0x200, 0x248,1) ):
#                        cfgs[i][2] =  hex( int( femb_precfgs[5][wr_addr - 0x200], 16) )
#                        cfgs[i][3] =  cfgs[i][2]
#                    else:
#                        cfgs[i][2] =  hex( int(cfgs[i][2]  , 16) )
#                        if (cfgs[i][3].find("/") < 0 ):
#                            cfgs[i][3] =  hex(int(cfgs[i][3], 16))
#                        else:
#                            cfgs[i][3] = "  "  
#
#            for cfg in cfgs[1:]:
#                femb_cfgs.append([ai, wi, fi, fw_ver,int(cfg[0]), hex(int(cfg[1],16)), cfg[2],cfg[3],cfg[4],  ] )
#
#
#csvfile =  root_path + 'ProtoDUNE_SP_FEMBs_Config_rms.csv'
#    
#with open (csvfile, 'w') as fp:
#    for x in femb_cfgs:
#        fp.write(",".join(str(i) for i in x) +  "," + "\n")
#
#
#
