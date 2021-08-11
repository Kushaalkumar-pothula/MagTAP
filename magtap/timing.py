import subprocess
import logging

def call_exploredat(topo_file):
    """
    Call exploredat

    PARAMETERS
    ----------
    topo_file: string
        Topocentric series file
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"[INTERNAL: EXPLOREDAT]: Topocentric file = {topo_file} ")
    logging.info("----------")
    subprocess.call(["exploredat", topo_file])

def call_gettoas(bestprof, pfd, timfile):
    """
    Call GetTOAs

    PARAMETERS
    ----------
    bestprof: string
        .bestprof file
    
    pfd: string
        .pfd file
    
    timfile: string
        .tim file
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    path = r'~/work/shared/PSC/magnetar/testdata/get_TOAs.py'
    logging.info(f"[INTERNAL: GetTOAs]: bestprof = {bestprof}; pfd = {pfd}; timfile = {timfile} ")
    logging.info("----------")
    subprocess.call(["path", "-t", bestprof, "-n", str(4), pfd])
    
    
