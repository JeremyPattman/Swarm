from math import *
import random,time

class Velocity:
    def __init__(self):
        self._angleDegrees=25
        self._speed=5

    def xMove(self):
        return round(cos(self.angleRadians())*self._speed)

    def yMove(self):
        return round(sin(self.angleRadians())*self._speed)

    def angleRadians(self):
        return radians(self._angleDegrees)

    def randomise(self,maxSpeed=10):
        self._angleDegrees=random.randint(0,359)
        self._speed=random.randint(1,maxSpeed)

    def turn(self,degrees):
        self._angleDegrees=self._angleDegrees+degrees
        self._angleDegrees=self._angleDegrees%360
        
    def changeSpeed(self,speedDiference):
        self._speed=self._speed+speedDiference


    def isGoingUp(self):
        return(self._angleDegrees > 180 and self._angleDegrees < 360)

    def isGoingDown(self):
        return(self._angleDegrees > 0 and self._angleDegrees < 180)

    def isGoingRight(self):
        return(self._angleDegrees > 270 or self._angleDegrees < 90)
                   
    def isGoingLeft(self):
        return (self._angleDegrees > 90 and self._angleDegrees < 270)

    def downBounce(self):
        if self.isGoingDown():
            if self.isGoingRight():
                a = 90 - self._angleDegrees
                self._angleDegrees = 270 + a
            elif self.isGoingLeft():
                a = self._angleDegrees - 90
                self._angleDegrees = 270 - a
            else:
                self._angleDegrees = 270               
                
    def upBounce(self):
        if self.isGoingUp():
            if self.isGoingRight():
                a = self._angleDegrees - 270
                self._angleDegrees = 90 - a
            elif self.isGoingLeft():
                a = 270 - self._angleDegrees
                self._angleDegrees = 90 + a
            else:
               self._angleDegrees = 90
               
    def rightBounce(self):
        if self.isGoingRight():
            if self.isGoingUp():
                a = 360 - self._angleDegrees
                self._angleDegrees = 180 + a
            elif self.isGoingDown():
                a = self._angleDegrees
                self._angleDegrees = 180 - a
            else:
               self._angleDegrees = 180
               
    def leftBounce(self):
        if self.isGoingLeft():
            if self.isGoingUp():
                a = self._angleDegrees - 180
                self._angleDegrees = 360 - a
            elif self.isGoingDown():
                a = 180 - self._angleDegrees
                self._angleDegrees = a
            else:
               self._angleDegrees = 0

