import pygame

from core.assets import assets
from core.config import (
    BACKGROUND_PATH,
    DRINK_ICON_SIZE,
    DRINK_POSITION,
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

    def run(self):
        while self.running:
            self._process_events()
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
                self._select_ingredient(event.pos)

    def _select_ingredient(self, position):
        ingrediente = self.slot_grid.item_at(position)
        if ingrediente is None:
            return

        self.item_selecionado = ingrediente
        self.bebida.adicionar_ingrediente(ingrediente)
        print(f"Ingrediente selecionado: {ingrediente.nome}")

    def _render(self):
        self.screen.blit(self.background, (0, 0))
        self.hud.draw(self.screen)
        self.slot_grid.draw(self.screen)

        if self.item_selecionado:
            self.bebida_view.draw(
                self.screen,
                self.item_selecionado,
                DRINK_POSITION,
                DRINK_ICON_SIZE,
                rotation=90,
            )

        self.copo_view.draw(self.screen, GLASS_POSITION)
        self.barra_ml.draw(
            self.screen,
            self.bebida.ml_atual,
            self.copo.capacidade_ml,
            ML_BAR_POSITION,
        )

        pygame.display.flip()
