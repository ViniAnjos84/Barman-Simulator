import pygame

from core.assets import assets
from core.config import (
    SLOT_COLUMNS,
    SLOT_GAP,
    SLOT_ICON_SIZE,
    SLOT_ROWS,
    SLOT_SIZE,
    SLOTS_PER_PAGE,
)


class SlotGrid:
    def __init__(self, itens, x, y, pagina=1):
        self.itens = itens
        self.x = x
        self.y = y
        self.pagina = pagina

        self.colunas = SLOT_COLUMNS
        self.linhas = SLOT_ROWS
        self.itens_por_pagina = SLOTS_PER_PAGE
        self.largura, self.altura = SLOT_SIZE
        self.espaco = SLOT_GAP
        self.slot_image = None

    def set_slot_image(self, image):
        self.slot_image = image

    def _itens_visiveis(self):
        inicio = (self.pagina - 1) * self.itens_por_pagina
        return self.itens[inicio:inicio + self.itens_por_pagina]

    def _rect(self, indice):
        coluna = indice % self.colunas
        linha = indice // self.colunas
        x = self.x + coluna * (self.largura + self.espaco)
        y = self.y + linha * (self.altura + self.espaco)
        return pygame.Rect(x, y, self.largura, self.altura)

    def draw(self, screen):
        for indice, item in enumerate(self._itens_visiveis()):
            rect = self._rect(indice)

            if self.slot_image:
                screen.blit(self.slot_image, rect)

            icon = assets.image(item.icone, SLOT_ICON_SIZE)
            icon_x = rect.x + (self.largura - icon.get_width()) // 2
            icon_y = rect.y + (self.altura - 90) // 2
            screen.blit(icon, (icon_x, icon_y))

    def item_at(self, mouse_position):
        for indice, item in enumerate(self._itens_visiveis()):
            if self._rect(indice).collidepoint(mouse_position):
                return item
        return None
