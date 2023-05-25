import cdflib
import datetime
import numpy as np
import os

def cdf2vlos_and_utc(path: str) -> tuple:
    """Return vlos and utc from a cdf file

    Args:
        path (str): path to a cdf file

    Returns:
        tuple: vlos is doppler shift values and utc is timestamps of vlos with utc
    """

    save_dir = os.path.join('/home/miyazaki/Documents_ubuntu/noise_reduction/data/npy', '/'.join(path.split('.')[0].split('/')[-4:-1]))

    filename = path.split('.')[0].split('/')[-1]
    npm_file_path = os.path.join(save_dir, filename)

    is_npm_file = os.path.isfile(npm_file_path+'_vlos.npy')

    if is_npm_file:
        vlos = np.load(npm_file_path+'_vlos.npy', allow_pickle=True)
        utc = np.load(npm_file_path+'_utc.npy', allow_pickle=True)
        return vlos, utc

    data = cdflib.cdf_to_xarray(path)

    epoch = data[list(data.coords)[1]].values
    unix_epoch = cdflib.cdfepoch.unixtime(epoch)
    utc = np.array([datetime.datetime.utcfromtimestamp(ue) for ue in unix_epoch])
    vlos = data[list(data.variables)[23]][:,:,2].T.values

    save_ndarray(vlos, save_dir, filename+'_vlos')
    save_ndarray(utc, save_dir, filename+'_utc')

    return vlos, utc #vlos, utc


def save_ndarray(array, save_dir, filename):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    np.save(os.path.join(save_dir, filename), array)
