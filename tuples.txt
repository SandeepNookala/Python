
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