""""
def myfunc(x):
      try:
          return 42/x
      except ZeroDivisionError:
            print('Error: you tired to divide by zero')

print(myfunc(2))
print(myfunc(12))
print(myfunc(0))
print(myfunc(1))
"""

print("How many cats do you have?")
cats = input()
try:
      if(int(cats)>=6):
          print("That is a lot of cats")

      else:
           print("that is not that many cats")   
except ValueError :
      print("You did not enter a number")