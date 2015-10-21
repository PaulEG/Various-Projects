from graphics import *
from random import randint
from random import random

class Tablet:
    def __init__(self, p):
        self.survives = True
        self.p = p
    def oneYearPasses(self):
        if random() < self.p:
            self.survives = False
    def survives(self):
        return self.survives
        
class Archive:
    def __init__(self,p):
        self.terminationYear = randint(1,200)
        self.startYear = max(0,self.terminationYear-50)
        self.tablets = []
        self.p = p
        for i in range(self.startYear, self.terminationYear):
            yearlyTablets = []
            for j in range(0, 10):
                yearlyTablets.append(Tablet(self.p))
            self.tablets.append(yearlyTablets)
    def getTerminationYear(self):
        return self.terminationYear
    def getStartYear(self):
        return self.startYear
    def ageArchive(self):
        for i in range(self.terminationYear-self.startYear):
            for j in range(i):
                for tablet in self.tablets[j]:
                    tablet.oneYearPasses()
    def getSurvivors(self):
        survivors =[]
        for i in range(len(self.tablets)-1):
            yearlyTabletCounter = 0
            for j in self.tablets[i]:
                if j.survives:
                    yearlyTabletCounter = yearlyTabletCounter + 1
            survivors.append(yearlyTabletCounter)
        return survivors

def main():
    print("This program simulates the superposition of a number of dead archive curves.")
    print("It assumes that within each archive tablets had a contant probability of being")
    print("lost before that archive as a whole was deposited.")
    p = eval(input("Please enter the probabilty a tablet will be lost in a given year: "))
    number = eval(input("Please enter the number of archives to simulate: "))
    totalTablets =[]
    for year in range(200):      #make empty list of years
        totalTablets.append(0)
        
    for i in range(5):
        tablets = Archive(p)
        tablets.ageArchive()
        startYear = tablets.getStartYear()
        survivors = tablets.getSurvivors()
        for year in range(len(survivors)-1):
            totalTablets[startYear + year] = totalTablets[startYear + year] + survivors[year]
    win = GraphWin("Dead archive curve", 1200,400)
    win.setCoords(0, 0, 200, number*2 + 1)
    for i in range(200):
        Rectangle(Point(i,0), Point(i+1, totalTablets[i])).draw(win)
            

main()
    

