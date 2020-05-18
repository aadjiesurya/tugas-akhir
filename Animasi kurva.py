import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import numpy as np
#=========================Baca Data dan pendefinisian=========================#
data = pd.read_table('0-10t4c.txt', delim_whitespace=True, header=None)
data = data[data[0]>0]
#data = data[(data[0]==2492) | (data[0]==2422)]
data.index = np.arange(0,len(data),1)
Cr, arest, n = 0.000281485582708, 3.91729907983, 0.124623225684
fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
#fig, (ax1 = plt.subplots()
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
#================Pendefinisain fungsi kurva dan animasi=======================#
def update_time():
    t = 0
    t_max = data[9].max()
    while t<t_max:
        t += anim.direction
        yield t

def update_plot(t):
    databaru = data[data[9]==t*4+1]
    komet = databaru[(databaru[0]>2501) & (databaru[0]<2559) & (databaru[0] != 2506) | (databaru[0]==2785)]
    ast = databaru[~databaru[0].isin(komet[0])]
    x1=ast[2]
    y1=ast[3]
    z1=ast[4]*180/np.pi
    x2=komet[2]
    y2=komet[3]
    z2=komet[4]*180/np.pi
    ax1.clear()
    ax2.clear()
    scat = ax1.scatter(x1,y1,c='b')
    scat1 = ax1.scatter(x2,y2,c='r')    
#   scat2 = ax2.scatter(x1,z1,c='b')
#    scat3 = ax2.scatter(x2,z2,c='r')
#    aright = np.array(ar(np.linspace(0.001,1.0,100.0)))
#    aleft = np.array(al(np.linspace(0.001,1.0,100.0)))
    ax1.plot(aright,np.linspace(0.001,1.0,100.0), c='b')
    ax1.plot(aleft,np.linspace(0.001,1.0,100.0), c='b')
    ax1.set_xlim([2.5,8])
    ax1.set_ylim([0,1])
    ax2.set_ylim([0,150])
    print t*4+1
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
#=========================Bagian animasi======================================#
fig.canvas.mpl_connect('key_press_event', on_press)
anim = ani.FuncAnimation(fig, update_plot, frames=update_time,
                         interval=100, repeat=True)
anim.running = True
anim.direction = +1
anim.save(')
plt.show()