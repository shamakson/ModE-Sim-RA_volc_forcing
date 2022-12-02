#=====================================
#
# Script to create the nc file for EVA input. 
#----------------------------------------
# The initial list of volcanic eruptions should be in txt file (or in other table style file.) containing the information on: years of eruptions, months, days, vssis (Tg S), sigmas (Tg S), NHflux, SHflux and latitudes.
# If the information on NH/SH flux is not available, set those values as -9999.
#
#======================================

from netCDF4 import Dataset
import numpy as np

#--------------------
# Read initial txt file
#--------------------

direct='data/out/'
txtf=direct+'paleao-ra_1.txt'
savedir='output/'

FILE=np.loadtxt(txtf,skiprows=1)

#dim=(350, 9)

#--------------------
# Transforming to netcdf.
#--------------------

n=FILE.shape[0]

years_o=FILE[:,0]
months=FILE[:,1]
days=FILE[:,2]
lats=FILE[:,-1]
ssis=FILE[:,3]
sigmas=FILE[:,4]


NHflux=FILE[:,5]
SHflux=FILE[:,6]

hemis=np.zeros((n))

for i in range(0,n):
    if (NHflux[i]==0 or SHflux[i]==0):
        hemis[i]=-1.
    elif (NHflux[i]==-9999. and SHflux[i]==-9999.):
        hemis[i]=-1.
    else:
        hemis[i]=NHflux[i]/SHflux[i]


### ------------ 1) If the list contains an eruption in a negative year. 

years=FILE[:,0]

yearCEs=np.zeros((n))

for i in range(0,n):
    if years[i]<0.:
        yearCEs[i]=years[i]-1.
    else:
        yearCEs[i]=years[i]


#--------------------
# Save it as netcdf
#--------------------

savename=savedir+'paleao-ra_1.nc'

dataset =Dataset(savename,'w',format='NETCDF4_CLASSIC') 


nerups=dataset.createDimension('nerup',None)

nerup=dataset.createVariable('nerup',np.float64,('nerup',))

year=dataset.createVariable('year',np.double,('nerup',))
yearCE=dataset.createVariable('yearCE',np.double,('nerup',))
month=dataset.createVariable('month',np.double,('nerup',))
day=dataset.createVariable('day',np.double,('nerup',))
lat=dataset.createVariable('lat',np.double,('nerup',))
ssi=dataset.createVariable('ssi',np.double,('nerup',))
hemi=dataset.createVariable('hemi',np.double,('nerup',))
sigma_ssi=dataset.createVariable('sigma_ssi',np.double,('nerup',),fill_value=-9999.)


year.units='year (ISO)'
year.long_name='year of eruption (ISO 8601, including year 0)'
yearCE.units='year (BCE/CE)'
yearCE.long_name='year of eruption (BCE/CE, no year 0)'
month.units='month'
month.long_name='month of eruption'
day.units='day'
day.long_name='day of eruption'
lat.units='degrees_north'
ssi.units='Tg [S]'
ssi.long_name='"volcanic stratospheric sulfur injection of eruption'
hemi.units=' '
hemi.long_name='hemispheric asymmetry (NH/SH) of aerosol spread for tropical eruptions based on ratio of Greenland to Antarctic flux'
sigma_ssi.units='Tg [S]'
sigma_ssi.long_name='Random uncertainty (1 sigma) in SSI'

import time 
dataset.description = 'Ice core-inferred volcanic stratospheric sulfur injection for the perod of -1500 BCE-1900 CE from Toohey and Sigl(2017)'  
dataset.history = 'File created by E. Samakinwa' + time.ctime(time.time())  
dataset.user = 'Palaeo-ra'
dataset.source= 'Toohey and Sigl(2017)' 

year[:]=years
yearCE[:]=yearCEs
month[:]=months
day[:]=days
lat[:]=lats
ssi[:]=ssis
hemi[:]=hemis
sigma_ssi[:]=sigmas

nerup[:]=np.arange(1,(n+1))

dataset.close()



