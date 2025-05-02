# D:\code\python\obstacle.py
import pygame
import os
import random
from define import GROUND_Y, BIRD_Y, OBSTACLE_SPEED_FACTOR, ASSET_PATH, WIDTH

def load_and_scale(path, scale):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (
        int(img.get_width() * scale),
        int(img.get_height() * scale)
    ))

class ObstacleAssets:
    def __init__(self):
        self.Baryonyx = [load_and_scale(os.path.join(f'{ASSET_PATH}/Baryonyx', f'Walk_00{i}.png'), 0.20) for i in range(9)]
        self.Styracosaurus = [load_and_scale(os.path.join(f'{ASSET_PATH}/Styracosaurus', f'Attack_00{i}.png'), 0.08) for i in range(6)]
        self.Alanqa = [load_and_scale(os.path.join(f'{ASSET_PATH}/Alanqa', f'Fly_00{i}.png'), 0.20) for i in range(4)]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, kind, assets):
        super().__init__()
        self.assets = assets

        if kind == 'ground':
            self.images = random.choice([self.assets.Baryonyx, self.assets.Styracosaurus])
            y = GROUND_Y
        else:
            self.images = self.assets.Alanqa
            y = BIRD_Y

        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=(WIDTH + 50, y))
        self.mask = pygame.mask.from_surface(self.image)  # Tạo mask ngay khi khởi tạo

        self.index = 0
        self.kind = kind

    def update(self, player_speed):
        move_dist = player_speed * OBSTACLE_SPEED_FACTOR
        self.rect.x -= move_dist

        self.index = (self.index + 0.1) % len(self.images)
        self.image = self.images[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)  # Cập nhật mask khi thay đổi ảnh

        if self.rect.right < 0:
            self.kill()