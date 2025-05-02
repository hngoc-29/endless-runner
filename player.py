import pygame
import os
from define import PLAYER_SPEED, PLAYER_MAX_SPEED, WIDTH, HEIGHT, PLAYER_SPEED_INCREMENT

scale_factor = 0.5  # Giảm kích thước nhân vật

def load_and_scale(path):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (
        int(img.get_width() * scale_factor),
        int(img.get_height() * scale_factor)
    ))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, soundJump):
        super().__init__()

        # Load các ảnh
        self.standing_images = [load_and_scale(os.path.join(image_path, 'nvbo.png'))]
        self.running_images = [load_and_scale(os.path.join(image_path, f'nvrun{i}.png')) for i in range(1, 7)]
        self.jumping_images = [load_and_scale(os.path.join(image_path, f'jump{i}.png')) for i in range(1, 3)]

        self.image = self.running_images[0]
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.mask = pygame.mask.from_surface(self.image)  # Tạo mask ngay khi khởi tạo

        self.speed = PLAYER_SPEED
        self.max_speed = PLAYER_MAX_SPEED
        self.gravity = 1
        self.jump_velocity = 12

        self.index = 0
        self.current_state = 'running'
        self.is_jumping = False
        self.is_crouching = False

        self.last_speed_increase_time = pygame.time.get_ticks()

        self.jump_sound = soundJump
        self.sound_ht = True

    def update(self, keys):
        # Nhảy
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = False
            self.update_jumping(keys)
            self.jump_velocity = 12
            self.current_state = 'jumping'

        # Ngồi
        self.is_crouching = keys[pygame.K_DOWN] or keys[pygame.K_s]

        # Tăng tốc
        current_time = pygame.time.get_ticks()

        # Kiểm tra xem đã 5 giây chưa để tăng tốc
        if current_time - self.last_speed_increase_time >= 5000:  # 5000ms = 5 giây
            if self.speed < self.max_speed:
                self.speed += PLAYER_SPEED_INCREMENT
            self.last_speed_increase_time = current_time  # Cập nhật thời gian tăng tốc

        # Cập nhật trạng thái
        if self.is_jumping:
            self.update_jumping(keys)
        elif self.is_crouching:
            self.update_crouching()
        else:
            self.update_running()

    def update_running(self):
        self.current_state = 'running'
        self.index += 0.08
        if self.index >= len(self.running_images):
            self.index = 0

        midbottom = self.rect.midbottom
        self.image = self.running_images[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)  # Cập nhật mask khi thay đổi ảnh
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom

    def update_jumping(self, keys):
        # Nếu đang nhảy lên
        if self.jump_velocity > 0:
            self.image = self.jumping_images[0]  # jump1.png
        else:
            self.image = self.jumping_images[1]  # jump2.png

        # Điều chỉnh trọng lực khi giữ SPACE
        gravity_effect = 0.5 if keys[pygame.K_SPACE] else self.gravity
        self.rect.y -= self.jump_velocity
        self.jump_velocity -= gravity_effect
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_velocity = 12
            self.current_state = 'jumping'
            if self.sound_ht:
                self.jump_sound.play()

        # Khi chạm đất
        if self.rect.bottom >= HEIGHT - 100:
            self.rect.bottom = HEIGHT - 100
            self.is_jumping = False
            self.jump_velocity = 12
            self.current_state = 'running'

    def update_crouching(self):
        self.current_state = 'crouching'
        midbottom = self.rect.midbottom
        self.image = self.standing_images[0]
        self.mask = pygame.mask.from_surface(self.image)  # Cập nhật mask khi thay đổi ảnh
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom

        self.rect.height -= 10
        self.rect.y += 10

