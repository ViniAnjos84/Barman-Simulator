import pygame
import os
from bebidas import Alcoolico  #, Energetico
from utils import carregar_imagem

class SlotItem:

    def __init__(self, itens, x, y, pagina=1):
        self.itens = itens
        self.pagina = pagina
        self.itens_por_pagina = 12

        self.colunas = 4
        self.linhas = 3

        self.largura = 90
        self.altura = 110
        self.espaco = 3

        self.x = x
        self.y = y

        self.slot_hud = pygame.image.load(
            os.path.join("images", "hud", "slot_hud.png")
        ).convert_alpha()

        self.slot_hud = pygame.transform.scale(
            self.slot_hud,
            (self.largura, self.altura)
        )

    def mostrar(self, tela):

        inicio = (self.pagina - 1) * self.itens_por_pagina
        fim = inicio + self.itens_por_pagina

        itens_pagina = self.itens[inicio:fim]

        for i, item in enumerate(itens_pagina):

            coluna = i % self.colunas
            linha = i // self.colunas

            x = self.x + coluna * (self.largura + self.espaco)
            y = self.y + linha * (self.altura + self.espaco)

            tela.blit(self.slot_hud, (x, y))

            icone = carregar_imagem(
                item.icone,
                (75, 75)
            )

            tela.blit(
                icone,
                (
                    x + (self.largura - 75) // 2,
                    y + (self.altura - 90) // 2
                )
            )

    def verificar_clique(self, pos_mouse):

        inicio = (self.pagina - 1) * self.itens_por_pagina
        fim = inicio + self.itens_por_pagina

        itens_pagina = self.itens[inicio:fim]

        for i, item in enumerate(itens_pagina):

            coluna = i % self.colunas
            linha = i // self.colunas

            x = self.x + coluna * (self.largura + self.espaco)
            y = self.y + linha * (self.altura + self.espaco)

            slot = pygame.Rect(
                x,
                y,
                self.largura,
                self.altura
            )

            if slot.collidepoint(pos_mouse):

                if isinstance(item, (Alcoolico)):  #, Energetico)):
                    print(f"Item clicado: {item.nome}")
                    return item

        return None