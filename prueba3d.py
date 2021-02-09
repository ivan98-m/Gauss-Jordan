import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def tresd():
    A=np.array([[2,4,6],[3,8,5],[-1,1,2]])
    b=np.array([22,27,2])
    sol=np.linalg.solve(A,b)
    print (sol)

    x,y=np.linspace(0,10,10),np.linspace(0,10,10)
    X,Y=np.meshgrid(x,y)

    Z1=(22-2*X-4*Y)/6
    Z2=(27-3*X-8*Y)/5
    Z3=(2+X-Y)/2

    fig=plt.figure()
    aux=fig.add_subplot(111,projection='3d')
    aux.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.Accent,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)

    aux.plot((sol[0],),(sol[1],),(sol[2]), lw=2,c='k',marker='X',markersize=7,markerfacecolor='white')
    aux.set_xlabel('X');aux.set_ylabel('Y');aux.set_zlabel('Z')

    plt.show()

def lista3():
    lista=[2,4,6,22,3,8,5,27,-1,1,2,2]
    graficar_3D(lista)

def graficar_3D(n):
    matriz=np.array(n).reshape(3,4)
    b=matriz[:,3]
    A=np.delete(matriz, 3, axis=1)
    print(A)
    print(b)
    solu=np.linalg.solve(A,b)
    print (solu)
    print(np.allclose(np.dot(A,solu), b))

    x,y=np.linspace(0,10,10),np.linspace(0,10,10)
    X,Y=np.meshgrid(x,y)

    #Z1=(22-2*X-4*Y)/6
    Z1=(n[3]-n[0]*X-n[1]*Y)/n[2]
    #Z2=(27-3*X-8*Y)/5
    Z2=(n[7]-n[4]*X-n[5]*Y)/n[6]
    #Z3=(2+X-Y)/2
    Z3=(n[11]-n[8]*X-n[9]*Y)/n[10]

    fig=plt.figure()
    aux=fig.add_subplot(111,projection='3d')
    aux.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.Accent,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
    aux.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)

    aux.plot((solu[0],),(solu[1],),(solu[2]), lw=2,c='k',marker='X',markersize=7,markerfacecolor='black')
    aux.set_xlabel('X');aux.set_ylabel('Y');aux.set_zlabel('Z')

    plt.show()


lista3()