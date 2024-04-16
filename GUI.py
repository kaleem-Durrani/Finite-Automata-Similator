import pygame, math


def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(math.radians(rotation)),
                                            end[1] + trirad * math.cos(math.radians(rotation))),
                                           (end[0] + trirad * math.sin(math.radians(rotation - 120)),
                                            end[1] + trirad * math.cos(math.radians(rotation - 120))),
                                           (end[0] + trirad * math.sin(math.radians(rotation + 120)),
                                            end[1] + trirad * math.cos(math.radians(rotation + 120)))))


# states class

state_group = pygame.sprite.Group()


class States(pygame.sprite.Sprite):

    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.image.load('redcircle.png')
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = posx, posy
        self.movement = None
        self.a_read = None
        self.b_read = None
        self.selected = None
        self.end_state = False
        self.dead_end = False

    def set_a_transitions(self, a_transition):
        self.a_read = a_transition

    def set_b_transitions(self, b_transition):
        self.b_read = b_transition

    def update(self):

        screen = pygame.display.get_surface()
        pos = pygame.mouse.get_pos()

        if self.dead_end:
            self.image = pygame.image.load('blackcircle-1.png')
            self.image = pygame.transform.smoothscale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('redcircle.png')
            self.image = pygame.transform.smoothscale(self.image, (80, 80))

        if self.end_state:
            pygame.draw.circle(screen, 'red', self.rect.center, 50, 3)

        if self.selected:
            arrow(screen, 'black', 'green', self.rect.center, pos, 5)

        if self.movement:
            self.rect.center = pygame.mouse.get_pos()

        elif self.a_read:
            arrow(screen, 'red', 'red', (self.rect.centerx, self.rect.centery - 10),
                  (self.a_read.rect.centerx, self.a_read.rect.centery - 10), 10)

        if self.b_read:
            arrow(screen, 'purple', 'purple', (self.rect.centerx, self.rect.centery + 10),
                  (self.b_read.rect.centerx, self.b_read.rect.centery + 10), 10)


# method for writing the state names

def write(screen, prompt, pos):
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('GeeksForGeeks', True, green, blue)
    text = font.render(prompt, True, green, blue)
    screen.blit(text, pos)
