#task 1

import math
class String():
    def __init__(self, string):
        self.string = string
    def printString(self):
        print(self.string.upper())

p1 = String(input())
p1.printString()


#task 2

class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2
p1 = Square(15)
print(p1.area())


#task3

class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2
class Rectangle(Square):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
p2 = Rectangle(15, 10)
print(p2.area())


#task 4

class Point():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def show(self):
        return self.x0, self.y0, self.x1, self.y1
    def move(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def dist(self):
        return (math.sqrt((self.x0 - self.x1) ** 2 + (self.y0 - self.y1) ** 2))
points = Point(1, 0, 5, 6)
points.move(0, 12, 12, 0)
print(points.dist())


#task 5

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, deposit):
        self.balance += deposit
        return self.balance
    def withdrawals(self, withdrawal):
        if self.balance < withdrawal:
            return f"You have only left {self.balance}"
        else:
            self.balance -= withdrawal
            return self.balance
a1 = Account("Rasul", 1000)
print(a1.deposit(1000))
print(a1.withdrawals(1999))
print(a1.withdrawals(2))


#task 6

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pn = list(filter(lambda x : x > 1 and all(x % y != 0 for y in range (2, int(x / 2) + 1)), numbers))
print(pn)    









































