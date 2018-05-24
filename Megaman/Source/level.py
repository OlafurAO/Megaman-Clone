import pygame;

pygame.init();

class Level:
    def __init__(self, game_display, screen_size, map):
        self.level_list = [];
        self.game_display = game_display;
        self.screen_size = screen_size;
        self.map = map;

        self.second_section_initialized = False;

        self.initialize_first_section();

    def draw(self, player_location):
        for i in self.level_list:
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 10, 10]);

    def initialize_first_section(self):
        for i in range(0, 3250, 20):
            self.level_list.append([int(i), int(self.screen_size[1]) - 50]);

        for i in range(50, 1000, 20):
            self.level_list.append([int(0), int(self.screen_size[1]) - i]);

        for i in range(60, 150, 20):
            self.level_list.append([int(1320), int(self.screen_size[1]) - i]);
            self.level_list.append([int(1410), int(self.screen_size[1]) - i]);


        for i in range(1320, 1420, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 140)]);

        for i in range(755, 800, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 230)]);
            self.level_list.append([int(i), int(self.screen_size[1] - 190)]);

        for i in range(200, 230, 20):
            self.level_list.append([int(755), int(self.screen_size[1] - i)]);
            self.level_list.append([int(800), int(self.screen_size[1] - i)]);

        for i in range(940, 1180, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 190)]);
            self.level_list.append([int(i), int(self.screen_size[1] - 230)]);

        for i in range(200, 230, 20):
            self.level_list.append([int(940), int(self.screen_size[1] - i)]);
            self.level_list.append([int(1180), int(self.screen_size[1] - i)]);

        for i in range(1040, 1080, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 370)]);
            self.level_list.append([int(i), int(self.screen_size[1] - 400)]);

        for i in range(370, 400, 20):
            self.level_list.append([int(1040), int(self.screen_size[1] - i)]);
            self.level_list.append([int(1080), int(self.screen_size[1] - i)]);

        for i in range(1790, 1880, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 180)]);

        for i in range(70, 180, 20):
            self.level_list.append([int(1790), int(self.screen_size[1] - i)]);
            self.level_list.append([int(1880), int(self.screen_size[1] - i)]);

        for i in range(2170, 2260, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 230)]);

        for i in range(70, 230, 20):
            self.level_list.append([int(2170), int(self.screen_size[1] - i)]);
            self.level_list.append([int(2260), int(self.screen_size[1] - i)]);


        for i in range(2690, 2770, 20):
            self.level_list.append([int(i), int(self.screen_size[1] - 230)]);

        for i in range(70, 230, 20):
            self.level_list.append([int(2690), int(self.screen_size[1] - i)]);
            self.level_list.append([int(2770), int(self.screen_size[1] - i)]);


        for i in range(3630, 3770, 20):
            self.level_list.append([int(i), int(self.screen_size[1]) - 190]);
            self.level_list.append([int(i), int(self.screen_size[1]) - 230]);

        for i in range(190, 230, 20):
            self.level_list.append([int(3630), int(self.screen_size[1]) - i]);
            self.level_list.append([int(3770), int(self.screen_size[1]) - i]);

        for i in range(3350, 4060, 20):
            self.level_list.append([int(i), int(self.screen_size[1]) - 50]);

        for i in range(4200, 7220, 20):
            self.level_list.append([int(i), int(self.screen_size[1]) - 50]);



    def scroll(self, move, player_location):
        for i in self.level_list:
            i[0] -= move;
        self.map.scroll(move, player_location);