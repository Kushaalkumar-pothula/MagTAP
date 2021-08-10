import subprocess
import os, glob
import argparse

import numpy as np
import matplotlib.pyplot as plt

from magtap.folding import *


# Parse command line arguments ----------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument(dest='files', type=str, help="Name/glob pattern for the FITS files to be analyzed.")
parser.add_argument(dest='parfile',type=str, help="Parameter file for the magnetar.")
parser.add_argument('-m', '--magnetar',type=str, dest='magnetar', default=None, help="Name of the magnetar. Used to name mask file.")
args = parser.parse_args()

files = args.files
parfile = args.parfile
magnetar = args.magnetar
#----------------------------------------------------------------------
if magnetar is not None:
    print("-----------------------------------------------------------------")
    print(f"Starting MagTAP: 1/3: rfifind...")
    print(f"Magnetar = {magnetar}")
    print(f"Files = {files}")
    print(f"Parameter file = {parfile}")
    print("Out: maskfile")
    print(f"maskfile = {magnetar}")
    print("-----------------------------------------------------------------")
    maskname = magnetar
    call_rfifind(files, maskname)
    print("MagTAP: 1/3: Completed rfifind.")

else:
    print("-----------------------------------------------------------------")
    print(f"Starting MagTAP: 1/3: rfifind...")
    print(f"Files = {files}")
    print(f"Parameter file = {parfile}")
    print("Out: maskfile")
    print(f"maskfile = mask")
    print("-----------------------------------------------------------------")
    call_rfifind(files)
    print("MagTAP: 1/3: Completed rfifind.")

maskfiles = glob.glob('*.mask')
maskfile = max(maskfiles, key=os.path.getctime)
