import subprocess
import logging
import glob
import argparse

from magtap.folding import *
from magtap.timing import *


#-Parse command line arguments ----------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument(dest='files', type=str, help="Name/glob pattern for the FITS files to be analyzed.")
parser.add_argument(dest='parfile',type=str, help="Parameter file for the magnetar.")
parser.add_argument(dest='maskfile',type=str, help="Mask file for rfifind.")
parser.add_argument(dest='topofile',type=str, help="Topocentric time series file for prepdata.")
parser.add_argument(dest='timfile',type=str, help=".tim file for GetTOAs.")
parser.add_argument(dest='DM',type=float, help="DM of the magnetar.")
parser.add_argument(dest='p',type=float, help="Period of the magnetar.")
args = parser.parse_args()


files = args.files
parfile = args.parfile
maskname = args.maskfile
toponame = args.topofile
timfile = args.timfile

DM = args.DM
p = args.p

#----------------------------------------------------------------------


#-Logging--------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='%(message)s')
#----------------------------------------------------------------------

#-Start----------------------------------------------------------------
logging.info("==============================================")
logging.info("  MagTAP: Magnetar Timing Analysis Pipeline   ")
logging.info("==============================================")

logging.info("Parameters:")
logging.info("-----------")
logging.info(f"Files = {files}")
logging.info(f"Parameter file = {parfile}")
logging.info(f"Maskfile name = {maskname}")
logging.info(f"Topocentric time series file name = {toponame}")
logging.info(f"TOAs file (.tim) name = {timfile}")
logging.info(f"DM = {DM}")
logging.info(f"p = {p}")

logging.info("=====================")

logging.info("Pipeline:")
logging.info("---------")
logging.info("1/5 : RFIFIND")
logging.info("2/5 : PREPDATA")
logging.info("3/5 : PREPFOLD")
logging.info("4/5 : EXPLOREDAT")
logging.info("5/5 : GetTOAs")

logging.info("=====================")


#-rfifind -------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(f" ***********[MagTAP: 1/5]: STARTING RFIFIND***********")

logging.info("In:")
logging.info("--------")
logging.info(f"Files = {files}")

logging.info("Out:")
logging.info("--------")
logging.info(f"Maskfile = {maskname}")
logging.info("-----------------------------------------------------------------")

call_rfifind(files, maskname)

logging.info("-----------------------------------------------------------------")
logging.info(" ***********[MagTAP: 1/5]: RFIFIND FINISHED***********")

   
maskfiles = glob.glob('*.mask')
maskfile = max(maskfiles, key=os.path.getctime)
logging.info(f" --> Selected maskfile for prepfold: {maskfile}")

#----------------------------------------------------------------------



#-Prepdata-------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(f" ***********[MagTAP: 2/5]: STARTING PREPDATA***********")

logging.info("In:")
logging.info("--------")
logging.info(f"Files = {files}")
logging.info(f"DM = {DM}")
logging.info(f"maskfile = {maskfile}")
logging.info(f"Parameter file = {parfile}")

logging.info("Out:")
logging.info("--------")
logging.info("Topocentric time series")
logging.info(f"Topocentric series file name = {toponame}")
logging.info("-----------------------------------------------------------------")

call_prepdata(files, DM, maskfile, toponame)

logging.info("***********[MagTAP: 2/5]: PREPDATA FINISHED***********")
logging.info("-----------------------------------------------------------------")

topocentric_all = glob.glob('*.dat')
topocentric_series = max(topocentric_all, key=os.path.getctime)
logging.info(f" --> Topocentric time series: {topocentric_series}")

#----------------------------------------------------------------------



#-prepfold-------------------------------------------------------------

logging.info("-----------------------------------------------------------------")
logging.info(" ***********[MagTAP 3/5]: STARTING PREPFOLD***********")

logging.info("In:")
logging.info("--------")
logging.info(f"Files = {files}")
logging.info(f"Parameter file = {parfile}")
logging.info(f"Maskfile = {maskfile}")
logging.info(f"Topocentric series file = {topocentric_series}")


logging.info("Out:")
logging.info("--------")
logging.info("Folded pulse profiles")
logging.info("-----------------------------------------------------------------")

call_prepfold(files, parfile, topocentric_series)

logging.info(" ***********[MagTAP 3/5]: PREPFOLD FINISHED***********")
logging.info("-----------------------------------------------------------------")

plots = glob.glob('*.ps')
plot_ps = max(plots, key=os.path.getctime)
subprocess.call(["convert", "-rotate", str(90), plot_ps, plot_ps+str(jpg)])
logging.info(f" --> Pulse profiles plot: {plot_ps+str(jpg)}")

#----------------------------------------------------------------------



#-Exploredat-----------------------------------------------------------
logging.info("-----------------------------------------------------------------")
logging.info(f" ***********[MagTAP: 4/5]: STARTING EXPLOREDAT***********")

logging.info("In:")
logging.info("--------")
logging.info(f"Topocentric series file = {topocentric_series}")

logging.info("Out:")
logging.info("--------")
logging.info("Topocentric series contents")

call_exploredat(topocentric_series)

logging.info(f" ***********[MagTAP: 4/5]: FINISHED EXPLOREDAT***********")
logging.info("-----------------------------------------------------------------")
#----------------------------------------------------------------------



#-GetTOAs--------------------------------------------------------------
bestprofs = glob.glob('*.bestprof')
bestprof = max(bestprofs, key=os.path.getctime)

pfds = glob.glob('*.pfd')
pfd = max(pfds, key=os.path.getctime)

logging.info("-----------------------------------------------------------------")
logging.info(f" ***********[MagTAP: 5/5]: STARTING GetTOAs***********")

logging.info("In:")
logging.info("--------")
logging.info(f"bestprof = {bestprof}")
logging.info(f"pfd = {pfd}")

logging.info("Out:")
logging.info("--------")
logging.info(f"TOAs = {timfile}")

call_gettoas(bestprof, pfd, timfile)

logging.info(f" ***********[MagTAP: 5/5]: FINISHED GetTOAs***********")
logging.info("-----------------------------------------------------------------")
#----------------------------------------------------------------------

logging.info("**************************")
logging.info("-----MagTAP FINISHED-----")
logging.info("**************************")
logging.info("Outputs:")
logging.info("--------")
logging.info(f" Maskfile: {maskfile}")
logging.info(f" Topocentric time series: {topocentric_series}")
logging.info(f" Pulse profiles plot: {plot_ps+str(jpg)}")
logging.info(f"TOAs = {timfile}")

