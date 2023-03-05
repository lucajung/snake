import pygame
from app.apple import Apple
from app.direction import DIRECTION
from collections import deque

"""
TOP-LEFT corner -> (0,0)
BOTTOM-RIGHT corner -> (max, max)
"""
class Player:
    def __init__(self, x, y, resolution, canvas_width, canvas_height):
        self.resolution = resolution
        self.max_lenght = 20
        self.x = x
        self.y = y
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.length = 1
        self.direction = DIRECTION.BOTTOM
        self.positions = deque(maxlen=self.max_lenght)
        self.positions.append((self.x, self.y))

    def move(self):
        if self.direction == DIRECTION.TOP:
            self.y = self.y - self.resolution
        elif self.direction == DIRECTION.RIGHT:
            self.x = self.x + self.resolution
        elif self.direction == DIRECTION.BOTTOM:
            self.y = self.y + self.resolution
        elif self.direction == DIRECTION.LEFT:
            self.x = self.x - self.resolution
        self.positions.append((self.x, self.y))

    def check_wall_collision(self):
        return self.x < 0 or self.x >= self.canvas_width or self.y < 0 or self.y >= self.canvas_height
    
    def check_self_collision(self):
        positions = list(self.positions)
        positions.reverse()
        positions = positions[:self.length]
        return len(positions) != len(set(positions))

    def check_on_apple(self, apple: Apple):
        return self.x == apple.x and self.y == apple.y

    def consume_apple(self):
        if self.length < self.max_lenght:
            self.length = self.length + 1

    def set_direction(self, direction):
        self.direction = direction

    def draw(self, pygame: pygame, surface: pygame.Surface):
        positions = list(self.positions)
        positions.reverse()
        for x in range(self.length):
            position = positions[x]
            rect = (position[0], position[1], self.resolution, self.resolution)
            pygame.draw.rect(surface, (0, 0, 0), rect)
            pygame.draw.rect(surface, (255, 255, 255), rect, 1)

