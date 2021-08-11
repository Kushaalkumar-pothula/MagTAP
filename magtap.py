import subprocess
import logging
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


#-Logging--------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='%(message)s')
#----------------------------------------------------------------------

#-rfifind -------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(f" => [MagTAP: 1/5]: STARTING RFIFIND...")

logging.info("In:")
logging.info("--------")
logging.info(f"Files = {files}")
logging.info(f"Parameter file = {parfile}")

logging.info("Out:")
logging.info("--------")
logging.info(f" --> Maskfile = {maskname}")
logging.info("-----------------------------------------------------------------")

call_rfifind(files, maskname)

logging.info("-----------------------------------------------------------------")
logging.info(" => [MagTAP: 1/5]: RFIFIND FINISHED.")

   
maskfiles = glob.glob('*.mask')
maskfile = max(maskfiles, key=os.path.getctime)
logging.info(f"Selected maskfile for prepfold: {maskfile}")

#----------------------------------------------------------------------



#-Prepdata-------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(f" => [MagTAP: 2/5]: STARTING PREPDATA")

logging.info("In:")
logging.info("--------")
logging.info(f"DM = {DM}")
logging.info(f"Files = {files}")
logging.info(f"Parameter file = {parfile}")
logging.info(f"maskfile = {maskfile}")

logging.info("Out:")
logging.info("--------")
logging.info("Topocentric time series")
logging.info(f" --> Topocentric series file name = {toponame}")
logging.info("-----------------------------------------------------------------")

call_prepdata(files, DM, maskfile, toponame)

logging.info("-----------------------------------------------------------------")
logging.info("[MagTAP: 2/5]: PREPDATA FINISHED")

topocentric_all = glob.glob('*.dat')
topocentric_series = max(topocentric_all, key=os.path.getctime)
logging.info(f" --> Topocentric time series: {topocentric_series}")

#----------------------------------------------------------------------



#-prepfold-------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(" => [MagTAP 3/5]: STARTING PREPFOLD...")

logging.info("In:")
logging.info("--------")
logging.info(f"DM = {DM}, Period = {p}")
logging.info(f"Files = {files}")
logging.info(f"Parameter file = {parfile}")
logging.info(f"Maskfile = {maskfile}")
logging.info(f"Topocentric series file = {topocentric_series}")


logging.info("Out:")
logging.info("--------")
logging.info("Folded pulse profiles")
logging.info("-----------------------------------------------------------------")

call_prepfold(files, parfile, topocentric_series)

logging.info("-----------------------------------------------------------------")
logging.info(" => [MagTAP 3/5]: PREPFOLD FINISHED.")

plots = glob.glob('*.jpg')
plot_jpg = max(plots, key=os.path.getctime)
logging.info(f" --> Pulse profiles plot: {plot_jpg}")

#----------------------------------------------------------------------

#-Exploredat-----------------------------------------------------------
logging.info("-----------------------------------------------------------------")

#----------------------------------------------------------------------

#-GetTOAs--------------------------------------------------------------
#----------------------------------------------------------------------

