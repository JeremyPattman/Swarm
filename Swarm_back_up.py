import pygame,random
from pygame.locals import *

## Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class Bot:
    def __init__(self):
        self._x = 600
        self._y = 400
        self._xMove = random.randint(-5,5)
        self._yMove = random.randint(-5,5)
        self._rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def move(self):
        self._x = self._x + self._xMove
        self._y = self._y + self._yMove


class App:
    def __init__(self):
        self._running = True
        self._screen = None
        self._size = self.width, self.height = 1200, 800

        self._Bots = []
        for i in range (1,50):
            self._Bots.append(Bot())
  
    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        ## add the game code to be executed on each cycle

        for i in range(0,len(self._Bots)):
            if self._Bots[i]._x >= self.width or self._Bots[i]._x <= 0:
                self._Bots[i]._xMove = -1 * self._Bots[i]._xMove
            if self._Bots[i]._y >= self.height or self._Bots[i]._y <= 0:
                self._Bots[i]._yMove = -1 * self._Bots[i]._yMove
               
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
