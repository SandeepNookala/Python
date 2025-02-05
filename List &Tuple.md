
#List:
******
1.collection of different datatypes inside [].
2.ordered collection
3.mutable 

#creating list in Different ways:
*********************************
#list with range
L1 = [ [i,j] for i in range(5) for j in range(5) if i%2 ==0 and j%2 ==1 ]

print(L1)
print(type(L1))


#list from a string

word_str = 'sandeep is a big data engineer'

L2 = word_str.split(' ')
print(L2)
print(type(L2))

#empty list

L3 = []

print(L3)
print(type(L3))

#empty list using list function

L4 = list()

print(L4)
print(type(L4))


#functions:
***********
1.append()  insert value at last

2.insert()  insert value at specified index

3.extend()  join list another list

4.min()     find minimum value in list

5.max()     find max value in list

6.pop()     removes last element if index not given

7.count()   number of similar elements

8.sort()    asending order

9.reverse() reverse the elements in list 

10.copy()   copy of existing list .changes in copied list will not effect origin list

11.clear()  

12.len()    find Number elements in list

13.index   find index of particular element

#functions:
***********

list = [307,0.0,-1.3,'closed']

#reassign last value to completed in list (List Mutability)
list[3] = 'Completed'
print(list)

#how to add new value in list
list.append('sandeep')
print(list)

#how to add new value in list at specified index
list.insert(3,100)
print(list)

#how to remove value in list
list.remove('Completed')
print(list)

#how to remove value in list
list.pop()
print(list)

#find length,min and max value of list
print(max(list))
print(min(list))
print(len(list))

#find index of particular element
print(list.index(100))

#create new list from another list
sales_list = list.copy()
print(sales_list)

#combine two lists
sales_list.extend(list)
print(sales_list)

#find count of repated value in list
print(sales_list.count(100))

#sort list
sales_list.sort(reverse= True)  #desending order
print(sales_list)

sales_list.sort(reverse= False) #asending order
print(sales_list)

#reverse list
sales_list.reverse()
print(sales_list)

#clear list
sales_list.clear()
print(sales_list)


#operators:
***********
l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]
l2 = [[1, 3], [2, 4], [5, 6]]

#Membership operators

print([1,3] in l1)
print(100 not in l1)

#comparison operators

print(l1 == l2)
print(l1[:3] == l2)

#math operators  concatenation ,repetition
print(l1+l2) #concatenation
print(l1 *2) #repetition



#List Coding:
*************


#1.accessing elements of list using index and silce operator?
*************************************************************
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(l[2])              #gives second index value
print(l[2:])             #gives list of values which starts from 3rd index till last index
print(l[:2])             #gives list of first two index's values
print(l[-2])             #gives last index value
print(l[-2:])            #gives list of last two index's
print(l[:-2])            #gives list of values which start last 3 rd index to till last index


#2.accessing elements of list using index?
******************************************
l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

print(l[1])
print(l[1][1])


#3.print even ang odd index elements in list  list using for loop?
******************************************************************
l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

for i in range(len(l)):
    if i % 2 == 0:
        print('even elements',l[i])
    else:
        print('odd elements',l[i])
		

#4.print +ve ang -ve index elements in list  using for loop?
************************************************************
l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

for i in range(len(l)):
    print(l[i],'+ve index element is:',l[i])
    print(l[i],'-ve index element is:',i-len(l))
	
	
#5.print +ve ang -ve index elements in list using while loop?
*************************************************************
l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

i = 0
while i < len(l):
    print(l[i],'+ve index element is:',l[i])
    print(l[i],'-ve index element is:',i-len(l))
    i = i+1


#6.print even and odd values in given list?
********************************************
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def even_odd():
    even_list =[ i for i in l if i %2 ==0]
    odd_list = [i for i in l if i%2 !=0]
    print(even_list)
    print(odd_list)

even_odd()


#7.How to move an element to the end of a list?
***********************************************
list = [1, 2, 3, 4, 5]
list.append(list.pop(0))
print(list)


#8.Swap first and last elements in a list?
******************************************
list = [1, 2, 3, 4, 5]
list[0],list[-1] = list[-1],list[0]
print(list)


#9.Swap first and last values in a list in Python using Slicing?
****************************************************************
list = [1, 2, 3, 4, 5]

first = list[:1]
last = list[-1:]
middle = list[1:-1]
new_list = last+middle+first
print(new_list)


#10.Swap first and last values in a list in Python using * operand?
*******************************************************************
list = [1, 2, 3, 4, 5]

start ,*middle,end = list
list = end ,*middle,start
print(list)


#11.display vowels present given word?
**************************************
l = 'hello sandeep how are you and his is a big data engineer'

vowels = 'aeiouAEIOU'

vowels_list = []

for i in l :
    if i in vowels:
        if i not in vowels_list:
            vowels_list.append(i)
print(vowels_list)


#12.find largest element in given array?
****************************************
arr = [63,54,98,34,89,42,18,100]
print(max(arr))


#13.find smallest element in given array?
*****************************************
arr = [63,54,98,34,89,42,18,100]
print(min(arr))


#14.find largest element in given array without using max function?
*******************************************************************
arr = [63,54,98,34,89,42,18,100]
def max_ele():
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num =i
    print(max_num)

max_ele()


#15.find smallest element in given array without using min function?
********************************************************************
arr = [63,54,98,34,89,42,18,100]

def larg_ele():
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num =i
    print(max_num)

larg_ele()


#16.find smallest element in given array?
*****************************************
arr = [63,54,98,34,89,42,18,100]

def small_ele():
    min_ele = arr[0]
    for i in arr:
        if i < min_ele:
            min_ele= i
    print(min_ele)

small_ele()


#17.convert string into list - using split?
*******************************************
date='18-04-2022'
date_list = date.split('-')
print(date_list)


#18.write a program to find missing number in array?
****************************************************
def miss_num():
    array_sum = sum(arr)
    n= arr[-1]
    natural_sum = (n*(n+1))//2
    miss_num = natural_sum-array_sum
    print(miss_num)
miss_num()

a =[1,2,3,4,6,7,8,9]



#19.write a program to print common elements two lists with their count?
************************************************************************
l1 = [40,50,60,80,100]
l2 = [50,100,150,200]
l3 = []

def comm_ele():

    count = 0
    for i in l1:
        if i in l2:
            l3.append(i)
            count = count+1
    print('common list:',l3,'no.of elements:',count)

comm_ele()


#20.write a program to print common elements in two lists with their count using sets?
**************************************************************************************

l1 = [40,50,60,80,100]
l2 = [50,100,150,200]

l1_set = set(l1)
l2_set = set(l2)

l3 = l1_set & l2_set

print('common elements',l3,'count',len(l3))


#21.write a program to convert two lists in dictonary?
******************************************************

l1 = [1,2,3,4,5,6,7]
l2 = ['one','two','three','four','five','six','seven']
dic1 = dict(zip(l1,l2))
print(dic1)


#22.write a program to reverse list in python?
**********************************************
# using reverse keyword
l1 = [1,2,3,4,5,6,7,8,9,10]
l1.reverse()
print(l1)

#using slicing operator
l2 = [1,2,3,4,5,6,7,8,9,10]
print(l2[::-1])

#using reversed keyword
l3 = [1,2,3,4,5,6,7,8,9,10]
l4 = list(reversed(l3))
print(l4)

#using for loop
l5 = [1,2,3,4,5,6,7,8,9,10]
n= len(l5)
l6 =[]
for i in range(n-1,-1,-1):
    l6.append(l5[i])
print(l6)


#23.write a program to remove duplicates in python list?
*********************************************************
arr = [1,2,3,4,5,6,6,5,4,3,2,1]

#using set 

uni_arr = list(set(arr))

print(uni_arr)

#using empty list

uni_arr1 = []

for i in arr:
    if i not in uni_arr1:
        uni_arr1.append(i)
print(uni_arr1)

#using lambda function

uni_lambda = lambda x : list(set(x))
print(uni_lambda(arr))


#24.find out pairs with given sum in a array?
*********************************************
arr =[5,7,4,3,9,8,19,21]
sum = 26
n = len(arr)
right = 0
left = n-1

for i in arr:
    if arr[right]+arr[left] == sum:
        print(arr[right],arr[left])
        right= right+1
        left= left-1


#25.Find minimum difference between  two elements of array?
***********************************************************
arr =[22,59,7,4,99,19]
arr.sort()
def min_diff():
    n = len(arr)
    min_dif = 9999999
    for i in range(n-1):
        if arr[i+1]-arr[i] < min_dif:
            min_dif = arr[i+1]-arr[i]
    print(min_dif)

min_diff()



#26.Maximum Difference between two elements of array?
*****************************************************
arr =[5,32,45,4,12,18,25]
arr.sort()

def max_diff():
    max_diff = -999999
    n = len(arr)
    for i in range(n-1):
        arr[i+1] -arr[i] > max_diff
        max_diff = arr[i+1] -arr[i]
    print(max_diff)
max_diff()



*********************************************************
#Tuple:
*******

1.collection of different datatypes inside round brackets () .
2.ordered collection
3.immutable
4.Tuple takes much lesser space than a List in Python.
5.Tuple is faster than a List in Python. So it gives us good performance.
6.Since Tuple is immutable, we can use it in cases like Dictionary creation.

#creating tuple in different ways:
**********************************

l = [1,2,3,4,5,5,4,3,2,1]

# tuple from list
tup1 = tuple(l)
print(tup1)
print(type(tup1))

# tuple from string
a = 'sandeep is a big data engineer'
tup2 = tuple(a.split(" "))
print(tup2)
print(type(tup2))

# empty tuple
tup3 = ()
print(tup3)
print(type(tup3))

# empty tuple with tuple function
tup4 = tuple()
print(tup4)
print(type(tup4))

#functions:
***********

tuple is immutability so functions like append,insert,pop functions won't work 

1.len()     find Number of elements in tuple

2.min()     find minimum value in tuple

3.max()     find max value in tuple

4.count()   find count of similar elements 

5.index()   find index of particular element

6.sorted()  sort the given tuple

#functions:
**********

#accessing elements by index ,slice operator:
*********************************************
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,(11,12))

#slice operator:

print(t[2])              #gives second index value
print(t[2:])             #gives tuple of values which starts from 3rd index till last index
print(t[:2])             #gives tuple of first two index's values

print(t[-2])             #gives tuple index value
print(t[-2:])            #gives tuple of last two index's
print(t[:-2])            #gives tuple of values which start last 3 rd index to till last index

#index:
print(t[-1][1])          


#Print length,max and min values in tuple:
******************************************
orders_tuple = (10,20,1,3,0,7,10,10,7)

print(max(orders_tuple))                             
print(min(orders_tuple))
print(len(orders_tuple))
print(orders_tuple.count(10))
print(sorted(orders_tuple))
print(orders_tuple.index(0))


#operators:
***********
orders_tuple = (10,20,1,3,0,7,10,10,7)
sales_tuple =  (7,10,10,7)

#Membership operators:
**********************
print( 3 in orders_tuple)
print(11 not in orders_tuple)

#comparison operators:
**********************
print(orders_tuple != sales_tuple)
print(orders_tuple[5:] == sales_tuple)


#math operators concatenation ,repetition:
******************************************
print('repetation',(sales_tuple)*3)
print('concatination',(sales_tuple)+(orders_tuple))


#1.convert tuple into string with '_' seperator:
*********************************************
works with only strings

a = ('Nookala','sandeep','patel')
print(a)
print('_'.join(a))


#2.print sum and avg of given tuple using for loop:
**************************************************
t = (1,2,3,4,5)
n = len(t)
sum = 0
for i in range(n):
    sum = sum+t[i]
print('sum',sum)
print('avg',sum/n)


#3.print sum and avg of given tuple:
************************************
t = (1,2,3,4,5)
print('sum',sum(t))
print('avg',sum(t)//len(t))

#4.print even and odd values from tuple:
*****************************************
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
even_list = []
odd_list = []

for i in t :
    if i %2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(tuple(even_list))
print(tuple(odd_list))

#5.print even and odd values from tuple using filter function:
**************************************************************
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

def even(i):
    if i%2 == 0:
        return True
    else:
        return False
even_tup = tuple(filter(even,t))
print(even_tup)

def odd(i):
    if i%2 != 0:
        return True
    else:
        return False
odd_tup = tuple(filter(odd,t))
print(odd_tup)


#6.write a program to convert dictonary in to tuple pair?
*********************************************************

dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
print(tuple(dic.items()))

#or

for i in dic.items():
    print(i)



