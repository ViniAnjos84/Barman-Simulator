import pygame
import sys
import os
import huds
from bebidas import *
from copo import *
from utils import *
from slots import SlotItem

LARGURA = 1200
ALTURA = 650
FPS = 60

CAMINHO_BACKGROUND = os.path.join(
    "images",
    "background",
    "background.png"
)

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Barman Game")

relogio = pygame.time.Clock()
tempo_bebida = None
derramando = False

background = pygame.image.load(CAMINHO_BACKGROUND).convert()
background = pygame.transform.scale(
    background,
    (LARGURA, ALTURA)
)

drinks_hud, desk_hud, order_hud = huds.carregar_huds()

drinks_hud = pygame.transform.scale(drinks_hud, (460, 500))
desk_hud = pygame.transform.scale(desk_hud, (460, 560))
order_hud = pygame.transform.scale(order_hud, (300, 515))

slot_item = SlotItem(alcoolicos, x=65, y=160)
item_selecionado = None
copo_selecionado = copo_baixo
mascara_copo = criar_mascara_transparencia(copo_selecionado.mascara, (copo_selecionado.x, copo_selecionado.y))
bebida_atual = Bebida("", copo_selecionado)


rodando = True
while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if derramando:
                        bebida_atual.salvar_quantidade(tempo_bebida)
                        derramando = False

                    else:
                        item = slot_item.verificar_clique(evento.pos)

                        if item:
                            item_selecionado = item
                            tempo_bebida = pygame.time.get_ticks()
                            derramando = True
                            bebida_atual.adicionar_ingrediente(ingrediente=item_selecionado, quantidade=0)

    tela.blit(background, (0, 0))

    tela.blit(drinks_hud, (20, 70))
    tela.blit(order_hud, (900, 67))
    tela.blit(desk_hud, (470, 55))

    slot_item.mostrar(tela)

    if item_selecionado and derramando:
        desenhar_bebida(tela, item_selecionado, x_bebida=550, tempo_inicio=tempo_bebida)

    if len(bebida_atual.ingredientes):
        encher_copo(tela, bebida_atual, mascara_copo, 600, 330, tempo_bebida, derramando)

    copo_selecionado.desenhar_copo(tela, 600, 330)

    desenhar_barra_ml(tela, bebida_atual, x=820, y=330, tempo_inicio=tempo_bebida, derramando=derramando)

    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
sys.exit()