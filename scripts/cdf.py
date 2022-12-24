import cdflib
import datetime
import numpy as np

def cdf2vlos_and_utc(path: str) -> tuple:
    """Return vlos and utc from a cdf file

    Args:
        path (str): path to a cdf file

    Returns:
        tuple: vlos is doppler shift values and utc is timestamps of vlos with utc
    """

    data = cdflib.cdf_to_xarray(path)

    epoch = data[list(data.coords)[1]].values
    unix_epoch = cdflib.cdfepoch.unixtime(epoch)
    utc = [datetime.datetime.utcfromtimestamp(ue) for ue in unix_epoch]
    vlos = data[list(data.variables)[23]][:,:,2].T.values
    return vlos, utc #vlos, utc
