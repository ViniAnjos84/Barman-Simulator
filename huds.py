import pygame
import os

def carregar_huds():
    caminho = os.path.join("images", "hud")

    drinks_hud = pygame.image.load(
        os.path.join(caminho, "drinks_hud.png")
    ).convert_alpha()

    desk_hud = pygame.image.load(
        os.path.join(caminho, "desk_hud.png")
    ).convert_alpha()

    order_hud = pygame.image.load(
        os.path.join(caminho, "order_hud.png")
    ).convert_alpha()

    return drinks_hud, desk_hud, order_hud

def carregar_copos():
    caminho = os.path.join("images", "glasses")
    