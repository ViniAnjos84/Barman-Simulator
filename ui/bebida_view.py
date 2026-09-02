import pygame

from core.assets import assets
from core.config import GRADIENT_HEIGHT


class BebidaView:
    def draw(self, screen, ingrediente, position, size, rotation=0):
        image = assets.image(ingrediente.icone, size, rotation)
        screen.blit(image, position)

    def draw_fluxo(self, screen, ingrediente, position, size, tempo_inicio):
        """Desenha o fluxo visual enquanto o ingrediente está sendo adicionado."""
        image = assets.image(ingrediente.icone, size, 90)
        x = position[0] + image.get_width() // 2
        y = position[1] + image.get_height() // 2

        tempo = pygame.time.get_ticks() - tempo_inicio
        altura = min(tempo // 3, 310)
        pygame.draw.rect(screen, ingrediente.cor, (x - 10, y, 20, altura))

    def draw_liquido(
        self,
        screen,
        bebida,
        position,
        quantidade_em_andamento=0,
    ):
        """Desenha o líquido por volume, com degradê entre ingredientes consecutivos."""
        if not bebida.ingredientes or bebida.copo is None:
            return

        largura, altura_copo = bebida.copo.tamanho
        capacidade = bebida.copo.capacidade_ml
        if capacidade <= 0:
            return

        area_liquido = pygame.Surface((largura, altura_copo), pygame.SRCALPHA)
        ml_total = 0

        for indice, item in enumerate(bebida.ingredientes):
            quantidade = item.quantidade_ml
            if indice == len(bebida.ingredientes) - 1:
                quantidade += quantidade_em_andamento

            if quantidade <= 0:
                continue

            quantidade = min(quantidade, capacidade - ml_total)
            if quantidade <= 0:
                break

            altura = (quantidade / capacidade) * altura_copo
            y_liquido = (
                altura_copo
                - altura
                - (ml_total / capacidade) * altura_copo
            )

            pygame.draw.rect(
                area_liquido,
                item.ingrediente.cor,
                (0, int(y_liquido), largura, int(altura)),
            )

            # O degradê fica na interface entre a bebida atual e a anterior.
            if indice > 0 and GRADIENT_HEIGHT > 0:
                cor_anterior = bebida.ingredientes[indice - 1].ingrediente.cor
                cor_atual = item.ingrediente.cor
                y_degrade = int(y_liquido + altura - GRADIENT_HEIGHT)

                for pixel in range(GRADIENT_HEIGHT):
                    fator = pixel / GRADIENT_HEIGHT
                    cor = (
                        int(cor_atual[0] * (1 - fator) + cor_anterior[0] * fator),
                        int(cor_atual[1] * (1 - fator) + cor_anterior[1] * fator),
                        int(cor_atual[2] * (1 - fator) + cor_anterior[2] * fator),
                    )
                    pygame.draw.line(
                        area_liquido,
                        cor,
                        (0, y_degrade + pixel),
                        (largura, y_degrade + pixel),
                    )

            ml_total += quantidade
            if ml_total >= capacidade:
                break

        mask = assets.transparency_mask(
            bebida.copo.mascara,
            bebida.copo.tamanho,
        )
        area_liquido.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(area_liquido, position)
