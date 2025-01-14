

#Strings:
*********
string is immutable,we cannot make modification on existing string.

#types of strings:
******************

'      '      : singleline Strings
"      "      : singleline Strings
"""    """    : Multiline Strings

#print strings:
***************

print('Hello world')
print('sandeep') 
print("sandeep's Pen")
print("""Hi 
sandeeep """)


#concatenation of strings with sep:
*****************************
fname = "Sandeep"
lname = "Nookala"

print("Your Name is:",fname+'_'+lname)


#string formatting(f-string):
*****************************
first_name = "sandeep"
last_name = "nookala"

print(f"my full name is {fname}_{lname}")
print(f"My first name is {first_name} my last name is {last_name}")


#length of string(len()):
*************************
print("Length of String:",len(fname))


#Indexing:
*********
1.Indexing Helps to get a one particular charater

2.represents in square brakets:[]

3.Index starts from 0

4.first character is 0

5.last character is -1


#print random characters?
*************************
name = "sandeep_Nookala"
print(name[0])
print(name[:1])
print(name[8])
print(name[:8])


#Slicing:
********
Slicing helps to get slice of charaters /piece of charaters


#print words using slice operator?
*********************************
b = 'sandeep is BigData Engineer'

print(b[0])         # first character in string
print(b[-1])        # last character in string
print(b[6])         # fifth character in string
print(b[1:6])       # second to fifth character in string


#even character positions in string?
************************************
print(b[0:len(b):2])
print(b[0::2])      


#odd character  positions in string?
************************************
print(b[1:len(b):2])
print(b[1::2])
   

#prints from 0-6 indexes?
*************************
name ='sandeep_Nookala'
print(name[0:7])  
print(name[:7])   


#prints from 8 index to till end?
*********************************
name ='sandeep_Nookala'
print(name[8:15]) 
print(name[8:])   
print(name[8:len(name)]) 


#Print last 5 characters?
*************************
name * 'sandeep_Nookala'
print(name[-5:])  
print(name[-5:len(name)])


#functions:
**********
1.startswith()  :checks string starts with given character

2.endswith()    :checks string ends with given character

3.capitalize()  :prints capital case character

4.lower()       :prints lower case characters

5.upper()       :prints upper case characters

6.title()       :prints titile case characters

7.swapcase()

8.lstrip()      :removes left side space

9.rstrip()      :removes right side space

10.strip()      :removes spaces in string

11.replace()    :repace one character with other character

12.index()      :index returns the index of 1st occurence .if not found throw exception

13.find()       :Returns index of first occurence. if not found returns:1

14.count()      :counts similar characters

15.split()      :split one string in two stringes


#change the case of strings using title,capitalise,upper,lower,swapcase?
************************************************************************
word = 'sandeep is BigData Engineer'

print(b.upper())
print(b.lower())
print(b.swapcase())
print(b.title())
print(b.capitalize())


#index():
*********
name ='sandeep_Nookala'
print(name.index("x"))


#find():
********
name ='sandeep_Nookala'
print(name.find('x'))





*****************************************************
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
**************************************************************************


#Tuple:
*******
1.collection of different datatypes inside () .
2.ordered collection
3.immutable 


#functions: 
***********
tuple is immutability so functions like append,insert,pop functions won't work 

1.len() :find Number od elements in list

2.min() :find minimum value in list

3.max() :find max value in list

4.count()

5.in

6.not in


#creatiing tuple in different ways:
***********************************

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


#Print list and its type:
*************************

tuple = (1,"2013*07*25 00:00:00.0",11599,"closed")
print(type(tuple))
print(tuple)

#accessing elements by index ,slice operator:
*********************************************

t = (1,2,3,4,5,(1,1),2,3,(4,5))
#slice operator
print(t[:2])                     #gives first two elements in tuple
print( t[::-1])                  #gives reverse order of tuple elements
print(t[::2])                    #skips one element

# index
print(t[5][1])                   #fouth element second value


#Print length ,max and min values in tuple:
*******************************************
orders_tuple = (10,20,1,3,0,7,10,10,7)
print(orders_tuple)
print(len(orders_tuple))
print(max(orders_tuple))
print(min(orders_tuple))


#find count of repated value in tuple:
*************************************
print(orders_tuple.count(10))


#Membership operators:
**********************
print( 3 in orders_tuple)
print(3 not in orders_tuple)


#math operators: concatenation ,repetition:
*******************************************

t = ((1,1),(2,3),(4,5))
t1 = (1,2,3,4,5)

print('repetation',t*2)                       
print('concatination',t+t1)                       


#find len,count,index,sorted,min,max of given tuple:
****************************************************

t = (1,2,3,4,5,1,2,3,4,5)

print('length of tuple',len(t))
print('count of 5 ',t.count(5))
print('index of 5',t.index(5))
print('sorted',sorted(t))
print('max element of tuple',max(t))
print('min element of tuple',min(t))





*****************************************************************************8
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

**************************************************
#Dictionary: {}
***********

1.collection of key value pairs in {}.
2.values are mutable : add or remove value of particular key
3.keys are immutable: like it will not accept lists as keys
4.unordered collection


#creation of dic:
*****************

d = {}                                                      #empty dictionary

print(d,type(d))

d1 = {4:'sandeep',3:'satish',1:'krishna',2:'padma'}         # key and value pairs

print(d1,type(d1))


#Print Dictionary:
******************
word = {"car":"4 wheels","bike":"2 wheels",6:"bus",(1,2,3):"three",}

print(word)


#Print any value of key:
***********************
print(word["car"])
print(word[6])


#Print value of key without error message if not exit:
******************************************************
print(word.get((1,2,3))) 
print(word.get(4))   #to aviod error will you get function


#reassign value in Dictionary (dic Mutability):
***********************************************
word = {"car":"4 wheels","bike":"2 wheels"}
word["bus"] = "6 wheels"
word["car"] = "passenger car"
print(word)


#convert list of tuples into Dictionary:
****************************************
orders_list = [(101,10000),(102,20000),(103,15000)]

orders_dic = dict(orders_list)
print(orders_dic)
print(orders_dic[102])


#prints only Dictionary keys:
*****************************
order_keys = orders_dic.keys()
print(order_keys)


#prints only Dictionary values:
*******************************
order_values = orders_dic.values()
print(order_values)


#prints only Dictionary items:
******************************
order_item = orders_dic.items()
print(order_item)


#convert dictionary into list:
******************************
order_dic = {101: 10000, 102: 20000, 103: 15000}
order_list = list(order_dic.items())
print(order_list)


#find length of dict:
*********************
print(len(order_dic))


#clear dictionary:
******************
order_dic.clear()
print(order_dic)


#Covert Dictionary into string:
*******************************
works with only strings

d = {'4':'sandeep','3':'satish','1':'krishna','2':'padma'}
seperator ='_'

b = seperator.join(d)
c = seperator.join(d.values())
print(b)
print(c)


#access elements in dic:
************************

d1 = {4:'sandeep',3:'satish',1:'krishna',2:'padma',5:'sandeep',6:'satish'}

print(d1.items())           #prints keys and vales
print(d1.keys())            #prints only keys
print(d1.values())          #prints only values
print(d1[3])                #gives value for associated key


#functions delete,clear:
************************

d = {4:'sandeep',3:'satish',1:'krishna',2:'padma',5:'sandeep',6:'satish'}

del d[6]          #remove particular element

print(d)

d.clear()         #removes all elements

print(d)


#functions len,get,pop,popitem,copy,update:
*******************************************

d = {4:'sandeep',3:'satish',1:'krishna',2:'padma'}
x ={5:'sweety',6:'notty'}


print('length of dic',len(d))
print('get 2(key) value is:',d[2])

d.pop(2)                 #remove particular key
print(d)


d.popitem()              #removes key-value pair
print(d)



d.update(x)              #adds new key value pairs from another dic
print(d)

d1 = d.copy()            #copy dic elements to another dic
print(d1)
