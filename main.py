# Authors: Ciana, Zohair, Aaron, Mateo
# F1 - Optional Project
# MATH 2472
# 12/04/2020
#
# This program uses Taylor polynomials
# to estimate values of the base-e exponential, sine,
# and cosine functions for inputs in the interval [−5, 5].
# The calculator allows the user to select a function
# (either e^x, sin x, or cos x and a real value of x from
# the interval [−5, 5], and should return the correct value
# of the function at the selected value of x, accurate to at least eight decimal places.


# Finished function for finding factorial of a value
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    f = factorial(5)
    print(f)


if __name__ == "__main__":
    main()
