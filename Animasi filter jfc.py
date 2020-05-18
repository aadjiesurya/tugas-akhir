# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:36:58 2019

@author: aadjie
"""

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
#from matplotlib import rc
#rc('text', usetex = True)
data = pd.read_table('0-10t4c.txt', delim_whitespace=True, header=None)
calib = pd.read_table('banding1.txt', delim_whitespace=True, header=None)
data = data[data[0]>0]
def tsd(row):
    x = aj/row[2]
    y = 2*np.cos(row[4])
    z = np.sqrt((row[2]/aj)*(1-row[3]**2))
    return x+y*z
aj = 5.2044    
data['tiserand']=data.apply(tsd, axis=1)
data =data[data[0].isin(calib[0])]
#data = data[data[0].isin(calib[0])]
Cr, arest, n = 0.000281485582708, 3.91729907983, 0.124623225684
'''t = 1
df = pd.DataFrame()
baru = []
while t <313:
    databaru = data[data[9]==t*4+1]
    jfc = databaru[(databaru['tiserand']<3) & (databaru['tiserand']>2)]
    tis = databaru[(databaru['tiserand']>=3) | (databaru['tiserand']<=2)]
    x1=len(jfc[0])
    x2=len(tis[0])
    baru.append(x2)
    t+=1
df = df.append(baru)
print df.mean()
print df.median()
print df.mode()
print df.min()
print df.max()'''
fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
#fig, ax1 = plt.subplots()
#========================Pendefinisian Fungsi di kurva========================#
def ar(e):
    p = 2.0
    z = -2.0*Cr/(9*p*n*e)
    x = (16.0*Cr*e/(3*n))**0.5
    c = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
    return (z+x*c)*arest+arest
def al(e):
    p = 2.0
    z = -2.0*Cr/(9*p*n*e)
    x = (16.0*Cr*e/(3*n))**0.5
    c = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
    return (z-x*c)*arest+arest
def tise(a):
    Tj = 3
    return (1-aj*(Tj-(aj/a))**2/(4*a))**0.5
def aphe(a):
    Q = 5.4588
    return (Q/a)-1
#========================Pendefinisian Animasi========================#
def update_time():
    t = -1
    t_max = 312
    while t<t_max:
        t += anim.direction
        yield t
def update_plot(t):
    databaru = data[data[9]==t*4+1]
    jfc = databaru[(databaru['tiserand']<3) & (databaru['tiserand']>2)]
    tis = databaru[(databaru['tiserand']>=3) | (databaru['tiserand']<=2)]
    x1=jfc[2]
    y1=jfc[3]
    z1=jfc[4]*180/np.pi
    x2=tis[2]
    y2=tis[3]
    z2=tis[4]*180/np.pi
    ax1.clear()
    ax2.clear()
    aright = np.array(ar(np.linspace(0.001,1.0,100.0)))
    aleft = np.array(al(np.linspace(0.001,1.0,100.0)))
    etise = np.array(tise(np.linspace(2.5,aj)))
    eap = np.array(aphe(np.linspace(2.5,aj)))
    ax2.plot([5.2044,5.2044],(np.linspace(0,1,2)), c='orange', ls='--')
    ax2.plot(np.linspace(2.5,aj),etise, c='black',ls='--')
    ax2.plot(np.linspace(2.5,aj),eap, c='orange')
    ax2.plot(aright,np.linspace(0.001,1.0,100.0), c='purple')
    ax2.plot(aleft,np.linspace(0.001,1.0,100.0), c='purple')
    ax2.set_xlim([2.5,5.5])
    ax2.set_ylim([0,1])
    ax1.set_ylim([0,180])
    ax2.set_xlabel('$a$ (au)')
    ax2.set_ylabel('$e$')
    ax1.set_ylabel('$i$ (derajat)')
    ax1.set_yticks(np.arange(0,151,30))
    plt.rcParams.update({'font.size':16})
    scat = ax2.scatter(x1,y1,c='blue',edgecolor="")
    scat1 = ax2.scatter(x2,y2,c='red',edgecolor="")    
    scat2 = ax1.scatter(x1,z1,c='blue',edgecolor="")
    scat3 = ax1.scatter(x2,z2,c='red',edgecolor="")
    print t*4+1, len(x1), len(x2), len(x1)+len(x2)
    return scat,
def on_press(event):
    if event.key.isspace():
        if anim.running:
            anim.event_source.stop()
        else:
            anim.event_source.start()
        anim.running ^= True
    elif event.key == 'left': 
        anim.direction = -1
    elif event.key == 'right':
        anim.direction = +1

    # Manually update the plot
    if event.key in ['left','right']:
        t = anim.frame_seq.next()
        update_plot(t)
        plt.draw()

fig.canvas.mpl_connect('key_press_event', on_press)
anim = ani.FuncAnimation(fig, update_plot, frames=313,
                         interval=250)
anim.running = True
anim.direction = +1
anim.save('nonjfc.mp4',bitrate=100)
plt.show()