
Python is interpreted language and code is executed line by line.

#Comments:
**********
single line comment -    #
multiline comment   -    """    """


#Variables:
***********
course_name = "BigData"
course_fee = 30000
course_rating = 4.9
is_starting = True
total_revenue = None


#DataTypes:
***********
Holds only one value,5 main simple dataTypes.

1.int    = numericals (0,1, etc)

2.float  = decimals  (0.2,4.9, etc)

3.bool   = True or False

4.string = chareters ("sandeep","harsha" etc)

5.None   = No value


#type():
********
Gives you datatype of given variable


#Type casting:
**************
Convert one variable into another variable


#print datatype of given variable?
**********************************
course_name = "BigData"
course_fee = 30000
course_rating = 4.9
is_starting = True
total_revenue = None

print(type(course_name))
print(type(course_fee))
print(type(course_rating))
print(type(is_starting))
print(type(total_revenue ))


#print Int value by taking string?
**********************************
income = "1000"
New_income = int(income)+(int(income)*.1)

print(New_income)


#Types of operators:
********************

#A.arthmetic operations:
************************

1. addition (+)
2. multiplication (*)
3. subtraction (*)
4. division (/)
5. modulo (%) *gives reminder
6. floor (//) *gives interger
7. power (**) 


#prints outputs of the Python arthametic operators?
#**************************************************
a =10
b =10

print('addition:',a+b)
print('subtraction:',a-b)
print('multiplication:',a*b)
print('division:',a/b)
print('floor division:',a//b)
print('module:',a%b)
print('exponent',a**b)


#prints total_revenue,avg_order_price?
#*************************************
bigdata_fee =800
azure_fee   =600
bigdata_enrollments =20
azure_enrollments =40

total_revenue = (bigdata_fee*bigdata_enrollments)+(azure_fee*azure_enrollments)
avg_order_price = total_revenue/(bigdata_enrollments+azure_enrollments)
print(total_revenue)
print(avg_order_price)


#B.in and not in operaters(membership operators):
*************************************************
Name = "Sandeep Nookala"

print(sandeep in Name)
print(sandeep not in Name)


#C.is and is not operators (identity operaters):
************************************************

a ='sandeep'
b ='sandeep is big data Engineer'

print( a is b)
print(a is not b)


#D.Relational operators/comparison operators:
*********************************************

1.==

2.>

3.<

4.>=

5.<=

6.!=

a ='sandeep'
b ='sandeep is big data Engineer'

print('a is equal to b:',a==b)
print('a is greaterthen b:',a>b)
print('a is lessthen b:',a<b)
print('a is greaterthen or equal b:',a>=b)
print('a is lessthen or equal b:',a<=b)
print('a is not equal b:',a!=b)


#E.logical Operaters:
*********************
1. and
2. or
3. not

print(True and False)
print(True and True)
print(True or False)
print(False or True)
print(not True)
print(not False)


#user input function:
********************
salary = int(input("Enter your salary:"))
hike  = int(input("Enter Hike percentage:"))

New_salary = salary + ((salary*hike)/100)
print(New_salary)


#math functions:
***************
1.ceil : higer value
2.floor : lower value
3.fabs(Absolute value): removes + and -


import math
total_sales = -20.56
print(math.ceil(total_sales))
print(math.floor(total_sales))
print(math.fabs(total_sales))



#conditional statements:
***********************
1.If 
2.elif 
3.else


#prints students grades by taking user input,80 >= marks :A grade,35<= marks :Passed But B grade,35 > marks:fails?
******************************************************************************************************************
Marks =int(input("Enter your Marks:"))

if Marks>=80:
   print("A grade")
elif Marks>=35:
   print("Passed But B grade")
else:
   print("Fail")


#prints person eligible to vote or not By taking age and Crime recoders?
************************************************************************
Age = int(input("Enter your age:"))
Crime = input("Enter Yes or No:")

if Age >= 18 and Crime == 'No':
    print('Your Eligible to Vote')
else:
    print('Your Not Eligible to Vote')


#special characters:
********************
1. \  : escape character
2. \n : newline
3. \t : tab space


#DataStructures: 
****************
4 Main data structures/collection data types in python, these holds more then one value

#a.sequence: 
************
can't chages ordering

1.list = [1,2,3,4,5]

2.tuple = (1,2,3,4,5)


#b.Non-sequence:
****************
ordering not important

3.dictionary ={"animal":"cat","fruits":"apple","model":15}

4.set = {1,2,3,4,5}


#Mutable vs Immutable:
**********************

#Mutable Data Structures:
*************************

1.List

2.set

3.dictionary

#immutable Data Structures:
***************************
1.string

2.tuple


