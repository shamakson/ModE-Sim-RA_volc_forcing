#import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import datetime
import random

%matplotlib inline

#specify the file location and name

data= 'eruption_list_Palaeo-ra.txt'

headers = ['year','month','day','VSSI','sigma','NHflux','SHflux', 'lat']

########################################################################################################################
########################################################################################################################

df = pd.read_csv(data, delimiter='\t', skiprows=range(0,1), names=headers, usecols=[0,1,2,3,4,5,6,7])

VSSI = df['VSSI']

sigma = df['sigma']

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



del df['VSSI']

df['VSSI']= new_vssi

df=df[['year','month','day', 'VSSI','sigma','NHflux', 'SHflux', 'lat']]

df.to_csv('out/paleao-ra_Jan_1.csv', sep='\t', na_rep='0')



