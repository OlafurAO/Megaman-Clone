from bullet import Bullet;
import pygame;

pygame.init();

class Player:
    def __init__(self, screen_size, game_display, level):
        self.sprite_sheet = Sprite_Sheet(pygame.image.load('C:\\Users\\Ólafur\\Desktop\\Python\\Game Development\\Megaman\\Grafix\\many_sprite.png'), 10, 7);

        self.game_display = game_display;
        self.screen_size = screen_size;
        self.location = [int(screen_size[0] / 2 - 405), int(screen_size[1] / 2)];
        self.actual_location = [int(screen_size[0] / 2 - 405), int(screen_size[1] / 2)];

        self.health = 50;

        self.bullet_list = [];
        self.hit_box_top_bottom = [];
        self.hit_box_right = [];
        self.hit_box_left = [];

        self.hit_box_sides = [];

        self.cell_index = 0;
        self.count = 0;

        self.player_moving = False;
        self.player_in_air = False;
        self.player_shooting = False;
        self.backwards_animation = False;
        self.collision_right = False;
        self.collision_left = False;
        self.recovery = 0;
        self.recovery_two = 0;

        self.direction = "Right";

        self.initialize_hit_box();

        self.level = level;

    def initialize_hit_box(self):
        self.hit_box_top_bottom.append([self.location[0] + 45, self.location[1] + 50]);
        self.hit_box_top_bottom.append([self.location[0] + 45, self.location[1] + 45]);
        self.hit_box_top_bottom.append([self.location[0] + 50, self.location[1] + 45]);
        self.hit_box_top_bottom.append([self.location[0] + 55, self.location[1] + 45]);
        self.hit_box_top_bottom.append([self.location[0] + 60, self.location[1] + 45]);
        self.hit_box_top_bottom.append([self.location[0] + 65, self.location[1] + 45]);
        self.hit_box_top_bottom.append([self.location[0] + 65, self.location[1] + 50]);
        self.hit_box_top_bottom.append([self.location[0] + 75, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 70, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 65, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 60, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 55, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 50, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 45, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 40, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 35, self.location[1] + 120]);
        self.hit_box_top_bottom.append([self.location[0] + 30, self.location[1] + 120]);


        self.hit_box_left.append([self.location[0] + 25, self.location[1] + 120]);
        self.hit_box_left.append([self.location[0] + 30, self.location[1] + 115]);
        self.hit_box_left.append([self.location[0] + 35, self.location[1] + 110]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 105]);
        self.hit_box_left.append([self.location[0] + 35, self.location[1] + 100]);
        self.hit_box_left.append([self.location[0] + 30, self.location[1] + 100]);
        self.hit_box_left.append([self.location[0] + 25, self.location[1] + 100]);
        self.hit_box_left.append([self.location[0] + 25, self.location[1] + 95]);
        self.hit_box_left.append([self.location[0] + 25, self.location[1] + 90]);
        self.hit_box_left.append([self.location[0] + 30, self.location[1] + 85]);
        self.hit_box_left.append([self.location[0] + 35, self.location[1] + 80]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 75]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 70]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 65]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 60]);
        self.hit_box_left.append([self.location[0] + 40, self.location[1] + 55]);

        self.hit_box_right.append([self.location[0] + 80, self.location[1] + 120]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 55]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 60]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 65]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 70]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 75]);
        self.hit_box_right.append([self.location[0] + 75, self.location[1] + 80]);
        self.hit_box_right.append([self.location[0] + 75, self.location[1] + 85]);
        self.hit_box_right.append([self.location[0] + 80, self.location[1] + 90]);
        self.hit_box_right.append([self.location[0] + 80, self.location[1] + 95]);
        self.hit_box_right.append([self.location[0] + 80, self.location[1] + 100]);
        self.hit_box_right.append([self.location[0] + 75, self.location[1] + 100]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 100]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 105]);
        self.hit_box_right.append([self.location[0] + 70, self.location[1] + 110]);
        self.hit_box_right.append([self.location[0] + 75, self.location[1] + 115]);
    def render_player(self):
        for i in range(0, self.health):
            pygame.draw.rect(self.game_display, (100, 250, 100), [0 + i * 2, 0, 10, 20]);

        if(self.recovery > 0):
            if(self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 10;
            else:
                self.cell_index = 19;
            self.recovery -= 1;
        if(self.recovery_two > 0):
            self.recovery_two -= 1;

        elif(self.player_moving and not self.player_in_air and not self.player_shooting):
            if (self.direction == 'Right'):
                if(self.cell_index > 5 or self.cell_index < 3):
                    self.cell_index = 3;
                if (self.count % 8 == 0):
                    if (self.cell_index == 5):
                        self.cell_index = 5;
                        self.backwards_animation = True;
                    if (self.backwards_animation):
                        if (self.cell_index == 3):
                            self.backwards_animation = False;
                        else:
                            self.cell_index -= 1;
                    if (self.cell_index != 5 and not self.backwards_animation):
                        self.cell_index += 1;

            elif (self.direction == 'Left'):
                if (self.cell_index > 6 or self.cell_index < 4):
                    self.cell_index = 4;
                if (self.count % 8 == 0):
                    if (self.cell_index == 4):
                        self.cell_index = 4;
                        self.backwards_animation = True;
                    if (self.backwards_animation):
                        if (self.cell_index == 6):
                            self.backwards_animation = False;
                        else:
                            self.cell_index += 1;
                    if (self.cell_index != 4 and not self.backwards_animation):
                        self.cell_index -= 1;
        elif(self.player_in_air and self.player_shooting):
            if(self.direction == "Right" or self.direction == 'None'):
                self.cell_index = 16;
            else:
                self.cell_index = 13
        elif(self.player_shooting and not self.player_moving):
            if(self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 12;
            else:
                self.cell_index = 17;
        elif(self.player_shooting and self.player_moving):
            if(self.direction == 'Right'):
                if (self.cell_index > 15 or self.cell_index < 13):
                    self.cell_index = 13

                if (self.count % 7 == 0):
                    if (self.cell_index == 15):
                        self.cell_index = 15;
                        self.backwards_animation = True;
                    if (self.backwards_animation):
                        if (self.cell_index == 13):
                            self.backwards_animation = False;
                        else:
                            self.cell_index -= 1;
                    if (self.cell_index != 15 and not self.backwards_animation):
                        self.cell_index += 1;

            if (self.direction == 'Left'):
                if(self.cell_index == 17):
                    self.cell_index = 16;
                if (self.cell_index > 16 or self.cell_index < 14):
                    self.cell_index = 15;
                if (self.count % 7 == 0):
                    if (self.cell_index == 14):
                        self.cell_index = 14;
                        self.backwards_animation = True;
                    if (self.backwards_animation):
                        if (self.cell_index == 16):
                            self.backwards_animation = False;
                        else:
                            self.cell_index += 1;
                    if (self.cell_index != 14 and not self.backwards_animation):
                        self.cell_index -= 1;
        elif(self.player_shooting and not self.player_in_air and not self.player_moving):
            if(self.direction == 'Right' or self.direction == 'Left'):
                self.cell_index = 12;
            else:
                self.cell_index = 17;
        elif(self.player_in_air):
            if(self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 6;
            else:
                self.cell_index = 3;
        if(len(self.bullet_list) != 0):
            for i in self.bullet_list:
                i.draw(self.game_display);

        self.sprite_sheet.draw(self.game_display, self.cell_index % self.sprite_sheet.total_cell_count, self.location[0], self.location[1], self.direction)
    def draw_hitboxes(self):
        for i in self.hit_box_top_bottom:
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);

        for i in self.hit_box_left:
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);

        for i in self.hit_box_right:
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);

        for i in self.hit_box_sides :
            pygame.draw.rect(self.game_display, (255, 255, 255), [i[0], i[1], 5, 5]);
    def player_jump(self, player_jump_counter, player_jump_cooldown):
        if(player_jump_counter == 25 or self.location[1] != self.screen_size[1] - 150):
            self.player_in_air = True;
        if(player_jump_counter <= 25 and player_jump_counter != 0):
            self.location[1] -= 10;
            for i in self.hit_box_top_bottom:
                i[1] -= 10;
            for i in self.hit_box_right:
                i[1] -= 10;
            for i in self.hit_box_left:
                i[1] -= 10;

        if(player_jump_counter == 0 and self.player_in_air):
            for i in self.level.level_list:
                for j in self.hit_box_top_bottom:
                    if(i[0] == j[0] and i[1] == j[1] + 10):
                        self.player_in_air = False;

            if(self.player_in_air):
                self.location[1] += 10;
                for i in self.hit_box_top_bottom:
                    i[1] += 10;
                for i in self.hit_box_right:
                    i[1] += 10;
                for i in self.hit_box_left:
                    i[1] += 10;
            else:
                self.player_in_air = False;
               # self.player_shooting = False;
               # self.reset_player_after_jump();
    def move_player(self, move, player_moving, player_jump_counter, player_jump_cooldown):
        self.player_jump(player_jump_counter, player_jump_cooldown);

        if(self.recovery > 0):
            move = 0;

        if (self.player_moving and self.direction == 'Right' and self.location[0] >= self.screen_size[0] - 350 and not self.collision_right):
            self.level.scroll(move, self.actual_location[0]);
            self.actual_location[0] += move;
            move = 0;

        elif (self.player_moving and self.direction == 'Left' and self.location[0] <= 300 and not self.collision_left):
            self.level.scroll(move, self.actual_location[0]);
            self.actual_location[0] += move;
            move = 0;

        if (self.player_moving and self.direction == 'Right' and self.location[0] >= self.screen_size[0] - 350 and not self.collision_right and self.player_in_air):
            self.level.scroll(move, self.actual_location[0]);
            self.actual_location[0] += move;
            move = 0;

        if (self.player_moving and self.direction == 'Left' and self.location[0] <= 300 and not self.collision_left and self.player_in_air):
            self.level.scroll(move, self.actual_location[0]);
            self.actual_location[0] += move;
            move = 0;

        if((move > 0 and self.direction == 'Left') or (move < 0 and self.direction == 'Right')):
            self.player_shooting = False;

        if(player_moving):
            if (self.direction == 'Right'):
                for i in self.hit_box_right:
                    if(i in self.level.level_list):
                        self.collision_right = True;

                if not(self.collision_right):
                    self.location[0] += move;
                    self.actual_location[0] += move;

                    for i in self.hit_box_right:
                        i[0] += move;
                    for i in self.hit_box_left:
                        i[0] += move;
                    for i in self.hit_box_top_bottom:
                        i[0] += move;

            else:
                for i in self.hit_box_left:
                    if (i in self.level.level_list):
                        self.collision_left = True;

                if not(self.collision_left):
                    self.location[0] += move;
                    self.actual_location[0] += move;

                    for i in self.hit_box_right:
                        i[0] += move;
                    for i in self.hit_box_left:
                        i[0] += move;
                    for i in self.hit_box_top_bottom:
                        i[0] += move;

            if not(self.player_in_air):
                if not(self.player_moving):
                    self.player_moving = True;
                    self.count = 0;
                    if(move > 0):
                        if (self.collision_right):
                            self.collision_right = False;

                        self.direction = 'Right';
                        self.cell_index = 3;
                    elif(move < 0):
                        if (self.collision_left):
                            self.collision_left = False;

                        self.direction = 'Left';
                        self.cell_index = 6;
                self.count += 1;

            else:
                if (move > 0):
                    if(self.collision_right):
                        self.collision_right = False;

                    self.direction = 'Right';
                    self.cell_index = 3;
                elif(move < 0):
                    if(self.collision_left):
                        self.collision_left = False;

                    self.direction = 'Left';
                    self.cell_index = 6;

        else:
            if(self.direction == 'Right'):
                self.cell_index = 0;
            elif(self.direction == 'Left'):
                self.cell_index = 9;
            self.player_moving = False;

        if(move > 0):
            self.direction = 'Right';
        elif(move < 0):
            self.direction = 'Left';
    def player_shoot(self, player_shoot_cooldown):
        if (player_shoot_cooldown > 0):
            if(player_shoot_cooldown == 20):
                if not(self.cell_index >= 13 and self.cell_index <= 15):

                    if(self.cell_index >= 2 and self.cell_index <= 5 or self.cell_index == 12):
                        self.cell_index += 10;

                    elif(self.cell_index >= 4 and self.cell_index <= 6 or self.cell_index == 17):
                        self.cell_index += 10;

                if(self.direction == 'Right' or self.direction == 'None'):
                    bullet = Bullet(self.location[0] + 100, self.location[1] + 80, 1);
                else:
                    bullet = Bullet(self.location[0] + 40, self.location[1] + 80, -1);

                self.bullet_list.append(bullet);
                self.player_shooting = True;

        if(player_shoot_cooldown == 0 and self.player_shooting):
            if (self.direction == 'Right' or self.direction == 'Left' or self.direction == 'None'):
                self.player_shooting = False;
                self.reset_player_after_shot();
    def reset_player_after_jump(self):
        if(self.player_moving and not self.player_shooting):
            if (self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 3;
            else:
                self.cell_index = 6;

        elif(self.player_shooting and self.player_moving):
            if(self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 13;
            else:
                self.cell_index = 16;

        else:
            if (self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 1;
            else:
                self.cell_index = 9;
    def reset_player_after_shot(self):
        if (self.player_moving):
            self.cell_index -= 10;
        else:
            if (self.direction == 'Right' or self.direction == 'None'):
                self.cell_index = 0;
            else:
                self.cell_index = 9;
    def get_hurt(self):
        if(self.recovery_two <= 0):
            self.recovery = 20;
            self.recovery_two = 40;
            self.health -= 10;

class Sprite_Sheet:
    def __init__(self, sheet, cols, rows):

        self.sheet = pygame.transform.scale(sheet.convert_alpha(), (1500, 1200));

        self.sheet_right = pygame.transform.flip(self.sheet, True, False);

        self.cols = cols;
        self.rows = rows;
        self.total_cell_count = cols * rows;

        self.rect = self.sheet.get_rect();

        self.cell_width = int(self.rect.width / cols);
        self.cell_height = int(self.rect.height / rows);
        self.cells = [];

        for index in range(self.total_cell_count):
            self.cells.append((index % self.cols * self.cell_width,
                               int(index / cols) * self.cell_height,
                               self.cell_width, self.cell_height));

    def draw(self, game_display, cell_index, x, y, direction):
        if(direction == "Right" or direction == "None"):
            game_display.blit(self.sheet, (x, y), self.cells[cell_index]);
        elif(direction == "Left"):
            game_display.blit(self.sheet_right, (x - 37, y), self.cells[cell_index]);