from core.config import DRINKS_DIR
from models.ingrediente import Ingrediente


def _alcool(nome, arquivo, cor):
    return Ingrediente(nome, f"{DRINKS_DIR}/alcoholic_drinks/{arquivo}", cor)


VODKA = _alcool("Vodka", "vodka.png", (235, 235, 235))
GIN = _alcool("Gin", "gin.png", (210, 230, 220))
CACHAÇA = _alcool("Cachaça", "cachaca.png", (245, 245, 245))
RUM = _alcool("Rum", "rum.png", (180, 90, 40))
WHISKY = _alcool("Whisky", "whisky.png", (200, 120, 50))
TEQUILA = _alcool("Tequila", "tequila.png", (255, 180, 20))

ALCOOLICOS = [VODKA, GIN, CACHAÇA, RUM, WHISKY, TEQUILA]
