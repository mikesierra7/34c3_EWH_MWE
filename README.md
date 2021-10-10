# 34c3_EWH_MWE
This minimum working example (MATLAB or Octave) is supplemental material to the talk "Watching the changing Earth", given at the 34th Chaos Communications Congress on the 27. December 2017 in Leipzig, Germany  ([abstract](https://fahrplan.events.ccc.de/congress/2017/Fahrplan/events/8964.html), [video](https://media.ccc.de/v/34c3-8964-watching_the_changing_earth)).
This example calculates the Equivalent Water Height (EWH) as an expression of mass change between May 2002 and May 2017 for Greenland using the ITSG-GRACE2016 gravity field solutions (Mayer-Gürr et al. 2016). Spatial averaging with a Gaussian filter is used for destriping.

This example does **NOT** include corrections for additional gravity effects (e.g. GIA) or leakage. The intend of this demo is solely to give an example of the evaluation of gravity field solutions provided in spherical harmonic coefficients.

The calculations are described in Wahr et al. (1998) with simulated GRACE data and Wahr (2007) with results from the GRACE mission. A more general documentation on the calculation of gravity field functionals from spherical harmonic coefficients can be found in Barthelmes (2013). A more detailed discussion of the Earth's gravity field and its characteristics is provided in textbooks on geodesy, e. g., Hofmann-Wellenhof and Moritz (2006), and Torge and Müller (2012).

The GRACE monthly solutions used in the example can be found at the [Institute of Geodesy, Graz University of Technology](https://www.tugraz.at/institute/ifg/downloads/gravity-field-models/itsg-grace2016/):
<ftp://ftp.tugraz.at/outgoing/ITSG/GRACE/ITSG-Grace2016/monthly/monthly_n120>

The Resources.pdf contains additional information and links, including online repositories of gravity field data and services.

**How to run**

* Download data files for 2002-05 and 2017-05 into data subfolder
* Run example.m in MATLAB or Octave
* Run example.py for a python version. The [Cartopy](https://scitools.org.uk/cartopy/docs/latest/index.html) package is required for plotting coastlines in the result. Cartopy will automatically download the required coastlines data.

**References**

* Barthelmes, F. (2013): Definitions of Functionals of the Geopotential and Their Calculation from Spherical Harmonic Models. Scientific Technical Report STR09/02. GFZ Potsdam, URL: <http://icgem.gfz-potsdam.de/theory>
* Hofmann-Wellenhof, B. and Moritz, H. (2006): Physical Geodesy, 2nd Edition. Springer, Wien/New York. ISBN: [3-211-33544-7](http://www.worldcat.org/title/physical-geodesy/oclc/758109268)
* Mayer-Gürr, Torsten; Behzadpour, Saniya; Ellmer, Matthias; Kvas, Andreas; Klinger, Beate; Zehentner, Norbert (2016): ITSG-Grace2016 - Monthly and Daily Gravity Field Solutions from GRACE. GFZ Data Services. DOI: [10.5880/icgem.2016.007](http://doi.org/10.5880/icgem.2016.007)
* Torge, W. and Müller, J. (2012): Geodesy, 4th Edition. De Gruyter, Berlin/Boston. ISBN [978-3-11-020718-7](http://www.worldcat.org/title/geodesy/oclc/987088700)
* Wahr, J., M. Molenaar, and F. Bryan (1998), Time variability of the Earth's gravity field: Hydrological and oceanic effects and their possible detection using GRACE, J. Geophys. Res., 103(B12), 30205–30229, DOI: [10.1029/98JB02844](http://doi.org/10.1029/98JB02844).
* Wahr, J. (2007): Time Variable Gravity Fields from Satellites. In: Herring, T.A. (Ed.): Treatise on Geophysics, Vol 3, pp. 193-213. DOI: [10.1016/B978-0-444-53802-4.00065-8](https://doi.org/10.1016/B978-0-444-53802-4.00065-8)
