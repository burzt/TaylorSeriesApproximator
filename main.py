# Authors: Aaron Elam, Zohair Khan, Mateo Escamilla, Ciana Pike
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

import math   # only used for for absolute value

validFunctionList = ["e^x", "cos(x)", "sin(x)"]

# Finished function for finding factorial of a value
def factorial(n):
  # base case
    if n == 0:
        return 1
    else:
      # recursively multiply n and previous factorial
        return n * factorial(n - 1)

# Function for calculating Taylor series approximation of a given function
def taylor(function, x):
  sum = 0
  n = 100   # should be sufficiently high
  allowedError = 0.00000001
  # Note: '**' denotes exponential in Python
  if(function == 'sin(x)'):
    for k in range(n):
      # Perform Taylor series approximation
      sum += (-1)**k * ((x**((2*k)+1))/factorial((2*k)+1))
      errorValue = (1/factorial(k+1))*(abs(x)**(k+1))
      # If the Taylor inequality is good, return sum. Otherwise, continue
      if(errorValue <= allowedError):
        print(f"Error of Taylor sim for {function}: {errorValue:.11f} at n = {k}")
        print(f"\nValue of {function} where x = {x} is: {sum}")
        return sum
      else:
        pass
  if(function == 'cos(x)'):
    for k in range(n):
      sum += ((-1)**k / factorial(2*k)) * x**(2*k)
      errorValue = (1/factorial(k+1))*(abs(x)**(k+1))
      # If the Taylor inequality is good, return sum. Otherwise, continue
      if(errorValue <= allowedError):
        print(f"Error of Taylor sim for {function}: {errorValue:.11f} at n = {k}")
        print(f"\nValue of {function} where x = {x} is: {sum}")
        return sum
      else:
        pass
  if(function == 'e^x'):
    for k in range(n):
      sum += x**k/factorial(k)
      errorValue = (149/factorial(k+1)) # 149 is approx max of e^5
      if(errorValue <= allowedError):
        print(f"Error of Taylor sim for {function}: {errorValue:.11f} at n = {k}")
        print(f"\nValue of {function} where x = {x} is: {sum}")
        return sum
      else:
        pass

def main():
    # This while true loop will ask for function, then x until user enters both correctly.
    while True:
      try:
        function = input("Enter the function you want: (e^x, cos(x), sin(x)): ")
        if function in validFunctionList:
          ## Ask user for float in range [-5,5]
          user_x = float(input(f"Enter the x you want to use in {function} (in range [-5,5]): "))
          if -5 <= user_x <= 5:
            break # leave while True loop bc function and x are valid
          print("Enter a valid x between -5 and 5 inclusive.\n")
        print("Enter a valid function such as 'e^x', 'cos(x)', or 'sin(x)' exactly as printed.\n")
      except Exception as e:  # just in case there's a major messup
        print(e)
    # end while true loop

    # Calculate Taylor series approximation
    myApprox = taylor(function, user_x)


# weird python stuff we gotta have
if __name__ == "__main__":
    main()