import scipy.optimize as opt
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def dijkstras(M, n):    #return a list with list[i]=length of shortest path from n to i
    N=len(M)
    list=[]
    dis=np.zeros(N)
    for i in range(N):
        dis[i]=3000
    dis[n]=0
    temp=0
    for x in range(N-1):
        min=3000
        for j in range(N):
            if(dis[j]<min and j not in list):
                min=dis[j] 
                temp=j
        list.append(temp)
        for j in range(N):
            if(M[temp][j]!=0 and j not in list):
                if(dis[j]>dis[temp]+M[temp][j]):
                    dis[j]=dis[temp]+M[temp][j]
    return dis

def distanceMatrix(A):  #A adjacency matrix (the higher the weigth of an edge the closer the two vertices)
    N=len(A)
    for i in range(N):
        for j in range(N):
            if(i==j):
                A[i][j]=0
            else:
                if(A[i][j]!=0):
                    A[i][j]=(1/A[i][j])**0.5    #inverse weight of the matrix
    D=np.zeros((N, N))
    for i in range(N):
        D[i]=dijkstras(A, i)
    return D

def minimizationFunction(x, D):    #x=x0...x(N-1)y0...y(N-1) squared sum of differences between distances on the graph to be displayed and on the distance matrix
    N=len(D)
    sum=0
    for i in range(N):
        for j in range(i, N):
            a=(x[i]-x[j])**2+(x[i+N]-x[j+N])**2
            sum+=a-2*D[i][j]*(a)**0.5
    return sum
    
def graphCoordinate(D):
    N=len(D)
    x0=np.zeros(2*N)    #initial value before minimizing 
    A=opt.fmin(minimizationFunction, x0, args=(D,), xtol=0.0001)
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(N):
        x[i]=A[i]
        y[i]=A[i+N]
    z=[x, y]
    return z

def display(A, dico):
    name=dico[0]    #dictionary where name[i]=label of the vertex i
    D=distanceMatrix(A)
    Z=graphCoordinate(D)
    plt.plot
    N = len(A)
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(N):
        x[i]=Z[0][i]
        y[i]=Z[1][i]
    colors = np.random.rand(N)
    area = 1  # 0 to 15 point radii
    plt.scatter(x, y, s=area, marker='.', alpha=0.5)
    for i in range(N):
        r=np.random.random()
        if(r<0.5):
            plt.annotate(name[i], xy=(x[i], y[i]), xytext=(0, 1), textcoords='offset points', 
             ha='center', va='bottom', fontsize=1)
        else:
            plt.annotate(name[i], xy=(x[i], y[i]), xytext=(0, -1), textcoords='offset points', 
             ha='center', va='top', fontsize=1)
    plt.savefig('graphtest.eps', format='eps', dpi=1000)

    
A=np.load('matrixtest.npy')
dico=np.load('dicotest.npy')    
    
display(A, dico)




