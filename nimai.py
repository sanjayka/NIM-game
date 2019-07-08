import pygame
import sys
import time

BG_color = (220, 255, 255)
box_color = (55, 230, 230)
circle_color = (255, 111, 97)
outline_color = (255, 31, 0)
submit_color = (255, 99, 71)
line_color = (37, 116, 77)

submit = 0
bit_list = [1 for _ in range(25)]

def mouse_pos():
    (mouseX, mouseY) = pygame.mouse.get_pos()
    #print(mouseX, mouseY)
    if(mouseY>=120 and mouseY<=170):
        index = (mouseX-125)/50
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
            pygame.draw.circle (display, (box_color), (150+(i*50), 145),20, 20)
            pygame.display.update()
            bit_list[i] = 0



class NimGame:

    def __init__(self, n):

        self.n = n

    def startState(self):

        return self.n

    def isEnd(self, state):

        return True if state == 0 else False

    def utility(self, state, player):

        if state == 0:
            if player == 1:
                # you lost
                return float('-inf')
            else:
                # you won!
                return float('+inf')

    def actions(self, state):
        # the possible actions at a particular state
        if state >= 3:
            return [1,2,3]
        return range(1, state+1)

    def successor(self, state, action):

        if action > state:
            return 0
        return state - action

def max_heuristic(game, state, player):

    act = 1
    val = float('+inf')

    lis = game.actions(state)

    if((state - 1) % 4 == 0):
        act = 1
        val = float('-inf')

    elif((state - 2) % 4 == 0):
        act = 2
        val = float('-inf')

    elif((state - 3) % 4 == 0):
        act = 3
        val = float('-inf')

    return (val, act)


def minimaxPolicy(game, state, player):

    def recurse(state, player):

        # start with the base case
        if game.isEnd(state) == True:

            return (game.utility(state, player), None)
        if cache.has_key((state, player)):
            return cache[(state, player)]


        choices = [(recurse(game.successor(state, action), -1*player)[0], action) for action in game.actions(state)]


        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val


    value, action = recurse(state, player)
    return (value, action)

cache = {}

if __name__ == "__main__":

    pygame.init()
    width = 1500
    height = 300

    counter = 0


    display = pygame.display.set_mode((width, height ) )
    display.fill(BG_color)
    pygame.draw.rect(display, (submit_color), [650, 30, 200, 50])

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect = text_objects("Submit", smallText)
    TextRect.center = (750,53)
    display.blit(TextSurf, TextRect)
    pygame.draw.rect(display, (box_color), [125, 120, 1250, 50])
    pygame.draw.line (display, (line_color), (125 , 120), (1375, 120), 2)
    pygame.draw.line (display, (line_color), (125 , 170), (1375, 170), 2)
    for i in range(0,1300,50):
        pygame.draw.line (display, (line_color), (125 +i, 120), (125+i, 170), 2)
    for i in range(0,1250,50):
        pygame.draw.circle (display, (circle_color), (150+i, 145),20, 20)
    pygame.display.update()


    game = NimGame(25)

    state = game.startState()
    print "current state is", state
    while (state > 0):
        action = 0

        running = 1
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                if event.type is pygame.MOUSEBUTTONDOWN:
                    if(submit != 1):
                        if(counter > 0):
                            submit_button()
                        index = mouse_pos()
                        if(index != -1):
                            counter += 1
                            bit_list[index] = 2
                            pygame.draw.circle (display, (outline_color), (150+(index*50), 145),20, 20)
                            pygame.display.update()
                    else:
                        erase(bit_list)
                        running = 0

        print "you removed ",counter
        submit = 0
        state -= counter
        print "current state is", state
        time.sleep(1)
        counter = 0
        if state == 0:
            print "You won!"
            break
        #val, act = minimaxPolicy(game, state, 1)
        val, act = max_heuristic(game, state, 1)
        state -= act
        print "computer removed ",act
        x = 0
        i = 0
        while(x != act):
            if(bit_list[i] == 1):
                bit_list[i] = 2
                x += 1
            i += 1

        erase(bit_list)
        pygame.display.update()
        print cache

        print "computer moves state to", state
        if state == 0:
            print "You Lost!"
