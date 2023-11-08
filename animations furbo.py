# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 23:36:11 2023

@author: rcorr
"""
import pandas as pd
from matplotlib import pyplot as plt
import os
import footyviz
import imageio





d=pd.read_csv('Real_vs_Barcelona_Calma.csv')

df = d.loc[d['bgcolor'] == 'white']

df = df.set_index('frame') 
df1=d.loc[d['bgcolor'] == 'maroon']
df1 = df1.set_index('frame') 
d=d.set_index('frame')

 

for i in range(len(d)-1):
    fig, ax, dfFrame = footyviz.draw_frame(d, t=i)
    fig, ax, dfFrame = footyviz.add_voronoi_to_fig(fig, ax, dfFrame)
    plt.savefig('./figsv/framev_'+str(i)+'.png', transparent=False)
    plt.close()


limagenes = []

for i in os.listdir("./figsv" ):
    lm = os.path.join("./figsv" , i)
    limagenes.append(lm)

limagenes_ordenado = sorted(limagenes,
                                      key=lambda x: int(x.split("_")[1].split(".")[0]))

imagenes = []

for nombre in limagenes_ordenado:
    x=imageio.imread(nombre) 
    imagenes.append(x)

ngif = 'GolMadrid.gif'
imageio.mimsave(ngif, imagenes, duration=1.5)

"""
plt.figure()
fig, ax, dfFrame = footyviz.draw_frame(df, t=6.5)
fig, ax, dfFrame = footyviz.draw_frame(df1, t=6.5)
fig, ax, dfFrame = footyviz.draw_frame(d, t=6.5)


fig, ax, dfFrame = footyviz.draw_frame(d, t=4)
fig, ax, dfFrame = footyviz.add_voronoi_to_fig(fig, ax, dfFrame)
"""

