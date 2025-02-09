import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("CLUBSTEPA")
pygame.mixer.init()

pygame.mixer.music.load('clubstep.mp3')

text_surface = pygame.font.Font('arialmt.ttf',36).render('Hello, Pygame!', True, (255, 0, 255))

while 1:
    screen.blit(text_surface, (100, 100))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                pygame.mixer.music.play()
            elif i.button == 3:
                pygame.mixer.music.stop()

    pygame.time.delay(20)
