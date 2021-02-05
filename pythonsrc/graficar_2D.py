from pylab import *
import matplotlib.pyplot as plt
import numpy as np

def graficar_2d(n):
    print("SI ESTAMOS EN LA GRAFICA")
    plt.clf()

    x = range(-10, 10)
    plt.xlabel("X", fontsize=20)
    plt.ylabel("Y", fontsize=20)
    x1=(str(n[0])+ "x" + " + "+ "("+str(n[1])+")" +"y"  +" = "+str(n[2]))
    x2=(str(n[3])+ "x" +" + "+ "("+str(n[4])+")"+  "y"  + " = "+str(n[5]))
    plt.xlabel("X", fontsize=20)
    plt.ylabel("Y", fontsize=20)

    plt.plot(x, [ecua1(i,n) for i in x], label=x1)
    plt.plot(x, [ecua2(i,n) for i in x], label=x2)

    plt.legend(loc="upper left")
    #plt.axis(ymin=0)

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-11, 11)
    plt.ylim(-11, 11)

    show()

def ecua1(x, n):
    x1=float(n[0])
    y1=float(n[1])
    xr=float(n[2])
    return (-((x1)*x)+(xr))/(y1)

def ecua2(x, n):
    x2=float(n[3])
    y2=float(n[4])
    yr=float(n[5])
    return (-((x2)*x)+(yr))/(y2)