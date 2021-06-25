# Fire severity assesment using normalised burn ratio #
This repository contains functions:
- Saturated Growth Model for Field measurements of fire severity,
- Spectral optimality functions for index evaluation.

## Background information ##
Fire severity can be defined as the degree of environmental change induced by a fire and is  an important fire regime attribute of interest to fire emissions modelers and 
post-fire rehabilitation planners. Remotely sensed fire severity is traditionally assessed using multispectral imagery by means of the differenced normalized burn ratio (dNBR) (García and Caselles, 1991).This spectral index is based on the fire-induced reflectance changes in the near infrared (NIR) and short-wave infrared (SWIR) spectral regions. Our study aims to evaluate the spectral sensitivity of the dNBR using hyperspectral imagery by identifying the optimal bi-spectral NIR-SWIR combination. This assessment capitalized upon the unique opportunity stemming from the pre- and post-fire airborne acquisitions over the Rim (2013) and King (2014) fires in California with the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) sensor. We were evaluated based on a comparison with 83 Geometrically structured Composite Burn Index (GeoCBI) field measurements of fire severity and an optimality statistic calculated for  fire-induced spectral displacements (De Santis and Chuvieco, 2009; Key and Benson, 2006; Roy et al., 2006; Thenkabail et al., 2002; Verstraete and Pinty, 1996).

## Field data measurements of fire severity ##
Fire severity was assessed in the field using the Geometrically structured Composite Burn Index (GeoCBI) protocol, a modified version of Key and Benson’s Combustion Burn Index (CBI) (De Santis and Chuvieco, 2009; Key and Benson, 2006). GeoCBI accounts for the fractional cover in each plot by deviding the ecosystem into five different stata (Veraverbeke et al., 2010). The strata are: (I) substrates; (II) herbs, low shrubs, and small trees shorter than 1 m; (III) tall shrubs and trees of 1 to 5 m; (IV) trees of 5 to 20 m; and (V) trees taller than 20 m. Ratings are given on a continuous scale from zero to three based on semi-quantitative expert judgement approach, hence this is inherently prone to some degree of subjectivity. Fire severity scores are for example assigned to soil and rock cover and color changes, the percentage change in leaf area index, char height, and percentage of green vegetation (De Santis and Chuvieco, 2009; Veraverbeke et al., 2010). Based on the stratum averages, GeoCBI ratings are proportional to the corresponding fraction of cover of each stratum, resulting in a weighted average between zero and three that expresses plot-level fire severity. 

A non-linear model based on a saturated growth model was used to describe the relationship between GeoCBI and the dNBRs (Hall et al., 2008). The use of a saturated growth model is justified by the asymptotic behavior exhibited across the dNBR scatter plots in previous studies (Hall et al., 2008; Van Wagtendonk et al., 2004; Veraverbeke et al., 2010). This unravels the inability and underestimation of the approach to differentiate among higher fire severity plots (García and Caselles, 1991; Hall et al., 2008). The regression results of the saturated growth model were evaluated using two goodness-of-fit parameters: (i) the coefficient of determination R2 and (ii) the root mean squared error (RMSE). The coefficient of determination R2 estimates the proportion of variability that is fully that is explained by the model. The RMSE is a goodness of fit parameter that measure of how much a response variable differs from the model predictions and is expressed in the same units as the dependent variable. 



## Spectral index optimality ##
Spectral index optimality quantifies the index’s sensitivity to change, in this case fire-induced ecosystem changes (Roy et al., 2006; Veraverbeke et al., 2010). 
In the case of normalized difference spectral indices, the optimality of an index is defined by the direction and magnitude of pixel displacements in the bi-spectral
space (Verstraete and Pinty, 1996).This can be illustrated by the displacement from unburned U to burned B in the bi-spectral space. Within the bi-spectral space, 
the y-axis represents the NIR reflectance forall indices. Whereas the x-axis represents the SWIR reflectance for the dNBR indices. The vector |UB| consists of the 
sum of the vectors |UO| and |OB|. A spectral index is then sensitive to displacements that are perpendicular to the index isolines. In this case, the spectral index 
is sensitive to the displacement from U to the optimally sensed O. 
In contrast, the spectral index is insensitive to displacements along isolines, in this case the vector |OB|. By measuring the distances of the vectors |UO| and |OB|, the index
optimality is defined as:

Optimality = 1 – (|OB|/|UB|)

As |OB| can never exceed |UB|, the optimality varies between zero and one. When the optimality equals zero, then the index is completely insensitive to the change of interest. 
An optimality score of one indicates that an index performs ideally in monitoring the change of interest, in this case fire severity. All pixels within the fire perimeter were used in this analysis. We used the median statistic for the evaluation of each bi-spectral space due to the non-normal optimality distributions and its robustness in the presence of outliers. 


### References ###
- De Santis, A., Chuvieco, E., 2009. GeoCBI: A modified version of the Composite Burn Index for the initial assessment of the short-term burn severity from remotely sensed data. Remote Sensing of Environment 113, 554–562. https://doi.org/10.1016/j.rse.2008.10.011

- García, M.J.L., Caselles, V., 1991. Mapping burns and natural reforestation using thematic mapper data. Geocarto International 6, 31–37. https://doi.org/10.1080/10106049109354290

- Hall, R.J., Freeburn, J.T., De Groot, W.J., Pritchard, J.M., Lynham, T.J., Landry, R., 2008. Remote sensing of burn severity: experience from western Canada boreal fires. International Journal of Wildland Fire 17, 476–489.

- Key, C.H.; Benson, N.C. Landscape Assessment (LA) Sampling and Analysis Methods. Available online: https://www.fs.usda.gov/treesearch/pubs/24066 (accessed on 20 January 2021).

- Roy, D.P., Boschetti, L., Trigg, S.N., 2006. Remote sensing of fire severity: Assessing the performance of the normalized burn ratio. IEEE Geoscience and Remote Sensing Letters 3, 112–116. https://doi.org/10.1109/LGRS.2005.858485

- Thenkabail, P.S., Smith, R.B., De Pauw, E., 2002. Evaluation of narrowband and broadband vegetation indices for determining optimal hyperspectral wavebands for agricultural crop characterization. Photogrammetric Engineering and Remote Sensing 68, 607–621.

- Veraverbeke, S.S.N., Verstraeten, W.W., Lhermitte, S., Goossens, R., 2010. Evaluating Landsat Thematic Mapper spectral indices for estimating burn severity of the 2007 Peloponnese wildfires in Greece. International Journal of Wildland Fire 19, 558–569. https://doi.org/10.1071/WF09069

- Verstraete, M.M., Pinty, B., 1996. Designing optimal spectral indexes for remote sensing applications. IEEE Transactions on Geoscience and Remote Sensing 34, 1254–1265. https://doi.org/10.1109/36.536541
