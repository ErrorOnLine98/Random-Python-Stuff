#####################################################
# Greatest Common Divisor Using Euclidean Algorithm #
# Adam King                                         #
# Last Updated: 5/10/2021                           #
#####################################################

# The purpose of this program is to calculate the GCD of two ints using the Euclidean algorithm.
# I originally made this to help me with Cryptography homework.

import math

print("This program calculates the greatest common divisor (GCD) of two integers.")
print("It also provides a demonstration of the steps involved to get the answer.")
print("You will provide two integers (a and b) to calculate gcd(a,b).")

a = int(input("a: "))
b = abs(int(input("b: ")))

while b > 0:
    # Demonstration of algorithm
    q = math.floor(a / b)
    print(str(a) + " = " + str(b) + " x " + str(q) + " + " + str(a % b))

    # Implementation
    c = b
    b = a % b
    a = c

print(str(a) + " is the gcd.")
