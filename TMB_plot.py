#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:49:20 2020

@author: shihyu
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

Group1=pd.read_excel(r'Inputs/TMBcount_group1.xlsx')[['Sample name','TMB(mb)']]
Group2=pd.read_excel(r'Inputs/TMBcount_group2.xlsx')[['Sample name','TMB(mb)']]

#Overlap box plot
df={}
bp={}
#df[0]=Group1[['SNV']].rename({'SNV':'Group1'})
df[0]=Group1[['TMB(mb)']].rename({'TMB(mb)':'Group1'})
df[1]=Group2[['TMB(mb)']].rename({'TMB(mb)':'Group2'})
colour=['firebrick','cornflowerblue']
fig, ax = plt.subplots()
for i in [0,1]:
    bp[i]=df[i].plot.box(ax=ax,
                         color={'whiskers':colour[i],
                                'caps':colour[i],
                                'medians':colour[i],
                                'boxes':colour[i]})
    
red_patch=mpatches.Patch(color='firebrick',label='Group1')
blue_patch=mpatches.Patch(color='cornflowerblue',label='Group2')
plt.legend(handles=[red_patch,blue_patch])
plt.show()


#Scatter box plot
df=pd.concat([Group1,Group2],keys=['Group1','Group2'])
TMB=df['TMB(mb)'].tolist()
typ=['Group1' for i in range(14)]+(['Group2' for i in range(14)])
dat={'TMB(mb)':TMB,'Type':typ}
df=pd.DataFrame(dat)
sns.set(style='whitegrid')
ax=sns.boxplot(x='Type',y='TMB(mb)',data=df.iloc[:28,:],width=0.2,palette='Set3')
ax=sns.swarmplot(x='Type',y='TMB(mb)',data=df.iloc[:28,:],color='darkolivegreen')


#Overlap scatter box plot
df={}
bp={}
df[0]=Group1[['TMB(mb)']].rename({'TMB(mb)':'Group1'})
df[0]['Type']="Group1"
df[1]=Group2[['TMB(mb)']].rename({'TMB(mb)':'Group2'})
df[1]['Type']="Group2"
colour=['firebrick','cornflowerblue']
fig, ax = plt.subplots()
for i in [0,1]:
    sns.set(style='whitegrid')
    bp[i]=sns.swarmplot(x='Type',y='TMB(mb)',data=df[i],color=colour[i])
df2=pd.concat([df[0],df[1]])
bp[2]=sns.boxplot(y='TMB(mb)',data=df2,width=0.2,palette='Set3')

red_patch=mpatches.Patch(color='firebrick',label='Group1')
blue_patch=mpatches.Patch(color='cornflowerblue',label='Group2')
plt.legend(handles=[red_patch,blue_patch])
plt.ylabel('TMB(mb)')
plt.xlabel('Combine Group1 and Group2 data')
