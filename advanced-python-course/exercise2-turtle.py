#!/usr/bin/python3
import math
import random
from typing import final

## EX 1
#
class Point:
    def __init__(self,x=0):
        self.x = x

    def __str__(self):
        return f'Point[{self.x}]'

    def __getitem__(self,index):
        self.__check(index)
        return self.x

    def __setitem__(self,index,value):
        self.__check(index)
        self.x = value

    def __add__(self,number):
        return Bod(self.x + number)

    def __check(self,index):
        '''Index check helper
           index is invalid if not 0 and not -1
        '''
        if index not in (0,-1):
            raise ValueError(f'Index out of range: {index}')

    def distance(self):
        return abs(self.x)

    def shift(self,dx):
        self.x += dx


## EX 2
#
class Point2D(Point):
    def __init__(self,x=0,y=0):
        super().__init__(x)
        self.y = y

    def __str__(self):
        return f'Point2D[{self.x},{self.y}]'

    def __iadd__(self,number):
        self.shift(number, number)
        return self

    def __eq__(self,nextb):
        return self.x == nextb.x and self.y == nextb.y

    def __getitem__(self,index):
        self.__check(index)
        return self.x if index in (0,-2) else self.y

    def __setitem__(self,index,value):
        self.__check(index)
        if index in (0,-2):
            self.x = value
        else:
            self.y = value

    def __check(self,index):
        '''Index check helper
           index is invalid if less than -2 or greater than 1
        '''
        if index < -2 or index > 1:
            raise ValueError(f'Index out of range: {index}')

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    def shift(self,dx,dy):
        super().shift(dx)
        self.y += dy

## EX 3
#
class Point3D(Point2D):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z = z

    def __str__(self):
        return f'Point3D[{self.x},{self.y},{self.z}]'

    def __iadd__(self,number):
        self.shift(number,number,number)
        return self

    def __getitem__(self,index):
        self.__check(index)
        if index in (0,-3):
            return self.x
        return self.y if index in (1,-2) else self.z

    def __setitem__(self,index,value):
        self.__check(index)
        if index in (0,-3):
            self.x = value
        elif index in (1,-2):
            self.y = value
        else:
            self.z = value

    def __eq__(self,nextb):
        return self.x == nextb.x and self.y == nextb.y and self.z == nextb.z

    def __check(self,index):
        '''Index check helper
           index is invalid if less than -3 or greater than 2
        '''
        if index < -3 or index > 2:
            raise ValueError(f'Index out of range: {index}')

    @staticmethod
    def from_tuples(source, inverted=False):
        '''Create list of objects from source list of tuples'''

        if not isinstance(source,list):
            raise TypeError('Parameter must be a lists')

        result = list()

        for x,y,z in source:
            if inverted:
                x,y,z = -x,-y,-z
            result.append(Bod3D(x,y,z))

        return result

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def shift(self,dx,dy,dz):
        super().shift(dx,dy)
        self.z += dz

def show(data):
    for point in data:
        print(point)

class Parent:
    @final
    def print(self):
        print('printing')

class Child(Parent):
    def print(self):
        print('better print')


l,h = 10,100
points = [Point3D(random.randint(l,h),random.randint(l,h),random.randint(l,h)) for cnt in range(50)]
#show(points)

match = list(filter(lambda p:p.x + p.y >= p.z,points))
show(match)

points = Point3D.from_tuples([(1,2,3),(8,12,3)], inverted=True)
print(points[0])
print(points[1])









