# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:42:19 2021
This script is aims to unwrap the stacked GeoTiffs over the Rim and King fires


@author: MaxvanGerrevink
"""
#%%
import rioxarray
import numpy as np
import rasterio
#%% King fire data
data_pre = rioxarray.open_rasterio(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\output_cutouts\full_pre.tif")
data_post = rioxarray.open_rasterio(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\output_cutouts\full_post.tif")
# mask of fire perimeter
mask = rasterio.open(r'C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\output_cutouts\full_mask.tif').read(1)

# NOTE: water absorption bands are excluded in the stacked GeoTiff
#%% Rim fire data
data_pre = rioxarray.open_rasterio(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\Rim\output_cutouts\full_pre.tif")
data_post = rioxarray.open_rasterio(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\output_cutouts\full_post.tif")
# mask of fire perimeter
mask = rasterio.open(r'C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\Rim\output_cutouts\full_mask.tif').read(1)

# NOTE: water absoption bands are included in the stacked GeoTiff
#%% Data Processing
# =============================================================================
# Pre-fire bands
# =============================================================================
# Nir spectral bands
for i in range (32,96):
    band = np.array(data_pre.sel(band = i)) # select band (note python indexing)
    band[band == -1.7e+308] = 'nan' # remove nodata values
    band = band * mask # apply mask to retrive fire perimeter
    band[band == -0] = 'nan' # set nan values
    band = band.ravel() # transformation to 1d array
    print('band selection completed:'+ ' ' +str(i+1)) #build-in itteration check
# Swir spectral bands
for i in range (98,200):
    band = np.array(data_pre.sel(band = i)) # select band (note python indexing)
    band[band == -1.7e+308] = 'nan' # remove nodata values
    band = band * mask # apply mask to retrive fire perimeter
    band[band == -0] = 'nan' # set nan values
    band = band.ravel() # transformation to 1d array
    
    print('band selection completed:'+ ' ' +str(i+1)) #build-in itteration check
    
    # save bands to folder
    np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\bands\full\Pre\SWIR\band{}.npy".format(i+1),band)
    #np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\Rim\bands\full\Pre\SWIR\band{}.npy".format(i+1),band)

# =============================================================================
# Post-fire bands
# =============================================================================


for i in range (32,96):
    band = np.array(data_post.sel(band = i)) # select band (note python indexing)
    band[band == -1.7e+308] = 'nan' # remove nodata values
    band = band * mask # apply mask to retrive fire perimeter
    band[band == -0] = 'nan' # set nan values
    band = band.ravel() # transformation to 1d array
        
    print('band selection completed:'+ ' ' +str(i+1))
    np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\bands\full\Post\NIR\band{}.npy".format(i+1),band)
    #np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\Ring\bands\full\Post\NIR\band{}.npy".format(i+1),band)
    

for i in range (98,106):
    band = np.array(data_post.sel(band = i)) # select band (note python indexing)
    band[band == -1.7e+308] = 'nan' # remove nodata values
    band = band * mask # apply mask to retrive fire perimeter
    band[band == -0] = 'nan' # set nan values
    band = band.ravel() # transformation to 1d array
    
    print('band selection completed:'+ ' ' +str(i+1))
    np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\King\bands\full\Post\SWIR\band{}.npy".format(i+1),band)
    #np.save(r"C:\VUAmsterdam\Thesis_EC\Data\Optimality\Masks\Rim\bands\full\Post\SWIR\band{}.npy".format(i+1),band)

