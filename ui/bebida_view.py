import pygame

from core.assets import assets


class BebidaView:
    def draw(self, screen, ingrediente, position, size, rotation=0):
        image = assets.image(ingrediente.icone, size, rotation)
        screen.blit(image, position)

    def draw_liquido(self, screen, bebida, position):
        """Desenha as camadas da bebida dentro do copo, sem animação de derramamento."""
        if not bebida.ingredientes or bebida.copo is None:
            return

        mask = assets.image(bebida.copo.mascara, bebida.copo.tamanho)
        largura, altura = mask.get_size()
        capacidade = bebida.copo.capacidade_ml
        ml_total = min(bebida.ml_atual, capacidade)

        if capacidade <= 0 or ml_total <= 0:
            return

        # A máscara define a área interna do copo. As camadas são desenhadas
        # de baixo para cima respeitando a quantidade de cada ingrediente.
        altura_liquido = int(altura * (ml_total / capacidade))
        topo_liquido = altura - altura_liquido

        acumulado = 0
        for item in bebida.ingredientes:
            camada_altura = int(altura * (item.quantidade_ml / capacidade))
            if camada_altura <= 0:
                continue

            camada = pygame.Surface((largura, altura), pygame.SRCALPHA)
            camada.fill((*item.ingrediente.cor, 255))

            # Mantém somente a faixa correspondente à camada atual.
            inicio = altura - int(altura * (acumulado + item.quantidade_ml) / capacidade)
            fim = altura - int(altura * acumulado / capacidade)
            inicio = max(topo_liquido, inicio)
            fim = max(inicio, fim)

            alpha = pygame.Surface((largura, altura), pygame.SRCALPHA)
            alpha.fill((0, 0, 0, 0))
            alpha.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
            camada.blit(alpha, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            faixa = pygame.Surface((largura, altura), pygame.SRCALPHA)
            faixa.blit(camada, (0, 0))
            faixa.fill((0, 0, 0, 0), (0, 0, largura, inicio))
            faixa.fill((0, 0, 0, 0), (0, fim, largura, altura - fim))
            screen.blit(faixa, position)

            acumulado += item.quantidade_ml
