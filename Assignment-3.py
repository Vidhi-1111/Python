# Task 1
n= int(input(" Enter a number: "))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
result= factorial(n)
print("Factorial for the number is" ,result)

# Task 2
from math import sqrt
n= int(input("Enter a number: "))
print("Square Root: ",sqrt(n))
from math import log
print("Logarithm: ",log(n))
from math import sin
from math import radians
print("Sine: ",sin(n))

