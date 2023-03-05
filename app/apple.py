import pygame
import random
import pygame.gfxdraw


class Apple:
    def __init__(self, resolution, canvas_width, canvas_height):
        self.x = 0
        self.y = 0
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.resolution = resolution

    def move_to_random_position(self):
        self.x = int(random.randint(self.resolution, self.canvas_width - self.resolution) / self.resolution) * self.resolution
        self.y = int(random.randint(self.resolution, self.canvas_height - self.resolution) / self.resolution) * self.resolution

    def draw(self, pygame: pygame, surface: pygame.Surface):
        x = int(self.x + self.resolution / 2)
        y = int(self.y + self.resolution / 2)
        r = int(self.resolution / 2 - 3)
        pygame.gfxdraw.aacircle(surface, x, y, r, (100, 100, 100))
        pygame.gfxdraw.filled_circle(surface, x, y, r, (100, 100, 100))
