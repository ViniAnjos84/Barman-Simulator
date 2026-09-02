import pygame

imagens = {}

def carregar_imagem(caminho, tamanho=None, rotacao=0):

    chave = (caminho, tamanho, rotacao)

    if chave not in imagens:

        imagem = pygame.image.load(caminho).convert_alpha()

        if tamanho:
            imagem = pygame.transform.scale(
                imagem,
                tamanho
            )

        if rotacao:
            imagem = pygame.transform.rotate(
                imagem,
                rotacao
            )

        imagens[chave] = imagem

    return imagens[chave]

def criar_mascara_transparencia(caminho, tamanho):

    mascara = carregar_imagem(caminho, tamanho)

    transparencia = pygame.Surface(
        mascara.get_size(),
        pygame.SRCALPHA
    )

    for x in range(mascara.get_width()):
        for y in range(mascara.get_height()):

            r, g, b, a = mascara.get_at((x, y))

            if r == 255 and g == 255 and b == 255:
                transparencia.set_at(
                    (x, y),
                    (255, 255, 255, 255)
                )
            else:
                transparencia.set_at(
                    (x, y),
                    (255, 255, 255, 0)
                )

    return transparencia

def encontrar_area_liquido(mascara):

    largura, altura = mascara.get_size()

    pixels = pygame.surfarray.array3d(mascara)

    pontos_y = []

    for y in range(altura):
        for x in range(largura):

            r, g, b = pixels[x, y]

            if r > 200 and g > 200 and b > 200:
                pontos_y.append(y)
                break

    if not pontos_y:
        return 0, 0

    topo = min(pontos_y)
    base = max(pontos_y)

    return topo, base

def desenhar_bebida(tela, bebida, x_bebida, tempo_inicio):

    imagem = carregar_imagem(
        bebida.icone,
        (300, 300),
        90
    )

    x = x_bebida + (imagem.get_width() // 2)
    y = 30

    tela.blit(imagem, (x, y))

    x_tampa = x
    y_tampa = y + imagem.get_height() // 2

    tempo = pygame.time.get_ticks() - tempo_inicio

    altura = min(tempo // 3, 310)

    pygame.draw.rect(tela, bebida.cor, (x_tampa - 10, y_tampa, 20, altura))

def encher_copo(tela, bebida, mascara, x, y, tempo_inicio, derramando):

    ATRASO = 600
    VELOCIDADE = 40
    ALTURA_DEGRADE = 15

    altura_copo = mascara.get_height()
    area_liquido = pygame.Surface(mascara.get_size(), pygame.SRCALPHA)
    ml_total = 0

    for i, ingrediente in enumerate(bebida.ordem):
        quantidade = bebida.quantidades[i]

        if i == len(bebida.ordem) - 1 and derramando:
            tempo = pygame.time.get_ticks() - tempo_inicio

            if tempo > ATRASO:
                tempo_enchendo = tempo - ATRASO
                quantidade += (tempo_enchendo * VELOCIDADE / 1000)

        altura = (quantidade / bebida.copo.ml_copo) * altura_copo
        y_liquido = (altura_copo - altura - (ml_total / bebida.copo.ml_copo) * altura_copo)
        pygame.draw.rect(area_liquido, ingrediente.cor, (0, int(y_liquido), mascara.get_width(), int(altura)))

        if i > 0:
            cor_anterior = bebida.ordem[i - 1].cor
            cor_atual = ingrediente.cor
            y_degrade = int(y_liquido + altura - ALTURA_DEGRADE)

            for pixel in range(ALTURA_DEGRADE):
                fator = pixel / ALTURA_DEGRADE
                cor = (
                    int(cor_atual[0] * (1 - fator) + cor_anterior[0] * fator),
                    int(cor_atual[1] * (1 - fator) + cor_anterior[1] * fator),
                    int(cor_atual[2] * (1 - fator) + cor_anterior[2] * fator)
                )

                pygame.draw.line(area_liquido, cor, (0, y_degrade + pixel), (mascara.get_width(), y_degrade + pixel))

        ml_total += quantidade

    area_liquido.blit(mascara, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    tela.blit(area_liquido, (x, y))

def desenhar_barra_ml(tela, bebida, x, y, largura=20, altura=200, tempo_inicio=None, derramando=False):

    ATRASO = 500
    VELOCIDADE = 40

    ml = bebida.ml_atual

    if derramando and tempo_inicio is not None:

        tempo = pygame.time.get_ticks() - tempo_inicio

        if tempo > ATRASO:

            tempo_enchendo = tempo - ATRASO
            ml += tempo_enchendo * VELOCIDADE / 1000

    ml = min(ml, bebida.copo.ml_copo)

    pygame.draw.rect(
        tela,
        (100, 100, 100),
        (x, y, largura, altura)
    )

    proporcao = ml / bebida.copo.ml_copo

    altura_preenchida = int(altura * proporcao)

    pygame.draw.rect(
        tela,
        (200, 50, 50),
        (
            x,
            y + altura - altura_preenchida,
            largura,
            altura_preenchida
        )
    )