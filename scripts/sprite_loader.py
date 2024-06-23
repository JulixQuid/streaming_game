import pygame
import cv2

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
