# 34c3_EWH_MWE
Minimum working example to calculate the Equivalent Water Height (EWH) from GRACE data.  This example calculates 
change between May 2002 and May 2017 for Greenland using the ITSG-GRACE2016 gravity field solutions (Mayer-Gürr et al. 2016). Spatial averaging with a Gaussian filter is used for destriping.

This example does **NOT** include corrections for additional gravity effects, e.g., GIA or leakage. The intend of this demo is solely to give an example of the evaluation of gravity field solutions provided in spherical harmonic coefficients.

The calculations are described in Wahr et al. (1998) with simulated GRACE data and Wahr (2007) with results from the GRACE mission.

A more general documentation on the calculation of gravity field functionals from spherical harmonic coefficients can be found in Barthelmes (2013)

GRACE monthly sollutions used in the example files can be found at: 
<ftp://ftp.tugraz.at/outgoing/ITSG/GRACE/ITSG-Grace2016/monthly/monthly_n120>

References

* Barthelmes, F. (2013): Definitions of Functionals of the Geopotential and Their Calculation from Spherical Harmonic Models. Scientific Technical Report STR09/02. GFZ Potsdam, URL: <http://icgem.gfz-potsdam.de/theory>
* Mayer-Gürr, Torsten; Behzadpour, Saniya; Ellmer, Matthias; Kvas, Andreas; Klinger, Beate; Zehentner, Norbert (2016): ITSG-Grace2016 - Monthly and Daily Gravity Field Solutions from GRACE. GFZ Data Services. DOI: [icgem.2016.007](http://doi.org/10.5880/icgem.2016.007)
* Wahr, J., M. Molenaar, and F. Bryan (1998), Time variability of the Earth's gravity field: Hydrological and oceanic effects and their possible detection using GRACE, J. Geophys. Res., 103(B12), 30205–30229, DOI: [10.1029/98JB02844](http://doi.org/10.1029/98JB02844).
* Wahr, J. (2007): Time Variable Gravity Fields from Satellites. In: Herring, T.A. (Ed.): Treatise on Geophysics, Vol 3. DOI: [B978-0-444-53802-4.00065-8](https://doi.org/10.1016/B978-0-444-53802-4.00065-8)
