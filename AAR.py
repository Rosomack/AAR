# -*- coding: utf-8 -*-

from PIL import Image
import os
from Assets import Asset

asset = Asset.open_asset("test.png", Asset.XHDPI)
asset.downscale(Asset.HDPI).save("debug/out-png-hdpi.png")
asset.downscale(Asset.MDPI).save("debug/out-png-mdpi.png")
asset.downscale(Asset.LDPI).save("debug/out-png-ldpi.png")

asset = Asset.open_asset("test.9.png", Asset.XHDPI)
asset.downscale(Asset.HDPI).save("debug/out-png-hdpi.9.png")
asset.downscale(Asset.MDPI).save("debug/out-png-mdpi.9.png")
asset.downscale(Asset.LDPI).save("debug/out-png-ldpi.9.png")