import pygame;
from player import Sprite_Sheet;

pygame.init();

class Map:
    def __init__(self, image, game_display):
        self.image = pygame.transform.scale(image.convert_alpha(), (10000, 1250));
        self.game_display = game_display;
        self.location = [0, 0];

        self.enemy_list = [];

    def draw(self):
        self.game_display.blit(self.image, (self.location[0], self.location[1]));

        for i in self.enemy_list:
            i.move(0);
            i.draw();

    def scroll(self, move, player_location):
        self.location[0] -= move;

class Enemy:
    def __init__(self, location, game_display):
        self.sprite_sheet = Sprite_Sheet(pygame.image.load('C:\\Users\\Ólafur\\Desktop\\Python\\Game Development\\Scott Pilgrim Demo\\Grafix\\many_sprite.png'), 10, 7);
        self.game_display = game_display;
        self.location = [location, 420];
        self.direction = 'Left';
        self.cell_index = 6;

    def move(self, move):
        self.location[0] -= 5 + move;

    def draw(self):
        self.sprite_sheet.draw(self.game_display, self.cell_index, self.location[0], self.location[1], self.direction);