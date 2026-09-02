import os

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
FPS = 60
WINDOW_TITLE = "Barman Game"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

BACKGROUND_PATH = os.path.join(IMAGE_DIR, "background", "background.png")
HUD_DIR = os.path.join(IMAGE_DIR, "hud")
DRINKS_DIR = os.path.join(IMAGE_DIR, "drinks")
GLASSES_DIR = os.path.join(IMAGE_DIR, "glasses")

DRINKS_HUD_SIZE = (460, 500)
DESK_HUD_SIZE = (460, 560)
ORDER_HUD_SIZE = (300, 515)

SLOT_SIZE = (90, 110)
SLOT_ICON_SIZE = (75, 75)
SLOT_GAP = 3
SLOT_COLUMNS = 4
SLOT_ROWS = 3
SLOTS_PER_PAGE = SLOT_COLUMNS * SLOT_ROWS

GLASS_SIZE = (200, 200)
GLASS_POSITION = (600, 330)
DRINK_ICON_SIZE = (300, 300)
DRINK_POSITION = (550, 30)
ML_BAR_POSITION = (820, 330)
ML_BAR_SIZE = (20, 200)

# Velocidade original de preenchimento: 40 ml/s após 600 ms.
FILL_DELAY_MS = 600
FILL_SPEED_ML_PER_SECOND = 40
GRADIENT_HEIGHT = 15
