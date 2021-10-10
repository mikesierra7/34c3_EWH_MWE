#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function for calculation equivalent water height
    LegendreFunctions: calculate Legendre functions P_nm
    coeffisort: sort spherical harmonic coefficients from a list into a 
        triangular matrix
    waterheight: calculate equivalent water height
    GaussFilterCoeff: calculate filter coefficients for a Gaussian Filter
    LoveNumbers: interpolate Love numbers up to a given degree
"""

import numpy as np

class LegendreFunctions:
    def __init__(self, maxdegree):
        self.LF1 = np.zeros((maxdegree+1,maxdegree+1))
        self.LF1[1,1]= np.sqrt(3)
        self.LF2 = np.zeros((maxdegree+1,maxdegree+1))
        self.maxdegree = maxdegree
        for n in range(2,maxdegree+1):
            self.LF1[n,n] = np.sqrt((2*n+1)/(2*n))
        for m in range(0, maxdegree):
            for n in range(m+1, maxdegree+1):
                f=(2*n+1)/((n+m)*(n-m))
                self.LF1[n,m] = np.sqrt(f*(2*n-1))
                self.LF2[n,m] = np.sqrt(f*(n-m-1)*(n+m-1)/(2*n-3))
    def __call__(self, theta):
        cosTheta = np.cos(theta)
        sinTheta = np.sin(theta)
        Pnm = np.zeros((self.maxdegree+1,self.maxdegree+1))
        Pnm[0,0] = 1.0
        for n in range(1,self.maxdegree+1):
            Pnm[n,n] = self.LF1[n,n]*sinTheta*Pnm[n-1,n-1]
        for m in range(0,self.maxdegree):
             Pnm[m+1,m] = self.LF1[m+1,m]*cosTheta*Pnm[m,m]
        for m in range(0,self.maxdegree):
            for n in range(m+2,self.maxdegree+1):
                Pnm[n,m] = self.LF1[n,m]*cosTheta*Pnm[n-1,m] - self.LF2[n,m]*Pnm[n-2,m]
        return Pnm

def coeffisort(mat,maxdegree):
    cnm=np.zeros((maxdegree+1,maxdegree+1))
    snm=np.zeros((maxdegree+1,maxdegree+1))
    for row in mat:
        if row[0] > maxdegree:
            break
        cnm[int(row[0]),int(row[1])]=row[2]
        snm[int(row[0]),int(row[1])]=row[3]
    return cnm, snm

def waterheight(lambdao,thetao,cnm,snm,deg_max, lf, kn,R=0.6378136460E+07):
    """
    Calculation of equivalent water height
     Solves the following Equation
                oo             l
          R d  =====         =====
             E \     2 l + 1 \       _                    _                _
     h  = ----  >    -------  >    /dC   cos(m lambda) + dS sin(m lambda)\ P  (cos theta)
      w   3 d  /     1 + k   /     \  lm                                 /  lm
             w =====      l  =====
               l = 2         m = 0

    Parameters
    ----------
    lambdao : longitude of calculation point in radians
    thetao : colatitude of calculation point in radians
    cnm, snm : spherical harmonic coefficients
    deg_max : maximum degree of calculation
    lf: Legendre Functions
    kn: Love numbers
    R : radius of the Earth in m
        The default is 0.6378136460E+07.

    Returns
    -------
    ewh : equivalent water height

    """
    rho_e = 5540.0 #Erde kg/m^3
    rho_w = 1000.0 # Wasser
    ewh=np.zeros((1,len(lambdao)+1))
    ewh[0,0] = thetao
    Pnm = lf(thetao)
    ilong = 1
    ord_mat=np.outer(np.ones((deg_max+1,1)),np.arange(0,deg_max+1))
    deg_mat=np.transpose(ord_mat)
    kn_mat=np.outer(kn[0:deg_max+1],np.ones((deg_max+1,1)))
    for long in lambdao:
        lam_mat=long*ord_mat
        mt1=cnm*np.cos(lam_mat)
        mt2=snm*np.sin(lam_mat)
        mt3=Pnm*(mt1+mt2)
        mfak=(2*deg_mat+1)/(1+kn_mat)
        herg=mfak[2:,:]*mt3[2:,:]
        sumo=np.sum(herg)
        ewh[0,ilong] = R*rho_e/(3.0*rho_w)*sumo
        ilong = ilong+1

    return ewh

def GaussFilterCoeff(R, fr, maxdegree):
    """
    calculate Gaussian filter coefficients for filter radius fr and max degree n
    References
        Wahr, J., Molenaar, M., Bryan, F. (1998): Time variability of the Earth's 
        gravity field: Hydrological and oceanic effects and their possible detection 
        using GRACE, J. Geophys. Res., 103(B12), 30205–30229, DOI: 10.1029/98JB02844.

    Parameters
    ----------
    R : Earth radius in kilometer 
    fr : filter radius in kilometer
    maxdegree : maximum degree of spherical harmonic coefficients

    Returns
    -------
    coeff: coeff Gaussian filter coefficients

    """
    b=np.log(2)/(1-np.cos(fr/R))
    
    coeff = np.zeros((maxdegree+1,1))
    coeff[0] = 1
    coeff[1] = (1+np.exp(-1*b))/(1-np.exp(-2*b))-1/b
    
    for n in range(2,maxdegree+1):
        coeff[n] = -((2*n-1)/b)*coeff[n-1]+coeff[n-2]
        
    return coeff    
        
def LoveNumbers(maxdegree):
    """
    Interpolate Love Numbers for PREM Earth Model, after
    Wahr, J. (2007): Time Variable Gravity Fields from Satellites. In: Herring, 
    T.A. (Ed.): Treatise on Geophysics, Vol 3.

    Parameters
    ----------
    maxdegree : maximum degree of spherical harmonic coefficients

    Returns
    -------
    erg: list of Love numbers

    """
    degs=np.arange(2,maxdegree+1)
    kl=np.array([[2., -0.303],
        [3., -0.194],
        [4., -0.132],
        [5., -0.104],
        [6., -0.089],
        [7., -0.081],
        [8., -0.076],
        [9., -0.072],
        [10., -0.069],
        [12., -0.064],
        [15., -0.058],
        [20., -0.051],
        [30., -0.040],
        [40., -0.033],
        [50., -0.027],
        [70., -0.020],
        [100., -0.014],
        [150., -0.010],
        [200., -0.007]])
        
    erg=np.interp(degs,kl[:,0],kl[:,1])
    erg=np.insert(erg,0,[0,0])
    return erg