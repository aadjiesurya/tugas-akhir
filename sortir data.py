from scipy.integrate import quad
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
import pylab as pl
"""Besaran Orbit Hilda"""
a_jup = 5.2044
n_j = 8.308215045623607E-02 
n = n_j*7.0/4.0
p_hil = (360/n)*365.2524
arest = (n_j**2*a_jup**3/n**2)**(0.3333)
alpha = arest/a_jup       #Alpha = ahilda/ajup
"""==========================Fungsi gangguan b=============================="""
def b1(x):                          #Fungsi b s=1/2 j=2
    return np.cos(x)/((1-2*alpha*np.cos(x)+alpha**2)**0.5*np.pi)
def b2(x):                          #Fungsi b s=3/2 j=1
    return np.cos(0)/((1-2*alpha*np.cos(x)+alpha**2)**1.5*np.pi)
def b3(x):                          #Fungsi b s=3/2 j=2
    return np.cos(x)/((1-2*alpha*np.cos(x)+alpha**2)**1.5*np.pi)
def b4(x):                          #Fungsi b s=3/2 j=3
    return np.cos(2*x)/((1-2*alpha*np.cos(x)+alpha**2)**1.5*np.pi)    
res1, err1 = quad(b1, 0, 2*np.pi)
res2, err2 = quad(b2, 0, 2*np.pi)
res3, err3 = quad(b3, 0, 2*np.pi)
res4, err4 = quad(b4, 0, 2*np.pi)

Db = 0.5*(res2-2*alpha*res3+res4)
f = 1.0/48.0*(147*res1+alpha*Db)
Cr =(1.0/1047.0)*n*f
print Cr, arest, n
"""===============================Pembacaan file============================"""
file=open('results (1).csv','r')
data=file.readlines()
"""====================Fungsi lebar setengah sumbu panjang=================="""
mjd = []
abaru = []
ebaru = []
ibaru = []
ombaru = []
wbaru = []
mabaru = []
nbaru = []
dabaru = []
debaru = []
dibaru = []
dombaru = []
dwbaru = []
dmabaru = []
dnbaru = []
abaru1 = []
ebaru1 = []
atambahan = []
etambahan = []
akurang = []
ekurang = []
nama = []
for line in range(len(data)):
    if data[line][0] != "#":
        """Kurva Gangguan Resonan 3:2"""
        e = float(data[line].split(',')[1])
        a = float(data[line].split(',')[2])
        p = 2.0
        z = -2.0*Cr/(9*p*n*e)
        x = (16.0*Cr*e/(3*n))**0.5
        c = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
        akanan = (z+x*c)*arest+arest
        akiri = (z-x*c)*arest+arest
        """Kurva Aphelion"""
        Q = 5.4588
        eap = (Q/a)-1
        """Kurva Tisserand"""
        aj = 5.2044
        Tj = 3
        etis = (1-aj*(Tj-(aj/a))**2/(4*a))**0.5
        #if a<=akanan and a>=akiri:
           # mjd.append(float(data[line].split(',')[0]))
          #  abaru.append(a)
           # ebaru.append(e)
        e1 = float(data[line].split(',')[1])
        a1 = float(data[line].split(',')[2])
        p1 = 2.0
        z1 = -2.0*Cr/(p*n*e)
        x1 = (16.0*Cr*e/(3*n))**0.5
        c1 = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
        akanan1 = (z1+x1*c1)*arest+arest
        akiri1 = (z1-x1*c1)*arest+arest
        #if a<=akanan1 and a>=akiri1:
           # abaru1.append(a1)
           # ebaru1.append(e1)
        if a>=akanan1 and a<=akanan:
            atambahan.append(a)
            etambahan.append(e)
            mjd.append(float(data[line].split(',')[0]))
            ibaru.append(data[line].split(',')[3])
            ombaru.append(data[line].split(',')[4])
            wbaru.append(data[line].split(',')[5])
            mabaru.append(data[line].split(',')[6])
            nbaru.append(data[line].split(',')[7])
            dabaru.append(data[line].split(',')[8])
            debaru.append(data[line].split(',')[9])
            dibaru.append(data[line].split(',')[10])
            dombaru.append(data[line].split(',')[11])
            dwbaru.append(data[line].split(',')[12])
            dmabaru.append(data[line].split(',')[13])
            dnbaru.append(data[line].split(',')[14])
            nama.append(data[line].split(',')[16])
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
def ar1(e):
    p = 2.0
    z = -2.0*Cr/(p*n*e)
    x = (16.0*Cr*e/(3*n))**0.5
    c = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
    return (z+x*c)*arest+arest
def al1(e):
    p = 2.0
    z = -2.0*Cr/(p*n*e)
    x = (16.0*Cr*e/(3*n))**0.5
    c = (1.0+(Cr/(27.0*p**2*e**3*n)))**0.5
    return (z-x*c)*arest+arest
def tise(a):
    aj = 5.2044
    Tj = 3
    return (1-aj*(Tj-(aj/a))**2/(4*a))**0.5
def aphe(a):
    Q = 5.4588
    return (Q/a)-1
import csv
rows = zip(mjd, atambahan, etambahan, ibaru, ombaru, wbaru, mabaru, nbaru, dabaru, debaru, dibaru, dombaru, dwbaru, dmabaru, dnbaru, nama)
with open('index_tambahan.csv','w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
x = np.array(abaru)
y = np.array(ebaru)
z = np.array(ibaru)
x1 = np.array(atambahan)
y1 = np.array(etambahan)
aright = np.array(ar(np.linspace(0.001,1.0,100.0)))
aleft = np.array(al(np.linspace(0.001,1.0,100.0)))
aright1 = np.array(ar1(np.linspace(0.001,1.0,100.0)))
aleft1 = np.array(al1(np.linspace(0.001,1.0,100.0)))
etise = np.array(tise(np.linspace(3.4,4.4)))
eap = np.array(aphe(np.linspace(3.4,4.4)))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,y)
ax.scatter(x1,y1, c='r')
ax.plot(aright,np.linspace(0.001,1.0,100.0), c='b')
ax.plot(aleft,np.linspace(0.001,1.0,100.0), c='b')
ax.plot(aright1,np.linspace(0.001,1.0,100.0), c='r')
ax.plot(aleft1,np.linspace(0.001,1.0,100.0), c='r')
ax.plot(np.linspace(3.4,4.4),etise, c='g')
ax.plot(np.linspace(3.4,4.4),eap, c='b')
plt.xlim(3.4, 4.4)
plt.ylim(0.0,1)
ax.scatter(x,y)
ax.plot(aright,np.linspace(0.001,1.0,100.0))
ax.plot(aleft,np.linspace(0.001,1.0,100.0))
plt.xlim(3.4,4.4)
plt.ylim(0,60)
plt.rcParams.update({'font.size':12})
ax.set_xlabel('a (au)')
ax.set_ylabel('i (deg)')
plt.savefig('kurva_hilda.jpg')
plt.show()

