import pygame
import sys
import time

submit = 0

def mouse_pos():
    (mouseX, mouseY) = pygame.mouse.get_pos()
    #print(mouseX, mouseY)
    if(mouseY>=120 and mouseY<=170):
        index = (mouseX-125)/50
        print(index)
        return index
    return -1

def text_objects(text,font):
    textSurface=font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()

def submit_button():
    (mouseX, mouseY) = pygame.mouse.get_pos()
    if(mouseX >= 650 and mouseX<=850 and mouseY>=30 and mouseY<=80):
        print "clicked"
        global submit
        submit = 1

def erase(bit_list):
    for i in range(25):
        if(bit_list[i] == 2):
            pygame.draw.circle (display, (0, 255, 0), (150+(i*50), 145),20, 2)
            pygame.display.update()
            bit_list[i] = 0

pygame.init()
width = 1500
height = 200

#make the pygame window
display = pygame.display.set_mode((width, height ) )
display.fill((230, 255, 242))
pygame.draw.rect(display, (0, 255, 0), [650, 30, 200, 50])

smallText = pygame.font.Font("freesansbold.ttf",20)
TextSurf, TextRect = text_objects("Submit", smallText)
TextRect.center = (750,53)
display.blit(TextSurf, TextRect)
pygame.draw.rect(display, (0, 255, 0), [125, 120, 1250, 50])
for i in range(0,1300,50):
    pygame.draw.line (display, (0,0,0), (125 +i, 120), (125+i, 170), 1)
for i in range(0,1250,50):
    pygame.draw.circle (display, (100,149,237), (150+i, 145),20, 2)
pygame.display.update()

bit_list = [1 for _ in range(25)]
print bit_list
running = True
#while (running):
    #print (submit,running)
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type is pygame.MOUSEBUTTONDOWN:
            if(submit != 1):
                submit_button()
                index = mouse_pos()
                if(index != -1):
                    #counter += 1
                    bit_list[index] = 2
                    pygame.draw.circle (display, (230, 0, 0), (150+(index*50), 145),20, 2)
                    pygame.display.update()
            else:
                erase(bit_list)
                running = 0
