import cdflib
import datetime
import numpy as np

def vlos_epoch_from_cdf(path):
    data = cdflib.cdf_to_xarray(path)
    
    epoch = data[list(data.coords)[1]].values
    unix_epoch = cdflib.cdfepoch.unixtime(epoch)
    timestamp = [datetime.datetime.utcfromtimestamp(ue) for ue in unix_epoch]
    return data[list(data.variables)[23]][:,:,2].T, timestamp #vlos, timestamp