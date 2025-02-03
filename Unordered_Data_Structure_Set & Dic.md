*****************************************************************************
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




#19. write a program to remove common elements from two python sets?


#symetric difference

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}

s3 = s1.symmetric_difference(s2)

print(s3)

























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



#20. write a program to remove duplicates in python dictionary?

dict1 = {
    'car':["Ford","Toyota","Ford","Toyota"],
    'brand':["Must","Ranz","Must","Ranz"]
}

dict2 = {}

for key,value in dict1.items():
    dict2[key] = set(value)

print(dict2)



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




