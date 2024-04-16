import time

import pygame
from Debug import debug
from GUI import write
from GUI import state_group, arrow
from MainLoop_Functions import drag, drop, add_state, remove_state
from Button import Button

pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("DFA")

# pointer to the last state added
current = None
test = None

current_sprite = None
initial_selection = True
selected_sprite = None
count = 0

flag = 0
set_arrow = 'a'

base_font = pygame.font.Font(None, 32)
user_input = ''
input_rect = pygame.Rect(50, 580, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
list1 = []

active = False

input_img = pygame.image.load('blackcircle-1.png').convert_alpha()
input_img = pygame.transform.smoothscale(input_img, (100, 50))

submit_button = Button(100, 650, input_img)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

            if pygame.mouse.get_pressed()[0] == 1:
                drag()

        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0] == 0:
                drop()

        if event.type == pygame.KEYDOWN:

            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                if event.unicode == 'a' or event.unicode == 'b':
                    user_input += event.unicode

            if event.key == pygame.K_UP:
                current = add_state()

            if event.key == pygame.K_DOWN:
                if state_group:
                    current = remove_state(current)
                    if count >= len(state_group) - 1 and count > 0:
                        count -= 1

            if event.key == pygame.K_a:
                set_arrow = 'a'
            if event.key == pygame.K_b:
                set_arrow = 'b'

            if event.key == pygame.K_RIGHT:
                if count < len(state_group) - 1:
                    count += 1

            if event.key == pygame.K_LEFT:
                if count > 0:
                    count -= 1

            if event.key == pygame.K_q:
                if state_group:
                    sp = state_group.sprites()[count]
                    if not sp.dead_end:
                        if sp.end_state:
                            sp.end_state = False
                        else:
                            sp.end_state = True

            if event.key == pygame.K_w:
                if state_group:
                    if count != 0:
                        sp = state_group.sprites()[count]
                        if not sp.end_state:
                            if sp.dead_end:
                                sp.dead_end = False
                            else:
                                sp.dead_end = True

    screen.fill((200, 200, 200))

    state_group.update()
    state_group.draw(screen)

    # Submit buttonn function
    if submit_button.draw(screen):
        list1[:0] = user_input
        if state_group:
            current_state = state_group.sprites()[0]
        flag2 = 0
        if state_group:
            for i in range(len(list1)):
                if list1[i] == 'a':
                    if current_state.a_read:
                        current_state = current_state.a_read
                        print('read a')
                        if current_state.dead_end:
                            print('Dead End!')
                            break
                        # time.sleep(0.2)
                    else:
                        print('Dead End')
                        flag2 = 1
                        user_input = ''
                        list1 = []
                        break
                elif list1[i] == 'b':
                    if current_state.b_read:
                        current_state = current_state.b_read
                        print('read b')
                        if current_state.dead_end:
                            print('Dead End!')
                            break
                        # time.sleep(0.2)
                    else:
                        print("Dead End")
                        flag2 = 1
                        user_input = ''
                        list1 = []
                        break
        if state_group:
            if flag2 == 1:
                print("invalid String")
            else:
                if current_state.end_state:
                    print("valid string")
                else:
                    print("invalid string")
            user_input = ''
        list1 = []

    # text box color
    if active:
        color = color_active
    else:
        color = color_passive

    #     text box
    pygame.draw.rect(screen, color, input_rect, 4)
    text_surface = base_font.render(user_input, True, (100, 100, 100))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(text_surface.get_width() + 10, 100)

    for i, y in enumerate(state_group):
        write(screen, "q" + str(i), (y.rect.centerx - 40, y.rect.centery - 10))

    # for setting transition of a
    if set_arrow == 'a':

        if initial_selection:
            for i in state_group:
                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[2] == 1:
                        current_sprite = i
                        current_sprite.selected = True
                        initial_selection = False
                        break

        if not initial_selection:

            for i in state_group:
                # if i == current_sprite:
                #     continue

                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[1] == 1:
                        current_sprite.set_a_transitions(i)
                        current_sprite.selected = False
                        initial_selection = True
                        current_sprite = None
                        break

        if current_sprite:
            if pygame.mouse.get_pressed()[0] == 1:
                current_sprite.selected = False
                current_sprite = None
                initial_selection = True

    # For setiing  transition of b
    elif set_arrow == 'b':
        if initial_selection:
            for i in state_group:
                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[2] == 1:
                        current_sprite = i
                        current_sprite.selected = True
                        initial_selection = False
                        break

        if not initial_selection:

            for i in state_group:
                # if i == current_sprite:
                #     continue

                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[1] == 1:
                        current_sprite.set_b_transitions(i)
                        current_sprite.selected = False
                        initial_selection = True
                        current_sprite = None
                        break

        if current_sprite:
            if pygame.mouse.get_pressed()[0] == 1:
                current_sprite.selected = False
                current_sprite = None
                initial_selection = True

    if state_group:
        arrow(screen, 'blue', 'blue',
              (state_group.sprites()[0].rect.centerx - 100, state_group.sprites()[0].rect.centery - 30),
              (state_group.sprites()[0].rect.centerx - 30, state_group.sprites()[0].rect.centery - 30), 8)

    if selected_sprite is None:
        if state_group:
            selected_sprite = state_group.sprites()[count]

    write(screen, 'Selected State -->', (10, 10))
    if state_group:
        debug("q" + str(count), 10, 200)
    else:
        debug('None', 10, 200)

    write(screen, 'A-Transition = ', (700, 10))
    arrow(screen, 'red', 'red', (850, 15), (910, 15), 7)
    write(screen, 'B-Transition = ', (700, 40))
    arrow(screen, 'purple', 'purple', (850, 50), (910, 50), 7)
    write(screen, 'Initial State = ', (700, 70))
    arrow(screen, 'blue', 'blue', (850, 80), (910, 80), 7)
    write(screen, "End State = ", (700, 100))
    pygame.draw.circle(screen, 'red', (850, 110), 15, 3)
    pygame.draw.circle(screen, 'red', (850, 110), 8, 3)
    write(screen, "Dead End = ", (700, 135))
    pygame.draw.circle(screen, 'black', (850, 145), 12, 4)

    write(screen, 'Applying Transition for', (350, 10))
    debug(set_arrow, 10, 590)

    write(screen, 'Press key "A" or "B" to set a or b transitions ', (10, 35))

    write(screen, "Press 'q' for selecting and unselecting end state", (10, 60))

    write(screen, "Test!", (submit_button.rect.left + 25, submit_button.rect.top + 15))

    write(screen, 'Enter your String here for Testing :', (30, 540))
    write(screen, "Press 'w' for End state and 'q' for Dead End.", (550, 670))

    pygame.display.flip()
    clock.tick(60)
