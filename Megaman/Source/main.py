from player import Player;
from level import Level;
from map import Map;
import pygame;

pygame.init();

screen_size = (800, 600);
game_display = pygame.display.set_mode(screen_size);
clock = pygame.time.Clock();

FPS = 50;

def render_screen(player, level, map, move, player_moving, player_jump_counter, player_jump_cooldown, player_shoot_cooldown):
    game_display.fill((0, 0, 0));
    map.draw();
    player.player_shoot(player_shoot_cooldown);
    player.move_player(move, player_moving, player_jump_counter, player_jump_cooldown);
    player.render_player();

    #level.draw();
    #player.draw_hitboxes();

    pygame.display.update();
    clock.tick(FPS);

def main():
    map = Map(pygame.image.load('C:\\Users\\Ólafur\\Desktop\\Python\\Game Development\\Megaman\\Grafix\\NES - Super Mario Bros - World 1-1.png'), game_display);
    level = Level(game_display, screen_size, map);
    player = Player(screen_size, game_display, level);
    game_over = False;
    player_moving = False;

    player_jump_counter = 0
    player_jump_cooldown = 0;
    player_shoot_cooldown = 0;
    player_shoot_cooldown_two = 0;
    move = 0;

    joystick = [];

    for i in range(0, pygame.joystick.get_count()):
        joystick.append(pygame.joystick.Joystick(i));

    for i in joystick:
        i.init();
        print('Detected gamepad: ' + i.get_name());
        print('Initializing ' + i.get_name());

    while not game_over:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                game_over = True;
            #################################################
            # Keyboard
            #################################################
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_d):
                    move += 5;
                    player_moving = True;
                elif(event.key == pygame.K_a):
                    move -= 5;
                    player_moving = True;
                if(event.key == pygame.K_SPACE):
                    if(player_jump_counter == 0 and player_jump_cooldown == 0):
                        player_jump_counter = 25;
                if(event.key == pygame.K_k):
                    if(player_shoot_cooldown_two == 0):
                        player_shoot_cooldown = 20;
                        player_shoot_cooldown_two = 10;

                if(event.key == pygame.K_s):
                    player.get_hurt();

            #################################################
            # Gamepad
            #################################################
            if(event.type == pygame.JOYBUTTONDOWN):
                print('Button Pressed ' + str(event.button));

                if(event.button == 1):
                    if (player_jump_counter == 0 and player_jump_cooldown == 0):
                        player_jump_counter = 25;
                if(event.button == 0):
                    if (player_shoot_cooldown_two == 0):
                        player_shoot_cooldown = 20;
                        player_shoot_cooldown_two = 10;


            if(event.type == pygame.JOYAXISMOTION):
                print('D-Pad Pressed ' + str(event.axis) + ' Axis: ' + str(joystick[event.joy].get_axis(event.axis)));

                if(event.axis == 0):
                    if(joystick[event.joy].get_axis(event.axis) == 0.999969482421875):
                        move += 5;
                        player_moving = True;
                    elif(joystick[event.joy].get_axis(event.axis) == -1):
                        move -= 5;
                        player_moving = True;
                    else:
                        move = 0;
                        player_moving = False;

            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_d or event.key == pygame.K_a):
                    move = 0;
                    player_moving = False;
            if(event.type == pygame.JOYBUTTONUP):
                if(event.type == pygame.JOYAXISMOTION):
                    move = 0;
                    player_moving = False;

        render_screen(player, level, map, move, player_moving, player_jump_counter, player_jump_cooldown, player_shoot_cooldown);

        if(player_jump_counter <= 25 and player_jump_counter != 0):
            if not(player.player_in_air):
                player_jump_counter = 0;
            elif(player.player_in_air):
                player_jump_counter -= 1;
            if(player_jump_counter <= 0):
                player_jump_cooldown = 5;

        if(player_jump_cooldown > 0):
            if not(player.player_in_air):
                player_jump_cooldown -= 1;


        if(player_shoot_cooldown > 0):
            player_shoot_cooldown -= 1;

        if(player_shoot_cooldown_two > 0):
            player_shoot_cooldown_two -= 1;

if __name__ == '__main__':
    main();