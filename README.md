# 研究用
## clone repository
```bash
git clone --recursive https://github.com/mmov1099/noise_reduction.git
```
## install openexr
```bash
git clone https://github.com/AcademySoftwareFoundation/openexr.git && \
mkdir build_directory && cd build_directory && \
cmake ../openexr && \
make && sudo make install && \
cd .. && rm -rf openexr && rm -rf openexr build_directory
```
こっち？
```bash
sudo apt-get install libopenexr-dev
pip install OpenEXR
```
いや，こっち？
```bash
pip install git+https://github.com/jamesbowman/openexrpython.git
sudo apt-get install -y openexr
```
## install torch
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```

## download data
```bash
pwd #noise_reduction
python scripts/download_data.py --names ['hok'] --years [2017]
```

You can download multiple radar names and years in the list.

See [here](https://ergsc.isee.nagoya-u.ac.jp/data/ergsc/ground/radar/sd/) for radar names and the years you can obtain them.