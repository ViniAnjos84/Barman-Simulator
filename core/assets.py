import os
import pygame


class AssetManager:
    """Carrega e mantém assets em cache para evitar leituras repetidas do disco."""

    def __init__(self):
        self._images = {}

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


assets = AssetManager()
