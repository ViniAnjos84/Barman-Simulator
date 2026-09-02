from core.assets import assets


class BebidaView:
    def draw(self, screen, ingrediente, position, size, rotation=0):
        image = assets.image(ingrediente.icone, size, rotation)
        screen.blit(image, position)
