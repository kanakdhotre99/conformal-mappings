#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cmath
import ipywidgets as wg
from IPython.display import display


# In[20]:


def confmap(function,n):
    def f(z):
        return(eval(function))
    def plotc(Z,col):
        x_vals = [z.real for z in Z]
        y_vals = [z.imag for z in Z]
        plt.plot(x_vals,y_vals,color=col)
    def ngrid_z(n):
        for j in np.ndarray.tolist(np.linspace(-n,n,n)):
            plotc([complex(i,j) for i in np.ndarray.tolist(np.linspace(-n,n,n))],'red')
            plotc([complex(j,i) for i in np.ndarray.tolist(np.linspace(-n,n,n))],'blue')
    def ngrid_w(n):
        for j in np.ndarray.tolist(np.linspace(-n,n,n)):
            plotc([f(complex(i,j)) for i in np.ndarray.tolist(np.linspace(-n,n,n))],'red')
            plotc([f(complex(j,i)) for i in np.ndarray.tolist(np.linspace(-n,n,n))],'blue')
    plt.subplot(1,2,1)
    ngrid_z(n)
    plt.axis('equal') 
    plt.subplot(1,2,2)
    ngrid_w(n)
    plt.axis('equal')


# In[23]:


function = wg.Text(value='Function')
n = wg.IntSlider(description='Mesh Size')
button = wg.Button(description="Plot")
display(function,n,button)
def on_button_clicked(b):
    confmap(function.value,n.value)
button.on_click(on_button_clicked)

