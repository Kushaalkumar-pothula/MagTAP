import subprocess
import os, glob
import argparse

import numpy as np
import matplotlib.pyplot as plt

from magtap.folding import *


#-Parse command line arguments ----------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument(dest='files', type=str, help="Name/glob pattern for the FITS files to be analyzed.")
parser.add_argument(dest='parfile',type=str, help="Parameter file for the magnetar.")
parser.add_argument(dest='maskfile',type=str, help="Mask file for rfifind.")
parser.add_argument(dest='topofile',type=str, help="Topocentric time series file for prepdata.")
parser.add_argument(dest='DM',type=float, help="DM of the magnetar.")
parser.add_argument(dest='p',type=float, help="Period of the magnetar.")
parser.add_argument('-m', '--magnetar',type=str, dest='magnetar', default=None, help="Name of the magnetar. Used to name mask file.")
args = parser.parse_args()


files = args.files
parfile = args.parfile
maskname = args.maskfile
toponame = args.topofile

DM = args.DM
p = args.p

#----------------------------------------------------------------------


#-rfifind -------------------------------------------------------------

print("-----------------------------------------------------------------")
print(f" => [MagTAP: 1/5]: STARTING RFIFIND...")

print("In:")
print("--------")
print(f"Files = {files}")
print(f"Parameter file = {parfile}")

print("Out:")
print("--------")
print(f" --> Maskfile = {maskname}")
print("-----------------------------------------------------------------")

call_rfifind(files, maskname)

print("-----------------------------------------------------------------")
print(" => [MagTAP: 1/5]: RFIFIND FINISHED.")

   
maskfiles = glob.glob('*.mask')
maskfile = max(maskfiles, key=os.path.getctime)
print(f"Selected maskfile for prepfold: {maskfile}")

#----------------------------------------------------------------------



#-Prepdata-------------------------------------------------------------

print("-----------------------------------------------------------------")
print(f" => [MagTAP: 2/5]: STARTING PREPDATA")

print("In:")
print("--------")
print(f"DM = {DM}")
print(f"Files = {files}")
print(f"Parameter file = {parfile}")
print(f"maskfile = {maskfile}")

print("Out:")
print("--------")
print("Topocentric time series")
print(f" --> Topocentric series file name = {toponame}")
print("-----------------------------------------------------------------")

call_prepdata(files, DM, maskfile, toponame)

print("-----------------------------------------------------------------")
print("[MagTAP: 2/5]: PREPDATA FINISHED")

topocentric_all = glob.glob('*.dat')
topocentric_series = max(topocentric_all, key=os.path.getctime)
print(f" --> Topocentric time series: {topocentric_series}")

#----------------------------------------------------------------------



#-prepfold-------------------------------------------------------------

print("-----------------------------------------------------------------")
print(" => [MagTAP 3/5]: STARTING PREPFOLD...")

print("In:")
print("--------")
print(f"DM = {DM}, Period = {p}")
print(f"Files = {files}")
print(f"Parameter file = {parfile}")
print(f"Maskfile = {maskfile}")
print(f"Topocentric series file = {topocentric_series}")


print("Out:")
print("--------")
print("Folded pulse profiles")
print("-----------------------------------------------------------------")

call_prepfold(files, parfile, topocentric_series)

print("-----------------------------------------------------------------")
print(" => [MagTAP 3/5]: Finished prepfold.")

plots = glob.glob('*.jpg')
plot_jpg = max(plots, key=os.path.getctime)
print(f" --> Pulse profiles plot: {plot_jpg}")

#----------------------------------------------------------------------

#-Exploredat-----------------------------------------------------------
#----------------------------------------------------------------------

#-GetTOAs--------------------------------------------------------------
#----------------------------------------------------------------------

