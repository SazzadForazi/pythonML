"""
import random
import sys  
import os
import math
import pyperclip #copy/paste
x = random.randint(1, 10)
# print(x)
# sys.exit()
# print("noot overflow")

pyperclip.copy('Hello world!!')
x=pyperclip.paste()
print(x)

"""
#####################################
# def myfun():
#       print('hello!')
#       print('world!!')
# myfun()
# myfun()
# myfun()


###################################
""""
def hello(name):
      print('hello '+str(name))

hello('Alice')
hello('Bob')  
"""
####################################
"""
def myfun(num):
      return num+1;
x=myfun(125)     
print(x) 
"""
#############################################
# print("hello",end ='')
# print("world")
###########################################


# Global abd local Scopes
x=250  #global
def some_function():
      x=150 #local
      print("Inside "+ str(x))
some_function()                
print("Outside "+ str(x))