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
======================
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




