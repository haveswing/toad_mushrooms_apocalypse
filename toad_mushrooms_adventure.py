import pygame
from pygame.locals import *
import random
import time
import os
import sys

height = 500
width = 500

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((height, width))
# screen.set_caption("Toad Mushroom Experience")

running = 1
fps = 30

#colors:
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)
ipercolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

background = pygame.image.load("background.gif")

mushroom = pygame.image.load("mushroom.gif")
mushx = random.randint(0, 372)
mushy = 0

toad = pygame.image.load("toad.gif")
toadx = 423 / 2
toady = 355

movement = 64

counter = 0
counterx = 14
countery = 14


def mushrain():
    mushx = random.randint(0, 372)
    mushy = 0
    speed = 64
    # mushspawn = USEREVENT + 1

    for fallingdown in range(9):
        screen.blit(mushroom, (mushx,mushy))


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        else:
            print(event)

    ipercolorA = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ipercolorB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    clock = pygame.time.Clock()
    clock.tick(fps)

    # psybackground:
    # screen.fill(ipercolorA)
    # pygame.display.flip()
    # screen.fill(ipercolorB)
    # pygame.display.flip()

    countersurface = font.render(str(counter), False, (255, 255, 255))

    screen.blit(background, (0, 0))
    # screen.blit(mushroom, (mushx, mushy))
    mushrain()
    screen.blit(toad, (toadx, toady))
    screen.blit(countersurface, (counterx, countery))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                toadx -= movement
                counter -= 1
            if event.key == K_d:
                toadx += movement
                counter += 1
            if event.key == K_w:
                # toady -= movement
                print("W key is disabled.")
            if event.key == K_s:
                # toady += movement
                print("S key is disabled.")

        if toadx < -64:
            toadx = toadx + 42
        if toadx > 423:
            toadx = toadx - 42

    if event.type == QUIT:
        pygame.quit()
        exit()
