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

validFunctionList = ["e^x", "cos", "sin"]

# Finished function for finding factorial of a value (in case we need it)
def factorial(n):
  # base case
    if n == 0:
        return 1
    else:
      # recursively multiply n and previous factorial
        return n * factorial(n - 1)

# Function for calculating Taylor series approximation of a given function
def taylor(function, x):
  if(function == 'sin'):
    
  if(function == 'cos'):

  if(function == 'e^x'):
    n = 4 #test different values here, could automate this out later
    for i in range(n):
      
  

# Finished function to check error of our approximation
# Accuracy needs to be within 0.00000001 (7 zeroes)
def errorChecker(function, x, myApprox):
  if(function == 'sin'):
    realValue = math.sin(x)               # does sine
  if(function == 'cos'):
    realValue = math.cos(x)               # does cosine
  if(function == 'e^x'):
    realValue = math.exp(x)
  errorValue = abs(realValue - myApprox)  # take absolute value of difference
  print(f"Accuracy of Taylor sim for {function}: {errorValue}")


def main():
    # This while true loop will ask for function, then x until user enters both correctly.
    while True:
      try:
        function = input("Enter the function you want: (e^x, cos, sin): ")
        if function in validFunctionList:
          ## Ask user for float in range [-5,5]
          user_x = int(input(f"Enter the x you want to use in {function} (in range [-5,5]): "))
          if -5 <= user_x <= 5:
            break # leave while True loop bc function and x are valid
          print("Enter a valid x between -5 and 5 inclusive.\n")
        print("Enter a valid function such as 'e^x', 'cos', or 'sin' exactly as printed.\n")
      except Exception as e:  # just in case there's a major messup
        print(e)
    # end while true loop


    # Calculate Taylor series approximation
    myApprox = taylor(function, user_x)

    # Check error of our Taylor series approximation
    errorChecker(function, user_x, myApprox)


# weird python stuff we gotta have
if __name__ == "__main__":
    main()
