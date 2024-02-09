#task 1

def my_recipe():
    ounces = 28.3495231 * grams
    print(ounces)

grams = float(input())

my_recipe()

#task 2

def centigrade():
    fahrenheit = float(input())
    centigrade = (5 / 9) * (fahrenheit - 32)
    print(centigrade)

centigrade()

#task 3

def solve(numheads, numlegs):
    rabbits = (numlegs - (2 * numheads)) / 2
    chickens = numheads - rabbits
    print("Rabbits:", int(rabbits))
    print("Chickens:", int(chickens))

numheads = 35
numlegs = 94

solve(numheads, numlegs)

#task 4

string = input()
list1 = [int(x) for x in string.split()]

def checkprime(n):
    if n < 2:
        return False
    for x in range(2, int(n / 2) + 1):
        if n % x == 0:
            return False
    return True

def priming(mylist):
    prime_numbers = [x for x in mylist if checkprime(x)]
    return prime_numbers

print(priming(list1))

#task 5

from itertools import permutations

def print_permutations():
    input_str = input("Enter a string: ")
    perms = permutations(input_str)
    
    for perm in list(perms):
        print(''.join(perm))

print_permutations()

#task 6

input_str = input("Enter words separated by space: ")
mylist = [str(x) for x in input_str.split()]

def reverse(mylist):
    return mylist[::-1]

print(" ".join(reverse(mylist)))

#task 7

mylist = [int(x) for x in input_str.split()]

def has_33(mylist):
    for i in range(len(mylist) - 1):
        if (mylist[i] == 3 and mylist[i+1] == 3):
            return True
    return False

print(has_33(mylist))

#task 8

input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def has_007(mylist):
    for i in range(len(mylist) - 1):
        if (mylist[i] == 0 and mylist[i+1] == 0 and mylist[i+2] == 7):
            return True
    return False

print(has_007(mylist))

#task 9

from math import *

def vol_sphere():
    v = (4 / 3) * pi * (r)**3
    print(v)

r = float(input())

vol_sphere()

#task 10

input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def uniqe(mylist):
    new = []
    for x in mylist:
        if(x not in new):
            new.append(x)
    return new

print(uniqe(mylist))

#task 11

word = input("write a word: ")

def polindrome(word):
    word2 = word[::-1]
    if(word == word2):
        return "Yes"
    else:
        return "NO"
print(polindrome(word))

#task 12

input_str = input("Enter elements separated by space: ")
mylist = [int(x) for x in input_str.split()]

def histogram(mylist):
    new_list = []  
    for x in mylist: 
        s = "*" * x  
        new_list.append(s)  
    return new_list  

result = histogram(mylist)
for x in result:
    print(x)

#task 13
    
import random
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
random = random.randint(1,20)
continue1 = True
counter = 0
while(continue1):
    counter = counter + 1
    x = int(input())
    if(x == random):
        print(f"Good job, {name}! You guessed my number in {counter} guesses!")
        continue1 = False
    else:
        print("Take a guess")

