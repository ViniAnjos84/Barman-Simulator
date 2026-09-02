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

        largura, altura = bebida.copo.tamanho
        capacidade = bebida.copo.capacidade_ml
        ml_total = min(bebida.ml_atual, capacidade)

        if capacidade <= 0 or ml_total <= 0:
            return

        mask = assets.transparency_mask(bebida.copo.mascara, bebida.copo.tamanho)
        acumulado = 0

        for item in bebida.ingredientes:
            inicio = altura - int(
                altura * (acumulado + item.quantidade_ml) / capacidade
            )
            fim = altura - int(altura * acumulado / capacidade)
            inicio = max(0, inicio)
            fim = min(altura, fim)

            if fim <= inicio:
                acumulado += item.quantidade_ml
                continue

            camada = pygame.Surface((largura, altura), pygame.SRCALPHA)
            camada.fill((*item.ingrediente.cor, 255))

            # Aplica a máscara transparente do interior do copo.
            camada.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            # Mantém somente a faixa correspondente à quantidade deste ingrediente.
            camada.fill((0, 0, 0, 0), (0, 0, largura, inicio))
            camada.fill((0, 0, 0, 0), (0, fim, largura, altura - fim))

            screen.blit(camada, position)
            acumulado += item.quantidade_ml
