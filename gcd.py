# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers without leaving a remainder. In other words, it is the largest number that evenly divides both integers.


import math

# Example usage:
a = 8
b = 12
gcd = math.gcd(a, b)
print("GCD of", a, "and", b, "is", gcd)




# solutuion 2
def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = 86
b = 98
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')