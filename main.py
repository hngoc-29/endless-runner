import pygame
import random
from define import *
from logic import draw, game_over, draw_score, main_menu
from player import Player
from obstacle import Obstacle, ObstacleAssets

# Khởi tạo Pygame và font chỉ một lần
pygame.init()
pygame.font.init()

# Tạo cửa sổ game
WINDOWGAME = pygame.display.set_mode((WIDTH, HEIGHT))

# Thông tin game
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load(programIcon))

# Tải và scale background
BACKGROUND_IMAGE = pygame.image.load(backgroundImage).convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, WINDOWGAME.get_size())

#audio
pygame.mixer.init()
pygame.mixer.music.load(backgroundSound)
pygame.mixer.music.set_volume(0.3 if SOUND_BG else 0)
pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền liên tục

# Âm thanh hiệu ứng
jump_sound = pygame.mixer.Sound(jumpSound)
leverup_sound = pygame.mixer.Sound(leverUpSound)
fail_sound = pygame.mixer.Sound(failSound)

# Tạo đối tượng nhân vật
player = Player(WIDTH // 4, HEIGHT - 100, IMAGE_PATH, jump_sound)  # Cập nhật đường dẫn ảnh
player_group = pygame.sprite.Group(player)

# Thiết lập âm lượng hiệu ứng
jump_sound.set_volume(0.5)
leverup_sound.set_volume(0.7)
fail_sound.set_volume(0.7)

# nhóm obstacles
obstacle_assets = ObstacleAssets()
obstacles = pygame.sprite.Group()

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, OBSTACLE_SPAWN_INTERVAL)

WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 48)

# Gọi menu chính
main_menu(WINDOWGAME, BACKGROUND_IMAGE, font, pygame.mixer, player)

clock = pygame.time.Clock()
score = 0
last_score_time = pygame.time.get_ticks()
isProgramRun = True
while isProgramRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isProgramRun = False
        elif event.type == SPAWN_EVENT and not is_dead:
            kind = random.choice(['ground', 'bird'])
            obs = Obstacle(kind, obstacle_assets)
            obstacles.add(obs)

    if not is_dead:
        keys = pygame.key.get_pressed()
        player_group.update(keys)
        obstacles.update(player.speed)

        draw(WINDOWGAME, BACKGROUND_IMAGE, player.speed)
        player_group.draw(WINDOWGAME)
        obstacles.draw(WINDOWGAME)

        # Kiểm tra va chạm
        for o in obstacles:
            if pygame.sprite.collide_mask(player, o):
                is_dead = True
                if player.sound_ht:
                    fail_sound.play()
                result = game_over(WINDOWGAME, int(score))
                if result == 'restart':
                    obstacles.empty()
                    score = 0
                    last_score_time = pygame.time.get_ticks()
                    is_dead = False
                elif result == 'menu':
                    main_menu(WINDOWGAME, BACKGROUND_IMAGE, font, pygame.mixer, player)
                    obstacles.empty()
                    score = 0
                    last_score_time = pygame.time.get_ticks()
                    is_dead = False
                else:
                    isProgramRun = False
                break
        
        # Tính điểm chỉ khi chưa chết
        current_time = pygame.time.get_ticks()
        min_interval = 100  # không cho nhỏ hơn 200ms (tức 5 điểm/s)
        interval = max(1000 / player.speed, min_interval)

        if current_time - last_score_time >= interval:
            score += 1
            last_score_time = current_time
            if(player.sound_ht and score % 100 == 0):
                leverup_sound.play()

    draw_score(WINDOWGAME, score, pygame.font.SysFont(None, 36))

    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.0f}", True, WHITE)
    WINDOWGAME.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
