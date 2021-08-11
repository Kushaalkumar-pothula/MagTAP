# MagTAP

MagTAP (Magnetar Timing Analysis Pipeline) is a Python pipeline to simplify folding and timing Magnetar data, built for Magnetar Timing research group at the Pulsar Search Collaboratory (PSC).

MagTAP uses PRESTO, the standard tool for pulsar data anaysis, for folding and timing data.

MagTAP pipeline consists of:
1. `rfifind`
2. `prepdata`
3. `prepfold`
4. `exploredat`
5. `get_TOAs.py`

These steps are run sequentially, and MagTAP finds the required files (mask file and topocentric time series file) by itself, removing user interaction.

## Installation
Installation using `git clone` is the recommended method:
```zsh
❯ https://github.com/Kushaalkumar-pothula/MagTAP.git
❯ cd MagTAP
```
## Usage
MagTAP is a command-line tool, and it accepts arguments, like files and values, as flags. To view help, use the `-h` or `--help` flag:

```zsh
❯ python magtap.py --help
usage: magtap.py [-h] files parfile maskfile topofile timfile DM p

positional arguments:
  files       Name/glob pattern for the FITS files to be analyzed.
  parfile     Parameter file for the magnetar.
  maskfile    Mask file for rfifind.
  topofile    Topocentric time series file for prepdata.
  timfile     .tim file for GetTOAs.
  DM          DM of the magnetar.
  p           Period of the magnetar.

optional arguments:
  -h, --help  show this help message and exit
```

## Requirements
MagTAP requires:
- Python >= 3.7

## Known Bugs
The only bug is that `get_TOAs.py` (5th step) is not able to get arguments, this is expected to be resolved soon.

## Author
This code was written by [Kushaal Kumar Pothula](https://kushaalkumarpothula.wordpress.com/) during his junior year of high school, as a member of magnetar timing research team @ Pulsar Search Collaboratory.
