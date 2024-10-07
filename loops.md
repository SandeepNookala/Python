
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