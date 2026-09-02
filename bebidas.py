import pygame

class Bebida:

    def __init__(self, nome, copo):

        self.nome = nome
        self.copo = copo
        self.ingredientes = []
        self.quantidades = []
        self.ordem = []
        self.preparo = None
        self.personalizacoes = []
        self.ml_atual = 0

    def adicionar_ingrediente(self, ingrediente, quantidade):

        self.ingredientes.append(ingrediente)
        self.quantidades.append(quantidade)
        self.ordem.append(ingrediente)

    def salvar_quantidade(self, tempo_inicio):

        ATRASO = 600
        VELOCIDADE = 40

        tempo = pygame.time.get_ticks() - tempo_inicio

        if tempo <= ATRASO:
            return

        tempo_enchendo = tempo - ATRASO

        quantidade = tempo_enchendo * VELOCIDADE / 1000

        indice = len(self.quantidades) - 1

        self.quantidades[indice] += quantidade
        self.ml_atual += quantidade

        if self.ml_atual > self.copo.ml_copo:

            excesso = self.ml_atual - self.copo.ml_copo

            self.quantidades[indice] -= excesso
            self.ml_atual = self.copo.ml_copo

class Alcoolico:

    def __init__(self, nome, icone, cor):
        self.nome = nome
        self.icone = "images/drinks/alcoholic_drinks/"+icone
        self.cor = cor

vodka = Alcoolico(
    "Vodka",
    "vodka.png",
    (235, 235, 235)
)

gin = Alcoolico(
    "Gin",
    "gin.png",
    (210, 230, 220)
)

cachaca = Alcoolico(
    "Cachaça",
    "cachaca.png",
    (245, 245, 245)
)

rum = Alcoolico(
    "Rum",
    "rum.png",
    (180, 90, 40)
)

whisky = Alcoolico(
    "Whisky",
    "whisky.png",
    (200, 120, 50)
)

tequila = Alcoolico(
    "Tequila",
    "tequila.png",
    (255, 180, 20)
)

alcoolicos = [
    vodka,
    gin,
    cachaca,
    rum,
    whisky,
    tequila
]
