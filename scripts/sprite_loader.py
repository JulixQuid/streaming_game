import pygame
import cv2
import os

class SpriteLoader:
    
    @staticmethod
    def load_sprites_fixed_size(image_path, fixed_w, fixed_h):
        sprite_sheet = pygame.image.load(image_path)
        sprites = []
        y=0
        for x in range(0, sprite_sheet.get_width(), fixed_w):
            if x + fixed_w <= sprite_sheet.get_width() and y + fixed_h <= sprite_sheet.get_height():
                sprite = sprite_sheet.subsurface(pygame.Rect(x, y, fixed_w, fixed_h))
                sprites.append(sprite)
            else:
                print(f"Warning: Subsurface rectangle at ({x}, {y}, {fixed_w}, {fixed_h}) outside surface area.")
        return sprites

    @staticmethod
    def load_all_characters(assets_path,sizes=None):
        all_characters = {}
        folders = os.listdir(os.path.join(assets_path,"characters"))
        for folder in folders:
            sprite_sheets = os.listdir(os.path.join(assets_path,"characters",folder))
            if sizes is not None:
                w,h = sizes[folder]
            else:
                w,h = 48,48 
            all_characters[folder] = {}
            for sheet in sprite_sheets:
                path_sheet = os.path.join(assets_path,"characters",folder,sheet)
                all_characters[folder][sheet.split('.')[0]] = SpriteLoader.load_sprites_fixed_size(path_sheet,48,48)
        return all_characters

