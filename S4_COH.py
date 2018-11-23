# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Sep 30 17:13:06 2018
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
import sys


rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/test_statis/"
rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/coh_results_uvx/"
rpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/coh_results/"
t_pat = sys.argv[1]
PCE = t_pat + "COH_ProtoDUNE_CE_characterization_summary" + ".csv"
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
cohccs_title = ccs[0]
cohccs = ccs[1:]


if (True):
    cohccs_title  =["APA no", "Wire", "APA wire no"] + cohccs_title  
    lenapa = len(cohccs)
    print lenapa
    for c in range(lenapa):
        apa_side = (cohccs[c][0][0])
        apano = int(cohccs[c][0][1])
        fembloc = int(cohccs[c][0][2:4])
        wire_type = cohccs[c][2][0]
        fembwire_no = int(cohccs[c][2][1:3])
        #set B01 X(U/V)#01 as start, clock-wise wire number
        if (wire_type == "X" ):
            w_femb = 48
        else:
            w_femb = 40
        apawireno = ( fembloc -1 ) * w_femb + (w_femb-fembwire_no) + 1
        apawireinfo = [apano, wire_type , apawireno]
        cohccs[c] = apawireinfo + cohccs[c] 
    
    apa_ccs_title = cohccs_title
    apa_ccs =cohccs 
     
    def wires_sorted ( apa_ccs, apano = 1, wiretype = "U" ):
        wires_ccs = []
        for cc in apa_ccs:
            if (cc[0] == apano) and (cc[1] == wiretype):
                egain = float(cc[19])
                x = [cc[0], cc[1], cc[2], int(float(cc[23])*egain), int(float(cc[25])*egain), int(float(cc[27])*egain), cc[21], cc[3][0]+ cc[3][2:4], int(cc[-1]) ]
                wires_ccs.append(x) 
        wires_ccs = sorted(wires_ccs, key= lambda i : i[2])
        return wires_ccs  
    
    def rms_dis_plot(wt, clfys, direct = 1 ):
        fig = plt.figure(figsize=(12,6))
        lenwt = len(wt)
        lenwth = lenwt//2
        fembloc = "A00"
        if direct == 1: #0~400
            x_range = range(lenwth)
            axlim = [1,lenwth+1]
            plt.xlim(axlim)
        elif direct == 2:#400 --> 800
            x_range = range(lenwth, lenwt)
            axlim = [lenwth + 1,lenwt+1]
            plt.xlim(axlim)
        elif direct == 3:#400 --> 1
            x_range = range(lenwth)
            axlim = [lenwth+1,1]
            plt.xlim(axlim)
        elif direct == 4:#800 --> 400
            x_range = range(lenwth, lenwt)
            axlim = [lenwt + 1,lenwth+1]
            plt.xlim(axlim)
    
        if axlim[0] > axlim[1]:
            x_pos1 = axlim[0] - 100
            x_pos2 = axlim[0] - 200
            xoft = 35
        else:
            x_pos1 = axlim[0] + 100
            x_pos2 = axlim[0] + 200
            xoft = 5
     
        for i in x_range: 
            if fembloc != wt[i][7]:
                fembloc = wt[i][7]
                plt.text (wt[i][2]+xoft, 1850, "%s"%fembloc, fontsize=20 )
                plt.vlines(wt[i][2], 0, 2000, color='c', linestyles="dotted", linewidth=0.8)
    
            for x in clfys:
                if wt[i][6] in x[0]:
                    if wt[i][8] >= 4:
                        #plt.bar([wt[i][2]], [wt[i][3]], color = x[1], width = 1)
                        plt.bar([wt[i][2]], [wt[i][4]], color = x[1], width = 1)
                        #plt.bar([wt[i][2]], [wt[i][5]], color = x[1], width = 1)
                    else:
                        #plt.bar([wt[i][2]], [wt[i][3]], color = x[1], width = 1)
                        #if wt[i][3] > 2000:
                        #    plt.bar([wt[i][2]], 1000, color = 'orange', width = 1)
                        #else:
                        #    plt.bar([wt[i][2]], [wt[i][3]//2], color = 'orange', width = 1)
 
                        plt.bar([wt[i][2]], [wt[i][4]], color = x[1], width = 1)
                        if wt[i][4] > 2000:
                            plt.bar([wt[i][2]], 1000, color = 'orange', width = 1)
                        else:
                            plt.bar([wt[i][2]], [wt[i][4]//2], color = 'orange', width = 1)

                        #plt.bar([wt[i][2]], [wt[i][5]], color = x[1], width = 1)
                        #if wt[i][5] > 2000:
                        #    plt.bar([wt[i][2]], 1000, color = 'orange', width = 1)
                        #else:
                        #    plt.bar([wt[i][2]], [wt[i][5]//2], color = 'orange', width = 1)
 
        plt.ylim([0,2000])
    
        #istatus = "RawCOH"
        istatus = "PostCOH"
        #istatus = "COHCOH"
        plt.text (x_pos1,     1650, "$\\blacksquare$: %s"%clfys[0][2], color = clfys[0][1], fontsize=16 )
        plt.text (x_pos1,     1550, "$\\blacksquare$: %s"%clfys[1][2], color = clfys[1][1], fontsize=16 )
        plt.text (x_pos1,     1450, "$\\blacksquare$: %s"%clfys[2][2], color = clfys[2][1], fontsize=16 )
        plt.text (x_pos2, 1650, "$\\blacksquare$: %s"%clfys[3][2], color = clfys[3][1], fontsize=16 )
        plt.text (x_pos2, 1550, "$\\blacksquare$: %s"%clfys[4][2], color = clfys[4][1], fontsize=16 )
        plt.text (x_pos2, 1450, "$\\blacksquare$: No Flitering", color = "orange", fontsize=16 )
        plt.title( "%s Plane of APA%d"%(wiretype, apano), fontsize = 20)
        plt.xlabel( "APA Channel Num", fontsize = 20)
        plt.ylabel( "ENC / e$^-$", fontsize = 20)
        plt.tick_params(labelsize=20)
        plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
        #plt.savefig("/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/plots_uvx/%s_%s_%s_Plane_of_APA%d_direct%d.png"%(istatus,t_pat, wiretype, apano, direct))
        plt.savefig("/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/plots/%s_%s_%s_Plane_of_APA%d_direct%d.png"%(istatus,t_pat, wiretype, apano, direct))
        plt.close()
    
    import matplotlib.pyplot as plt
    clfys =  [[ ["C01","C02","C03","C04","C05","C06"], "m", "Inactive"],
                [["C07"], "b", "Sticky"],
                [["C08"], "k", "Open"],
                [["C09", "C10", "C11"],"r", "ENC > 800e$^-$"],
                [["C12"], "g", "ENC <= 800e$^-$"] ]
    for apano in range(1,4,1):
        for wiretype in ["U", "V", "X"]:
            wt = wires_sorted ( apa_ccs, apano = apano, wiretype = wiretype)
            rms_dis_plot(wt, clfys, direct = 1 )
            rms_dis_plot(wt, clfys, direct = 4 )
            
    for apano in range(4,7,1):
        for wiretype in ["U", "V", "X"]:
            wt = wires_sorted ( apa_ccs, apano = apano, wiretype = wiretype)
            rms_dis_plot(wt, clfys, direct = 2 )
            rms_dis_plot(wt, clfys, direct = 3 )
    


#if (True):
if (False):
    ###########export results ###################
    i = ccs_title 
    b =  [i[0], i[1],i[2], i[6], i[7], i[8], i[9], i[21], i[22], i[10], "ENC \ e-", i[11], i[14],  i[16], "Pulse Postive Amplitude",  "Pulse Negative Amplitude", i[34], i[35], "Code", "Code Description"]
    c =[b] #set title
    
    all_ccs = [
        [bad_adc_ccs   , "C01", "ADC Sync Phase Error "],                               
        [fe900_ccs     , "C02", "Inactive FE ASIC"],                               
        [inact_fe_ccs  , "C03", "Inactive FE Channels "],                               
        [none_gain_ccs , "C04", "FE channels fails calibration"],                               
        [big_gain_ccs  , "C05", "Inverted Gain > 180 e-/bin "],                               
        [small_gain_ccs, "C06", "Inverted Gain < 90 e-/bin"],                               
        [stuck_ccs     , "C07", "Channels with signifcant stuck bit"],                               
        [open_ccs      , "C08", "Broken connection pre FE input"],                               
        [noisechn2k_ccs, "C09", "ENC > 2000e-"],                               
        [noisechn1k_ccs, "C10", "1000e- < ENC <= 2000 e- "],
        [noisechn8h_ccs, "C11", "800e- < ENC <= 1000 e-  "],
        [good_ccs      , "C12", "Good"],                                 
        ]
    
    for ccs_x in all_ccs:
        for i in ccs_x[0]:
            b =  [i[0], i[1],i[2], i[6], i[7], i[8], i[9], i[21], i[22], i[10], int(float(i[11])*float(i[34])),  i[11], i[14], i[16], str(float(i[17])-float(i[10])),  str(float(i[18])-float(i[10])), i[34], i[35], ccs_x[1], ccs_x[2],]
            c.append(b)
    
    rfile =  rpath + PCE[0:-4] + "_summary" + ".csv"
    print rfile
    with open (rfile, 'w') as fp:
        for x in c:
            fp.write(",".join(str(i) for i in x) +  "," + "\n")
    
    ###########export results end ###################

#if (True):
if (False):
    #############Make histogram plot
    uwire_ccs =  wires_ana ( good_ccs, wire = "U" )
    uparas =  paras_ana (uwire_ccs)
    
    vwire_ccs =  wires_ana ( good_ccs, wire = "V" )
    vparas =  paras_ana (vwire_ccs)
    
    xwire_ccs =  wires_ana ( good_ccs, wire = "X" )
    xparas =  paras_ana (xwire_ccs)
    
    unoise2k_ccs =  wires_ana ( noisechn2k_ccs , wire = "U" )
    unoise2kparas =  paras_ana (unoise2k_ccs)
    unoise1k_ccs =  wires_ana ( noisechn1k_ccs , wire = "U" )
    unoise1kparas =  paras_ana (unoise1k_ccs)
    unoise8h_ccs =  wires_ana ( noisechn8h_ccs , wire = "U" )
    unoise8hparas =  paras_ana (unoise8h_ccs)
    
    vnoise2k_ccs =  wires_ana ( noisechn2k_ccs , wire = "X" )
    vnoise2kparas =  paras_ana (vnoise2k_ccs)
    vnoise1k_ccs =  wires_ana ( noisechn1k_ccs , wire = "V" )
    vnoise1kparas =  paras_ana ( vnoise1k_ccs)
    vnoise8h_ccs =  wires_ana ( noisechn8h_ccs , wire = "V" )
    vnoise8hparas =  paras_ana (vnoise8h_ccs)
    
    xnoise2k_ccs =  wires_ana ( noisechn2k_ccs , wire = "X" )
    xnoise2kparas =  paras_ana (xnoise2k_ccs)
    xnoise1k_ccs =  wires_ana ( noisechn1k_ccs , wire = "X" )
    xnoise1kparas =  paras_ana ( xnoise1k_ccs)
    xnoise8h_ccs =  wires_ana ( noisechn8h_ccs , wire = "X" )
    xnoise8hparas =  paras_ana (xnoise8h_ccs)
    
    
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    import matplotlib.patches as mpatches
    import matplotlib.mlab as mlab
    
    fig = plt.figure(figsize=(12*2,6*2))
    ax1 = plt.subplot2grid((3*10, 3*10), (0*10+0, 0*10+1), colspan=9, rowspan=8)
    ax2 = plt.subplot2grid((3*10, 3*10), (0*10+0, 1*10+1), colspan=9, rowspan=8)
    ax3 = plt.subplot2grid((3*10, 3*10), (0*10+0, 2*10+1), colspan=9, rowspan=8)
    ax4 = plt.subplot2grid((3*10, 3*10), (1*10+0, 0*10+1), colspan=9, rowspan=8)
    ax5 = plt.subplot2grid((3*10, 3*10), (1*10+0, 1*10+1), colspan=9, rowspan=8)
    ax6 = plt.subplot2grid((3*10, 3*10), (1*10+0, 2*10+1), colspan=9, rowspan=8)
    ax7 = plt.subplot2grid((3*10, 3*10), (2*10+0, 0*10+1), colspan=9, rowspan=8)
    ax8 = plt.subplot2grid((3*10, 3*10), (2*10+0, 1*10+1), colspan=9, rowspan=8)
    ax9 = plt.subplot2grid((3*10, 3*10), (2*10+0, 2*10+1), colspan=9, rowspan=8)
    #ax1 = plt.subplot2grid((3, 3), (0+0, 0+0), colspan=1, rowspan=1)
    #ax2 = plt.subplot2grid((3, 3), (0+0, 1+0), colspan=1, rowspan=1)
    #ax3 = plt.subplot2grid((3, 3), (0+0, 2+0), colspan=1, rowspan=1)
    #ax4 = plt.subplot2grid((3, 3), (1+0, 0+0), colspan=1, rowspan=1)
    #ax5 = plt.subplot2grid((3, 3), (1+0, 1+0), colspan=1, rowspan=1)
    #ax6 = plt.subplot2grid((3, 3), (1+0, 2+0), colspan=1, rowspan=1)
    #ax7 = plt.subplot2grid((3, 3), (2+0, 0+0), colspan=1, rowspan=1)
    #ax8 = plt.subplot2grid((3, 3), (2+0, 1+0), colspan=1, rowspan=1)
    #ax9 = plt.subplot2grid((3, 3), (2+0, 2+0), colspan=1, rowspan=1)
    
    
    
    def enc_hist_plt (ax, ys, noise2k, noise1k, noise8h, binw = 10, plane = "U plane", title="Histogram of ENC of ", x_t = "ENC / e$^-$", y_t = "Channel Counts" ) :
        ys_mean0 =  np.mean(ys)
        ys_mean = ( ys_mean0 // binw ) * binw 
        ys_std = np.std(ys)
        N = len(ys)
        sigma3 = int(( ((ys_std*3)//binw) + 1 )*binw)
        ax.grid()
        label = "%dchns: %d $\pm$ %d e$^-$"%(N, ys_mean0, ys_std)
        weights = np.ones_like(ys)/float(len(ys))
        #ax.hist(ys,  weights=weights,  bins=(sigma3*2//10), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', label= label, color='b', rwidth=0.9 )
        ax.hist(ys,   bins=(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', label= label, color='g', rwidth=0.8 )
        gaussian_x = range(int(ys_mean - sigma3), int(ys_mean + sigma3 ), 1 )
        gaussian_y = mlab.normpdf(gaussian_x, ys_mean0, ys_std) 
        ax.plot(gaussian_x, gaussian_y*binw*N, color='b')
    
        ys = noise2k
        N1 = len(ys)
        if (N1 > 0 ):
            ys_mean0 =  np.mean(ys)
            ys_mean = ( ys_mean0 // binw ) * binw 
            ys_std = np.std(ys)
            sigma3 = int(( ((ys_std*3)//binw) + 1 )*binw)
            ax.hist(ys,  bins=(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', color='r', rwidth=0.9 )
    
        ys = noise1k
        N2 = len(ys)
        if (N2 > 0 ):
            ys_mean0 =  np.mean(ys)
            ys_mean = ( ys_mean0 // binw ) * binw 
            ys_std = np.std(ys)
            sigma3 = int(( ((ys_std*3)//binw) + 1 )*binw)
            ax.hist(ys,  bins=(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', color='r', rwidth=0.9 )
    
        ys = noise8h
        N3 = len(ys)
        if (N3 > 0 ):
            ys_mean0 =  np.mean(ys)
            ys_mean = ( ys_mean0 // binw ) * binw 
            ys_std = np.std(ys)
            label = "%dchns: > 800 e$^-$"%(N1 + N2 + N3)
            sigma3 = int(( ((ys_std*3)//binw) + 1 )*binw)
            ax.hist(ys,  bins=(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', label = label, color='r', rwidth=0.9 )
    
    
        ax.set_title( title + plane + " (%d Chns)"%(N+N1+N2+N3), fontsize = 18 )
        ax.set_ylabel(y_t, fontsize = 20 )
        ax.set_ylim([0,1000])
        ax.set_xlabel(x_t, fontsize = 20 )
        ax.set_xlim([0,2000])
        ax.legend(loc='best', fontsize = 20)
        ax.tick_params(labelsize=20)
    
    def gain_hist_plt (ax, ys, noise2k, noise1k, noise8h, binw = 2, plane = "U plane", title="Histogram of Gain of ", x_t = "Inverted Gain / (e$^-$/bit)", y_t = "Channel Counts" ) :
        tmp = []
        for i in ys:
            tmp.append(i)
        for i in noise2k:
            tmp.append(i)
        for i in noise1k:
            tmp.append(i)
        for i in noise8h:
            tmp.append(i)
        ys = tmp
        ys_mean0 =  np.mean(ys)
        ys_mean = ( ys_mean0 // binw ) * binw 
        ys_std = np.std(ys)
        N = len(ys)
        sigma3 = int(( ((ys_std*3)//binw) + 1 )*binw)
        ax.grid()
        label = "%dchns, %d $\pm$ %d (e$^-$/bit)"%(N, ys_mean0, ys_std)
        weights = np.ones_like(ys)/float(len(ys))
        ax.hist(ys,   bins=(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', label= label, color='g', rwidth=0.8 )
        gaussian_x = range(int(ys_mean - sigma3), int(ys_mean + sigma3 ), 1 )
        gaussian_y = mlab.normpdf(gaussian_x, ys_mean0, ys_std) 
        ax.plot(gaussian_x, gaussian_y*binw*N, color='b')
    
        ax.set_title( title + plane + " (%d Chns)"%(N), fontsize = 18 )
        ax.set_ylabel(y_t, fontsize = 20 )
        ax.set_ylim([0,1000])
        ax.set_xlabel(x_t, fontsize = 20 )
        ax.set_xlim([50,200])
        ax.legend(loc='best', fontsize = 20)
        ax.tick_params(labelsize=20)
    
    def inl_hist_plt (ax, ys, noise2k, noise1k, noise8h, binw = 1, plane = "U plane", title="Histogram of INL of ", x_t = "Nonlinearity / %", y_t = "Channel Counts" ) :
        tmp = []
        for i in ys:
            tmp.append(i)
        for i in noise2k:
            tmp.append(i)
        for i in noise1k:
            tmp.append(i)
        for i in noise8h:
            tmp.append(i)
        ys = np.array(tmp) * 100
        ys_mean0 =  np.mean(ys)
        ys_mean =  ys_mean0 
        ys_std = np.std(ys)
        N = len(ys)
        sigma3 = (( ((ys_std*3)/binw) + 1 )*binw)
        ax.grid()
        label = "%dchns\n%.2f $\pm$ %.2f %%"%(N, ys_mean0, ys_std)
        weights = np.ones_like(ys)/float(len(ys))
        ax.hist(ys,   bins=int(sigma3*2//binw), stacked = True,range=(ys_mean-sigma3, ys_mean+sigma3),  histtype='bar', label= label, color='g', rwidth=0.8 )
    
        ax.set_title( title + plane + " (%d Chns)"%(N), fontsize = 18 )
        ax.set_ylabel(y_t, fontsize = 20 )
        ax.set_ylim([0,1000])
        ax.set_xlabel(x_t, fontsize = 20 )
        ax.set_xlim([0,2])
        ax.legend(loc='best', fontsize = 20)
        ax.tick_params(labelsize=20)
    
    
     
     
    #plt.text(0.05, 0.05, 'Provided by BNL CE Group', fontsize=30, color='gray', ha='right', va='top', alpha=0.5)
        
    
    ##return peds, encs, sfencs, fpgs, inls, pps, pns 
    ##enc_hist_plt (ax1, uparas[1], unoiseparas[1], noise1k, noise8h, plane = "U plane", title="Histogram of Gain", x_t = "ENC / e$^-$", y_t = "Normalized counts" ) 
    enc_hist_plt (ax1, uparas[1], unoise2kparas[1] , unoise1kparas[1] , unoise8hparas[1], binw = 20, plane = "U plane", title="Histogram of ENC of ", x_t = "ENC / e$^-$", y_t = "Channel Counts" ) 
    enc_hist_plt (ax2, vparas[1], vnoise2kparas[1] , vnoise1kparas[1] , vnoise8hparas[1], binw = 20, plane = "V plane", title="Histogram of ENC of ", x_t = "ENC / e$^-$", y_t = "Channel Counts" ) 
    enc_hist_plt (ax3, xparas[1], xnoise2kparas[1] , xnoise1kparas[1] , xnoise8hparas[1], binw = 20, plane = "X plane", title="Histogram of ENC of ", x_t = "ENC / e$^-$", y_t = "Channel Counts" ) 
    
    gain_hist_plt (ax4, uparas[3], unoise2kparas[3] , unoise1kparas[3] , unoise8hparas[3], binw = 2, plane = "U plane", title="Histogram of Gain of ", x_t = "Inverted Gain / (e$^-$/bit)", y_t = "Channel Counts" ) 
    gain_hist_plt (ax5, vparas[3], vnoise2kparas[3] , vnoise1kparas[3] , vnoise8hparas[3], binw = 2, plane = "V plane", title="Histogram of Gain of ", x_t = "Inverted Gain / (e$^-$/bit)", y_t = "Channel Counts" ) 
    gain_hist_plt (ax6, xparas[3], xnoise2kparas[3] , xnoise1kparas[3] , xnoise8hparas[3], binw = 2, plane = "X plane", title="Histogram of Gain of ", x_t = "Inverted Gain / (e$^-$/bit)", y_t = "Channel Counts" ) 
    
    inl_hist_plt (ax7, uparas[4], unoise2kparas[4] , unoise1kparas[4] , unoise8hparas[4], binw = 0.05, plane = "U plane", title="Histogram of INL of ", x_t = "Nonlinearity / %", y_t = "Channel Counts" ) 
    inl_hist_plt (ax8, vparas[4], vnoise2kparas[4] , vnoise1kparas[4] , vnoise8hparas[4], binw = 0.05, plane = "V plane", title="Histogram of INL of ", x_t = "Nonlinearity / %", y_t = "Channel Counts" ) 
    inl_hist_plt (ax9, xparas[4], xnoise2kparas[4] , xnoise1kparas[4] , xnoise8hparas[4], binw = 0.05, plane = "X plane", title="Histogram of INL of ", x_t = "Nonlinearity / %", y_t = "Channel Counts" ) 
    
    
    
    plt.tight_layout( rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig("./abc.png")
    plt.close()
    
    #############Make histogram plot
