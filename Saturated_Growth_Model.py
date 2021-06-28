# -*- coding: utf-8 -*-
"""
Created on Sun Nov 7 15:32:32 2020
This script is aims to create a saturated growth model based on GeoCBI data.
It calculates the optimal parameters for a saturated growth regression curve based on GeoCBI and spectral values. 
These spectral values consist of differences between pre-and post-fire spectral imageries.
Based on this script the Saturated_Growth_model can be imported. 
To do this in your own script use the following code:

    root_folder = 'C:\VUAmsterdam\Research_project\scripts'  # Setting rootfolder where you save this file
    os.chdir(root_folder) # Working directory
    from Saturated_Growth_Model import Saturated_Growth_Model as SGM
    
By Max van Gerrevink
"""
#%% Importing libaries
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from math import sqrt

#%% Saturated growth curve
def Saturated_Growth_Model(GeoCBI,SpectralIndex):
    # estimate the GeoCBI    
    def GeoCBI_estimate(x, a, b): # Input paramters for saturated growth curve function
        GeoCBI_predicted = x*(1/(a*x+b)) # GeoCBI predictions based on saturated growth
        return GeoCBI_predicted
    
    # parameters
    x = GeoCBI # Defining GeoCBI as parameter
    y = SpectralIndex # Defining the spectral band as parameter
    n = len(y) # length of data set
    
    
    # curvfitting
    popt, pcov = curve_fit(GeoCBI_estimate, x.values.ravel(), y.values.ravel(), maxfev=1000000) # Estimating parmeters based on curve fitting function


    # retrieve obtimal parameter values
    a = np.around(popt[0],3) # Retrieving a-value from curve fitting
    b = np.around(popt[1],3) # Retrieving b-value from curve fitting
    
    
    # predicted curve paramters
    px = np.linspace(0, 3.3,n) # Create list to compute saturated growth curve
    py = GeoCBI_estimate(px, a, b) # Computing predicted y-values
    
    # calculate regression confidence interval
    py = unp.nominal_values(py) # Converting into nominal values
    
    
   
    # compute r-squared
    r2 = np.around(r2_score(y, GeoCBI_estimate(x,a,b)),3) # rounded at 3 decimals

    # compute root mean square error
    rmse = np.round(sqrt(mean_squared_error(y, GeoCBI_estimate(x,a,b))),3) # rounded at 3 decimals
    
    # returning tuple [y = 0, x = 1, py = 2, px = 3, r2 = 4, rmse = 5, a = 6, b = 7]
    
    return y,x,py,px,r2,rmse,a,b
