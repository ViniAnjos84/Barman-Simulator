import os
import pygame


class AssetManager:
    """Carrega e mantém assets em cache para evitar leituras repetidas do disco."""

    def __init__(self):
        self._images = {}
        self._masks = {}

    def image(self, path, size=None, rotation=0):
        key = (path, size, rotation)

        if key not in self._images:
            image = pygame.image.load(path).convert_alpha()

            if size:
                image = pygame.transform.scale(image, size)

            if rotation:
                image = pygame.transform.rotate(image, rotation)

            self._images[key] = image

        return self._images[key]

    def image_from(self, directory, filename, size=None, rotation=0):
        return self.image(os.path.join(directory, filename), size, rotation)

    def transparency_mask(self, path, size):
        key = (path, size)
        if key in self._masks:
            return self._masks[key]

        source = self.image(path, size)
        mask = pygame.Surface(source.get_size(), pygame.SRCALPHA)

        for x in range(source.get_width()):
            for y in range(source.get_height()):
                r, g, b, _ = source.get_at((x, y))
                alpha = 255 if r == 255 and g == 255 and b == 255 else 0
                mask.set_at((x, y), (255, 255, 255, alpha))

        self._masks[key] = mask
        return mask


assets = AssetManager()
