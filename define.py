import os

WIDTH, HEIGHT = 1000, 500

TITLE = 'RUNNER'

ROOT_PATH = os.path.dirname(__file__)
ASSET_PATH = os.path.join(ROOT_PATH, 'assets')

IMAGE_PATH = os.path.join(ASSET_PATH, 'images')

programIcon = os.path.join(IMAGE_PATH, 'logoGame.ico')
backgroundImage = os.path.join(IMAGE_PATH, 'background.png')

SOUNDS_PATH = os.path.join(ASSET_PATH, 'sounds')
backgroundSound = os.path.join(SOUNDS_PATH, 'background.mp3')
jumpSound = os.path.join(SOUNDS_PATH, 'jump.wav')
leverUpSound = os.path.join(SOUNDS_PATH, 'leverup.wav')
failSound = os.path.join(SOUNDS_PATH, 'fail.wav')
SOUND_BG = True   # Background music

FPS = 60

# Thông số về nhân vật
PLAYER_START_X = 100  # Vị trí xuất phát của nhân vật (trục X)
PLAYER_START_Y = 600  # Vị trí xuất phát của nhân vật (trục Y)
PLAYER_JUMP_VELOCITY = 15  # Vận tốc ban đầu khi nhảy
PLAYER_GRAVITY = 0.8  # Trọng lực áp dụng khi rơi
PLAYER_MAX_SPEED = 250  # Tốc độ tối đa của nhân vật
PLAYER_SPEED = 90  # Tốc độ di chuyển của nhân vật
PLAYER_SPEED_INCREMENT = 3 #Tăng speed

# Thông số spawn obstacle
OBSTACLE_SPAWN_INTERVAL = 1500   # ms giữa hai lần spawn
GROUND_Y = HEIGHT - 100          # Y của mặt đất
BIRD_Y = HEIGHT - 150            # Y của chim bay
OBSTACLE_SPEED_FACTOR = 0.08      # hệ số nhân với player.speed để di chuyển obstacle

score = 0
is_dead = False
