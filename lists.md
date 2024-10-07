
#List:
*****
1.collection of different datatypes inside [].
2.ordered collection
3.mutable 


#functions:
**********
1.append()  :insert value at last

2.insert()  :insert value at specified index

3.extend()  :join list another list

4.min()     :find minimum value in list

5.max()     :find max value in list

6.pop()     :removes last element

7.count()   :number of similar elements

8.sort()    :asending order

9.reverse() :desending order

10.copy()   :copy of existing list .changes in copied list will not effect origin list

11.clear()  :

12.len()    :find Number od elements in list


#creating list in Different ways:
*********************************


l = [[i,j] for i in range(5) for j in range(5) if i%2 ** 0 and j%2 !=0]           #list with range
print(l)


y = 'sandeep is big data engineer'
l1 = y.split(' ')                                                                 #list from a string
print(l1)


l2 = []                                                                           #empty list
print(l2)


l3 = list()                                                                       #empty list using list function
print(l3)

print(type(l))
print(type(l1))


#Print list and its type:
*************************
list = [1,"2013*07*25 00:00:00.0",11599,"closed"]
print(type(list))
print(list)


#reassign value in list (List Mutability):
******************************************
list[3] = "COMPLETED"
print(list)


#how to add new value in list:
******************************
list.append(1000)   #adding values at last
print(list)


#how to add new value in list at specified index:
*************************************************
list.insert(1,500)  #adding values at specific index
print(list)


#how to remove value in list:
*****************************
list.pop()  #removes last value
print(list)


#find length,min and max value of list:
***************************************
orders_list = [10,111,4,5,6,7,8,10,111]
print(len(orders_list))
print(min(orders_list))
print(max(orders_list))


#find count of repated value in list:
*************************************
print(orders_list.count(10))


#sort list:
***********
orders_list.sort()
print(orders_list)


#reverse list:
**************
orders_list.reverse()
print(orders_list)


#clear list:
************
l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]

print(l1.clear())


#create new list from another list:
***********************************
new_orders = orders_list.copy()
new_orders[1] = 100
print(new_orders)
print(orders_list)


#Membership operators:
**********************
print( 10 in orders_list)
print(12 not in orders_list)

l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]
print(10 in l1)
print(100 not in l1)


#comparison operators:
**********************
l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]
l2 = [[1, 3], [2, 4], [5, 6]]

print(l1 == l2)
print(l1 != l2)
print(l1>l2)
print(l1<l2)


#math operators : concatenation ,repetition:
********************************************
l1 = [[1,3],[2,4],[5,6]]
l2 = [6,7,8,9,10]

l3 = l1+l2     #concatenation
l4 = l1*3      #repetition

print(l3)
print(l4)


#use different functions in list len,count,index:
*************************************************
l = [0,1,0,3,2,1,2,3,4,1,4,3]

print('length of list:',len(l))

print('count of given element 4 is:',l.count(4))

print('index of given element 4 is:',l.index(4))


#use different functions in list append,insert,extend:
******************************************************
l1 = [1,3,2,4]

l2 = [5,6,7,8,9]

l2.append(10)          #add new element in list at end
l2.append([1,2,3,4,5])
l1.insert(0,0)         #insert new element in first position
l1.extend(l2)          #join two l2 list in l1 list

print(l2)
print(l1)


#use different functions in list remove,pop:
********************************************
l1 = [1,3,2,4,5]
l2 = [5,6,7,8,9,10]


l1.pop()           #removes last item in list
l2.remove(5)       #removes given element from list

print(l1)
print(l2)


#use different functions in list reverse,sort,copy:
***************************************************
l1 = [1,3,2,4,5]

l2 = [6,7,8,9,10]

l1.reverse()              #reverse all items in list

l4 = reversed(l1)

l1.sort(reverse = False)  #sort -asending order


l2.sort(reverse = True)   #sort -desending order

l3 = l2.copy()            #copy all l2 list elements to l3 list

print(l1)
print(l2)
print(l3)


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
