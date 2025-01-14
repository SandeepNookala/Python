

#Loops:
******
1.For loop
2.while loop


#print all elements,their data types:
*************************************
list1 =[1,"2013*07*25 00:00:00.0",11599,"closed"]

for i in list1:
    print(f"Element:{i} dataType:{type(i)}")


#print sum of first n numbers:
******************************
x = int(input("Enter Starting range:"))
y = int(input("Enter Ending Range"))

numbers =range(x,y)  
sum = 0

for i in numbers:
    sum = sum+i
print(sum)


#find sum of integers from order_amounts using for loop:
********************************************************
order_amount = [100,200,None,"invalid",300,400.5]
sum = 0
for i in order_amount:
    if type(i) == int or type(i) == float:
        sum = sum+i
    else:
        continue
print(sum)


#find sum of integers from order_amounts using while loop:
**********************************************************

order_amount = [100,200,None,"invalid",300,400.5]

i=0
sum=0
while i <len(order_amount):
    if type(order_amount[i]) == int or type(order_amount[i]) == float:
        sum = sum+order_amount[i]
    else:
        i=i+1
        continue
    i=i+1

print(sum)


#find the list of unique customers:
***********************************
customer_ids =[102,105,102,103,107,109,110,109]

unique_customers=[]
for i in customer_ids:
    if i not in unique_customers:
        unique_customers.append(i)
    else:
        continue
print(unique_customers)


#print even and odd numbers in any given range using for loop?
**************************************************************

n = int(input('Enter any Number:'))

for i in range(1,n+1):
    if i%2 == 0:
        print('Even Number',i)
    else:
        print('odd Number',i)
		
			
#print even and odd numbers in any given range using while loop?
****************************************************************

n = int(input('Enter any number:'))
i=1
while i <= n :
    if i%2 == 0:
        print('even number:',i)
    else:
        print('odd number:',i)
    i = i+1
	
	
#print only even numbers in any given range using continue?
***********************************************************

n = int(input('Enter any number:'))

for i in range(1,n+1):
    if i % 2 != 0:
        continue
    print('Even numbers',i)
	


functions:
==========

#write a function to print hello?
#================================

def greeting():
    print( 'hello world')
greeting()



#write a function to take name as input and print wish message by name?
#======================================================================

def wish(name):
    print('hello',name,'how are you')

wish('sandeep')
wish('satish')
wish('krishna')



#write a function to take two numbers as input and print its sum and  squre value?
#=================================================================================

def fun(a,b):

    print('sum',a+b)
    print('avg',a+b/2)

fun(10,20)
fun(20,30)



#write a function to take number as input check whether it is even or odd?
#=========================================================================

def fun(a):

    if a%2 == 0:
        print(a,'Even number')
    else:
        print(a,'odd number')

fun(10)
fun(11)


#write a function to find factorial of given number using function and while loop?
#=================================================================================

def fact(n):

    num =1
    while n>=1:
        num = n*num
        n = n-1
    print('factorial',num)

fact(3)
fact(4)
fact(5)


#write a function to find factorial of given number using function and for loop?
#==============================================================================


def fact(n):
    num =1
    for i in range(1,n+1):
        num = num*i
    print('factorial',num)
fact(3)
fact(4)
fact(5)



#factorial using inbuilt function:
#=================================

from math import *

print(factorial(3))

print(factorial(4))

print(factorial(5))



#return multipule values from function:
#======================================

def fun(a,b,c):

    summ = a+b+c
    multi = a*b*c
    avg = (a+b+c)/3

    print(summ,multi,avg)


fun(10,10,10)



#default arguments:
#==================

def arg(a = 'guest',b= 27):

    print('hai',a,'your age is:',b)

arg()



#keyword arguments:
#=================

def arg(a,b):


    print('i am',a,'i am working as',b)


arg('sandeep','Data Engineer')
arg('satish','Java Developer')


#variable length arguments:
#=========================

def arg(*s):

    for i in s:
        print(i)

arg(10,20,30,40,50)


##sum of given all numbers variable parameter:
#=============================================


def sum(*a):
    sum =0
    for i in a:
        sum = sum+i

    print (sum)

sum(10,10,10,10)


#global variables:
#=================

a= 10      #variable defined outside the function-global variable
def fun():
    print(a)

fun()


#local variables:
#================

a= 10

def fun():
    a=12    ##variable defined inside the function-local variable
    print(a)
fun()


#anonymous(lambda) function:
#===========================

#find sum and square of given numbers using anonymous function:
#==============================================================

summ = lambda x,y,z: x+y+z
mul = lambda x,y: x**y

print(summ(10,10,10))
print(mul(10,10))


#find biggest value of given values:
#===================================

big_small  = lambda x,y: x if x>y else y
print(big_small(10,9))



#filter even and values from list using lambda:
#==============================================

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even = list(filter(lambda x: x%2 == 0,l))

odd =  list(filter(lambda x:x%2 !=0,l))

print (even)
print(odd)



#filter even and odd values from tuple of 10 range using lambda:
#===============================================================

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


even =  tuple(filter(lambda x: x%2 ==0 ,t))

odd = tuple(filter(lambda x: x%2 != 0,t))

print(even)
print(odd)


#map:
=====

#print square of given tuple using lambda and map:
#=================================================

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


sq_tuple = tuple(map(lambda x:x*x,t))  #apply some functionality on every element in sequence generates new element
print(sq_tuple)



#multiple two list using lambda and map
#=======================================

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t1 = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

two_tuple = tuple(map(lambda x,y : x*y ,t,t1))

print(two_tuple)


#Reduce:
#=======

# Sum ,multiple all elements in list using reduce function
#==========================================================

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import *

sum = reduce(lambda x,y : x+y ,t)

mul = reduce(lambda x,y: x*y ,t)

print(sum)
print(mul)


#Nested Function: prints only outer functions
#===============


def out():
    print('outer function')

    def inn():
        print('inner function')

    print('second outer')

out()


#Nested Function:prints both outer and inner functions
#===============


def out():
    print('outer function')

    def inn():
        print('inner function')
    inn()

    print('second outer')

out()