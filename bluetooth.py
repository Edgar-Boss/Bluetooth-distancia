from bluepy.btle import Scanner, DefaultDelegate
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
            
        elif isNewData:
            print "Received new data from", dev.addr

k=0
puntos =np.zeros(10)
t=np.arange(0,10)
for j in range(10):
    print"//////////////////////////////////////////"
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(1.0)
    for dev in devices:
        if dev.addr == '4b:25:ed:74:c2:c5':#"f8:80:c9:d1:4a:b2":
            puntos[k]=dev.rssi
    k += 1

k=0
for p in puntos:
    if p==0:
        #print k
        puntos[k]=puntos[k-1]
    k+=1
    

print puntos

plt.plot(t,puntos,"--b")
plt.show()