'''#task 1 

import math

list1 = []
n = int(input("Сколько чисел будет в листе? "))

for i in range(n):
    i = int(input(Введите число: ))
    list1.append(i)

result = math.prod(list1)
print(result)'''


'''#task 2 

n = input()
cntUp = 0
cntLow = 0

for i in range(len(n)):
    if n[i].isupper():
        cntUp += 1
    else:
        cntLow += 1

print("Bolshih: ",cntUp)
print("Malenkih: ", cntLow)'''


'''#task 3

x = input()
revX = x[::-1]
if x == revX:
    print("Yes")
else:
    print("No")'''


'''#task 4

import time
import math

n,t = int(input()),int(input())
time.sleep(t/1000)
print(math.sqrt(n))
'''


'''#task 5

import random

def x(num):
    return True if num > 0 else False

n = int(input("Kol-vo elem: "))
tuple1 = tuple(x(random.randint(-100,100)) for i in range(n))
k = all(tuple1)

for i in tuple1:
    print(i, end=" ")
print()
print(k)'''
