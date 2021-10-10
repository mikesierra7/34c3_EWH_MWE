#!/usr/local/bin/python3

'''
Calculating the Equivalent Water Height (EWH) due to gravity change between 
two GRACE monthly solutions. This example calculates the EWH from gravity
change between May 2002 and May 2017 for Greenland using the ITSG-GRACE2016 
gravity field. Spatial averaging using a Gaussian filter is used for 
destriping. See also: 
Wahr, J. (2015): Time Variable Gravity Fields from Satellites. In: Herring, 
T.A. (Ed.): Treatise on Geophysics, Vol 3, pp 193-213.

This example does NOT include corrections for additional gravity effects,
e.g., GIA or leakage. 

The intend of this demo is solely to give an example of the evaluation of 
gravity field solutions provided in spherical harmonic coefficients.

For other locations change the variables lat and lon, where the latitude is
the polar distance, or colatitude, ranging from 0° to 180°. For other Epochs 
change file1 and file 2. 

ITSG-GRACE2016 Reference: 
Mayer-Gürr, Torsten; Behzadpour, Saniya; Ellmer, Matthias; Kvas, Andreas; 
Klinger, Beate; Zehentner, Norbert (2016): ITSG-Grace2016 - Monthly and Daily 
Gravity Field Solutions from GRACE. GFZ Data Services. 
http://doi.org/10.5880/icgem.2016.007

Plotting of the results requires the cartopy package. See documentation at
https://scitools.org.uk/cartopy/docs/latest/index.html
Cartopy will download the necessary coastlines
'''

import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pyfunc.plot_grav_field_libs as pgfl
from cartopy import crs as ccrs
from cartopy.mpl.gridliner import LatitudeFormatter , LongitudeFormatter

def ewh_calc():
    p = mp.Pool(mp.cpu_count())
    res=[p.apply_async(pgfl.waterheight, args = (rlam, ele , dc, ds, deg_max,lf,kn)) 
                       for ele in rlat 
                       ]
    p.close()
    p.join()
    ewh=np.zeros((len(rlat),len(rlam)+1))
    for hi in range(0,len(rlat)):
        ewh[hi,:] = res[hi].get()
    ewh= ewh[ewh[:,0].argsort()]
    ewh=np.delete(ewh, np.s_[0], axis=1)
    return ewh

# define common parameters
deg_max = 90
deg_list = np.arange(2, deg_max+1, 1) # from degree 2 to deg_max
R=6378.136 # Earth radius in km 
filterradius = 300.0 # filter radius in km; 0.0 for no filter

# region and step size of grid to calculate EWH
lam = np.arange(-180.0, 180.0, 1.0)
lat = np.arange(1.0, 180.0, 1.0)
rlam=lam*np.pi/180
rlat = lat*np.pi/180

# Gravity field
# Files can be downloaded from http://ifg.tugraz.at/ITSG-Grace2016
# this example uses unconstrained monthly solutions of degree 120
file1='data/ITSG-Grace2016_n120_2002-05.gfc'
file2='data/ITSG-Grace2016_n120_2017-05.gfc'

# read gravity field coefficients (degree, order, cnm, snm)
coeffi1 = np.loadtxt(file1, usecols=(1,2,3,4), skiprows= 19)
coeffi2 = np.loadtxt(file2, usecols=(1,2,3,4), skiprows= 19)
# filter coefficients
if filterradius > 0.0:
    fc=pgfl.GaussFilterCoeff(R, filterradius, deg_max)
    filter_coeff=np.outer(fc,np.ones((deg_max+1,1)))
else:
    filter_coeff=np.ones((deg_max+1,1))
        
# sort coefficients into triangular matrix
cnm1, snm1 = pgfl.coeffisort(coeffi1, deg_max)
cnm2, snm2 = pgfl.coeffisort(coeffi2, deg_max)
# coefficient difference
dc=(cnm2-cnm1)*filter_coeff
ds=(snm2-snm1)*filter_coeff
# Love numbers
kn = pgfl.LoveNumbers(deg_max)
# Legendre functions
lf = pgfl.LegendreFunctions(deg_max)

if __name__ == '__main__':
    # calculations
    w=ewh_calc()
    # Plot of result
    fig=plt.figure(figsize=[15,8])
    ax = plt.subplot(projection=ccrs.PlateCarree())
    imgextend = [-180, 180, -90, 90]
    t=ax.imshow(w,origin='upper',extent=imgextend, transform=ccrs.PlateCarree(),
                cmap='RdBu') 
    ax.coastlines('110m') # 50m is also available
    lonLabels = np.arange(-180, 181, 60)
    latLabels = np.arange(-90, 91, 30)
    gl=ax.gridlines(draw_labels=True,color='k',linewidth=1.5)
    gl.xlocator = mticker.FixedLocator(lonLabels)
    gl.ylocator = mticker.FixedLocator(latLabels)
    gl.xformatter = LongitudeFormatter()
    gl.yformatter = LatitudeFormatter()
    
    cbar=plt.colorbar(t)
    cbar.set_label('EWH / m', rotation=90)
    plt.show()
    

