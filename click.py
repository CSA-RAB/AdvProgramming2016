#Ryan Blaschke
#Advanced Computer Programming
#2/8/17
#click.py

#imports
import pygame, sys, os
from pygame.locals import *
import time

########################

########################################################################
'''This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
##############################################################################

#start pygame
pygame.init()

#main game loop
def main():
    moving=False
    catx = 10   #cat location
    caty = 60
    tiex = 400
    tiey = 60
    destinationx = 10
    destinationy = 60
    newdestinationx = 400
    newdestinationy = 60
    catImg = pygame.image.load('cat.png')   #cat image
    tieImg = pygame.image.load('tie.png')
    exit_button = pygame.image.load('exit_unclicked.png')   #exit unclicked image
    exit_clicked = pygame.image.load('exit_clicked.png')    #exit clicked image
    load_button = pygame.image.load('loadbtn.JPEG')         #load button image

    exitButton = False

    save_unclicked = pygame.image.load('save_unclicked.png')    #save unclicked image
    save_clicked = pygame.image.load('save_clicked.png')        #save clicked image

    soundeffect = pygame.mixer.Sound('Bomb_Exploding-Sound_Explorer-68256487.wav')    #sound effect

    def destination(x,base=10):         #for moving image to nearest 10
        return int(base*round(float(x)/base))

    def savePos(x,y):          #saving position
        savepos = open('positions.txt', 'w')
        savepos.write(str(x) + ',' + str(y))
        savepos.close()

    def loadIt():     #load position
        loadPos = open('position.txt', 'r')
        line = loadPos.readline()
        nums = line.split(',')
        x = int(nums[0])
        y = int(nums[1])
        loadPos.close()
        return (x, y)

    def canmove(destinationx, destinationy):  #checking to see if cat can move there
        soundeffect.play()
        global newdestinationx
        global newdestinationy
        global tiex
        global tiey
        if destinationx <= 10:
            destinationx = 10
        elif destinationx >= 400:
            destinationx = 400
        if destinationy >= 300:
            destinationy = 300
        elif destinationy <= 60:
            destinationy = 60
        return (destinationx, destinationy)

    def mouseCheck(mousex, mousey, destinationx, destinationy):    #mouse check for mouse location
        global newdestinationx
        global newdestinationy
        global tiex
        global tiey
        exitButton = False

        if mousey <= 60:

            if mousex <= 100 and mousex >= 10:
                exitButton = True
                DISPLAYSURF.blit(exit_clicked, (10, 10))

            elif mousex >= 390 and mousex <= 490:
                DISPLAYSURF.blit(save_clicked, (390, 10))
                savePos(destinationx, destinationy)
                savePos(newdestinationy, newdestinationy)

            elif mousex >= 200 and mousex <= 300:
                soundeffect.play()
                DISPLAYSURF.blit(load_clicked, (200, 10))
                destinationx, destinationy = loadPos()
                newdestinationy, newdestinationy = loadPos()

        else:
            soundeffect.play()
            moving = True
            destinationx = destination(mousex - 50)  # subtract 50 to get center
            # all below is checking edges, if hits edge it goes as far as possible
            if destinationx <= 10:
                destinationx = 0
            elif destinationx >= 400:
                destinationx = 400
            destinationy = destination(mousey - 50)
            if destinationy >= 300:
                destinationy = 300
            elif destinationy <= 60:
                destinationy = 60
            newdestinationx = destination(mousex - 50)
            if newdestinationx <= 10:
                newdestinationx = 0
            elif newdestinationx >= 400:
                newdestinationx = 400
            newdestinationy = destination(mousey - 50)
            if newdestinationy >= 300:
                newdestinationy = 300
            elif newdestinationy <= 60:
                newdestinationy = 60

        return (destinationx, destinationy, exitButton)

    while True:    #event handling loop

        DISPLAYSURF = pygame.display.set_mode((500, 400))  #set up display
        pygame.display.set_caption('Cat Mover')     #setting up caption
        DISPLAYSURF.blit(tieImg, (tiex, tiey))
        DISPLAYSURF.blit(catImg, (catx, caty))     #blit cat image
        DISPLAYSURF.blit(exit_button, (10, 10))    #blit exit button image
        DISPLAYSURF.blit(save_unclicked,(390,10))  #blit save button(unclicked) image
        DISPLAYSURF.blit(load_button, (170,10))    #blit load button image

        if exitButton:                #exit button action
            pygame.time.wait(100)
            pygame.quit()
            sys.exit()
        if moving:      #when moving do these actions according to if statement
            if catx > destinationx:
                catx -= 10
            elif catx < destinationx:
                catx += 10
            if caty > destinationy:
                caty -= 10
            elif caty < destinationy:
                caty += 10
            if tiex > newdestinationx:
                tiex -= 10
            elif tiex < newdestinationx:
                tiex += 10
            if tiey > newdestinationy:
                tiey -= 10
            elif tiey < newdestinationy:
                tiey += 10

        FPS = 30                   #setting Frame rate
        fpsClock = pygame.time.Clock()

        for event in pygame.event.get():    #event handler
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):  #if up arrow and escape pressed then quit
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:       #mouse button click actions
                mousex, mousey = event.pos       #mouse moves to event location of the click
                moving = True
                destinationx, destinationy, exitButton = mouseCheck(mousex, mousey, destinationx, destinationy)
                # key movements
            elif event.type == KEYUP:
                moving = True
                if event.key in (K_LEFT, K_a):  #arrow key left and a key action
                    newdestinationx, newdestinationy = canmove(newdestinationx, newdestinationy)
                    newdestinationx -= 10
                elif event.key in (K_UP, K_w):  #arrow key left and w key action
                    newdestinationx, newdestinationy = canmove(newdestinationx, newdestinationy)
                    newdestinationy -= 10
                elif event.key in (K_DOWN, K_s):  #arrow key down and s key action
                    newdestinationx, newdestinationy = canmove(newdestinationx, newdestinationy)
                    newdestinationy += 10
                elif event.key in (K_RIGHT, K_d):  #arrow key right and d key action
                    newdestinationx, newdestinationy = canmove(newdestinationx, newdestinationy)
                    newdestinationx += 10


        pygame.display.update()    #update display
        fpsClock.tick(FPS)   #fps track



main()  #start