import sys

import merol3 as m3

import time
import datetime

start_time = time.time()

templates_info = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/templates_parameters_R2000.fits'
templates_dir = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/spectra/'

output_dir = '/mnt/lustre/smg/stellar_libraries/atlas9marcs/grid/'

test = m3.merol3(templates_info,templates_dir,output_dir)
test.prepare_templates()

teff_info = [5000,5500,100,100]
logg_info = [1.0,1.5,0.1,0.1]
feh_info  = [-0.2,0.2,0.1 ,0.1]

test.make_selected_grid(teff_info,logg_info,feh_info)

end_time = time.time()

print('     > total time = '+str((end_time-start_time)/60)+' min')


