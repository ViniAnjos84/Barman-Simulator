import pygame

from core.assets import assets
from core.config import (
    BACKGROUND_PATH,
    DRINK_ICON_SIZE,
    FILL_DELAY_MS,
    FILL_SPEED_ML_PER_SECOND,
    FPS,
    GLASS_POSITION,
    ML_BAR_POSITION,
    ML_BAR_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WINDOW_TITLE,
)
from data.copos import COPO_BAIXO
from data.ingredientes import ALCOOLICOS
from models.bebida import Bebida
from ui.barra_ml import BarraML
from ui.bebida_view import BebidaView
from ui.copo_view import CopoView
from ui.hud import HUD
from ui.slots import SlotGrid


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = assets.image(BACKGROUND_PATH, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.hud = HUD()
        self.slot_grid = SlotGrid(ALCOOLICOS, x=65, y=160)
        self.slot_grid.set_slot_image(self.hud.slot)

        self.copo = COPO_BAIXO
        self.copo_view = CopoView(self.copo)
        self.bebida_view = BebidaView()
        self.barra_ml = BarraML(*ML_BAR_SIZE)

        self.bebida = Bebida(copo=self.copo)
        self.item_selecionado = None
        self.derramando = False
        self.tempo_inicio = None

    def run(self):
        while self.running:
            self._process_events()
            self._update()
            self._render()
            self.clock.tick(FPS)

        pygame.quit()

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._click_ingrediente(event.pos)

    def _click_ingrediente(self, position):
        """Primeiro clique inicia o preenchimento; segundo clique para e salva a quantidade."""
        if self.derramando:
            self._finalizar_preenchimento()
            return

        ingrediente = self.slot_grid.item_at(position)
        if ingrediente is None:
            return

        if self.bebida.adicionar_ingrediente(ingrediente):
            self.item_selecionado = ingrediente
            self.tempo_inicio = pygame.time.get_ticks()
            self.derramando = True

    def _quantidade_em_andamento(self):
        if not self.derramando:
            return 0

        agora = pygame.time.get_ticks()
        return self.bebida.quantidade_em_andamento(
            self.tempo_inicio,
            agora,
            FILL_DELAY_MS,
            FILL_SPEED_ML_PER_SECOND,
        )

    def _finalizar_preenchimento(self):
        quantidade = self._quantidade_em_andamento()
        self.bebida.confirmar_ingrediente(quantidade)
        self.derramando = False
        self.tempo_inicio = None

    def _update(self):
        if not self.derramando:
            return

        quantidade = self._quantidade_em_andamento()
        if self.bebida.ml_atual + quantidade >= self.copo.capacidade_ml:
            self.bebida.confirmar_ingrediente(quantidade)
            self.derramando = False
            self.tempo_inicio = None

    def _render(self):
        self.screen.blit(self.background, (0, 0))
        self.hud.draw(self.screen)
        self.slot_grid.draw(self.screen)

        # CAMADA 1: líquido, usando a máscara do copo.
        self.bebida_view.draw_liquido(
            self.screen,
            self.bebida,
            GLASS_POSITION,
            quantidade_em_andamento=self._quantidade_em_andamento(),
        )

        if self.item_selecionado:
            # A imagem da garrafa está rotacionada 90°. A tampa fica na
            # extremidade esquerda da imagem; por isso, o X da imagem é
            # exatamente o centro horizontal do copo.
            x_garrafa = GLASS_POSITION[0] + self.copo.tamanho[0] // 2
            y_garrafa = 30
            posicao_garrafa = (x_garrafa, y_garrafa)

            # CAMADA 2: garrafa.
            self.bebida_view.draw(
                self.screen,
                self.item_selecionado,
                posicao_garrafa,
                DRINK_ICON_SIZE,
                rotation=90,
            )

            if self.derramando:
                # CAMADA 3: fluxo. Fica na frente da máscara do líquido,
                # mas ainda atrás do sprite/visualização do copo.
                self.bebida_view.draw_fluxo(
                    self.screen,
                    self.item_selecionado,
                    posicao_garrafa,
                    DRINK_ICON_SIZE,
                    self.tempo_inicio,
                )

        # CAMADA 4: copo por último, cobrindo o fluxo onde o sprite do copo
        # precisar ficar na frente.
        self.copo_view.draw(self.screen, GLASS_POSITION)

        self.barra_ml.draw(
            self.screen,
            self.bebida.ml_atual,
            self.copo.capacidade_ml,
            ML_BAR_POSITION,
            quantidade_em_andamento=self._quantidade_em_andamento(),
        )

        pygame.display.flip()
