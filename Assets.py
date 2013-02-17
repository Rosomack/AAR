# -*- coding: utf-8 -*-
"""
Class definitions to abstract the common operations on 9-patches and normal
images.
"""
import os
from PIL import Image
import copy
import math

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
        new_size = (int(self.img.size[0] * scale), int(self.img.size[1] * scale))
        return self.img.resize(new_size, Image.ANTIALIAS)
        
    @staticmethod
    def open_asset(path, dpi):
        if Asset.check_ninepatch(path):
            return NinePatchAsset(path, dpi)
        else:
            return Asset(path, dpi)
            
    @staticmethod
    def check_ninepatch(path):
        full_ext = ''
        path_tuple = os.path.splitext(path)
        while len(path_tuple[1]):
            full_ext = full_ext + path_tuple[1]
            if len(path_tuple[1]) == 0:
                break
            path_tuple = os.path.splitext(path_tuple[0])
            
        if '.9' in full_ext:
            return True
        else:
            return False
            
            
class NinePatchAsset(Asset):
    def __init__(self, file_path, file_dpi):
        Asset.__init__(self, file_path, file_dpi)
    def downscale(self, to_dpi):
        scale = float(to_dpi) / float(self.dpi) 
        old_size = self.img.size
        new_size = (int(math.floor(old_size[0] * scale)), int(math.floor(old_size[1] * scale)))
        crop_src_rect = (1, 1, old_size[0] - 1, old_size[1] - 1)
        crop_dest_size = (new_size[0] - 2, new_size[1] - 2)
        new_image = Image.new(self.img.mode, new_size) 
        #Resize and paste the center image
        stripped_image = self.img.crop(crop_src_rect)
        stripped_image.load()
        stripped_image = stripped_image.resize(crop_dest_size, Image.ANTIALIAS)
        new_image.paste(stripped_image, (1, 1, new_size[0] - 1, new_size[1] - 1))
        #Resize and paste the left border
        border = self.img.crop((0, 0, 1, old_size[1]))
        border.load()
        border = border.resize((1, new_size[1]))
        new_image.paste(border, (0, 0))
        #Resize and paste the top border
        border = self.img.crop((0, 0, old_size[0], 1))
        border.load()
        border = border.resize((new_size[0], 1))
        new_image.paste(border, (0, 0))
        #Resize and paste the right border
        border = self.img.crop((old_size[0] - 1, 0, old_size[0], old_size[1]))
        border.load()
        border = border.resize((1, new_size[1]))
        new_image.paste(border, (new_size[0] - 1, 0))
        #Resize and paste the bottom border
        border = self.img.crop((0, old_size[1] - 1, old_size[0], old_size[1]))
        border.load()
        border = border.resize((new_size[0], 1))
        new_image.paste(border, (0, new_size[1] - 1))
        return new_image
        
 