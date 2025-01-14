
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
