# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Tue Oct  9 11:50:45 2018
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


#P2_200mV_ledge = [ [1	,79	,2370 ] ,[2	,79	,2160 ] ,[5	,79	,1300 ]
#,[8	,79	,826  ] ,[10	,79	,660  ] ,[15	,79	,445  ]
#,[20	,79	,340  ] ,[30	,80	,230  ] ,[40	,84	,185  ]
#,[50	,93	,165  ] ,[60	,105	,155  ] ,[70	,137	,175  ]
#,[71	,138	,173  ] ,[72	,145	,175  ] ,[75	,190	,220  ]
#,[80	,530	,563  ] ,[90	,530	,500  ] ,[100	,530	,445  ]
#,[120	,500	,360  ] ,[150	,550	,320  ] ,[200	,1100	,475  ]
#,[250	,1700	,610  ] ,[300	,3100	,864  ] ]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE output \nwithout Pulse-Post-Ledge")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of Pulse-Post-Ledge", fontsize = 20)
#plt.text( 25, 700,  "SBND FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,5000])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p2_200mV_ledge.png")
#plt.close()

#P2_900mV_ledge = [ 
#[1	,50	,1611 ],
#[2	,54	,1605 ],
#[5	,88	,1600 ],
#[8	,140	,1609 ],
#[10	,175	,1611 ],
#[15	,220	,1356 ],
#[20	,230	,1067 ],
#[30	,290	,898  ],
#[40	,380	,883  ],
#[50	,470	,875  ],
#[60	,520	,810  ],
#[70	,550	,737  ],
#[80	,570	,670  ],
#[90	,610	,635  ],
#[100	,640	,600  ],
#[120	,710	,560  ],
#[150	,800	,506  ],
#[200	,1000	,483  ],
#[250	,1000	,391  ],
#[300	,1000	,331  ],      
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_900mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE Output \n Before Saturation")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of FE Gets Saturated", fontsize = 20)
#plt.text( 25, 700,  "SBND FEMB \nP2 FE ASIC(FE2CHN10) \nBL 900mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,1500])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p2_900mV.png")
#plt.close()
##

#P2_200mV_ledge = [ [1	,79	,2370 ] ,[2	,79	,2160 ] ,[5	,79	,1300 ]
#,[8	,79	,826  ] ,[10	,79	,660  ] ,[15	,79	,445  ]
#,[20	,79	,340  ] ,[30	,80	,230  ] ,[40	,84	,185  ]
#,[50	,93	,165  ] ,[60	,105	,155  ] ,[70	,137	,175  ]
#,[71	,138	,173  ] ,[72	,145	,175  ] ,[75	,190	,220  ]
#,[80	,530	,563  ] ,[90	,530	,500  ] ,[100	,530	,445  ]
#,[120	,500	,360  ] ,[150	,550	,320  ] ,[200	,1100	,475  ]
#,[250	,1700	,610  ] ,[300	,3100	,864  ] ]
#
#P2_900mV_ledge = [ 
#[1	,50	,1611 ],
#[2	,54	,1605 ],
#[5	,88	,1600 ],
#[8	,140	,1609 ],
#[10	,175	,1611 ],
#[15	,220	,1356 ],
#[20	,230	,1067 ],
#[30	,290	,898  ],
#[40	,380	,883  ],
#[50	,470	,875  ],
#[60	,520	,810  ],
#[70	,550	,737  ],
#[80	,570	,670  ],
#[90	,610	,635  ],
#[100	,640	,600  ],
#[120	,710	,560  ],
#[150	,800	,506  ],
#[200	,1000	,483  ],
#[250	,1000	,391  ],
#[300	,1000	,331  ],      
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 900,  "SBND FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p2_200mV_900mV.png")
#plt.close()



#
#P2_200mV_ledge = [ [1	,79	,2370 ] ,[2	,79	,2160 ] ,[5	,79	,1300 ]
#,[8	,79	,826  ] ,[10	,79	,660  ] ,[15	,79	,445  ]
#,[20	,79	,340  ] ,[30	,80	,230  ] ,[40	,84	,185  ]
#,[50	,93	,165  ] ,[60	,105	,155  ] ,[70	,137	,175  ]
#,[71	,138	,173  ] ,[72	,145	,175  ] ,[75	,190	,220  ]
#,[80	,530	,563  ] ,[90	,530	,500  ] ,[100	,530	,445  ]
#,[120	,500	,360  ] ,[150	,550	,320  ] ,[200	,1100	,475  ]
#,[250	,1700	,610  ] ,[300	,3100	,864  ] ]
#
#P2_200mV_1nA = [
#[1	,105	,2750 ]
#,[2	,110	,2750 ]
#,[5	,110	,1811 ]
#,[8	,110	,1150 ]
#,[10	,110	,920  ]
#,[15	,110	,617  ]
#,[20	,110	,465  ]
#,[30	,115	,330  ]
#,[40	,130	,270  ]
#,[50	,160	,274  ]
#,[60	,550	,772  ]
#,[70	,630	,761  ]
#,[80	,650	,690  ]
#,[90	,650	,611  ]
#,[100	,650	,552  ]
#,[120	,1000	,713  ]
#,[150	,1200	,693  ]
#,[200	,2100	,890  ]
#,[250	,5000	,1714 ]
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_200mV_1nA:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "500pA")
#plt.title( "Devision Plot of Pulse-Post-Ledge", fontsize = 20)
#plt.text( 25, 900,  "SBND FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "1nA")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p2_200mV_1nA.png")
#plt.close()



#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#
#fig = plt.figure(figsize=(12,8))
##ax1 = plt.subplot2grid((2*10, 2*10), (0*10, 0*10), colspan=9, rowspan=9)
##ax2 = plt.subplot2grid((2*10, 2*10), (0*10, 1*10), colspan=9, rowspan=9)
##ax3 = plt.subplot2grid((2*10, 2*10), (1*10+1, 0*10), colspan=9, rowspan=9)
##ax4 = plt.subplot2grid((2*10, 2*10), (1*10+1, 1*10), colspan=9, rowspan=9)
#ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1)
#ax2 = plt.subplot2grid((2, 2), (0, 1), colspan=1, rowspan=1)
#ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
#ax4 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)
# 
#P2_50us = [
#[90	,166	,0 	,0	,0 ],
#[100	,177	,35 	,150	,175 ],
#[110	,193	,50	,300	,125 ],
#[120	,208	,65	,375	,100 ],
#[130	,229	,78	,425	,90  ],   
#[150	,256	,100	,500	,75  ], 
#[180	,309	,135	,575	,60  ], 
#[200	,341	,145	,600	,50  ], 
#[250	,424	,175	,660	,50  ], 
#[300	,506	,185	,650	,40  ], 
#[350	,592	,195	,660	,30  ], 
#[400	,674	,190	,625	,30  ], 
#[450	,761	,195	,625	,30  ], 
#[500	,842	,195	,625	,30  ], 
#[600	,1012	,200	,575	,30  ], 
#[700	,1180	,240	,600	,30  ], 
#[800	,1346	,250	,600	,30  ], 
#[900	,1523	,360	,725	,25  ], ] 
#
#mvs = []
#amp = []
#ledge = []
#ledge_w = []
#ledge_g = []
#for i in P2_50us:
#    mvs.append(i[0])
#    amp.append(i[1])
#    ledge.append(i[2])
#    ledge_w.append(i[3])
#    ledge_g.append(i[4])
#amp = np.array(amp) *0.5
#ledge = np.array(ledge) *0.5
#
#ax1.plot(mvs, amp, color = 'b')
#ax1.scatter(mvs, amp, color = 'b')
#ax1.set_title( "FE Output Pulse", fontsize = 12)
#ax1.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax1.set_xlim([0,1000])
#ax1.set_ylabel( "FE Output Pulse Amplitude/ mV", fontsize = 12)
#ax1.set_ylim([0,800])
#
#
#ax2.plot(mvs, ledge, color = 'r')
#ax2.scatter(mvs, ledge, color = 'r')
#ax2.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax2.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax2.set_xlim([0,1000])
#ax2.set_ylabel( "Ledge Amplitude/ mV", fontsize = 12)
#ax2.set_ylim([0,200])
#
#
#ax3.plot(mvs, ledge_w, color = 'm')
#ax3.scatter(mvs, ledge_w, color = 'm')
#ax3.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax3.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax3.set_xlim([0,1000])
#ax3.set_ylabel( "Ledge Last Time/ us", fontsize = 12)
#ax3.set_ylim([0,800])
#
#
#ax4.plot(mvs, ledge_g, color = 'g')
#ax4.scatter(mvs, ledge_g, color = 'g')
#ax4.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax4.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax4.set_xlim([0,1000])
#ax4.set_ylabel( "Gap Between Pulse and Ledge / us", fontsize = 12)
#ax4.set_ylim([0,200])
#
#
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#plt.savefig("./p2_50us_ledge.png")
##plt.show()
#plt.close()

#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#fig = plt.figure(figsize=(12,8))
#ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1)
#ax2 = plt.subplot2grid((2, 2), (0, 1), colspan=1, rowspan=1)
#ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
#ax4 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)
#
#P2_10us = [
#[75	,629	,0      ,0      ,0    ],		
#[85	,711	,35	,200	,175  ],
#[100	,839	,70	,400	,120  ],
#[110	,921	,90	,475	,100  ],
#[120	,1002	,115	,524	,100  ],
#[130	,1091	,135	,625	,75   ],
#[150	,1250	,170	,675	,60   ],
#[180	,1498	,230	,800	,50   ],
#[200	,1668	,270	,825	,50   ],
#[250	,2081	,350	,900	,40   ],
#[300	,2500	,420	,1000	,40   ],
#[350	,2780	,480	,1000	,40   ],
#[400	,2782	,520	,1000	,40   ],
#[450	,2784	,560	,1000	,40   ],
#[500	,2785	,580	,1000	,40   ],
#]
#
#mvs = []
#amp = []
#ledge = []
#ledge_w = []
#ledge_g = []
#for i in P2_10us:
#    mvs.append(i[0])
#    amp.append(i[1])
#    ledge.append(i[2])
#    ledge_w.append(i[3])
#    ledge_g.append(i[4])
#amp = np.array(amp) *0.5
#ledge = np.array(ledge) *0.5
#
#ax1.plot(mvs, amp, color = 'b')
#ax1.scatter(mvs, amp, color = 'b')
#ax1.set_title( "FE Output Pulse", fontsize = 12)
#ax1.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax1.set_xlim([0,500])
#ax1.set_ylabel( "FE Output Pulse Amplitude/ mV", fontsize = 12)
#ax1.set_ylim([0,1500])
#
#
#ax2.plot(mvs, ledge, color = 'r')
#ax2.scatter(mvs, ledge, color = 'r')
#ax2.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax2.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax2.set_xlim([0,500])
#ax2.set_ylabel( "Ledge Amplitude/ mV", fontsize = 12)
#ax2.set_ylim([0,300])
#
#
#ax3.plot(mvs, ledge_w, color = 'm')
#ax3.scatter(mvs, ledge_w, color = 'm')
#ax3.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax3.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax3.set_xlim([0,500])
#ax3.set_ylabel( "Ledge Last Time/ us", fontsize = 12)
#ax3.set_ylim([0,1200])
#
#
#ax4.plot(mvs, ledge_g, color = 'g')
#ax4.scatter(mvs, ledge_g, color = 'g')
#ax4.set_title( "Pulse-Post-Ledge", fontsize = 12)
#ax4.set_xlabel( "Calibration Ramp Amplitude/ mV", fontsize = 12)
#ax4.set_xlim([0,500])
#ax4.set_ylabel( "Gap Between Pulse and Ledge / us", fontsize = 12)
#ax4.set_ylim([0,200])
#
#
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#plt.savefig("./p2_10us_ledge.png")
##plt.show()
#plt.close()
#


#P3_200mV_ledge = [ 
#[1	,85	,2600 ],
#[2	,85	,2460 ],
#[5	,85	,1405 ],
#[8	,85	,895  ],
#[10	,85	,720  ],
#[15	,85	,480  ],
#[20	,85	,370  ],
#[30	,85	,250  ],
#[40	,90	,205  ],
#[50	,95	,175  ],
#[60	,105	,165  ],
#[70	,120	,165  ],
#[80	,450	,497  ],
#[90	,500	,488  ],
#[100	,550	,475  ],
#[120	,580	,420  ],
#[150	,1100	,630  ],
#[200	,2000	,850  ], 
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P3_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE output \nwithout Pulse-Post-Ledge")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of Pulse-Post-Ledge", fontsize = 20)
#plt.text( 25, 700,  "SBND FEMB \nP3 FE ASIC(FE4CHN12) \nBL 200mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,5000])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p3_200mV_ledge.png")
#plt.close()
#
#
#P3_200mV_ledge = [ 
#[1	,85	,2600 ],
#[2	,85	,2460 ],
#[5	,85	,1405 ],
#[8	,85	,895  ],
#[10	,85	,720  ],
#[15	,85	,480  ],
#[20	,85	,370  ],
#[30	,85	,250  ],
#[40	,90	,205  ],
#[50	,95	,175  ],
#[60	,105	,165  ],
#[70	,120	,165  ],
#[80	,450	,497  ],
#[90	,500	,488  ],
#[100	,550	,475  ],
#[120	,580	,420  ],
#[150	,1100	,630  ],
#[200	,2000	,850  ], 
#]
#
#
#
#P3_200mV_1nA = [
#[1	,85	,2595 ]
#,[2	,95	,2634 ]
#,[5	,115	,1814 ]
#,[8	,115	,1150 ]
#,[10	,115	,970  ]
#,[15	,115	,650  ]
#,[20	,115	,490  ]
#,[30	,115	,335  ]
#,[40	,125	,280  ]
#,[50	,140	,250  ]
#,[60	,200	,295  ]
#,[70	,650	,800  ]
#,[80	,700	,755  ]
#,[90	,710	,685  ]
#,[100	,730	,632  ]
#,[120	,850	,622  ]
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P3_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P3_200mV_1nA:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "500pA")
#plt.title( "Devision Plot of Pulse-Post-Ledge", fontsize = 20)
#plt.text( 25, 900,  "SBND FEMB \nP3 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "1nA")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p3_200mV_1nA.png")
#plt.close()

#
#P3_900mV_ledge = [ 
#[1	,50	,1650 ],
#[2	,55	,1650 ],
#[5	,90	,1620 ],
#[8	,145	,1650 ],
#[10	,180	,1640 ],
#[15	,190	,1160 ],
#[20	,190	,886  ],
#[30	,220	,686  ],
#[40	,250	,600  ],
#[50	,300	,582  ],
#[60	,350	,572  ],
#[70	,390	,532  ],
#[80	,395	,487  ],
#[90	,430	,477  ],
#[100	,480	,472  ],
#[120	,570	,472  ],
#[150	,700	,467  ],
#[200	,1000	,487  ],
#[250	,1200	,472  ],
#[300	,1300	,432  ],
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P3_900mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE Output \n Before Saturation")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of FE Gets Saturated", fontsize = 20)
#plt.text( 25, 700,  "SBND FEMB \nP3 FE ASIC(FE6CHN2) \nBL 900mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,1500])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p3_900mV.png")
#plt.close()


#P3_200mV_ledge = [ 
#[1	,85	,2600 ],
#[2	,85	,2460 ],
#[5	,85	,1405 ],
#[8	,85	,895  ],
#[10	,85	,720  ],
#[15	,85	,480  ],
#[20	,85	,370  ],
#[30	,85	,250  ],
#[40	,90	,205  ],
#[50	,95	,175  ],
#[60	,105	,165  ],
#[70	,120	,165  ],
#[80	,450	,497  ],
#[90	,500	,488  ],
#[100	,550	,475  ],
#[120	,580	,420  ],
#[150	,1100	,630  ],
#[200	,2000	,850  ], 
#]
#
#
#P3_900mV_ledge = [ 
#[1	,50	,1650 ],
#[2	,55	,1650 ],
#[5	,90	,1620 ],
#[8	,145	,1650 ],
#[10	,180	,1640 ],
#[15	,190	,1160 ],
#[20	,190	,886  ],
#[30	,220	,686  ],
#[40	,250	,600  ],
#[50	,300	,582  ],
#[60	,350	,572  ],
#[70	,390	,532  ],
#[80	,395	,487  ],
#[90	,430	,477  ],
#[100	,480	,472  ],
#[120	,570	,472  ],
#[150	,700	,467  ],
#[200	,1000	,487  ],
#[250	,1200	,472  ],
#[300	,1300	,432  ],
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P3_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) *0.5
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P3_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) *0.5
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 900,  "SBND FEMB \nP3 FE ASIC(FE6CHN2) \nBL 900mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / mV", fontsize = 20)
#plt.grid()
#plt.ylim([0,1500])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./p3_200mV_900mV.png")
#plt.close()


#P2_200mV_ledge = [
#[1	,53	,2850 ],
#[2	,53	,2560 ],
#[5	,53	,1550 ],
#[8	,53	,990  ], 
#[10	,53	,799  ], 
#[15	,53	,535  ], 
#[20	,53	,412  ], 
#[30	,55	,285  ], 
#[40	,55	,215  ], 
#[50	,55	,186  ], 
#[60	,57	,156  ], 
#[70	,60	,143  ], 
#[80	,65	,137  ], 
#[90	,71	,136  ], 
#[100	,85	,140  ], 
#[120	,145	,200  ], 
#[150	,410	,430  ], 
#[200	,410	,320  ], 
#[250	,420	,267  ], 
#[300	,750	,407  ], 
#[400	,780	,330  ], 
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) 
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE output \nwithout Pulse-Post-Ledge")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of Pulse-Post-Ledge", fontsize = 20)
#plt.text( 25, 1500,  "ProtoDUNE FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / LSB", fontsize = 20)
#plt.grid()
#plt.ylim([0,3000])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,2000])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./P_p2_200mV_ledge.png")
#plt.close()
#
#P2_900mV_ledge = [ 
#[1	,55	,2716],
#[2	,58	,2707],
#[5	,93	,2705],
#[8	,145	,2668],
#[10	,180	,2653],
#[15	,185	,1822],
#[20	,185	,1375],
#[30	,185	,921 ],
#[40	,185	,705 ],
#[50	,185	,557 ],
#[60	,185	,470 ],
#[70	,500	,1069],
#[80	,600	,1125],
#[90	,650	,1077],
#[100	,650	,965 ],
#[120	,700	,875 ],
#[150	,850	,865 ],
#[200	,1100	,863 ],
#[250	,1400	,900 ],
#[300	,1500	,840 ],
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_900mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) 
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "Maximum FE Output \n Before Saturation")
#plt.legend (loc = "upper left", fontsize=20)
#plt.title( "Devision Plot of FE Gets Saturated", fontsize = 20)
#plt.text( 25, 1500,  "ProtoDUNE FEMB \nP2 FE ASIC(FE2CHN10) \nBL 900mV, 500pA \n14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / LSB", fontsize = 20)
#plt.grid()
#plt.ylim([0,3000])
#plt.xlim([0,300])
#plt.tick_params(labelsize=20)
#
#ax2 = plt.twinx()
#ax2.scatter(ts, mvs, color='g')
#ax2.plot(ts, mvs, color='g', label = "Calibration Ramp")
#ax2.set_ylim([0,2000])
#ax2.set_ylabel( "Calibration Ramp Amplitude/ mV", fontsize = 20)
#plt.legend (loc = "upper right", fontsize=20)
#plt.xlim([0,300])
#
#plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./P_p2_900mV.png")
#plt.close()
##

#P2_200mV_ledge = [
#[1	,53	,2850 ],
#[2	,53	,2560 ],
#[5	,53	,1550 ],
#[8	,53	,990  ], 
#[10	,53	,799  ], 
#[15	,53	,535  ], 
#[20	,53	,412  ], 
#[30	,55	,285  ], 
#[40	,55	,215  ], 
#[50	,55	,186  ], 
#[60	,57	,156  ], 
#[70	,60	,143  ], 
#[80	,65	,137  ], 
#[90	,71	,136  ], 
#[100	,85	,140  ], 
#[120	,145	,200  ], 
#[150	,410	,430  ], 
#[200	,410	,320  ], 
#[250	,420	,267  ], 
#[300	,750	,407  ], 
#[400	,780	,330  ], 
#]
#
#P2_900mV_ledge = [ 
#[1	,55	,2716],
#[2	,58	,2707],
#[5	,93	,2705],
#[8	,145	,2668],
#[10	,180	,2653],
#[15	,185	,1822],
#[20	,185	,1375],
#[30	,185	,921 ],
#[40	,185	,705 ],
#[50	,185	,557 ],
#[60	,185	,470 ],
#[70	,500	,1069],
#[80	,600	,1125],
#[90	,650	,1077],
#[100	,650	,965 ],
#[120	,700	,875 ],
#[150	,850	,865 ],
#[200	,1100	,863 ],
#[250	,1400	,900 ],
#[300	,1500	,840 ],
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs)
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) 
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 1500,  "ProtoDUNE FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / LSB", fontsize = 20)
#plt.grid()
#plt.ylim([0,3000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
##plt.show()
#plt.savefig("./Pp2_200mV_900mV.png")
#plt.close()


#P2_200mV_ledge = [
#[1	,53	,2850 ],
#[2	,53	,2560 ],
#[5	,53	,1550 ],
#[8	,53	,990  ], 
#[10	,53	,799  ], 
#[15	,53	,535  ], 
#[20	,53	,412  ], 
#[30	,55	,285  ], 
#[40	,55	,215  ], 
#[50	,55	,186  ], 
#[60	,57	,156  ], 
#[70	,60	,143  ], 
#[80	,65	,137  ], 
#[90	,71	,136  ], 
#[100	,85	,140  ], 
#[120	,145	,200  ], 
#[150	,410	,430  ], 
#[200	,410	,320  ], 
#[250	,420	,267  ], 
#[300	,750	,407  ], 
#[400	,780	,330  ], 
#]
#
#P2_900mV_ledge = [ 
#[1	,55	,2716],
#[2	,58	,2707],
#[5	,93	,2705],
#[8	,145	,2668],
#[10	,180	,2653],
#[15	,185	,1822],
#[20	,185	,1375],
#[30	,185	,921 ],
#[40	,185	,705 ],
#[50	,185	,557 ],
#[60	,185	,470 ],
#[70	,500	,1069],
#[80	,600	,1125],
#[90	,650	,1077],
#[100	,650	,965 ],
#[120	,700	,875 ],
#[150	,850	,865 ],
#[200	,1100	,863 ],
#[250	,1400	,900 ],
#[300	,1500	,840 ],
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) * (135.0 / 6250 ) * (np.array(ts)  ) 
#
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) * (135.0 / 6250 ) * (np.array(ts2)  )
#
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
# 
#fig = plt.figure(figsize=(12,8))
#
#plt.scatter(ts, outs, color='r')
#plt.plot(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 1500,  "ProtoDUNE FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "FE Output Measured by COTS ADC / LSB", fontsize = 20)
#plt.grid()
#plt.ylim([0,3000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.plot(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#
#plt.show()
##plt.savefig("./Pp2_200mV_900mV.png")
#plt.close()


#P2_200mV_ledge = [ [1	,79	,2370 ] ,[2	,79	,2160 ] ,[5	,79	,1300 ]
#,[8	,79	,826  ] ,[10	,79	,660  ] ,[15	,79	,445  ]
#,[20	,79	,340  ] ,[30	,80	,230  ] ,[40	,84	,185  ]
#,[50	,93	,165  ] ,[60	,105	,155  ] ,[70	,137	,175  ]
#,[71	,138	,173  ] ,[72	,145	,175  ] ,[75	,190	,220  ]
#,[80	,530	,563  ] ,[90	,530	,500  ] ,[100	,530	,445  ]
#,[120	,500	,360  ] ,[150	,550	,320  ] ,[200	,1100	,475  ]
#,[250	,1700	,610  ] ,[300	,3100	,864  ] ]
#
#P2_900mV_ledge = [ 
#[1	,50	,1611 ],
#[2	,54	,1605 ],
#[5	,88	,1600 ],
#[8	,140	,1609 ],
#[10	,175	,1611 ],
#[15	,220	,1356 ],
#[20	,230	,1067 ],
#[30	,290	,898  ],
#[40	,380	,883  ],
#[50	,470	,875  ],
#[60	,520	,810  ],
#[70	,550	,737  ],
#[80	,570	,670  ],
#[90	,610	,635  ],
#[100	,640	,600  ],
#[120	,710	,560  ],
#[150	,800	,506  ],
#[200	,1000	,483  ],
#[250	,1000	,391  ],
#[300	,1000	,331  ],      
#]
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) * (245/6250.0) * np.array(ts) 
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) * (245/6250.0) * np.array(ts2)
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#fig = plt.figure(figsize=(12,8))
#plt.scatter(ts, outs, color='r')
#plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 4000,  "SBND FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "Area / fC", fontsize = 20)
#plt.ylim([10,20000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#plt.grid(b = True, which = 'both')
#plt.legend (loc = "upper right", fontsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#plt.savefig("./p2_area.png")
#plt.close()
#
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs =  np.array(mvs) * 1.203
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 =  np.array(mvs2) * 1.203
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#fig = plt.figure(figsize=(12,8))
#plt.scatter(ts, outs, color='r')
#plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 150, 20,  "SBND FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "Injected Charge / fC", fontsize = 20)
#plt.ylim([10,20000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#plt.grid(b = True, which = 'both')
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
##plt.show()
#plt.savefig("./p2_injected_fC.png")
#plt.close()


#P2_200mV_ledge = [
#[1	,53	,2850 ],
#[2	,53	,2560 ],
#[5	,53	,1550 ],
#[8	,53	,990  ], 
#[10	,53	,799  ], 
#[15	,53	,535  ], 
#[20	,53	,412  ], 
#[30	,55	,285  ], 
#[40	,55	,215  ], 
#[50	,55	,186  ], 
#[60	,57	,156  ], 
#[70	,60	,143  ], 
#[80	,65	,137  ], 
#[90	,71	,136  ], 
#[100	,85	,140  ], 
#[120	,145	,200  ], 
#[150	,410	,430  ], 
#[200	,410	,320  ], 
#[250	,420	,267  ], 
#[300	,750	,407  ], 
#[400	,780	,330  ], 
#]
#
#P2_900mV_ledge = [ 
#[1	,55	,2716],
#[2	,58	,2707],
#[5	,93	,2705],
#[8	,145	,2668],
#[10	,180	,2653],
#[15	,185	,1822],
#[20	,185	,1375],
#[30	,185	,921 ],
#[40	,185	,705 ],
#[50	,185	,557 ],
#[60	,185	,470 ],
#[70	,500	,1069],
#[80	,600	,1125],
#[90	,650	,1077],
#[100	,650	,965 ],
#[120	,700	,875 ],
#[150	,850	,865 ],
#[200	,1100	,863 ],
#[250	,1400	,900 ],
#[300	,1500	,840 ],
#]
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs = np.array(lsbs) * (130/6250.0) * np.array(ts) 
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 = np.array(lsbs2) * (130/6250.0) * np.array(ts2)
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#fig = plt.figure(figsize=(12,8))
#plt.scatter(ts, outs, color='r')
#plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 25, 4000,  "ProtoDUNE FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "Area / fC", fontsize = 20)
#plt.ylim([10,20000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#plt.grid(b = True, which = 'both')
#plt.legend (loc = "upper right", fontsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#plt.savefig("./Pp2_area.png")
#plt.close()
#
#
#
#ts = []
#mvs = []
#lsbs = []
#for i in P2_200mV_ledge:
#    ts.append(i[0])
#    mvs.append(i[1])
#    lsbs.append(i[2])
#outs =  np.array(mvs) * 1.203
#ts2 = []
#mvs2 = []
#lsbs2 = []
#for i in P2_900mV_ledge:
#    ts2.append(i[0])
#    mvs2.append(i[1])
#    lsbs2.append(i[2])
#outs2 =  np.array(mvs2) * 1.203
#import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#import matplotlib.patches as mpatches
#import matplotlib.mlab as mlab
#fig = plt.figure(figsize=(12,8))
#plt.scatter(ts, outs, color='r')
#plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
#plt.title( "Dynamic Range", fontsize = 20)
#plt.text( 150, 20,  "ProtoDUNE FEMB \nP2 FE ASIC(FE8CHN13) \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
#plt.xlabel( "Time of Ramp / us", fontsize = 20)
#plt.ylabel( "Injected Charge / fC", fontsize = 20)
#plt.ylim([10,20000])
#plt.xlim([0,300])
#plt.scatter(ts2, outs2, color='b')
#plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
#plt.tick_params(labelsize=20)
#plt.grid(b = True, which = 'both')
#plt.legend (loc = "upper right", fontsize=20)
##plt.tick_params(labelsize=20)
#plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
##plt.show()
#plt.savefig("./Pp2_injected_fC.png")
#plt.close()


P3_200mV_ledge = [ 
[1	,85	,2600 ],
[2	,85	,2460 ],
[5	,85	,1405 ],
[8	,85	,895  ],
[10	,85	,720  ],
[15	,85	,480  ],
[20	,85	,370  ],
[30	,85	,250  ],
[40	,90	,205  ],
[50	,95	,175  ],
[60	,105	,165  ],
[70	,120	,165  ],
[80	,450	,497  ],
[90	,500	,488  ],
[100	,550	,475  ],
[120	,580	,420  ],
[150	,1100	,630  ],
[200	,2000	,850  ], 
]


P3_900mV_ledge = [ 
[1	,50	,1650 ],
[2	,55	,1650 ],
[5	,90	,1620 ],
[8	,145	,1650 ],
[10	,180	,1640 ],
[15	,190	,1160 ],
[20	,190	,886  ],
[30	,220	,686  ],
[40	,250	,600  ],
[50	,300	,582  ],
[60	,350	,572  ],
[70	,390	,532  ],
[80	,395	,487  ],
[90	,430	,477  ],
[100	,480	,472  ],
[120	,570	,472  ],
[150	,700	,467  ],
[200	,1000	,487  ],
[250	,1200	,472  ],
[300	,1300	,432  ],
]

ts = []
mvs = []
lsbs = []
for i in P3_200mV_ledge:
    ts.append(i[0])
    mvs.append(i[1])
    lsbs.append(i[2])
outs = np.array(lsbs) * (245/6250.0) * np.array(ts) 
ts2 = []
mvs2 = []
lsbs2 = []
for i in P3_900mV_ledge:
    ts2.append(i[0])
    mvs2.append(i[1])
    lsbs2.append(i[2])
outs2 = np.array(lsbs2) * (245/6250.0) * np.array(ts2)
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.mlab as mlab
fig = plt.figure(figsize=(12,8))
plt.scatter(ts, outs, color='r')
plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
plt.title( "Dynamic Range", fontsize = 20)
plt.text( 25, 4000,  "SBND FEMB \nP3 FE ASIC \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
plt.xlabel( "Time of Ramp / us", fontsize = 20)
plt.ylabel( "Area / fC", fontsize = 20)
plt.ylim([10,20000])
plt.xlim([0,300])
plt.scatter(ts2, outs2, color='b')
plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
plt.tick_params(labelsize=20)
plt.grid(b = True, which = 'both')
plt.legend (loc = "upper right", fontsize=20)
plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
plt.savefig("./Pp3_area.png")
plt.close()



ts = []
mvs = []
lsbs = []
for i in P3_200mV_ledge:
    ts.append(i[0])
    mvs.append(i[1])
    lsbs.append(i[2])
outs =  np.array(mvs) * 1.203
ts2 = []
mvs2 = []
lsbs2 = []
for i in P3_900mV_ledge:
    ts2.append(i[0])
    mvs2.append(i[1])
    lsbs2.append(i[2])
outs2 =  np.array(mvs2) * 1.203
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.mlab as mlab
fig = plt.figure(figsize=(12,8))
plt.scatter(ts, outs, color='r')
plt.semilogy(ts, outs, color='r', label = "FE BL 200mV")
plt.title( "Dynamic Range", fontsize = 20)
plt.text( 150, 20,  "SBND FEMB \nP3 FE ASIC \nBL 200mV, 14mV/fC, 2.0us", fontsize = 20)
plt.xlabel( "Time of Ramp / us", fontsize = 20)
plt.ylabel( "Injected Charge / fC", fontsize = 20)
plt.ylim([10,20000])
plt.xlim([0,300])
plt.scatter(ts2, outs2, color='b')
plt.semilogy(ts2, outs2, color='b', label = "FE BL 900mV")
plt.tick_params(labelsize=20)
plt.grid(b = True, which = 'both')
plt.legend (loc = "upper right", fontsize=20)
#plt.tick_params(labelsize=20)
plt.tight_layout( rect=[0.00, 0.05, 1, 0.95])
#plt.show()
plt.savefig("./Pp3_injected_fC.png")
plt.close()



