import pygame
from pygame.locals import *
import random
import time
import threading
import os
import sys

height = 500
width = 500

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption('Toad Mushrooms Apocalypse')
icon = pygame.image.load("icon.gif")
pygame.display.set_icon(icon)
pygame.font.init()
font = pygame.font.SysFont('Impact', 50)
font2 = pygame.font.SysFont('Impact', 25)
screen = pygame.display.set_mode((height, width),FULLSCREEN)
pygame.mixer.init()
playlist = ["ost.mid","ost1.mid","star.mid"]
select = (random.choice(playlist))
# pygame.mixer.music.load(select)
# p_ing = True
# if p_ing:
    # for i in range(3):
        # pygame.mixer.music.play(-1)

effect = pygame.mixer.Sound('jumpwav.wav')
effect1 = pygame.mixer.Sound('ouch.wav')
effect2 = pygame.mixer.Sound('LASRFAST.wav')

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

startbackground = pygame.image.load("startbgBW3.gif")
sbx = 0
sby = 0

splash = pygame.image.load("splash.gif")

title = pygame.image.load("title.gif").convert_alpha()

background = pygame.image.load("backgroundBW.gif")

mushroom = pygame.image.load("mushroomBW.gif")
mushx = random.randint(0, 372)
mushy = -64
speed = 32

toad = pygame.image.load("toad.gif")
toadx = 423 / 2
toady = 355
movement = 84
jump = 90
charging = False
toadcharge = pygame.image.load("toadcharge.gif")
time_counter = 0

lifex = 100
lifey = 20
lifeposx = 84
lifeposy = 42

counter = 0
counterx = 14
countery = 14

gover = pygame.image.load("gover.gif")

def uncharger():
    charging = False

def startscreen(sbx=sbx):
    srunning = 1
    pygame.mixer.music.load("ost2.MID")
    pygame.mixer.music.play(-1)
    while srunning:
        clock = pygame.time.Clock()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                srunning = 0
            else:
                print(event)

        # scrolling:
        if sbx >= -999:
            sbx -= 2.5
            print("scrolling!")

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                srunning = 0
                pygame.mixer.music.stop()
                gameloop()

            if event.key == K_ESCAPE:
                srunning = 0
                pygame.quit()
                exit()

        screen.blit(startbackground, (sbx, sby))

        screen.blit(splash, (0, 0))

        screen.blit(title, (0, 10))

        pygame.display.flip()

        pygame.display.update()

def gameloop(counter=counter,lifex=lifex,toadx=toadx,toady=toady,mushy=mushy,mushroom=mushroom,mushx=mushx,jump=jump,charging=charging,time_counter=time_counter):
    running = 1
    pygame.mixer.init()
    playlist = ["ost.mid","12f.mid","star.mid"]
    select = (random.choice(playlist))
    pygame.mixer.music.load(select)
    pygame.mixer.music.play(-1)


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

        if charging == True:
            screen.blit(toadcharge, (toadx, toady))

        rolling = [-90,90]
        rollingdir = random.choice(rolling)

        # mushrain:
        if mushy > -65 and mushy < 600:
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
            hallu.set_alpha(16)
            hallu.fill(ipercolorA)
            screen.blit(hallu, (0, 0))
            hallu.fill(ipercolorB)
            screen.blit(hallu, (0, 0))
            hallutag = font2.render(str("*poisoned*"), False, ipercolor)
            screen.blit(hallutag, (200, 36))

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
                    if toady == 355:
                        effect.play()
                        print("JUMP!")
                        for j1 in range(900):
                            toady -= 0.1
                        for d1 in range(900):
                            toady += 0.1
                if event.key == K_s:
                    if lifex <= 99:
                        effect2.play(1, fade_ms=1500)
                        lifex += 0.5
                        charging = True
                        # time_counter = clock.tick()
                        # if time_counter > 250:
                            # print("uncharging...")
                            # charging = False
                            # time_counter = 0
                        charging = False


                if event.key == K_ESCAPE:
                    running = 0
                    startscreen()

            # bounce:
            if toadx < -64:
                toadx = toadx + 42
                effect1.play()
                lifex -= 0.5
            if toadx > 423:
                toadx = toadx - 42
                effect1.play()
                lifex -= 0.5

            # game over:
            if lifex <= 0:
                running = 0
                gameover(countersurface)

            if event.type == QUIT:
                pygame.quit()
                exit()

def gameover(countersurface):
    drunning = 1
    pygame.mixer.music.load("ost2.MID")
    pygame.mixer.music.play(-1)
    while drunning:
        clock = pygame.time.Clock()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                srunning = 0
            else:
                print(event)

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    srunning = 0
                    pygame.mixer.music.stop()
                    startscreen()

                if event.key == K_ESCAPE:
                    drunning = 0
                    startscreen()

            if event.type == QUIT:
                pygame.quit()
                exit()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        startscreen()
        screen.blit(background, (0, 0))
        screen.blit(gover, (100, 0))
        screen.blit(countersurface, (counterx, countery))
        pygame.display.update()

startscreen()
# gameloop()
# gameover()