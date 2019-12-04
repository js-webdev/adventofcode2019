"""
Day 3
"""
import collections

class Coords:

    x = 0
    y = 0
    steps = 0

    points = []

    def __init__(self, x_start=0 , y_start=0 ):
        self.x = x_start
        self.y = y_start
        self.steps = 0
        self.points = []

    def move(self, direction):
        axis = direction[0]
        moveTo = direction[1:]

        if(axis == 'U'):
            self.moveY(int(moveTo))
        elif(axis == 'R'):
            self.moveX(int(moveTo))
        elif(axis == 'D'):
            self.moveY(int(moveTo)*-1)
        elif(axis == 'L'):
            self.moveX(int(moveTo)*-1)
        else:
            exit('FAIL')

    def moveX(self,moveTo: int):
        if(moveTo<0):
            for xa in range(moveTo,0):
                self.steps += 1
                self.x -= 1
                self.setPoint()
        else:
            for xs in range(0, moveTo):
                self.steps += 1
                self.x += 1
                self.setPoint()
    
    def moveY(self,moveTo: int):
        if(moveTo<0):
            for ys in range(moveTo,0):
                self.y -= 1
                self.steps += 1
                self.setPoint()
        else:
            for ya in range(0, moveTo):
                self.y += 1
                self.steps += 1
                self.setPoint()

    def setPoint(self):
        self.points.append({'x':self.x, 'y': self.y, 'steps': self.steps})
    
    def getCrossings(self):
        __points = []
        __duplicates = []
        for point in self.points:
            if point not in __points:
                __points.append(point)
            else:
                __duplicates.append(point)
        return __duplicates
    
    def cleanUp(self):
        __points = []
        for point in self.points:
            if point not in __points:
                __points.append(point)
        return __points

crossed = []

lines = open('day3-input.txt','r').read().split('\n')
line_one = lines[0].split(',')
line_two = lines[1].split(',')

coords_one = Coords()
for directiono in line_one:
    coords_one.move(directiono)

coords_two = Coords()
for directiont in line_two:
    coords_two.move(directiont)

coords_one.cleanUp()
coords_two.cleanUp()
#print(line_one, len(coords_one.points))
#exit()
sum_crossed = []
sum_step = []
for p1 in coords_one.points:
    for p2 in coords_two.points:
        if p1['x'] == p2['x'] and p1['y'] == p2['y'] and p1 not in crossed:
            crossed.append(p1)
            sum_crossed.append(((p1['x'] if p1['x']>0 else (p1['x']*-1)) + (p1['y'] if p1['y']>0 else (p1['y']*-1))))
            sum_step.append((p1['steps']+p2['steps']))

sum_crossed.sort()
sum_step.sort()

print("pos")
print(sum_crossed[0])
print("steps")
print(sum_step[0])
print("Done")    
