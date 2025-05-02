# D:\code\python\logic.py
import pygame
import os

from define import WIDTH, HEIGHT, ROOT_PATH
import define

bg1_x = 0
bg2_x = None  # Đặt là None để khởi tạo đúng 1 lần duy nhất

def draw(screen, BACKGROUND_IMAGE, player_speed):
    global bg1_x, bg2_x

    width = BACKGROUND_IMAGE.get_width()

    # Chỉ gán lại bg2_x nếu chưa gán lần nào
    if bg2_x is None:
        bg2_x = width

    # Di chuyển ảnh nền theo tốc độ của nhân vật
    bg1_x -= player_speed * 0.05  # Tăng tốc độ nền theo tốc độ nhân vật
    bg2_x -= player_speed * 0.05  # Tăng tốc độ nền theo tốc độ nhân vật

    # Nếu ảnh nền ra khỏi màn hình thì đặt lại vị trí nối tiếp
    if bg1_x <= -width:
        bg1_x = bg2_x + width
    if bg2_x <= -width:
        bg2_x = bg1_x + width

    # Vẽ 2 nền để nối nhau
    screen.blit(BACKGROUND_IMAGE, (bg1_x, 0))
    screen.blit(BACKGROUND_IMAGE, (bg2_x, 0))

# Đọc high score từ file
def read_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, 'r') as f:
        try:
            return int(f.read())
        except:
            return 0

HIGH_SCORE_FILE = os.path.join(os.getcwd(), 'assets\\highscore.txt')
# Ghi high score vào file
def write_high_score(score):
    # Tạo thư mục nếu chưa có
    os.makedirs(os.path.dirname(HIGH_SCORE_FILE), exist_ok=True)
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score))

# Hàm hiển thị màn hình Game Over, Score và High Score
def game_over(screen, score):
    # Đọc high score cũ
    high_score = read_high_score()
    if score > high_score:
        high_score = score
        write_high_score(high_score)

    # Thiết lập font
    title_font = pygame.font.SysFont(None, 72)
    info_font = pygame.font.SysFont(None, 36)

    # Tạo text
    title_surf = title_font.render('GAME OVER', True, (255, 0, 0))
    score_surf = info_font.render(f'Score: {score}', True, (255, 255, 255))
    high_surf = info_font.render(f'High Score: {high_score}', True, (255, 255, 0))
    prompt_surf = info_font.render('Press R to Restart or Q to Quit', True, (255, 255, 255))

    # Vị trí văn bản
    center_x, center_y = screen.get_width() // 2, screen.get_height() // 2
    title_rect = title_surf.get_rect(center=(center_x, center_y - 80))
    score_rect = score_surf.get_rect(center=(center_x, center_y - 20))
    high_rect = high_surf.get_rect(center=(center_x, center_y + 20))
    prompt_rect = prompt_surf.get_rect(center=(center_x, center_y + 80))

    clock = pygame.time.Clock()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                if event.key == pygame.K_q:
                    waiting = False
                    return 'menu'
            if event.type == pygame.QUIT:
                waiting = False
                return 'quit'

        screen.blit(title_surf, title_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(high_surf, high_rect)
        screen.blit(prompt_surf, prompt_rect)
        pygame.display.flip()
        clock.tick(15)

def draw_score(screen, score, color=(255, 255, 255)):
    high_score = read_high_score()
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {int(score)}/{high_score}", True, color)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

def main_menu(screen, background_image, font, bgSound, player):
    clock = pygame.time.Clock()
    high_score = read_high_score()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    define.SOUND_BG = not define.SOUND_BG
                    bgSound.music.set_volume(0.2 if define.SOUND_BG else 0)
                elif event.key == pygame.K_s:
                    player.sound_ht = not player.sound_ht
                elif event.key == pygame.K_SPACE:
                    waiting = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

        screen.blit(background_image, (0, 0))

        title_text = font.render("RUN DINO RUN", True, (255, 255, 255))
        instruction_text = font.render("Press space to start", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {int(high_score)}", True, (255, 255, 0))
        bg_music_text = font.render(f"[M] BGM: {'ON' if define.SOUND_BG else 'OFF'}", True, (100, 200, 255))
        sfx_text = font.render(f"[S] SFX: {'ON' if player.sound_ht else 'OFF'}", True, (100, 255, 100))

        screen.blit(title_text, title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4)))
        screen.blit(instruction_text, instruction_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
        screen.blit(high_score_text, high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50)))
        screen.blit(bg_music_text, (20, screen.get_height() - 80))
        screen.blit(sfx_text, (20, screen.get_height() - 40))

        pygame.display.flip()
        clock.tick(define.FPS)
