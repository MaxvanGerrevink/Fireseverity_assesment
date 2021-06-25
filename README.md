## Fireseverity_assesment ##

Fire severity can be defined as the degree of environmental change induced by a fire and is  an important fire regime attribute of interest to fire emissions modelers and 
post-fire rehabilitation planners. Remotely sensed fire severity is traditionally assessed using multispectral imagery by means of the differenced normalized burn ratio (dNBR).
This spectral index is based on the fire-induced reflectance changes in the near infrared (NIR) and short-wave infrared (SWIR) spectral regions. Our study aims to evaluate the
spectral sensitivity of the dNBR using hyperspectral imagery by identifying the optimal bi-spectral NIR-SWIR combination. This assessment capitalized upon the unique opportunity
stemming from the pre- and post-fire airborne acquisitions over the Rim (2013) and King (2014) fires in California with the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS)
sensor. 

# Spectral optimality #
Spectral index optimality quantifies the index’s sensitivity to change, in this case fire-induced ecosystem changes (Roy et al., 2006; Veraverbeke et al., 2010). 
In the case of normalized difference spectral indices, the optimality of an index is defined by the direction and magnitude of pixel displacements in the bi-spectral
space (Verstraete and Pinty, 1996).This can be illustrated by the displacement from unburned U to burned B in the bi-spectral space. Within the bi-spectral space, 
the y-axis represents the NIR reflectance forall indices. Whereas the x-axis represents the SWIR reflectance for the dNBR indices. The vector |UB| consists of the 
sum of the vectors |UO| and |OB|. A spectral index is then
sensitive to displacements that are perpendicular to the index isolines. In this case, the spectral index is sensitive to the displacement from U to the optimally sensed O. 
In contrast, the spectral index is insensitive to displacements along isolines, in this case the vector |OB|. By measuring the distances of the vectors |UO| and |OB|, the index
optimality is defined as:

Optimality = 1 – (|OB|/|UB|)	(1)

As |OB| can never exceed |UB|, the optimality varies between zero and one. When the optimality equals zero, then the index is completely insensitive to the change of interest. 
An optimality score of one indicates that an index performs ideally in monitoring the change of interest, in this case fire severity. All pixels within the fire perimeter were used
in this analysis.


# References #
