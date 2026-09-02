import pygame

from core.assets import assets


class CopoView:
    def __init__(self, copo):
        self.copo = copo

    def draw(self, screen, position):
        image = assets.image(self.copo.imagem, self.copo.tamanho)
        screen.blit(image, position)

    def mask(self):
        return assets.transparency_mask(self.copo.mascara, self.copo.tamanho)
