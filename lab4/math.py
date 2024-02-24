#task 1

from math import *

degree = float(input("Input degree: "))

print("Output radian: ", (degree * pi)/180)

#task 2

from math import *

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

print("Expected Output: ", (base1 + base2) * height / 2)

#task 3

from math import *

n = int(input("Input number of sides: "))
l = float(input("Input the lenght of a side: "))
apothem = l / (2 * tan(pi / n))
area = int((n * l * apothem) / 2)

print("The area of the polygon is: ", area)

#task 4

from math import *
l = float(input("Lenght of base: "))
h = float(input("Height of parallelogram: "))

print("Expected Output: ", l * h)