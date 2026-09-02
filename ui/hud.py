import pygame

from core.assets import assets
from core.config import DESK_HUD_SIZE, DRINKS_HUD_SIZE, HUD_DIR, ORDER_HUD_SIZE, SLOT_SIZE


class HUD:
    def __init__(self):
        self.drinks = assets.image_from(HUD_DIR, "drinks_hud.png", DRINKS_HUD_SIZE)
        self.desk = assets.image_from(HUD_DIR, "desk_hud.png", DESK_HUD_SIZE)
        self.order = assets.image_from(HUD_DIR, "order_hud.png", ORDER_HUD_SIZE)
        self.slot = assets.image_from(HUD_DIR, "slot_hud.png", SLOT_SIZE)

    def draw(self, screen):
        screen.blit(self.drinks, (20, 70))
        screen.blit(self.order, (900, 67))
        screen.blit(self.desk, (470, 55))
