#####################################################
# Greatest Common Divisor Using Euclidean Algorithm #
# Adam King                                         #
# Last Updated: 1/27/2022                           #
#####################################################

# The purpose of this program is to calculate the GCD of two ints using the Euclidean algorithm.
# I originally made this to help me with Cryptography homework.

import math


def gcd(a, b):
    while b > 0:
        # Demonstration of algorithm
        q = math.floor(a / b)
        print("\n")
        print(str(a) + " = " + str(b) + " x " + str(q) + " + " + str(a % b))

        # Implementation
        c = b
        b = a % b
        a = c

    return a


def main():
    print("This program calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.")
    print("It also provides a demonstration of the steps involved to get the answer.")
    print("You will provide two integers (a and b) to calculate gcd(a,b) = gcd(b, a % b).")
    print("The program will then print the steps and the answer.")
    print("Note: The program will not work if you provide a negative number for b. The program will automatically "
          "make b positive.\n")
    print("gcd(a,b)")

    a = int(input("a: "))
    b = abs(int(input("b: ")))

    print("\n" + str(gcd(a, b)) + " is the gcd.")


if __name__ == "__main__":
    main()
