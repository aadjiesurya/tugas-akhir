# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:33:42 2019

@author: aadjie
"""

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
"""
def read(x):
    y = pd.read_table(str(x)+'_0-5my_t3.txt', header=None, delim_whitespace=True)
    y = y.assign(bagian=int(x))
    return y[y[0]>0]
def read1(x):
    y = pd.read_table(str(x)+'_0-5my_t3.txt', header=None, delim_whitespace=True)
    y = y.assign(bagian=int(x))
    return y
hil1=read(1)
hil2=read(2)
hil3=read1(3)
hil4=read(4)
hil5=read(5)
hil6=read(6)
hil7=read(7)
hil8=read(8)
hil9=read(9)
hil10=read(10)
hil11=read(11)
total = hil1.append([hil2,hil3,hil4,hil5,hil6,hil7,hil8,hil9,hil10,hil11])
total.index = np.arange(0, len(total), 1)
total = total.assign(nomor=np.nan)
total = total.sort_values(['bagian',1])
#buat dump waktu dan pengurutan
urut = 0
total.iat[0,9] = 1
for line in range(len(total)-1):
    if total.iat[line,1] == total.iat[line-1,1]:
        total.iat[line,9] = urut
    elif total.iat[line,1] > total.iat[line-1,1]:
            urut = urut+1
            total.iat[line,9] = urut            
    else:
        urut = 1
        total.iat[line,9] = urut
total.iloc[-1, total.columns.get_loc('nomor')] = total.iloc[-2, total.columns.get_loc('nomor')]
total.loc[(total['bagian'] == 3) & (total[0]<0), 'bagian'] = 1.0
total = total.sort_values(['nomor','bagian',0])
total.index = np.arange(0, len(total), 1)

#buat index gabungan
total = total.assign(index=np.nan)
total.iat[0,10] = total.iat[0,0]
a = 0
b = 0
k = [0,255,509,764,1019,1274,1529,1784,2039,2294,2558]
for line in range(len(total)-1):
    if total.iat[line,9] == total.iat[line-1,9]:
        total.iat[line,1] = total.iat[line-1,1]
        if total.iat[line,0]>total.iat[line-1,0]:
            total.iat[line,10] = total.iat[line,0]+k[a]
            if total.iat[line,0] > total.iat[line+1,0]:
                a = a+1
        elif total.iat[line,0] < total.iat[line-1,0]:
            total.iat[line,10] = total.iat[line,0]+k[a]
    elif total.iat[line,9] > total.iat[line-1,9]:
        a = 0
        total.iat[line,10] = total.iat[line,0]+k[a]
total.iloc[-1, total.columns.get_loc('index')] =  total.iloc[-2, total.columns.get_loc('index')] + total.iloc[-1, total.columns.get_loc(0)] - total.iloc[-2, total.columns.get_loc(0)]
total=total[['index',1,2,3,4,5,6,7,'bagian','nomor',0]]
total.iat[-1,1] = total.iat[-2,1]
np.savetxt('5my.txt', total, delimiter=" ", fmt="%s")
"""
'''
def read(x):
    y = pd.read_table('discard'+str(x)+'.txt', delim_whitespace=True, header=None)
    y = y.assign(bagian=int(x))
    return y
hil1=read(1)
hil2=read(2)
hil3=read(3)
hil4=read(4)
hil5=read(5)
hil6=read(6)
hil7=read(7)
hil8=read(8)
hil9=read(9)
hil10=read(10)
hil11=read(11)
total = hil1.append([hil2,hil3,hil4,hil5,hil6,hil7,hil8,hil9,hil10,hil11])
total.index = np.arange(1, len(total)+1, 1)
k = np.array([0,255,509,764,1019,1274,1529,1784,2039,2294,2558])
total['ID'] = total[0]+k[total['bagian']-1]
total = total[['ID', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'bagian', 0]]
total = total.sort_values(['ID'])
np.savetxt('discard_total.txt', total, delimiter=' ', fmt="%s")'''
'''
data = pd.read_table('5myt3.txt', delim_whitespace=True, header=None)
pembanding = pd.read_csv('delta_data.csv')
data = data[~data[0].isin(pembanding['index_gabungan'])]
np.savetxt('5myt3cc.txt', data, delimiter=" ", fmt="%s")'''