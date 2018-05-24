import pygame;
pygame.init()

class Bullet:
    def __init__(self, x, y, multiplier):
        self.x = x;
        self.y = y;
        self.multiplier = multiplier;

    def move(self):
        self.x += 10 * self.multiplier;

    def draw(self, display):
        pygame.draw.rect(display, (255, 255, 255), [self.x, self.y, 5, 5]);
        self.move();

