import pygame,random,math
from pygame.locals import *
from Velocity import Velocity

## Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

## define the screen size
WIDTH = 1200
HEIGHT = 800

## define num of bots
NUM_OF_BOTS=100

## define detect ranges for avoidance and following
AVOID_RANGE=50
FOLLOW_RANGE= 2 * AVOID_RANGE

## for creating and using VERY sucsessful individual bots
class Bot:
    def __init__(self):
        self._x = random.randint(0,WIDTH)
        self._y = random.randint(0,HEIGHT)
        self._velocity=Velocity()
        self.randDirection()
        self._rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    def move(self):
        self._x = self._x + self._velocity.xMove()
        self._y = self._y + self._velocity.yMove()

    def randDirection(self):
        self._velocity.randomise(10)

    def getDistance(self,Bot):
        xDiffSqd = math.pow(math.fabs((Bot._x - self._x)),2)
        yDiffSqd = math.pow(math.fabs((Bot._y - self._y)),2)
        dist = math.sqrt(xDiffSqd + yDiffSqd)
        return dist

    def follow(self,botFollow):
        self._velocity._angleDegrees = botFollow._velocity._angleDegrees
        self._velocity._speed = botFollow._velocity._speed

    def avoid(self,botAvoid):
        ## us a simple avoidance algo that simply acts as if
        ## contact between the 2 bots has occurred and the self bot
        ## has bounced at an appropriate angle       

        ## bot is to the right of the avoid bot
        if self._x > botAvoid._x:
            if self._velocity.isGoingLeft():
                self._velocity.leftBounce()

        ## bot is to the left of the avoid bot
        if self._x < botAvoid._x:
            if self._velocity.isGoingRight():
                self._velocity.rightBounce()

        ## bot is below the avoid bot
        if self._y > botAvoid._y:
            if self._velocity.isGoingUp():
                self._velocity.upBounce()

        ## bot is above the avoid bot
        if self._y < botAvoid._y:
            if self._velocity.isGoingDown():
                self._velocity.downBounce()

class App:
    def __init__(self):
        self._running = True
        self._screen = None
        self._size = self.width, self.height = WIDTH, HEIGHT

        ## create an array of bot objects to create swarms
        self._Bots = []
        for i in range (1,NUM_OF_BOTS):
            self._Bots.append(Bot())

    def followAll(self):
        for i in range(0,len(self._Bots)):
            followIndex=-1
            closestDistance=100000000
            for j in range(0,len(self._Bots)):
                if i != j:
                    distance = self._Bots[i].getDistance(self._Bots[j])
                    if distance <= FOLLOW_RANGE and distance > AVOID_RANGE:
                        if distance < closestDistance:
                            followIndex = j
                            closestDistance=distance
            if followIndex != -1:
                self._Bots[i].follow(self._Bots[followIndex])

    def avoidAll(self):
        for i in range(0,len(self._Bots)):
            for j in range(0,len(self._Bots)):
                if i != j:
                    distance = self._Bots[i].getDistance(self._Bots[j])
                    if distance <= AVOID_RANGE:
                        self._Bots[i].avoid(self._Bots[j])


    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        ## add the game code to be executed on each cycle

        ## process the move logic for each bot
        self.avoidAll()

        self.followAll()
        
        for i in range(0,len(self._Bots)):
            ## check if the bot has hit the edge of the screen and if           
            ## it has bounce the bot off the side at the correct angle

            ## check for a right wall hit
            if self._Bots[i]._x >= self.width:
                self._Bots[i]._velocity.rightBounce()

            ## check for a left wall hit
            if self._Bots[i]._x <= 0:
                self._Bots[i]._velocity.leftBounce()
                
            ## check for a bottom wall hit
            if self._Bots[i]._y >= self.height:
                self._Bots[i]._velocity.downBounce()

            ## check for a top wall hit
            if self._Bots[i]._y <= 0:
                self._Bots[i]._velocity.upBounce()
                
            ## move the bot
            self._Bots[i].move()


    def on_render(self):
        ## add the game drawing (rendering) code to be executed on each cycle

        ## start with a blank white screen
        self._screen.fill(BLACK)

        ## Draw the bots as a small circle
        for i in range(0,len(self._Bots)):
            pygame.draw.circle(self._screen, self._Bots[i]._rgb, [self._Bots[i]._x, self._Bots[i]._y], 10)

        ## this must be the last line in the on_render() function
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
