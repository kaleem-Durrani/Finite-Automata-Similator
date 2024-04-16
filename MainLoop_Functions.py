import pygame, sys
from GUI import state_group
from GUI import States


def quit():
    pygame.quit()
    sys.exit()


def drag():
    for i in state_group:
        pos = pygame.mouse.get_pos()
        if i.rect.collidepoint(pos):
            i.movement = True
            break


def drop():
    for i in state_group:
        i.movement = False


def add_state():
    a = States(100, 100)
    state_group.add(a)
    current = a
    return current


def remove_state(current):
    if current is None:
        pass
    else:
        current.kill()
        if len(state_group) == 0:
            current = None
        else:
            current = state_group.sprites()[len(state_group) - 1]
    return current


# def selection(selected_sprite):
#     selected_sprite.selected = True
#
#
# def make_transition(selected_sprite, target_sprite):
#     selected_sprite.set_a_transitions(target_sprite)
#     selected_sprite.selected = False
#     target_sprite.selected = False

