# -*- coding: utf-8 -*-
"""pythonDecorators.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PqSaRojH3IRwYPOTzpN0Q0_hZJ-sdLpX

##Functions are objects!

Properties of first class functions:

- [x] You can store the function in a variable.
- [x] You can pass the function as a parameter to another function.
- [x] You can return the function from a function.
- [x] You can store them in data structures such as hash tables, lists, …
"""

#storing function return values
def greet(*args):
  return "Hi " + args[0] + ". Wish you a good "+ args[1]

atnight=greet("sam","night")
atmorning=greet("sam","morning")
atevening=greet("sam","evening")

atnight

#passing function to other functions
def sport(func):
  print(f"{func[0]} is the most {func[1]} sport")

def football():
  return ["football","popular"]

sport(football())

"""##Closures
***
Function which returns inner functions which have access in  the scope even after termination of that scope/ outer function



"""

def nth_power(exp):
  def inner(base):
    return pow(base,exp)
  return inner

square=nth_power(2)
square(4)

del nth_power

square(4)

"""
##Decorators
***
Decorators are functions that takes a function as an argument, it adds some functionality to the argument function and returns a function., all without altering the code of the function we passed in"""

def decorator(func):
  def wrapper():
    print("More features were added here in wrapper function")
    return func()
  return wrapper

@decorator
def quote():
  return (f"Hey , no pain no gain - ")

quote()
# motivate = decorator(quote)
# motivate()

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper
    
@my_timer
def fibonacci(no):
  if(no<=1):
    return 1
  return fibonacci(no-1) + fibonacci(no-2)

fibonacci(3)

from functools import lru_cache

@lru_cache(maxsize=3)
def fibonacci(no):
  if(no<=1):
    return 1
  return fibonacci(no-1) + fibonacci(no-2)

def main():
  for i in range(400):
    print(i,"\t",fibonacci(i),)

main()

def root(func):
  import math
  def wrapper(*args):
    x=math.sqrt(func())
    return x
  return wrapper

def mean(func):
  def wrapper(*args):
    x=func()
    return sum(x)/len(x)
  return wrapper

def square(func):
  def wrapper(*args):
    x=func()
    for i in range(len(x)):
      x[i]=x[i]**2
    return x
  return wrapper

@root
@mean
@square
def rms():
  return [2,3,5,6]