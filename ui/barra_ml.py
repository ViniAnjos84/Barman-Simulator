import pygame


class BarraML:
    def __init__(self, largura=20, altura=200):
        self.largura = largura
        self.altura = altura

    def draw(self, screen, ml, capacidade_ml, position):
        x, y = position
        pygame.draw.rect(screen, (100, 100, 100), (x, y, self.largura, self.altura))

        if capacidade_ml <= 0:
            return

        proporcao = min(max(ml / capacidade_ml, 0), 1)
        altura_preenchida = int(self.altura * proporcao)

        pygame.draw.rect(
            screen,
            (200, 50, 50),
            (x, y + self.altura - altura_preenchida, self.largura, altura_preenchida),
        )
