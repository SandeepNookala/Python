

#File Handling:
*************
Reading,writing,deleting,creating of File

#modes:
******
r-Read
w-write
a-append
r+-Read write
w+-write Read  

#process:
********
1)open()
2)read/write
3)close()


#read file
**********
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file1.read())
file1.close()

#read firstline for file
************************
firstline = open("D:\Big_Data\DataSets\word.txt",mode='r')
print(firstline.readline())
firstline.close()

#convert lines into list format
*******************************
list = open("D:\Big_Data\DataSets\word.txt",mode='r')
print(list.readlines())
list.close()


#write to file
**************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='w')
file1.write('Hi sandeep!')
file1.close()


#append to file
***************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='a')
file1.write('How are you?')
file1.close()

#read+write file
****************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='r+')
print(file1.read())
file1.write('how about you?')
file1.close()


#write+read file
****************
file1 = open("D:\Big_Data\DataSets\word1.txt",mode='w+')
file1.write('i am a big data engineer')
file1.seek(0)
print(file1.read())
file1.close()



#with read statment:
********************
with open("D:\Big_Data\DataSets\word1.txt",'r') as File:
    File=File.read()
    print(File)


#with write statment:
*********************
with open("D:\Big_Data\DataSets\word1.txt",'w') as File:
    File.write('How are you?')
	 
	
#tell:
******
tells current position of the pointer

file = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file.read())
print(file.tell())          #gives cursor location
file.close()

#seek:
******
moves cursor pointer to specified location
file = open("D:\Big_Data\DataSets\word1.txt",mode='r')
print(file.read())
file.seek(0)                   #moves cursor location to first index
print(file.tell())
file.close()


*************************************************

#Error /Exception handling:
***************************
Interupting Normal Excecution of a code


try:
  risky code
except:
  print('Error')
else:
  print('No Error')
finally:
  print('always prints message')

#Example:
********
balance = 550.90

try:
    deposit = float(input('Enter amount:'))
except ValueError:
    print("please Enter valid amount")
else:
    final_Balance = balance+deposit
    print(final_Balance)
finally:
    print("Thank you")
	
***************************************************

#1.module:
**********
is a single file(.py) containing python code. it can include functions classes and variables that can reuse in other programs.

#Example:
*********
1.mymodule.py

person = {'name': 'sandeep','age':30}
def say_hello(name):
    return print(f"hello,{name}!,How are you?")

def say_bye(name):
    return print(f"hello,{name},take care!")


2.practice.py

import mymodule
mymodule.say_hello('sandeep')
mymodule.say_bye('padma')

from mymodule import person
print(person['age'])


Results:

hello,sandeep!,How are you?
hello,padma,take care!
30


#2.packages:
************
collection of modules organized in directory with an __init__.py file.it allows to structure your python projects logically.

#Example:
my_pacakage/
    __init__.py
	math_utils.py
	mymodule.py
	string_utils.py

from my_pacakage import math_utils,mymodule,string_utils

#3.library:
***********
A library is a collection of modules and packages that provide pre-written functionality for your program.libraries are typically larger and more feature rich than packages or modules.

#Example:
import pandas as pd
import seaborn as sb


#4.pip:
*******
pip stands for "pip installs packages".it is tha package manager for python that allows you to install ,update and manage python libraries/packages from python package index(PyPi)

#Example:
pip install pandas
pip install seaborn
