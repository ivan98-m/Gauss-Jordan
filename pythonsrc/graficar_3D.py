import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def graficar_3d(n):
    matriz=np.array(n, dtype='float').reshape(3,4)
    b=matriz[:,3]
    A=np.delete(matriz, 3, axis=1)
    print(A)
    print(b)
    solu=np.linalg.solve(A,b)
    print (solu)
    print(np.allclose(np.dot(A,solu), b))

    xa = (int(abs(solu[0])) + 10)
    ya = (int(abs(solu[1])) + 10)
    x,y=np.linspace(-xa,xa, ya),np.linspace(-ya, xa, ya)
    X,Y=np.meshgrid(x,y)

    #Z1=(22-2*X-4*Y)/6
    Z1=(float(n[3])-float(n[0])*X-float(n[1])*Y)/float(n[2])
    #Z2=(27-3*X-8*Y)/5
    Z2=(float(n[7])-float(n[4])*X-float(n[5])*Y)/float(n[6])
    #Z3=(2+X-Y)/2
    Z3=(float(n[11])-float(n[8])*X-float(n[9])*Y)/float(n[10])

    fig=plt.figure()
    plt.clf()
    aux=fig.add_subplot(111,projection='3d')
    #Planos
    aux.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.Accent,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)


    aux.plot((solu[0],),(solu[1],),(solu[2]), lw=2,c='k',marker='X',markersize=7,markerfacecolor='black')
    aux.set_xlabel('X');aux.set_ylabel('Y');aux.set_zlabel('Z')

    #Interseccion
    x = round(solu[0], 3)
    y = round(solu[1], 3)
    z = round(solu[2], 3)
    ternaSolucion = ("(" + str(x) + ", " + str(y) + ", " + str(z) + ")")
    #aux.text(solu[0]+1, solu[1]+1, solu[2]+1, ternaSolucion, color='#000')

    aux.text(solu[0] + 2, solu[1] + 2, solu[2] + 2, ternaSolucion, size=10, rotation=0,
         ha="left", va="center", color="white",
         bbox=dict(boxstyle="round",
                   ec=(0, 0, 0),
                   fc=(0, 0, 0),
                   )
         )

    Ecuacion1 = (str(n[0])+ "x" + " + "+ "("+str(n[1])+")" + "y" + " + " + "("+ str(n[2])+")" + "z" + " = " + str(n[3]))
    Ecuacion2 = (str(n[4])+ "x" + " + "+ "("+str(n[5])+")" + "y" + " + " + "("+ str(n[6])+")" + "z" + " = " + str(n[7]))
    Ecuacion3 = (str(n[8])+ "x" + " + "+ "("+str(n[9])+")" + "y" + " + " + "("+ str(n[10])+")" + "z" + " = " + str(n[11]))

    aux.text2D(-0.30, 1.05, Ecuacion1, color="#7fc97f", fontweight="heavy", transform=aux.transAxes)
    aux.text2D(-0.30, 1.0, Ecuacion2, color="#8FB9CF", fontweight="heavy", transform=aux.transAxes)
    aux.text2D(-0.30, 0.95, Ecuacion3, color="#E89992", fontweight="heavy", transform=aux.transAxes)
    
    plt.show()
    plt.close()