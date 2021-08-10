import subprocess
import numpy as np

def call_rfifind(files, maskfilename="mask", time=1.0):
    """
    Call rfifind
    
    PARAMETERS:
    ----------
    files: FITS file or glob pattern
        FITS files for rfifind
    
    maskfilename: String, default="mask"
        Mask file name for rfifind output

    time: float
        Time for the -time flag of rfifind. Probably integration time
    """
    print(f"Starting rfifind with -time {time} and {files} files...")
    subprocess.call("rfifind", "-time", time, "-o", maskfilename, files)


def call_prepfold(files, dm, p, maskfile, parfile=None):
    """
    Call prepfold

    PARAMETERS
    ----------
    files: FITS file or glob pattern
        FITS files for rfifind

    dm: float
        Dispersion measure
    
    p: float
        Spin period
    
    maskfile: String
        Mask file name
    
    parfile: .par file
        Parameter file
    """
    print(f"Starting prepfold for {files}: DM = {dm} p = {p}, parfile = {parfile}")
    subprocess.call("prepfold", "-p", p, "-dm", dm, files, "-mask", maskfile, "-nosearch")


def call_prepdata(files, DM, maskfile, topofile = "topofile"):
    """
    Create a topocentric time series

    PARAMETERS
    ----------
    files: FITS file or glob pattern
        FITS files for rfifind

    dm: float
        Dispersion measure
    
    maskfile: String
        Mask file name
    
    topofile: String, default = "topofile"
        Filename for topocentric time series file
    """
    print(f"Starting prepdata for DM = {DM}, maskfile = {maskfile}, files = {files}")
    subprocess.call("prepdata", "-nobary", "-dm", DM, "-mask", maskfile, "-o", topofile, files)