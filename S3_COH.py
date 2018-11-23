# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Thu Sep 27 17:45:53 2018
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
t_pat = sys.argv[1]
PCE = t_pat + "_ProtoDUNE_CE_characterization_summary" + ".csv"
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

cpath = "/Users/shanshangao/Google_Drive_BNL/tmp/pd_tmp/coh_results/"

for root, dirs, files in os.walk(cpath):
    break

cohcsvfs = []
for f in files:
    if (".csv" in f) and ( "COH_" in f):
        cohcsvfs.append(f)

cohtitle = []
cohapa = []
for f in cohcsvfs:
    li = 0
    with open(cpath+f, 'r') as fp:
        for cl in fp:
            tmp = cl.split(",")
            x = []
            for i in tmp:
                x.append(i.replace(" ", ""))
            x = x[:-1]
            if ( li != 0 ):
                cohapa.append(x)
            else:
                cohtitle = x
            li = li + 1

cohccs_title = ccs_title + ["rawrms", "rawped", "postrms", "postped", "cohrms", "cohped", "coh_chns"]
cohccs = []
for ci in ccs:
    for cohi in cohapa:
        if (ci[0] == cohi[0]) and (ci[2] == cohi[4]) and (ci[3] == cohi[1]) and (ci[4] == cohi[2]) : 
            cohccs.append(ci + cohi[8:15])
            break

COH = t_pat + "COH_ProtoDUNE_CE_characterization_summary" + ".csv"
with open (rpath+COH, 'w') as fp:
    fp.write(",".join(str(i) for i in cohccs_title) +  "," + "\n")
    for x in cohccs:
        fp.write(",".join(str(i) for i in x) +  "," + "\n")

print len(cohccs)

