import pygame
from app.apple import Apple
from app.direction import DIRECTION

from app.player import Player

pygame.init()
pygame.display.set_caption('Snake RL game')

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
RESOLUTION = 30
GRID_COLOR = (200, 200, 200)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

surface = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

surface.fill(COLOR_WHITE)

font = pygame.font.Font(None, 25)
pygame.display.update()

clock = pygame.time.Clock()
player = Player(0,0, RESOLUTION, CANVAS_WIDTH, CANVAS_HEIGHT)
apple = Apple(RESOLUTION, CANVAS_WIDTH, CANVAS_HEIGHT)
apple.move_to_random_position()

def main():
    running = True
    frame_counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.set_direction(DIRECTION.LEFT)
                elif event.key == pygame.K_RIGHT:
                    player.set_direction(DIRECTION.RIGHT)
                elif event.key == pygame.K_UP:
                    player.set_direction(DIRECTION.TOP)
                elif event.key == pygame.K_DOWN:
                    player.set_direction(DIRECTION.BOTTOM)
        
        if frame_counter % 5 == 0:
            player.move()
            if player.check_on_apple(apple):
                player.consume_apple()
                apple.move_to_random_position()

        if not player.check_wall_collision() and not player.check_self_collision():
            surface.fill((255, 255, 255))

            for x in range(0, CANVAS_WIDTH, RESOLUTION):
                pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, CANVAS_HEIGHT))
            for y in range(0, CANVAS_HEIGHT, RESOLUTION):
                pygame.draw.line(surface, GRID_COLOR, (0, y), (CANVAS_WIDTH, y))

            player.draw(pygame, surface)
            apple.draw(pygame, surface)

            score = font.render("Score: {}".format(int(player.length)), True, COLOR_BLACK)

            surface.blit(score, (CANVAS_WIDTH - score.get_width() - 10, 10))
            pygame.display.flip()
        else:
            running = False
        
        frame_counter = frame_counter + 1
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()