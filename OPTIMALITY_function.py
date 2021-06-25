# -*- coding: utf-8 -*-
"""
Created on 14 March 2020
This script is an adapted version of Sander Veraverbeke's matlab sript.
It calculates the optimality based on differences in pre and post-fire 
spectral values. Optimality is defined by the direction and magnitude of 
pixel displacements in the bi-spectral space (Verstraete & Pinty, 1996)

This script uses 1-D array data as an inputfile, Optimality output is dependent on input size.
All input files must have the same shape.

Required packages: numpy version 1.20.2

To do this in your own script use the following code:
    root_folder = 'C:\VU_Amsterdam\Research_project\scripts'  # Setting rootfolder where you save this file
    os.chdir(root_folder) # Working directory
    from OPTIMALITY_function import Spectral_optimality as OPT
    
By Max van Gerrevink
"""
#%% Packages
import numpy as np
#%% Optimality function

def Spectral_optimality(xpre, ypre, xpost, ypost):
       
    NoData = -9999        
    xpre[np.isnan(xpre)] = NoData # Replacing nans with the no data value
    ypre[np.isnan(ypre)] = NoData # Replacing nans with the no data value
    xpost[np.isnan(xpost)] = NoData # Replacing nans with the no data value
    ypost[np.isnan(ypost)] = NoData # Replacing nans with the no data value
    
    
    # empty list to fill later, use the print value to retrieve the size!
    bperp = np.zeros(shape = np.shape(xpre)) # Intercept perpendicular line (slope = -1)
    apost = np.zeros(shape = np.shape(xpre))  # Slope post-fire line (intercept = 0)
    xideal = np.zeros(shape = np.shape(xpre))  # Ideal x-coordinate
    yideal = np.zeros(shape = np.shape(xpre))  # Ideal y-coordinate
    dinsens = np.zeros(shape = np.shape(xpre))  # Distance insensitive
    dsens = np.zeros(shape = np.shape(xpre)) # Distance sensitivity
    Opt = np.zeros(shape = np.shape(xpre))  # Optimality
    
    
    # Optimality equation
    for a,b in np.ndindex(xpre.shape):
            # Intercept perpendicular line (slope = -1)
            bperp[a,b] = xpre[a,b] + ypre[a,b] 
            if bperp[a,b] == 0.02:
                bperp[a,b] ='nan'
            # Slope post-fire line (intercept = 0)
            apost[a,b] = ypost[a,b]/xpost[a,b] 
            if apost[a,b] == 1:
                apost[a,b] ='nan'
            
            # Ideal x-coordinate
            xideal[a,b] = apost[a,b] + 1 
            xideal[a,b] = bperp[a,b]/ xideal[a,b]
            
            # Ideal y-coordinate
            yideal[a,b] = xideal[a,b] * apost[a,b] 
            
            # Distance insensitive
            dinsens[a,b] = ((xpost[a,b]-xideal[a,b])**2)
            dinsens[a,b] = dinsens[a,b] + ((ypost[a,b]-yideal[a,b])**2)
            dinsens[a,b] = dinsens[a,b]**(0.5)
            
            #distance sensitive
            dsens[a,b] = xpost[a,b]-xpre[a,b]
            dsens[a,b] = ((dsens[a,b]**2) + ((ypost[a,b]-ypre[a,b])**2))**(0.5)
            
            
            # Optimality                    
            Opt[a,b] = (dinsens[a,b]/dsens[a,b])
            Opt[a,b] = 1- Opt[a,b]
            if Opt[a,b] < 0:
                Opt[a,b] = 0     
    
    # Get optimality
    return Opt
    