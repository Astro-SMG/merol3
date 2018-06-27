import sys

import matplotlib.pyplot as plt

import merol3 as m3

from calculate_magnitudes import *
from calculate_indices import *

import time
import datetime

start_time = time.time()

####### setting up some variables for magnitudes and indices calculation ########

filter_list = 'sdss_manga_pipeline.res'
zero_point = 'AB'
redshift = 0.0

indices_list = 'MaNGA_range.def'

##### setting up directories #####

templates_info = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/templates_parameters_R2000.fits'
templates_dir = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/spectra/'

output_dir = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/grid/'

test = m3.merol3(templates_info,templates_dir,output_dir)
test.prepare_templates()

pars_star = (2500,-0.5,-2.50)
pars_lims = (100,0.1,0.1)

wavelength,flux,quality = test.single_star(pars_star,pars_lims)

##### calculating indices within the MaNGA wavelength range #####
indices, err_indices = calculate_indices(wavelength,flux*1e-17,indices_list,'test star',ef=0,rv=0,plot=False,sim=False)

######## calculating the magnitudes ########
mags = calculate_magnitudes(wavelength,flux*1e-17,filter_list,zero_point,redshift)

print('     >  Umag    = '+str(mags[0]))
print('     >  Gmag    = '+str(mags[1]))
print('     >  Rmag    = '+str(mags[2]))
print('     >  Imag    = '+str(mags[3]))
print('     >  Zmag    = '+str(mags[4]))
print('     >  OII3727 = '+str(indices[0]))
print('     >  HdA     = '+str(indices[1]))
print('     >  HdF     = '+str(indices[2]))
print('     >  CN1     = '+str(indices[3]))
print('     >  CN2     = '+str(indices[4]))
print('     >  Ca4227  = '+str(indices[5]))
print('     >  G4300   = '+str(indices[6]))
print('     >  HgA     = '+str(indices[7]))
print('     >  HgF     = '+str(indices[8]))
print('     >  Fe4383  = '+str(indices[9]))
print('     >  Ca4455  = '+str(indices[10]))
print('     >  Fe4531  = '+str(indices[11]))
print('     >  Fe4668  = '+str(indices[12]))
print('     >  Hbeta   = '+str(indices[13]))
print('     >  Hbetap  = '+str(indices[14]))
print('     >  OIII1   = '+str(indices[15]))
print('     >  OIII2   = '+str(indices[16]))
print('     >  Fe5015  = '+str(indices[17]))
print('     >  Mg1     = '+str(indices[18]))
print('     >  Mg2     = '+str(indices[19]))
print('     >  Mgb5177 = '+str(indices[20]))
print('     >  Fe5270  = '+str(indices[21]))
print('     >  Fe5335  = '+str(indices[22]))
print('     >  Fe5406  = '+str(indices[23]))
print('     >  Fe5709  = '+str(indices[24]))
print('     >  Fe5782  = '+str(indices[25]))
print('     >  NaD     = '+str(indices[26]))
print('     >  TiO1    = '+str(indices[27]))
print('     >  TiO2    = '+str(indices[28]))
print('     >  NaILaB  = '+str(indices[29]))
print('     >  NaISp   = '+str(indices[30]))
print('     >  NaICo   = '+str(indices[31]))
print('     >  Ca1     = '+str(indices[32]))
print('     >  Ca2     = '+str(indices[33]))
print('     >  Ca3     = '+str(indices[34]))
print('     >  MgI     = '+str(indices[35]))
print('     >  Ca1AZ   = '+str(indices[36]))
print('     >  Ca2AZ   = '+str(indices[37]))
print('     >  Ca3AZ   = '+str(indices[38]))
print('     >  CaT     = '+str(indices[39]))
print('     >  PaT     = '+str(indices[40]))
print('     >  sCaT    = '+str(indices[41]))

print('     > quality = '+str(quality))
plt.xlabel(r"Wavelength [$\AA$]")
plt.ylabel("Relative Flux")
plt.plot(wavelength,flux/np.median(flux),color='black',linewidth=1.0)
plt.show()

end_time = time.time()

print('     > total time = '+str((end_time-start_time)/60)+' min')


