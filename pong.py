#Credit the Invent With Python book (http://inventwithpython.com)
#for doRectsOverlap and isPointInsideRect functions
import pygame
#used to detect collisions in our game
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([1000,1000])
black = [0, 0, 0]

#the game's variables
#SECTION 1 - YOUR CODE HERE FOR CREATING VARIABLES AND FUNCTIONS
class Paddle():
    def __init__(self,color,pos,height,width):
        self.pos = pos
        self.height = height
        self.width = width
        self.color = color

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
    def upward(self):
        self.pos[1] -= 10
    def down(self):
        self.pos[1] -= -10
pygame.key.set_repeat(10,10)
player_paddle = Paddle((0,0,250),[0,0],150,30)
running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            print ("mouse moved")
            #SECTION 2 - YOUR CODE HERE FOR WHEN THE MOUSE IS MOVED

        pressed =  pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_UP]:
                if player_paddle.pos[1] > 0:
                    player_paddle.upward()
            if pressed[pygame.K_DOWN]:
                if player_paddle.pos[1] < 1000-player_paddle.height:
                    player_paddle.down()
            #SECTION 3 - YOUR CODE HERE FOR WHEN A KEY IS PRESSED

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #logic for moving everything in the game and checking collisions
    #SECTION 4 - YOUR CODE HERE FOR CHANGING VARIABLES AND CHECKING FOR COLLISIONS
    
    #draw everything on the screen
    #SECTION 5 - YOUR CODE HERE FOR DRAWING EVERYTHING
    pygame.draw.rect(screen,player_paddle.color,player_paddle.rect())

    
    #update the entire display
    pygame.display.update()


pygame.quit()
