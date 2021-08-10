import subprocess
import numpy as np

def call_rfifind(files, maskfileame='mask', time=1.0):
    """
    Call rfifind
    """
    print(f"Starting rfifind with -time {time} and {files} files...")
    subprocess.call("rfifind", "-time", time, "-o", maskfileame, files)

def call_prepfold(files, dm, p, maskfile, parfile=None):
    """
    Call prepfold
    """
    print(f"Starting prepfold for {files}: DM = {dm} p = {p}, parfile = {parfile}")
    subprocess.call("prepfold", "-p", p, "-dm", dm, files, "-mask", maskfile, "-nosearch")