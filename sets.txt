
#Sets: {}
******
1.set is unordered collection
2.each element is unique and is of immutable type(it won't accept list datatypes)
3.it is mutable datatype so we can add and remove elements


#creation of set:
****************
s = set()                    #this only on function to create empty set

print(s)


t = (1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)

s1 = set(t)                  #set from tuple 

print(s1)


#Print set and its type:
************************
order = {"closed",1,2.5,(1,2,3),"closed",1,2.5,(1,2,3)}
print(order)
print(type(order))


# different functions add,copy,update:
**************************************

s = {10, 20, 40, 60, 80, 100}

s.add(1000)                       # add 1000 to set

print(s)


s1 = s.copy()                     # copy set elements to another set

print(s1)


s.update(range(5))                # adds multiple elements at a time

print(s)


#different functions pop,remove,discard,clear:
**********************************************


s = {0, 1, 2, 3, 4, 10, 80, 20, 100, 40, 1000, 60}

s.pop()             #removes random element

s.remove(1000)      #removes particular element from set

s.discard(2000)     #removes particular element from set same like remove ,if element not exists we won't get error

s.clear()           #removes all element from set

print(s)


#membership operators:
**********************

s = {0, 1, 2, 3, 4, 10, 80, 20, 100, 40, 1000, 60}

print( 50 in s)
print(50 not in s)



#math operations :union,intersection,difference,symmetric difference:
********************************************************************

s = set( i for i in range (10))
s1 = set( i for i in range(10) if i%2 == 0)
s2 = set( i for i in range(10) if i%2 != 0)


s3 = s.union()
print(s3)


s4 = s.intersection(s1)
print(s4)

s5 = s.difference(s1)
print(s5)

s6 = s.symmetric_difference(s1)
print(s6)


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
