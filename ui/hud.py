import os
import pygame

from core.assets import assets
from core.config import DESK_HUD_SIZE, DRINKS_HUD_SIZE, HUD_DIR, ORDER_HUD_SIZE


class HUD:
    def __init__(self):
        self.drinks = assets.image_from(HUD_DIR, "drinks_hud.png", DRINKS_HUD_SIZE)
        self.desk = assets.image_from(HUD_DIR, "desk_hud.png", DESK_HUD_SIZE)
        self.order = assets.image_from(HUD_DIR, "order_hud.png", ORDER_HUD_SIZE)

        self.slot = assets.image_from(HUD_DIR, "slot_hud.png", (90, 110))

    def draw(self, screen):
        screen.blit(self.drinks, (20, 70))
        screen.blit(self.order, (900, 67))
        screen.blit(self.desk, (470, 55))


class GlassView:
    def __init__(self, copo):
        self.copo = copo

    def draw(self, screen, position):
        image = assets.image(self.copo.imagem, self.copo.tamanho)
        screen.blit(image, position)

    def mask(self):
        return assets.transparency_mask(self.copo.mascara, self.copo.tamanho)


class DrinkView:
    def draw(self, screen, ingrediente, position, size=(300, 300), rotation=90):
        image = assets.image(ingrediente.icone, size, rotation)
        screen.blit(image, position)


class MlBar:
    def __init__(self, width=20, height=200):
        self.width = width
        self.height = height

    def draw(self, screen, ml, capacidade_ml, position):
        x, y = position
        pygame.draw.rect(screen, (100, 100, 100), (x, y, self.width, self.height))

        if capacidade_ml <= 0:
            return

        proporcao = min(max(ml / capacidade_ml, 0), 1)
        preenchida = int(self.height * proporcao)

        pygame.draw.rect(
            screen,
            (200, 50, 50),
            (x, y + self.height - preenchida, self.width, preenchida),
        )
