from graphics import *
from time import sleep
from random import randint

class zombie:
    def __init__(self, point, window, speed):
        self.body = Circle(point,1)
        self.body.draw(window)
        self.win = window
        self.speed = speed
        self.killing = False
    def killing(self):
        return self.killing
    def move(self, target):
        location = self.body.getCenter()
        if (location.getX()-target.getX())**2+(location.getY()-target.getY())**2 < 1:
            self.killing = True
        else:
            if location.getX() > target.getX():
                self.body.move(-self.speed,0)
            else:
                self.body.move(self.speed,0)
            if location.getY() > target.getY():
                self.body.move(0,-self.speed)
            else:
                self.body.move(0,self.speed)
    def killCheck(self, hit):
        location = self.body.getCenter()
        if (location.getX()-hit.getX())**2+(location.getY()-hit.getY())**2 < 1:
            return True
        else:
            return False
    def kill(self):
        self.body.undraw()
class counter:
    def __init__(self, win, point, text, number):
        self.text = text
        self.point = point
        self.object = Text(point, text.format(number))
        self.object.draw(win)
        self.win = win
        print(text)
    def fix(self, number):
        self.object.undraw()
        self.object = Text(self.point, self.text.format(number))
        self.object.draw(self.win)

def main():
    win = GraphWin("Zombie attack!", 400,600)
    win.setCoords(0,0, 100,150)
    target = Circle(Point(50,50),1)
    target.setFill('red')
    target.draw(win)
    zombies = []
    hitPoints = 100
    killCount = 0
    killCounter = counter(win,Point(25,125),"Kills: {0}", killCount)
    hitCounter = counter(win,Point(75,125),"Hit Points: {0}", hitPoints)
    win.getMouse()
    #make the zombies
    for i in range(4):
        zombies.append(zombie(Point(randint(0,100),randint(0,100)), win, 0.01))
    #one game moment
    for t in range(100000):
        sleep(0.01)
        for i in zombies:
            if i.killing:
                print("You are being eaten by a zombie, hit points = {0}".format(hitPoints))
                hitPoints = hitPoints -1
                hitCounter.fix(hitPoints)
        p = win.checkMouse()
        for i in zombies:
            try:
                if i.killCheck(p):
                    i.kill()
                    zombies.remove(i)
                    killCount = killCount+1
                    killCounter.fix(killCount)
                    if randint(0,1)==0:
                        for i in range(2):
                            zombies.append(zombie(Point(randint(0,100),randint(0,100)), win, 0.01))
                    else:
                            zombies.append(zombie(Point(randint(0,100),randint(0,100)), win, 0.1-.09/killCount))
                    break
            except:
                break
        for i in zombies:
            i.move(target.getCenter())
        if hitPoints <= 0:
            break
    print("You killed {0} zombies".format(killCount))
main()
