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
## torch install
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```