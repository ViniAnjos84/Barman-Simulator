from core.config import GLASS_SIZE


class Copo:
    def __init__(self, nome, capacidade_ml, imagem, mascara):
        self.nome = nome
        self.capacidade_ml = capacidade_ml
        self.imagem = imagem
        self.mascara = mascara
        self.tamanho = GLASS_SIZE
