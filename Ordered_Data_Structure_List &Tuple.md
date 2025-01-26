
#List

1.collection of different datatypes inside [].
2.ordered collection
3.mutable 


#functions

1.append()  insert value at last

2.insert()  insert value at specified index

3.extend()  join list another list

4.min()     find minimum value in list

5.max()     find max value in list

6.pop()     removes last element

7.count()   number of similar elements

8.sort()    asending order

9.reverse() desending order

10.copy()   copy of existing list .changes in copied list will not effect origin list

11.clear()  

12.len()    find Number od elements in list


#creating list in Different ways



l = [[i,j] for i in range(5) for j in range(5) if i%2  0 and j%2 !=0]           #list with range
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


#Print list and its type

list = [1,20130725 000000.0,11599,closed]
print(type(list))
print(list)


#reassign value in list (List Mutability)

list[3] = COMPLETED
print(list)


#how to add new value in list

list.append(1000)   #adding values at last
print(list)


#how to add new value in list at specified index

list.insert(1,500)  #adding values at specific index
print(list)


#how to remove value in list

list.pop()  #removes last value
print(list)


#find length,min and max value of list

orders_list = [10,111,4,5,6,7,8,10,111]
print(len(orders_list))
print(min(orders_list))
print(max(orders_list))


#find count of repated value in list

print(orders_list.count(10))


#sort list

orders_list.sort()
print(orders_list)


#reverse list

orders_list.reverse()
print(orders_list)


#clear list

l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]

print(l1.clear())


#create new list from another list

new_orders = orders_list.copy()
new_orders[1] = 100
print(new_orders)
print(orders_list)


#Membership operators

print( 10 in orders_list)
print(12 not in orders_list)

l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]
print(10 in l1)
print(100 not in l1)


#comparison operators

l1 = [[1, 3], [2, 4], [5, 6], 6, 7, 8, 9, 10]
l2 = [[1, 3], [2, 4], [5, 6]]

print(l1 == l2)
print(l1 != l2)
print(l1l2)
print(l1l2)


#math operators  concatenation ,repetition

l1 = [[1,3],[2,4],[5,6]]
l2 = [6,7,8,9,10]

l3 = l1+l2     #concatenation
l4 = l13      #repetition

print(l3)
print(l4)


#use different functions in list len,count,index

l = [0,1,0,3,2,1,2,3,4,1,4,3]

print('length of list',len(l))

print('count of given element 4 is',l.count(4))

print('index of given element 4 is',l.index(4))


#use different functions in list append,insert,extend

l1 = [1,3,2,4]

l2 = [5,6,7,8,9]

l2.append(10)          #add new element in list at end
l2.append([1,2,3,4,5])
l1.insert(0,0)         #insert new element in first position
l1.extend(l2)          #join two l2 list in l1 list

print(l2)
print(l1)


#use different functions in list remove,pop

l1 = [1,3,2,4,5]
l2 = [5,6,7,8,9,10]


l1.pop()           #removes last item in list
l2.remove(5)       #removes given element from list

print(l1)
print(l2)


#use different functions in list reverse,sort,copy

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



#Tuple

1.collection of different datatypes inside round brackets () .
2.ordered collection
3.immutable
4.Tuple takes much lesser space than a List in Python.
5.Tuple is faster than a List in Python. So it gives us good performance.
6.Since Tuple is immutable, we can use it in cases like Dictionary creation.



#functions 

tuple is immutability so functions like append,insert,pop functions won't work 

1.len() find Number od elements in list

2.min() find minimum value in list

3.max() find max value in list

4.count()

5.in

6.not in


#creatiing tuple in different ways


l = [1,2,3,4,5,5,4,3,2,1]

t = tuple(l)                         # tuple from list

print(t)
print(type(t))


a = 'sandeep is a big data engineer'

t1 = tuple(a.split(' '))              # tuple from string

print(t1)
print(type(t1))


t2 = ()                                # empty tuple
print(t2)
print(type(t2))


t3 = tuple()                           # empty tuple with tuple function
print(t3)
print(type(t3))


#Print list and its type


tuple = (1,20130725 000000.0,11599,closed)
print(type(tuple))
print(tuple)

#accessing elements by index ,slice operator


t = (1,2,3,4,5,(1,1),2,3,(4,5))
#slice operator
print(t[2])                     #gives first two elements in tuple
print( t[-1])                  #gives reverse order of tuple elements
print(t[2])                    #skips one element

# index
print(t[5][1])                   #fouth element second value


#Print length ,max and min values in tuple

orders_tuple = (10,20,1,3,0,7,10,10,7)
print(orders_tuple)
print(len(orders_tuple))
print(max(orders_tuple))
print(min(orders_tuple))


#find count of repated value in tuple

print(orders_tuple.count(10))


#Membership operators

print( 3 in orders_tuple)
print(3 not in orders_tuple)


#math operators concatenation ,repetition


t = ((1,1),(2,3),(4,5))
t1 = (1,2,3,4,5)

print('repetation',t2)                       
print('concatination',t+t1)                       


#find len,count,index,sorted,min,max of given tuple


t = (1,2,3,4,5,1,2,3,4,5)

print('length of tuple',len(t))
print('count of 5 ',t.count(5))
print('index of 5',t.index(5))
print('sorted',sorted(t))
print('max element of tuple',max(t))
print('min element of tuple',min(t))
