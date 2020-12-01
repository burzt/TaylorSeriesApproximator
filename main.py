# Authors: Ciana, Zohair, Aaron, Mateo
# F1 - Optional Project
# MATH 2472
# 12/04/2020
#
# This program uses Taylor polynomials
# to estimate values of the base-e exponential, sine,
# and cosine functions for inputs in the interval [−5, 5].
# The calculator allows the user to select a function
# (either <<<<e^x, sin x, or cos x>>>>> and a real value of x from
# the interval [−5, 5], and should return the correct value
# of the function at the selected value of x, accurate to at least eight decimal places.

# Remember to Google what you wanna do. If you can do it in C++, you can do it in Python.
# and remember, indentation really matters in Python!

import math   # only used for for error checking
import enum   # enumerated values = set of symbolic names bound to unique, constant values

validFunctionList = ["e^x", "cos", "sin"]

# Finished function for finding factorial of a value
def factorial(n):
  # base case
    if n == 0:
        return 1
    else:
      # recursively multiply n and previous factorial
        return n * factorial(n - 1)

# Function to check error of our approximation
def errorChecker(type, x, myApprox):
  if(function == sine):
    # TODO: real sin(x) calculation here
    realValue = math.sin(x)
    #print(abs(realValue - myApprox))
  if(function == cos):
    #TODO: real cos(x) calculation here
    print("no error here baby :)")
    #print(abs(realValue - myApprox))
  if(function == e):
    # TODO: real e^x calculation here
    print("yo")
    #print(abs(realValue - myApprox))


def main():
    # This while true loop will keep asking User for input until it is correct
    while True:
      try:
        function = input("Enter the function you want: (e^x, cos, sin): ")
        if function in validFunctionList:
          break
        print("Enter a valid function such as 'e^x', 'cos', or 'sin' exactly as printed.\n")
      except Exception as e:  # just in case there's a major messup
        print(e)
    # end while true loop

    ## TODO

    # just here to show something
    f = factorial(5)
    print(f)


# weird python stuff we gotta have
if __name__ == "__main__":
    main()
