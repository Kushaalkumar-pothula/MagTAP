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
parser.add_argument(dest='DM',type=float, help="DM of the magnetar.")
parser.add_argument(dest='p',type=float, help="Period of the magnetar.")
parser.add_argument('-m', '--magnetar',type=str, dest='magnetar', default=None, help="Name of the magnetar. Used to name mask file.")
args = parser.parse_args()


files = args.files
parfile = args.parfile
magnetar = args.magnetar

DM = args.DM
p = args.p
#----------------------------------------------------------------------


#-rfifind -------------------------------------------------------------
if magnetar is not None:
    print("-----------------------------------------------------------------")
    print(f"Starting [MagTAP: 1/3]: rfifind...")
    print(f"Magnetar = {magnetar}")
    print(f"Files = {files}")
    print(f"Parameter file = {parfile}")
    print("Out: maskfile")
    print(f"maskfile = {magnetar}")
    print("-----------------------------------------------------------------")
    maskname = magnetar
    call_rfifind(files, maskname)
    print("-----------------------------------------------------------------")
    print("[MagTAP: 1/3]: Completed rfifind.")

else:
    print("-----------------------------------------------------------------")
    print(f"Starting MagTAP: 1/3: rfifind...")
    print(f"Files = {files}")
    print(f"Parameter file = {parfile}")
    print("Out: maskfile")
    print(f"maskfile = mask")
    print("-----------------------------------------------------------------")
    call_rfifind(files)
    print("-----------------------------------------------------------------")
    print("[MagTAP: 1/3]: Finished rfifind.")


maskfiles = glob.glob('*.mask')
maskfile = max(maskfiles, key=os.path.getctime)

print(f"Selected maskfile for prepfold: {maskfile}")
print(f"All maskfiles = {maskfiles}")
#----------------------------------------------------------------------


#-prepfold-------------------------------------------------------------
print("-----------------------------------------------------------------")
print("[MagTAP 2/3]: prepfold...")
print("In:")
print(f"DM = {DM}, Period = {p}")
print(f"Files = {files}")
print(f"Parameter file = {parfile}")
print("Out: Folded pulse profiles")
print(f"maskfile = {maskfile}")
print("-----------------------------------------------------------------")
call_prepfold(files, DM, p, maskfile)
print("-----------------------------------------------------------------")
print("[MagTAP 2/3]: Finished prepfold.")

#----------------------------------------------------------------------


