
# coding: utf-8

# In[22]:


#Pide al usuario valore para resolver las ecuaciones par un péndulo
#In: l
#Out: Plot
import numpy as np
import matplotlib.pyplot as plt


# In[23]:


#Se define la función
def F(x,y):
    f=-k*np.sin(x)+y
    return f


# In[24]:


#Se define la función Runge-Kutta
#name es el título de la gráfica
def RK(name):

    for i in range(1,tl):
    
#------calculos------------------
        xn=x[i-1]
        vn=F(xn,0)
    
        k1=dt*F(xn,vn)
        k2=dt*F(xn+dt/2,vn+k1/2)
        k3=dt*F(xn+dt/2,vn+k2/2)
        k4=dt*F(xn+dt,vn+k3)
    
#-------nuevos valores-----------
        v[i]=v[i-1]+(k1+2*k2+2*k3+k4)/6
        x[i]=x[i-1]+dt*v[i-1]
        
    plt.plot(t, x, label='Posición')
    plt.plot(t, v, label='Velocidad')
    plt.title(name)
    plt.grid()
    plt.legend()
    plt.xlabel('Tiempo')
    plt.show()


# In[25]:


name='Pendulo'
l = int(input('Enter lenght: '))
n= int(input('Enter intervals: '))
#constantes
g=9.81#gravedad
#l=1  #longitud del pendulo
k=g/l


#tiempo
t0=0
tf=4*np.pi
#n=30000  #Número de intervalos
dt=(tf-t0)/n  #intervalos de tiempo
t=np.arange(t0,tf+dt,dt) #tiempo
tl=t.size  #time lenght
x=np.zeros(tl)  #ángulo
v=np.zeros(tl)  #velocidad


#condiciones iniciales
x0=1  #posición inicial
v0=0  #velocidad inicial

x[0]=x0
v[0]=v0


# In[26]:


#Calcula utilizando RK
RK(name)

