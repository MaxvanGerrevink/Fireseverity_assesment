# Fire severity assesment using normalised spectral indicies #

Fire severity can be defined as the degree of environmental change induced by a fire and is  an important fire regime attribute of interest to fire emissions modelers and 
post-fire rehabilitation planners. Remotely sensed fire severity is traditionally assessed using multispectral imagery by means of the differenced normalized burn ratio (dNBR).
This spectral index is based on the fire-induced reflectance changes in the near infrared (NIR) and short-wave infrared (SWIR) spectral regions. Our study aims to evaluate the
spectral sensitivity of the dNBR using hyperspectral imagery by identifying the optimal bi-spectral NIR-SWIR combination. This assessment capitalized upon the unique opportunity
stemming from the pre- and post-fire airborne acquisitions over the Rim (2013) and King (2014) fires in California with the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) sensor. We were evaluated based on a comparison with 83 Geometrically structured Composite Burn Index (GeoCBI) field measurements of fire severity and an optimality statistic calculated for  fire-induced spectral displacements (De Santis and Chuvieco, 2009; Key and Benson, 2006; Roy et al., 2006; Thenkabail et al., 2002; Verstraete and Pinty, 1996). 

## Spectral optimality ##
Spectral index optimality quantifies the index’s sensitivity to change, in this case fire-induced ecosystem changes (Roy et al., 2006; Veraverbeke et al., 2010). 
In the case of normalized difference spectral indices, the optimality of an index is defined by the direction and magnitude of pixel displacements in the bi-spectral
space (Verstraete and Pinty, 1996).This can be illustrated by the displacement from unburned U to burned B in the bi-spectral space. Within the bi-spectral space, 
the y-axis represents the NIR reflectance forall indices. Whereas the x-axis represents the SWIR reflectance for the dNBR indices. The vector |UB| consists of the 
sum of the vectors |UO| and |OB|. A spectral index is then sensitive to displacements that are perpendicular to the index isolines. In this case, the spectral index 
is sensitive to the displacement from U to the optimally sensed O. 
In contrast, the spectral index is insensitive to displacements along isolines, in this case the vector |OB|. By measuring the distances of the vectors |UO| and |OB|, the index
optimality is defined as:

Optimality = 1 – (|OB|/|UB|)	(1)

As |OB| can never exceed |UB|, the optimality varies between zero and one. When the optimality equals zero, then the index is completely insensitive to the change of interest. 
An optimality score of one indicates that an index performs ideally in monitoring the change of interest, in this case fire severity. All pixels within the fire perimeter were used
in this analysis.


## References ##
De Santis, A., Chuvieco, E., 2009. GeoCBI: A modified version of the Composite Burn Index for the initial assessment of the short-term burn severity from remotely sensed data. Remote Sensing of Environment 113, 554–562. https://doi.org/10.1016/j.rse.2008.10.011

Key, C.H.; Benson, N.C. Landscape Assessment (LA) Sampling and Analysis Methods. Available online: https://www.fs.usda.gov/treesearch/pubs/24066 (accessed on 20 January 2021).

Roy, D.P., Boschetti, L., Trigg, S.N., 2006. Remote sensing of fire severity: Assessing the performance of the normalized burn ratio. IEEE Geoscience and Remote Sensing Letters 3, 112–116. https://doi.org/10.1109/LGRS.2005.858485

Thenkabail, P.S., Smith, R.B., De Pauw, E., 2002. Evaluation of narrowband and broadband vegetation indices for determining optimal hyperspectral wavebands for agricultural crop characterization. Photogrammetric Engineering and Remote Sensing 68, 607–621.

Veraverbeke, S.S.N., Verstraeten, W.W., Lhermitte, S., Goossens, R., 2010. Evaluating Landsat Thematic Mapper spectral indices for estimating burn severity of the 2007 Peloponnese wildfires in Greece. International Journal of Wildland Fire 19, 558–569. https://doi.org/10.1071/WF09069

Verstraete, M.M., Pinty, B., 1996. Designing optimal spectral indexes for remote sensing applications. IEEE Transactions on Geoscience and Remote Sensing 34, 1254–1265. https://doi.org/10.1109/36.536541
