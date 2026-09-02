import pygame
from utils import *

class Copo:

    def __init__(self, nome, ml, imagem, mascara):
        self.nome = nome
        self.ml_copo = ml
        self.imagem = "images/glasses/"+imagem
        self.mascara = "images/glasses/"+mascara
        self.x = 200
        self.y = 200

    def desenhar_copo(self, tela, x, y):

        imagem = pygame.image.load(self.imagem).convert_alpha()
        imagem = pygame.transform.scale(imagem, (self.x, self.y))
        tela.blit(imagem, (x, y))

copo_baixo = Copo("Copo Baixo", 300, "copo_baixo.png", "copo_baixo_mask.png")
mascara = pygame.image.load(copo_baixo.mascara)
mascara = pygame.transform.scale(mascara, (copo_baixo.x, copo_baixo.y))
imagens[copo_baixo.mascara] = mascara