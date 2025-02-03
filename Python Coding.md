
#1.find largest element in given array?

arr = [63,54,98,34,89,42,18,100]

def max():

    max = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    print(max)

max()



#2.find smallest element in given array?

arr = [63,54,98,34,89,42,18,100]

def min():

    min = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    print(min)

min()



#3. find substrings of string?

def substring():
    str = input('Enter string')
    n = len(str)

    for i in range(n):
        for j in range(i+1,n+1):
            print(str[i:j])
substring()




#4. find count of amazing substrings of string?

#amazing substring starts with vowel

def amz():

    str = input('Enter string:')
    n = len(str)
    count = 0
    v= 'aeiouAEIOU'

    for i in range(n):
        if str[i] in vowels:
            count = (count + n-i)
    print(count)

amz()



#5. write a program to find common letters between two strings?

def twostr():

    str1 = input('Enter string 1:')
    str2 = input('Enter string 2:')

    s1 = set(str1)
    s2 = set(str2)
    s3 = s1 & s2
    print('common letters:',s3)

twostr()



#6. write a program to print left rotation of string?

def leftrotation():
    str = input('Enter string :')
    n = len(str)
    temp = str + str

    for i in range(n):
        for j in range(n):
            print( temp[i+j],end ="")
        print()

leftrotation()



#7. write a program to check rotation of two given strings?

def checkrotation():

    str1 = input("Enter first string:")
    str2 = input("Enter second string:")

    s = str1 + str1

    if (len(str1) == len(str2)):
        if str2 in s:
            print(str2,'is roated string of ',str1)
        else:
            print(str2,'is not roated string of ',str1)
    else:
        print('length of strings not matching')

checkrotation()



#8. write a program to find frquency of words in string?

def frequency(str):

    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i] = d[i]+1
    print(d)

str = 'sandeep loves eating mangoes and sandeep loves eating banana'

frequency(str)



#9. write a program to find first non repeating character in string?


def non_rep():

    str = 'sanddeepsndeep'
    n = len(str)
    d={}

    for i in str:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] +1
    print(d)

    count = 0
    for i in range(n):
        if (d[str[i]] == 1):
            print(str[i],count)
        count = count +1

non_rep()



#10. write a program to find missing number in array?

a =[1,2,3,4,6,7,8,9]

def missing():

    sum1 = sum(a)
    n = a[-1]
    sum_natural = (n*(n+1)//2)
    missing_number = sum_natural -sum1
    print(missing_number)

missing()



#11. write a program to find given number is prime or not?

#a whole number greater than 1 that cannot be exactly divided by any whole number other than itself

num = int(input('Enter value:'))

def prime():
    flag = 0
    if (num>1):
        for i in range(2,num):
            if (num % i) == 0:
                flag =1
                break
        if flag == 0:
            print(' given number is prime number')
        else:
            print('given number is not prime number')
prime()



#12. write a program to print reverse string of given string?

def reverse(str):

    str = 'sandeep'
    re_str = ''

    for i in str:
        re_str = i+re_str
    print(re_str)

reverse(str)


def reverse(str):

    str = 'sandeep'

    re_str = str[::-1]
    print(re_str)

reverse(str)



#13. write a program to print reverse words in given sentence?

def reverse():
    str = 'Python is object orinted programming language'

    li = str.split(' ')
    #li.reverse()
    #re_li = li[::-1]
    re_li = list(reversed(li))
    print(re_li)

    re_str = ' '.join(re_li)
    print(re_str)

reverse()



#14. write a program to print common elements two lists?

def common():
    l1 = [40,50,60,80,100]
    l2 = [50,100,150,200]
    l3 = list()
    count = 0
    for i in l1:
        for j in l2:
            if (i == j) :
                l3.append(i)
                count = count +1
    print(l3)
    print('No.of common elements in list',count)

common()



def common():

    s1 = set(l1)
    s2 = set(l2)

    s3 = s1&s2
    l3 = list(s3)
    print(l3)
l1 = [40,50,60,80,100]
l2 = [50,100,150,200]
common()



#15. write a program to convert two lists in dictonary?

def list_dict():
    l1 = [1,2,3,4,5,6,7]
    l2 = ['one','two','three','four','five','six','seven']
    d = dict(zip(l1,l2))
    print(d)

list_dict()



#16. write a program to convert dictonary in to tuple pair?

def dict_tup():

    for i in x.items():
        print(i)


x = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}

dict_tup()



#17. write a program to reverse list in python?


#reverse

l1 = [1,2,3,4,5,6,7,8,9,10]

l1.reverse()

print(l1)


#slicing

l2 = l1[::-1]

print(l2)


#reversed

l2 = list(reversed(l1))

print(l2)


#for

l2 = list()

n = len(l1)

for i in range(n-1,-1,-1):
    l2.append(l1[i])

print(l2)



#18. write a program to remove duplicates in python list?

#using set function

arr2 = list(set(arr))

print(arr2)


#using duplicates using empty list

arr3 = []

for i in arr:
    if i not in arr3:
        arr3.append(i)
print(arr3)


#using lambda function

dup = lambda x : list(set(x))

print(dup(arr))



#19. write a program to remove common elements from two python sets?


#symetric difference

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}

s3 = s1.symmetric_difference(s2)

print(s3)



#20. write a program to remove duplicates in python dictionary?

dict1 = {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Must","Ranz","Must","Ranz"]
}

dict2 = {}

for key,value in dict1.items():
    dict2[key] = set(value)

print(dict2)



#21.find out pairs with given sum in a array?

arr =[5,7,4,3,9,8,19,21]
sum = 26


left = 0
n = len(arr)
right = n-1

while (left <= right):
    if (arr[left]+arr[right] == sum) :
        print('sum pair values',arr[left],arr[right])
        left = left+1
        right = right-1


#22.Find minimum difference between  two elements of array?

arr =[22,59,7,4,99,19]
arr.sort()

def min_diff():
    n = len(arr)
    min_diff = 9999999
    for i in range(n-1):
        if (arr[i+1]-arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
    print(min_diff)

min_diff()



#23.Maximum Difference between two elements of array?

arr =[5,32,45,4,12,18,25]
arr.sort()

def max_diff():


    diff = - 999999999
    n = len(arr)

    for i in range(n-1):
        if ( arr[i+1] - arr[i] > diff):
            diff = arr[i+1] - arr[i]
    print(diff)
max_diff()





#24.find length of last word in string?

x = 'hello sandeep '

def last():

    arr = x.split()

    last_word = arr[-1]

    print(len(last_word))

last()


*********************************************************************************

#Lists:
*******
#convert list into string with '_' seperator:
*********************************************
works with only strings

a = ['Nookala','sandeep','patel']
seperator ='_'

b = seperator.join(a)

print(b)


#accessing elements of list using index and silce operator:
**********************************************************

l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

print( l[1])      #second element
print(l[0:6:2])   #skip one element


print( l[1][1])   #indexing
print( l[2][0])   #indexing


#access of all elements +ve ang _ve index in list using for loop:
****************************************************************


l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

n = len(l)

for i in range(n):
    print( l[i],'element +Ve Index is',i)
    print( l[i],'element -ve Index is',i-n)
	
	
#access of all elements +ve ang _ve index in list using while loop:
******************************************************************

l = [[0, 1], [0, 3], [2, 1], [2, 3], [4, 1], [4, 3]]

n = len(l)

i=0

while i<n:
    print( l[i],'element +Ve Index is',i)
    print( l[i],'element -ve Index is',i-n)

    i=i+1


#eliminate duplictes in list using set function:
#**********************************************=

l = [1,2,3,4,5,6,7,7,6,5,4,3,2,1]

s = set(l)

l1 = list(s)

print(l1)


#eliminate duplictes in list using for loop:
********************************************

l = [1,2,3,4,5,6,7,7,6,5,4,3,2,1]

l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(l1)


#find the list of unique customers:
***********************************
customer_ids =[102,105,102,103,107,109,110,109]

unique_set = set(customer_ids)    #set doesn't hold duplicates
unique_customers = list(unique_set)
print(unique_customers)


#display vowels present given word:
***********************************

l = 'hello sandeep how are you and his is a big data engineer'

vowels = 'aeiouAEIOU'

found = []

for i in l:
    if i in vowels:
        if i not in found:
            found.append(i)

print(found)



#filter even and odd values in given list:
******************************************

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#even list

def even(i):
        if i%2 == 0:
            return True
        else:
            return False

even_list = list( filter(even,l) )

print(even_list)

# odd list
def odd(i):
    if i%2 != 0:
        return True
    else:
        return False

odd_list = list( filter(odd,l))

print(odd_list)


#How to move an element to the end of a list?
*********************************************
list = [1, 2, 3, 4, 5]

list.append(list.pop(0))
print(list)


#interchange first and last elements in a list?
***********************************************
# Initialize a list
list = [1, 2, 3, 4, 5]

# Interchange first and last elements
list[0],list[-1] = list[-1],list[0]

print(list)


#Interchange first and last elements using Temporary Value?
***********************************************************
# Swap function
def swap(list):
  size= len(list)
  temp=list[0]
  list[0] = list[size-1]
  list[size-1]=temp
  return list

# Driver code
new_list = [1, 2, 3, 4, 5]
print(swap(new_list))


#Swapping first and last items in a list using tuple variable?
**************************************************************
# Swap function
def swap(list):
    get = list[0],list[-1]
    list[-1],list[0] =get
    return list

# Driver code
new_list = [1, 2, 3, 4, 5]
print(swap(new_list))


#Swap first and last values in a list in Python using * operand?
****************************************************************
# Swap function
def swap(list):
    start,*middle,end = list
    list =end,*middle,start
    return list

# Driver code
new_list = [12, 35, 9, 56, 24]
print(swap(new_list))


#Swap first and last values in a list in Python using Slicing?
**************************************************************
# Swap function using slicing
def swap_slic(list):
  if len(list)>=2:
    list = list[-1:]+list[1:-1]+list[:1]
    return list

# Driver code
new_list = [12, 35, 9, 56, 24]
print(swap_slic(new_list))



#list
#####
#1.find largest element in given array?

arr = [63,54,98,34,89,42,18,100]

def max():

    max = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    print(max)

max()



#2.find smallest element in given array?

arr = [63,54,98,34,89,42,18,100]

def min():

    min = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    print(min)

min()




#10. write a program to find missing number in array?

a =[1,2,3,4,6,7,8,9]

def missing():

    sum1 = sum(a)
    n = a[-1]
    sum_natural = (n*(n+1)//2)
    missing_number = sum_natural -sum1
    print(missing_number)

missing()



#11. write a program to find given number is prime or not?

#a whole number greater than 1 that cannot be exactly divided by any whole number other than itself

num = int(input('Enter value:'))

def prime():
    flag = 0
    if (num>1):
        for i in range(2,num):
            if (num % i) == 0:
                flag =1
                break
        if flag == 0:
            print(' given number is prime number')
        else:
            print('given number is not prime number')
prime()



#14. write a program to print common elements two lists?

def common():
    l1 = [40,50,60,80,100]
    l2 = [50,100,150,200]
    l3 = list()
    count = 0
    for i in l1:
        for j in l2:
            if (i == j) :
                l3.append(i)
                count = count +1
    print(l3)
    print('No.of common elements in list',count)

common()



def common():

    s1 = set(l1)
    s2 = set(l2)

    s3 = s1&s2
    l3 = list(s3)
    print(l3)
l1 = [40,50,60,80,100]
l2 = [50,100,150,200]
common()



#15. write a program to convert two lists in dictonary?

def list_dict():
    l1 = [1,2,3,4,5,6,7]
    l2 = ['one','two','three','four','five','six','seven']
    d = dict(zip(l1,l2))
    print(d)
    
list_dict()



#16. write a program to convert dictonary in to tuple pair?

def dict_tup():

    for i in x.items():
        print(i)


x = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}

dict_tup()



#17. write a program to reverse list in python?


#reverse

l1 = [1,2,3,4,5,6,7,8,9,10]

l1.reverse()

print(l1)


#slicing

l2 = l1[::-1]

print(l2)


#reversed

l2 = list(reversed(l1))

print(l2)


#for

l2 = list()

n = len(l1)

for i in range(n-1,-1,-1):
    l2.append(l1[i])

print(l2)



#18. write a program to remove duplicates in python list?

#using set function

arr2 = list(set(arr))

print(arr2)


#using duplicates using empty list

arr3 = []

for i in arr:
    if i not in arr3:
        arr3.append(i)
print(arr3)


#using lambda function

dup = lambda x : list(set(x))

print(dup(arr))



#19. write a program to remove common elements from two python sets?


#symetric difference

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}

s3 = s1.symmetric_difference(s2)

print(s3)



#20. write a program to remove duplicates in python dictionary?

dict1 = {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Must","Ranz","Must","Ranz"]
}

dict2 = {}

for key,value in dict1.items():
        dict2[key] = set(value)

print(dict2)



#21.find out pairs with given sum in a array?

arr =[5,7,4,3,9,8,19,21]
sum = 26


left = 0
n = len(arr)
right = n-1

while (left <= right):
    if (arr[left]+arr[right] == sum) :
        print('sum pair values',arr[left],arr[right])
        left = left+1
        right = right-1


#22.Find minimum difference between  two elements of array?

arr =[22,59,7,4,99,19]
arr.sort()

def min_diff():
    n = len(arr)
    min_diff = 9999999
    for i in range(n-1):
        if (arr[i+1]-arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
    print(min_diff)

min_diff()



#23.Maximum Difference between two elements of array?

arr =[5,32,45,4,12,18,25]
arr.sort()

def max_diff():


    diff = - 999999999
    n = len(arr)

    for i in range(n-1):
        if ( arr[i+1] - arr[i] > diff):
            diff = arr[i+1] - arr[i]
    print(diff)
max_diff()


*********************************************************
#Tuple:
*******
#convert tuple into string with '_' seperator:
*********************************************
works with only strings

a = ('Nookala','sandeep','patel')
seperator ='_'

b = seperator.join(a)

print(b)


#print sum and avg of given tuple:
**********************************
t = (1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)

n = len(t)

sum = 0

for i in range(n):
    sum = sum+i
print('sum',sum)
print('avg',sum/n)



#filter even and odd values from tuple:
***************************************

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

n = len(t)

#even
def even(i):

        if i%2 ==0:
            return True
        else:
            return False

even_tuple = tuple(filter(even,t))
print(even_tuple)

#odd

def odd(i):
    if i%2 != 0:
        return True
    else:
        return False

odd_tuple = tuple(filter(odd,t))

print(odd_tuple)

**************************************************************
#list and tuple usecases
========================

#1.Add 18% Gst amount to orders amount list and print final transformed list?
==============================================================================*
#method1:
order_amount = [100,200,50,500,400,900,1200,70]
order_amount_with_gst =[]

for i in order_amount:
    order_amount_with_gst.append(i + (i*0.18))

print(order_amount_with_gst )


#method2:
#List comprehension:

order_amount = [100,200,50,500,400,900,1200,70]
order_amount_with_gst = [i+(i*0.18) for i in order_amount]
print(order_amount_with_gst)


#2.orders amount and gst is given in tuple ,find final transformed list?
======================================================================*
#method1:
order_amount = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]
order_amount_with_gst =[]

for x in order_amount:
    order_amount_with_gst.append(x[0]+((x[0]*x[1])/100))
print(order_amount_with_gst)


#method2:
#List comprehension:
order_amount = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]
order_amount_with_gst = [x[0]+((x[0]*x[1])/100) for x in order_amount]
print(order_amount_with_gst)


#3. orders amount and gst is given in tuple ,print order amount,gst,total amount in tuple inside final list using list comprehension?
======================================================================================================================
order_amount = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]
order_tuple = [(x[0],x[1],x[0]+(x[0]*x[1]/100)) for x in order_amount]
print(order_tuple)


#4.create this nested list.nested_list = [[1,1,1],[2,4,8],[3,9,27]]
==================================================================*

#method1:
new_list=[]
for i in range(1,4):
    new_list.append([i,i==2,i==3])
print(new_list)

#method2:
#List comprehension:
new_list = [[i,i==2,i==3] for i in range(1,4)]
print(new_list)


#5.flater this nested_list = [[1,1,1],[2,4,8],[3,9,27]]
======================================================*
#method1:

nested_list = [[1,1,1],[2,4,8],[3,9,27]]
flattened_list = []

for sub_list in nested_list:
  for item in sub_list:
    flattened_list.append(item)

print(flattened_list)

#method2:
#List comprehension:
nested_list = [[1,1,1],[2,4,8],[3,9,27]]
flattened_list =[item for sub_list in nested_list for item in sub_list]
print(flattened_list)


6. Print only closed order list from orders_list =[[101,"2013-07-25 00:00:00.0",11599,"CLOSED"],
[102,"2013-07-25 00:00:00.0",256,"PENDING_PAYMENT"],
[103,"2013-07-25 00:00:00.0",12111,"COMPLETE"]]


#method1:

orders_list =[[101,"2013-07-25 00:00:00.0",11599,"CLOSED"],
[102,"2013-07-25 00:00:00.0",256,"PENDING_PAYMENT"],
[103,"2013-07-25 00:00:00.0",12111,"COMPLETE"]]

for sublist in orders_list:
        if sublist[3] == "CLOSED":
            print(sublist)
        else:
            continue


#method2:
#List comprehension:
orders_list =[[101,"2013-07-25 00:00:00.0",11599,"CLOSED"],
[102,"2013-07-25 00:00:00.0",256,"PENDING_PAYMENT"],
[103,"2013-07-25 00:00:00.0",12111,"COMPLETE"]]

closed_order =[sublist for sublist in orders_list if sublist[3] == "CLOSED"]
print(closed_order)



#7.unpack given order_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]
========================================================================*
order_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]
order_id,order_date,customer_id,order_status = order_list
print(order_status)
print(customer_id)


#8.print new list without unwanted data?
========================================
customers = [1,"Sandeep,Nookala","XXXXXXX","XXXXXX","6303 heather Plaza","Brownsville","TX",78521]

print(customers[0:2],customers[4:])



#9. combain two lists?
#######################
customers = [1,"Sandeep,Nookala","XXXXXXX","XXXXXX","6303 heather Plaza","Brownsville","TX",78521]
orders_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]

customers.extend(order_list)
print(customers)


#10.print index and element with enumerate?
==========================================*
orders_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]
for x,y in enumerate(orders_list):
  print(f"index is:{x} element is:{y}")


#11.count the number of occurences of each word?
================================================
user_list = input("Enter word with ',' separeted")
input_list = user_list.split(',')
input_list_lower = [i.lower() for i in input_list]
unique_set = set(input_list_lower)
word_count = []

for i in unique_set:
  word_count.append((i,input_list_lower.count(i)))
print(word_count)


#12.count no.of each order status?
================================*
data = """order_id,order_date,customer_id,order_status
1,2013-07-25 00:00:00.0,11599,CLOSED
2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT
3,2013-07-25 00:00:00.0,12111,COMPLETE
4,2013-07-25 00:00:00.0,8827,CLOSED
5,2013-07-25 00:00:00.0,11318,COMPLETE
6,2013-07-25 00:00:00.0,7130,COMPLETE
7,2013-07-25 00:00:00.0,12111,COMPLETE
8,2013-07-25 00:00:00.0,8827,PROCESSING
9,2013-07-25 00:00:00.0,11318,PENDING_PAYMENT
10,2013-07-25 00:00:00.0,7130,PENDING_PAYMENT"""

#header
header = data.split("\n")[0]

#split with \n and remove header
line = data.split("\n")[1:]
#split word with ,
new_list = [word.split(",") for word in line]
#creating new list with 3rd index
order_status = [word[3] for word in new_list]
#unqiue words using set
order_status_set = set(order_status)
#count of unique words in order_status list
count = [(word,order_status.count(word)) for word in order_status_set]
print(count)



assignment-1:
13.count no.of transactions each status category?

transactions = 
[
[1,100,"success"],
[2,200,"pending"],
[3,300,"success"],
[4,400,"failed"],
[5,500,"success"],
[6,600,"pending"],
[7,700,"failed"],
[8,800,"success"],
[9,900,"pending"],
[10,600,"failed"]
]


assignment-2:
14. find avg salary for each department
employees = [
[101,'john','IT',60000],
[102,'alice','HR',50000],
[103,'Bob','Finance',70000],
[104,'Emma','IT',55000],
[105,'David','Finance',75000],
[106,'Sophia','HR',48000]
]









**********************************************************
#sets:
******


#print set with even numbers in range n:
***************************************

n = int(input('Enter any number:'))

s = set(i for i in range(n) if i %2 == 0)

print(s)


#print vowels present in given word using set:
**********************************************

word = ' sandeep is big data engineer'
w = set(word)

vowels = 'aeiouAEIOU'
v = set(vowels)

s = w.intersection(v)
print(w)
print(v)
print(s)


#get unique elements from list:
********************************

dup_list = [1,2,3,4,5,5,4,3,2,1]
unique_list = list(set(dup_list))
print(unique_list)


#Find invalid order status:
***************************

order_status = {"COMPLETE","PENDING","CLOSED","PROCESSING","CANCELED","PAYMENT_REVIEW","PENDING_PAYMENT","ON_HOLD","SUSPENDED"}
valid_order_status = {"COMPLETE","PENDING","CLOSED","PROCESSING","CANCELED","PAYMENT_REVIEW","PENDING_PAYMENT"}
invalid_order_status = order_status - valid_order_status
print(invalid_order_status)


***************************************************

#Dictionary: {}
***********
#how to merge two dictionaries:
*******************************

d = {4:'sandeep',3:'satish',1:'krishna',2:'padma'}
x ={5:'sweety',6:'notty'}

d.update(x)

print(d)


d1 = {4:'sandeep',3:'satish',1:'krishna',2:'padma'}
d2 ={5:'sweety',6:'notty'}

d3 = {**d1,**d2}

print (d3)


#create a dictionary from customers data?
*******************************************

customers_raw_data = """customer_id,customer_fname,customer_lname,address,city,state,pincode
11599,Sandeep,Nookala,6303 heather Plaza,Brownsville,TX,78521
356,David,Rodr,7605 Tawny horse Falls,chicago,IL,60625
11599,Satish,Nookala,4674 pakala Road,Narsampet,TG,506132"""

#method1:
customers_header = customers_raw_data.split("\n")[0].split(',')
customers_data = customers_raw_data.split("\n")[1:]

customers_dic = {}
for i in customers_data:
    customers_dic[i.split(',')[0]] = tuple(i.split(',')[1:])
print(customers_dic)

#method2:
customers_com= {i.split(',')[0] :tuple(i.split(',')[1:]) for i in customers_data}
print(customers_com)

print(customers_header)


#create nested dictionary from given dictionary? print pincode of customer any customer?
*****************************************************************************************

customers_header = ['customer_id', 'customer_fname', 'customer_lname', 'address', 'city', 'state', 'pincode']
customers_data = {'11599': ('Satish', 'Nookala', '4674 pakala Road', 'Narsampet', 'TG', '506132'), '356': ('David', 'Rodr', '7605 Tawny horse Falls', 'chicago', 'IL', '60625')}

final_customer ={}

for key,value in customers_data.items():
  final_customer[key] = {customers_header[1]:value[0],
                     customers_header[2]:value[1],
                     customers_header[3]:value[2],
                     customers_header[4]:value[3],
                     customers_header[5]:value[4],
                     customers_header[6]:value[5]}
print(final_customer)
print(final_customer.get("11599").get("pincode"))