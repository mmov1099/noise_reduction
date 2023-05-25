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

## Noise2Noise
### gaussian noise
The noise parameter is the maximum standard deviation σ.

for training
```
python scripts/noise2noise/train.py \
  --train-dir data/fitacf/hok/2017 --train-size 1000 \
  --valid-dir data/fitacf/hok/2017 --valid-size 200 \
  --ckpt-save-path ckpts \
  --nb-epochs 10 \
  --batch-size 1 \
  --loss l2 \
  --noise-type gaussian \
  --noise-param 50 \
  --plot-stats \
  --cuda \
  --clean-targets \
  --ckpt-overwrite
```

```bash
python scripts/noise2noise/test.py \
  --data data/fitacf/hok/2017 \
  --load-ckpt ckpts/gaussian-clean/n2n-gaussian.pt \
  --noise-type gaussian \
  --noise-param 50 \
  --crop-size 256 \
  --show-output 3 \
  --cuda
```
### poisson noise
The noise parameter is the Poisson parameter λ.
```
python3 train.py
  --loss l2 \
  --noise-type poisson \
  --noise-param 50 \
  --cuda
```
### test
```
python3 test.py \
  --data ../data \
  --load-ckpt ../ckpts/gaussian/n2n.pt \
  --noise-type gaussian \
  --noise-param 50 \
  --crop-size 256 \
  --show-output 3 \
  --cuda
```

## download data
```bash
pwd # noise_reduction
python scripts/download_data.py --names ['hok'] --years [2017]
```

You can download multiple radar names and years in the list.

See [here](https://ergsc.isee.nagoya-u.ac.jp/data/ergsc/ground/radar/sd/) for radar names and the years you can obtain.
