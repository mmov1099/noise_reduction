#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
from unet_parts import *
from pytorch_memlab import profile

class UNet(nn.Module):
    """Custom U-Net architecture for Noise2Noise (see Appendix, Table 2)."""

    def __init__(self, in_channels=1, out_channels=1):
        """Initializes U-Net."""

        super(UNet, self).__init__()

        # # Layers: enc_conv0, enc_conv1, pool1
        # self._block1 = nn.Sequential(
        #     nn.Conv2d(in_channels, 48, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.Conv2d(48, 48, 3, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.MaxPool2d(2))

        # # Layers: enc_conv(i), pool(i); i=2..5
        # self._block2 = nn.Sequential(
        #     nn.Conv2d(48, 48, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.MaxPool2d(2))

        # # Layers: enc_conv6, upsample5
        # self._block3 = nn.Sequential(
        #     nn.Conv2d(48, 48, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.ConvTranspose2d(48, 48, 3, stride=2, padding=1, output_padding=1))
        #     #nn.Upsample(scale_factor=2, mode='nearest'))

        # # Layers: dec_conv5a, dec_conv5b, upsample4
        # self._block4 = nn.Sequential(
        #     nn.Conv2d(96, 96, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.Conv2d(96, 96, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.ConvTranspose2d(96, 96, 3, stride=2, padding=1, output_padding=1))
        #     #nn.Upsample(scale_factor=2, mode='nearest'))

        # # Layers: dec_deconv(i)a, dec_deconv(i)b, upsample(i-1); i=4..2
        # self._block5 = nn.Sequential(
        #     nn.Conv2d(144, 96, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.Conv2d(96, 96, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.ConvTranspose2d(96, 96, 3, stride=2, padding=1, output_padding=1))
        #     #nn.Upsample(scale_factor=2, mode='nearest'))

        # # Layers: dec_conv1a, dec_conv1b, dec_conv1c,
        # self._block6 = nn.Sequential(
        #     nn.Conv2d(96 + in_channels, 64, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.Conv2d(64, 32, 3, stride=1, padding=1),
        #     nn.ReLU(inplace=True),
        #     nn.Conv2d(32, out_channels, 3, stride=1, padding=1),
        #     nn.LeakyReLU(0.1))

        bilinear = False
        self.n_channels = in_channels
        self.n_classes = out_channels
        self.bilinear = bilinear

        self.inc = (DoubleConv(in_channels, 64))
        self.down1 = (Down(64, 128))
        self.down2 = (Down(128, 256))
        self.down3 = (Down(256, 512))
        factor = 2 if bilinear else 1
        self.down4 = (Down(512, 1024 // factor))
        self.up1 = (Up(1024, 512 // factor, bilinear))
        self.up2 = (Up(512, 256 // factor, bilinear))
        self.up3 = (Up(256, 128 // factor, bilinear))
        self.up4 = (Up(128, 64, bilinear))
        self.outc = (OutConv(64, out_channels))

        # Initialize weights
        # self._init_weights()


    def _init_weights(self):
        """Initializes weights using He et al. (2015)."""

        for m in self.modules():
            if isinstance(m, nn.ConvTranspose2d) or isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight.data)
                m.bias.data.zero_()


    # def forward(self, x):
    #     """Through encoder, then decoder by adding U-skip connections. """

    #     # Encoder
    #     pool1 = self._block1(x)
    #     pool2 = self._block2(pool1)
    #     pool3 = self._block2(pool2)
    #     pool4 = self._block2(pool3)
    #     pool5 = self._block2(pool4)
    #     print()
    #     print('x',x.shape)
    #     print('pool1',pool1.shape)
    #     print('pool2',pool2.shape)
    #     print('pool3',pool3.shape)
    #     print('pool4',pool4.shape)
    #     print('pool5',pool5.shape)

    #     # Decoder
    #     upsample5 = self._block3(pool5)
    #     print('upsample5',upsample5.shape)
    #     concat5 = torch.cat((upsample5, pool4), dim=1)
    #     upsample4 = self._block4(concat5)
    #     print('upsample4',upsample4.shape)
    #     concat4 = torch.cat((upsample4, pool3), dim=1)
    #     upsample3 = self._block5(concat4)
    #     concat3 = torch.cat((upsample3, pool2), dim=1)
    #     upsample2 = self._block5(concat3)
    #     concat2 = torch.cat((upsample2, pool1), dim=1)
    #     upsample1 = self._block5(concat2)
    #     concat1 = torch.cat((upsample1, x), dim=1)

    #     # Final activation
    #     return self._block6(concat1)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        logits = self.outc(x)
        return logits
