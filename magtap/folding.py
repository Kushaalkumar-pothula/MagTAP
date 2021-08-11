import subprocess
import logging

def call_rfifind(files, maskfilename, time=1.0):
    """
    Call rfifind
    
    PARAMETERS:
    ----------
    files: FITS file or glob pattern
        FITS files for rfifind
    
    maskfilename: string
        Mask file name for rfifind output

    time: float
        Time for the -time flag of rfifind. Probably integration time
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"[INTERNAL: RFIFIND] -time = {time}; files = {files}; maskfile = {maskfilename}")
    logging.info("----------")
    subprocess.call(["rfifind", "-time", time, "-o", maskfilename, files])

def call_prepdata(files, DM, maskfile, topofile):
    """
    Create a topocentric time series

    PARAMETERS
    ----------
    files: FITS file or glob pattern
        FITS files for rfifind

    dm: float
        Dispersion measure
    
    maskfile: string
        Mask file name
    
    topofile: string
        Filename for topocentric time series file
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"[INTERNAL: PREPDATA] DM = {DM}; maskfile = {maskfile}; files = {files}; topo-file = {topofile}")
    logging.info("----------")
    subprocess.call(["prepdata", "-nobary", "-dm", DM, "-mask", maskfile, "-o", topofile, files])


def call_prepfold(files, parfile, topofile):
    """
    Call prepfold

    PARAMETERS
    ----------
    files: FITS filename or glob pattern
        FITS files for rfifind
    
    parfile: string
        Parameter file name

    topofile: string
        Filename for topocentric time series file
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"[INTERNAL: PREPFOLD] Files= {files}; topo-file = {topofile}; parfile = {parfile}")
    logging.info("----------")
    subprocess.call(["prepfold", "-par", parfile, "-nosearch", "-n", 128, "-fine", topofile])

