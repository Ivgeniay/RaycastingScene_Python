import math

# game settings
WIDTH = 1200
HEIGHT = 800
RESOLUTION = (WIDTH, HEIGHT)
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
TITLE = "Kek game"
FPS = 60
TILE = 100

# ray casting setting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 40
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 *DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
player_rot_speed = 0.02

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
COLORS = [WHITE, BLACK, RED, GREEN, BLUE, DARKGRAY, PURPLE]