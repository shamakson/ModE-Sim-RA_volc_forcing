#import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import datetime
import random

#specify the file location and name

data= 'eruption_list_Palaeo-ra.txt'

headers = ['#year','month','day','VSSI','sigma','NHflux','SHflux', 'lat','']

########################################################################################################################
########################################################################################################################

df = pd.read_csv(data, delimiter='\t', skiprows=range(0,1), index_col=0, names=headers, usecols=[0,1,2,3,4,5,6,7,8])

VSSI = df['VSSI']

sigma = df['sigma']

month = df['month']

upper = VSSI + sigma

lower = VSSI - sigma

df['upper']= upper

df['lower']= lower

#function that select randomly from float
#Not predefined, random.randint(start,end) only works for integer

def rand_float_range(start, end):
    return random.random() * (end - start) + start

#############################################################
#Select randomly between upper and lower bounds
#Append to a new list and replace VSSI
#write out all in text tab delimited format
#############################################################
new_vssi=[]
for u, l in zip(upper, lower):
    var= rand_float_range(u,l)
    new_vssi.append(var)

new_month=[]
for i in month:
    var2=random.randint(1,12)
    new_month.append(var2)


#############################################################
del df['VSSI']
df['VSSI']= new_vssi
#############################################################
del df['month']
df['month']= new_month
#############################################################
df=df[['month','day', 'VSSI','sigma','NHflux', 'SHflux', 'lat','']]
df.to_csv('output.csv', sep='\t', na_rep='0')
###########################################

