
#Sets: {}
******
1.set is unordered collection
2.each element is unique and is of immutable type(it won't accept list datatypes)
3.it is mutable datatype so we can add and remove elements


#creation of set:

s = set()                         #this only on function to create empty set
print(s)
print(type(s))                    #prints datatype

#create set from tuple:

order = ("closed",1,2.5,(1,2,3),"closed",1,2.5,(1,2,3))
order_set = set(order)
print(order_set)


#set with even numbers in range 10:

even_set = set(i for i in range(10) if i % 2 == 0)
print(even_set)


#functions:
***********
#add,copy,update:
*****************

order_set = {'closed', 2.5, (1, 2, 3), 1}

order_set.add(100)                        #add 100 to set
print(order_set)
sales_set = order_set.copy()              #copy set elements to another set
print(sales_set)
order_set.update(range(5))                #adds multiple elements at a time
print(order_set)


#pop,remove,discard,clear:
**************************

order_set = {'closed', 2.5, (1, 2, 3), 1}

order_set.pop()                           #removes random element
print(order_set)

order_set.remove('closed')                #removes particular element from set
print(order_set)

order_set.discard(2)                      #removes particular element from set same like remove ,if element not exists we won't get error
print(order_set)

order_set.clear()                         #removes all element from set
print(order_set)


#operators:
***********
#membership operators:
**********************
order_set = {'closed', 2.5, (1, 2, 3), 1}

print(2.5 in order_set)
print(10 not in order_set)


#math operations:
*****************
order_set = set( i for i in range(10))
even_set = set(i for i in range(5) if i%2 == 0)
odd_set = set(i for i in range(5) if i%2 !=0)

print(even_set)
print(odd_set)

#union
set_union = even_set.union(odd_set)
print(set_union)

#intersection
set_intersect = order_set.intersection(set_union)
print(set_intersect)


s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}

#difference
set_diff = s1.difference(s2)                # removes only matching elements from s2

print(set_diff)

#symetric difference
set_sym_diff = s1.symmetric_difference(s2)  # removes common elements from two python sets
print(set_sym_diff)


#1.write a program to print common elements in two lists using sets & their count?

l1 = [40,50,60,80,100]
l2 = [50,100,150,200]

comm_list = set(l1) & set(l2)

print(comm_list,len(comm_list))


#2.get unique elements from list:
********************************

dup_list = [1,2,3,4,5,5,4,3,2,1]

print(list(set(dup_list)))


#3.print vowels present in given word using set:
**********************************************

word = ' sandeep is big data engineer'

vowels = 'aeiouAEIOU'

word_set = set(word)
print(word_set)
vowels_set = set(vowels)
print(vowels_set)

word_vowels = set(word) & set(vowels)
print(word_vowels)

#or

word_vowels2 = word_set.intersection(vowels_set)
print(word_vowels2)


#4.Find invalid order status:
***************************

order_status = {"COMPLETE","PENDING","CLOSED","PROCESSING","CANCELED","PAYMENT_REVIEW","PENDING_PAYMENT","ON_HOLD","SUSPENDED"}
valid_order_status = {"COMPLETE","PENDING","CLOSED","PROCESSING","CANCELED","PAYMENT_REVIEW","PENDING_PAYMENT"}

invalid_order_status = order_status - valid_order_status
print(invalid_order_status)



**************************************************
#Dictionary: {}
***********

1.collection of key value pairs in {}.
2.values are mutable : add or remove value of particular key
3.keys are immutable: like it will not accept lists as keys
4.unordered collection


#creation of dic:
*****************
#empty dictionary:
emp_dict = {}                         
print(emp_dict)
print(type(emp_dict))

#empty dictionary using dict keyword:
new_dic = dict()                      
print(new_dic)
print(type(new_dic))

#dictionary with key and value pairs:

vehicle_dic = {"car":"4","bike":"2","bus":"8","truck":"10"}
print(vehicle_dic)
print(type(vehicle_dic))

#functions:
***********
#keys(): 

print(vehicle_dic.keys())                          #prints only keys #immutable

#values(): 
print(vehicle_dic.values())                        #prints only values #mutable

#items(): 
print(vehicle_dic.items())                         #prints keys and values in tuple pairs

#print keys values:

print('bus wheels are:',vehicle_dic['bus'])        #gives value for associated key
print('car wheels are:',vehicle_dic['car'])

#get():
print(vehicle_dic.get('train'))                   #gives none if keys doesnot exist we use get function to aviod errors
print(vehicle_dic['train'])                       #gives errors

#length
print('length of dicionary is:',len(vehicle_dic))

#copy
transport_dic = vehicle_dic.copy()                 #copy Dictionary elements to another Dictionary
print(transport_dic)

#clear
transport_dic.clear()
print(vehicle_dic)

#delete:
********
print(vehicle_dic)
del vehicle_dic['bus']                     #remove particular key values
print(vehicle_dic)

#pop():
print(vehicle_dic.pop('car'))               #remove particular key 

#popitem():
print(vehicle_dic.popitem())                #removes last iteam 

#update():
x = {'auto':'3'}
vehicle_dic.update(x)                        #add/merge two dicionaries
print(vehicle_dic)


#reassign value in Dictionary (dic Mutability):
***********************************************
vehicle_dic = {"car":"4","bike":"2","bus":"8","truck":"10"}

vehicle_dic['bus'] = 10
vehicle_dic['car'] = 5
print(vehicle_dic)


#convert list of tuples into Dictionary:

orders = [(101,10000),(102,20000),(103,15000)]

orders_list = dict(orders)
print(orders_list)
print(orders_list[102])


#convert dictionary into list:
******************************
order_dic = {101: 10000, 102: 20000, 103: 15000}

print(list(order_dic.items()))


#Covert Dictionary into string:
*******************************
join works with only strings

name_dic= {'4':'sandeep','3':'satish','1':'krishna','2':'padma'}

name_string = ' '.join(name_dic.keys())             #convert keys into string 
print(name_dic)
print(name_string)

name_string = ' '.join(name_dic.values())           #convert values into string 
print(name_dic)
print(name_string)


#write a program to convert two lists in dictonary?

l1 = [1,2,3,4,5,6,7]
l2 = ['one','two','three','four','five','six','seven']

list_dic = dict(zip(l1,l2))
print(list_dic)



#write a program to convert dictonary in to tuple pair?

x = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
print(tuple(x.items()))

#or

tuple_pairs = tuple(i for i in x.items())
print(tuple_pairs)



#write a program to remove duplicates in python dictionary?

veh_dict = {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Must","Ranz","Must","Ranz"]
}

veh_uniq = {}

for key,value in veh_dict.items():
    veh_uniq[key] = set(value)
print(veh_uniq)




#how to merge two dictionaries:
*******************************

d = {4:'sandeep',3:'satish',1:'krishna',2:'padma'}
x ={5:'shrey',6:'avey'}

d.update(x)
print(d)

#or

y = {**d,**x}
print(y)


