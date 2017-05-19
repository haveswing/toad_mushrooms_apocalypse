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
font = pygame.font.SysFont('Impact', 50)
screen = pygame.display.set_mode((height, width))
pygame.mixer.init()
playlist = ["ost.mid","ost1.mid","ost2.MID"]
select = (random.choice(playlist))
pygame.mixer.music.load(select)
p_ing = True
if p_ing:
    for i in range(3):
        pygame.mixer.music.play(-1)
effect = pygame.mixer.Sound('jumpwav.wav')
effect1 = pygame.mixer.Sound('ouch.wav')
# screen.set_caption("Toad Mushrooms Adventure")

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
mushy = -64
speed = 64

toad = pygame.image.load("toad.gif")
toadx = 423 / 2
toady = 355
movement = 84


lifex = 100
lifey = 20
lifeposx = 84
lifeposy = 42

counter = 0
counterx = 14
countery = 14


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
    screen.blit(toad, (toadx, toady))
    rolling = [-90,90]
    rollingdir = random.choice(rolling)

    # mushrain:
    if mushy > -65 and mushy < 3000:
        screen.blit(mushroom, (mushx, mushy))
        mushy = mushy + speed
        mushroom = pygame.transform.rotate(mushroom, rollingdir)
        if mushy == 576:
            counter += 1
    else:
        mushx = random.randint(0, 372)
        mushy = -64

    # collisions:
    if toadx >= mushx-64 and toadx <= mushx+64:
        if toady >= mushy-64 and toady <= mushy+64:
            lifex -= 10
            effect1.play()
            print("OUCH!")

    # hallucinations:
    if lifex <= 20:
        ipercolorA = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ipercolorB = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        hallu = pygame.Surface((width, height))
        hallu.set_alpha(142)
        hallu.fill(ipercolorA)
        screen.blit(hallu, (0, 0))
        hallu.fill(ipercolorB)
        screen.blit(hallu, (0, 0))

    if lifex <= 0:
        print("GAME OVER!")

    pygame.draw.rect(screen, black, (lifeposx-5, lifeposy-5, 110, 30))
    pygame.draw.rect(screen, green, (lifeposx, lifeposy, lifex, lifey))
    screen.blit(countersurface, (counterx, countery))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                toadx -= movement
                effect.play()
            if event.key == K_d:
                toadx += movement
                effect.play()
            if event.key == K_w:
                # toady -= movement
                print("W key is disabled.")
            if event.key == K_s:
                # toady += movement
                print("S key is disabled.")

        # bounce:
        if toadx < -64:
            toadx = toadx + 42
            effect1.play()
            lifex -= 0.5
        if toadx > 423:
            toadx = toadx - 42
            effect1.play()
            lifex -= 0.5

    if event.type == QUIT:
        pygame.quit()
        exit()
