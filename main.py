# Example file showing a basic pygame "game loop"
import random
import pygame
import time
import os
import datetime
import pandas as pd


#
def get_a_new_number(low, high):
    return random.randint(a=low, b=high)


def is_snake_reached_apple(joints, apple_pos):
    joint_head = joints[0]
    if abs(joint_head[0] - apple_pos[0]) < 10 and abs(joint_head[1] - apple_pos[1]) < 10:
        return True
    else:
        return False
    # if abs(snake_head_pos[0] - apple_pos[0]) < 10 and abs(snake_head_pos[1] - apple_pos[1]) < 10:
    #     # if snake_head_pos == apple_pos:
    #     return True
    # else:
    #     return False


# Description: This function is responsible to save the player's score into the file
def save_score_in_score_board(player_name_input, minutes, seconds, date_now, hour_now):
    df.loc[len(df.index)] = [player_name_input, f'{minutes:02}:{seconds:02}',
                             date_now, hour_now]
    df.sort_values(by='play_time', inplace=True)
    df.reset_index(inplace=True, drop=True)
    df.to_csv('score_board.csv', header=True, index=False)


def handle_boundaries(player_position, current_score):
    if current_score > 5:
        if player_position.y == 0:
            player_position.y = screen.get_height()
        elif player_position.y == screen.get_height():
            player_position.y = 0

        if player_position.x == screen.get_width():
            player_position.x = 0
        elif player_pos.x == 0:
            player_pos.x = screen.get_width()

    return player_position


if __name__ == '__main__':

    if os.path.exists('score_board.csv'):
        print('Loading the score board to memory')
        df = pd.read_csv('score_board.csv')
    else:
        print('CSV file was not found')
        df = pd.DataFrame(columns=['Player_name', 'play_time', 'date', 'time'])
        df.to_csv('score_board.csv', header=True, index=False)

    points_to_reach_game_over = 20
    # When time_duration_to_move_apple is higher than the apple changes its position
    # in slower rate
    time_duration_to_move_apple = 300

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1180, 670))
    clock = pygame.time.Clock()
    running = True

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_pos_offset = pygame.Vector2(0, 0)
    apple_position = pygame.Vector2(get_a_new_number(0, screen.get_width()),
                                    get_a_new_number(0, screen.get_height()))  # pygame.Vector2(590, 335)
    dt = 0

    x_apple = get_a_new_number(0, screen.get_width())
    y_apple = get_a_new_number(0, screen.get_height())

    frame_number = 0
    score = 0

    print('Welcome to the Game snake!')
    player_name_input = input('Please enter your name: ')
    date_now = datetime.date.today()
    hour_now = datetime.datetime.now().time()
    started = time.time()
    super_power = 'not'
    snake_length = 1

    snake_joints_position = [player_pos]

    while running and score < points_to_reach_game_over:
        frame_number += 1
        time_passed = int(time.time() - started)
        if frame_number % time_duration_to_move_apple == 0:
            # print(f'frame_number = {frame_number}')
            x_apple = get_a_new_number(0, screen.get_width())
            y_apple = get_a_new_number(0, screen.get_height())
            apple_position = pygame.Vector2(x_apple, y_apple)
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            # here we are checking if the user wants to exit the game
            if event.type == pygame.QUIT:
                print('Mory is closing the game')
                running = False

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("lightblue")
        screen.fill((85, 240, 171))

        pygame.draw.circle(screen, (255, 0, 0), apple_position, 7.5)

        # pygame.draw.circle(screen, (0, 0, 0), player_pos, 10)

        # pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
        for joint_pos in snake_joints_position:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(joint_pos.x, joint_pos.y, 15, 15))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if player_pos_offset.y != 15:  # The snake not going down
                player_pos_offset.y = -15  # The snake will go up
            player_pos_offset.x = 0
        if keys[pygame.K_DOWN]:
            if player_pos_offset.y != -15:  # The snake not going up
                player_pos_offset.y = 15  # The snake will go down
            player_pos_offset.x = 0
        if keys[pygame.K_LEFT]:
            if player_pos_offset.x != 15:  # The snake not going right
                player_pos_offset.x = -15  # The snake will go left
            player_pos_offset.y = 0
        if keys[pygame.K_RIGHT]:
            if player_pos_offset.x != -15:  # The snake not going left
                player_pos_offset.x = 15  # The snake not going right
            player_pos_offset.y = 0

        # print(f'player_pos: {player_pos.x, player_pos.y},'
        #       f' apple_position: ({x_apple, y_apple})')

        # player_pos = handle_boundaries(player_position=player_pos, current_score=score)

        pygame.display.set_caption(
            f'Mory your score is: {score}, Time: {time_passed} Seconds, Super power is {super_power} active')

        snake_ate_an_apple = is_snake_reached_apple(snake_joints_position, apple_position)

        if snake_ate_an_apple:
            score += 1
            # New position for the apple
            x_apple = get_a_new_number(0, screen.get_width())
            y_apple = get_a_new_number(0, screen.get_height())
            apple_position = pygame.Vector2(x_apple, y_apple)

            tail = snake_joints_position[-1]
            new_tail = tail.copy()
            # joint.y += player_pos_offset.y
            # joint.x += player_pos_offset.x
            new_tail.y = new_tail.y + player_pos_offset.y
            new_tail.x = new_tail.x + player_pos_offset.x

            snake_joints_position.append(new_tail)

            # make it faster
            if score == 5:
                super_power = ''
                time_duration_to_move_apple = 100

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(20) / 1000

        # for joint in snake_joints_position:
        #     joint.y += player_pos_offset.y
        #     joint.x += player_pos_offset.x
        new_head = pygame.Vector2(snake_joints_position[0].x + player_pos_offset.x,
                                  snake_joints_position[0].y + player_pos_offset.y)

        snake_joints_position = [new_head] + snake_joints_position[:-1]
        # player_pos.y += player_pos_offset.y
        # player_pos.x += player_pos_offset.x

    pygame.quit()

    minutes = time_passed // 60
    seconds = time_passed % 60

    if score == points_to_reach_game_over:
        save_score_in_score_board(player_name_input, minutes, seconds, date_now, hour_now)

    print('*' * 50)
    print(df)
    print('*' * 50)

    print(f'{player_name_input} you have scored: {score}, it took you: {minutes:02}:{seconds:02} ')
    print("Bye")
