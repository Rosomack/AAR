# -*- coding: utf-8 -*-
"""
Class definitions to abstract the common operations on 9-patches and normal
images.
"""
import os
from PIL import Image
import copy

class Asset:
    XHDPI = 320
    HDPI = 240
    MDPI = 160
    LDPI = 120
    
    def __init__(self, file_path, image_dpi):
        self.img = Image.open(file_path)
        self.filename = os.path.split(file_path)[1]
        self.dpi = image_dpi
        
    def clone(self, other):
        new_asset = copy.deepcopy(self)
        new_asset.img = self.img
        new_asset.filename = self.filename
        new_asset.dpi = self.dpi
        
    def downscale(self, to_dpi):
        scale = float(to_dpi) / self.dpi   
        new_size = (self.img.size[0] * scale, self.img.size[1] * scale)
        self.img = self.img.resize(new_size, "ANTIALIAS")
        
    @staticmethod
    def open_asset(path, dpi):
        if Asset.check_ninepatch(path):
            return NinePatchAsset(path, dpi)
        else:
            return Asset(path, dpi)
            
    @staticmethod
    def check_ninepatch(path):
        full_ext = ''
        for root, ext in os.path.splitext(path):
            full_ext = full_ext + ext
            if len(ext) == 0:
                break
        if '.9' in full_ext:
            return True
        else:
            return False
    

class NinePatchAsset(Asset):
    def __init__(self, file_dpi):
        Asset.__init__(file_dpi)
    def downscale(self):
        pass
 