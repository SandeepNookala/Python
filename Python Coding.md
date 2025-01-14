
#string
#######

#1.Write a Python program to reverse given string?
**************************************************
word = 'Python'

def rev_str(word):
    print(word[::-1])
rev_str(word)


#2.Write a Python program to reverse the order of words in a sentence?
**********************************************************************
word = 'Python is object orinted programming language'

def rev_word(word):
    list = word.split(' ')
    result = " ".join(reversed(list))
    print(result)
    
rev_word(word)


#3.write a program to print reverse only characters in each and every word in given sentence?
*********************************************************************************************
word = 'Python is object orinted programming language'

def rev_word_char(word):
    list = word.split(" ")
    rev_word = " ".join(reversed(list))
    result = rev_word[::-1]
    print(result)
rev_word_char(word)



#4.Write a Python program to check if a string is a palindrome?
***************************************************************
word = 'rotator'

def palindrome():
    if word == word[::-1]:
        print('string is a palindrome')
    else:
        print('string is not palindrome')

palindrome()


#5.Write a Python program to check if two strings are anagrams?
***************************************************************
word1 = 'night' 
word2 = 'thing'

def anagram():
    if sorted(word1) == sorted(word2):
        print('two strings are anagrams')
    else:
        print('two strings are not anagrams')
anagram()


#6.Write a Python program to check if a string contains only digits?
********************************************************************
word = '123456'

def digit():
    if word.isdigit():
        print("given word is string contains only digits")
    else:
        print("given word is not string contains only digits")
digit()


#7.Write a Python program to capitalize the first letter of each word in a sentence?
************************************************************************************
word = 'sandeep loves eating mangoes and sandeep loves eating banana'

word_list = word.split()

def capital():
    result =' '.join(i.capitalize() for i in word_list)
    print(result)
capital()


#8.find all possible substrings of string?
******************************************
word = 'python'
n = len(word)
def sub_str(word):
    for i in range(n):
        for j in range(i+1,n+1):
            print(word[i:j])
sub_str(word)


#9.find length of last word in string?
**************************************
word = 'hello sandeep'

def last_word_len():
    list_word = word.split(' ')
    print(len(list_word[-1]))
last_word_len()


#10.Write a Python program to find the index of the first occurrence of a substring in a string?
************************************************************************************************
word = 'sandeep'
sub_str = 'e'

def first_occur():
    print(word.find('e'))
first_occur()


#11.Write a Python program to count the number of occurrences of a specific substring in a string?
**************************************************************************************************
word = 'sandeep'
sub_str = 'e'
count = 0

def first_occur():
    print(word.count(sub_str))

first_occur()


#12.find count of amazing substrings of string?
**********************************************
#amazing substring starts with vowel

word = 'python'
vowels = 'aeiouAEIOU'
n = len(word)

def amz_sub_str(word):
    count=0
    for i in range(n):
        if word[i] in vowels:
            count = count+n-i
    print(count)
amz_sub_str(word)


#13.Write a Python program to replace all occurrences of a substring with another substring?
********************************************************************************************
word = 'sandeep'
sub_str = 'ee'


def sub_rep():
    print(word.replace(sub_str,'##'))

sub_rep()


#14.write a program to find common letters between two strings?
***************************************************************
word1 = 'sandeep'
word2 = 'satish'

def comm_char():
    s1 = set(word1)
    s2 = set(word2)
    s3 = s1&s2
    print(s3)
comm_char()


#15.write a program to print left rotation of string?
****************************************************
word = 'sandeep'
n = len(word)

def left_rotation(word):
    for i in range(n):
        print(word[i:]+word[:i])

left_rotation(word)


#16.write a program to print right rotation of string?
******************************************************
word = 'sandeep'
n = len(word)

def right_rotate(word):
    for i in range(n):
        print(word[-i:]+word[:-i])
right_rotate(word)


#17.write a program to check rotation of two given strings?
**********************************************************
word1 = 'sandeep'
word2 = 'psandee'

new_word = word1+word1

def check_rotate():
    if len(word1) ==  len(word2):
        if word2 in new_word:
            print(word2, ':is ratation of word1')
        else:
            print(word2,':is not ratation of word1')
    else:
        print('word2, word1 length are not same')

check_rotate()

#18.Write a Python program to check if a string contains only unique characters?
********************************************************************************
word= 'python'
set_word = set(word)

def uniq():
    if len(set_word) == len(word):
        print('string contains only unique characters')
    else:
        print('string contains duplicate characters')

uniq()

#19.Write a Python program to remove all duplicates from a string and return the result?
****************************************************************************************
word = 'aabccbdcbe'

def dup():
    set_word = set(word)
    result = "".join(sorted(set_word))
    print(result)
dup()


#20.write a program to find frquent/repetative characters in string?
********************************************************************
word = 'sandeep'
dic ={}

def feq_char():
    for i in word:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i] =1
    print(dic)
feq_char()


#21.Write a Python program to find the most frequent/repetative character in a string?
**************************************************************************************
word = 'sanddeeep'
dic ={}

def max_feq_char():
    for i in word:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i] =1
 
    first_num = sorted(dic.values(),reverse = True)[0]
    
    for i in dic:
        if dic[i] == first_num:
            print('first most frequent character',i)
    
max_feq_char()


#22.Write a Python program to find the second most frequent character in a string?
**********************************************************************************
word = 'sanddeeep'
dic ={}

def max_feq_char():
    for i in word:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i] =1
 
    sec_num = sorted(dic.values(),reverse = True)[1]
    
    for i in dic:
        if dic[i] == sec_num:
            print('second most frequent character',i)
    
max_feq_char()


#23.Write a Python program to find the longest word in a sentence?
******************************************************************
word = 'sandeep loves eating mangoes and sandeep loves eating banana'

list_word = word.split()

def long_word():
    return max(list_word,key= len)

long_word()



#24.write a program to find all non repeating characters, first non repeating character in string?
**************************************************************************************************
word = 'aabccbdcbe'
new_list =[]

def non_rep():
    for i in word:
        if word.count(i) == 1:
            new_list.append(i)
    print("all non repeating characters",new_list)   
    print("first non reprating character",new_list[0])   
non_rep()


#25.Write a Python program to count the occurrences of each word in a sentence?
*******************************************************************************
word = 'sandeep loves eating mangoes and sandeep loves eating banana'

list_word = word.split(" ")
dic = {}

def word_feq():
    for i in list_word:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
        
    print(dic)

word_feq()


#26.Write a program to count the number of vowels in a string?
**************************************************************
word= 'sandeep'
vowels= 'aeiouAEIOU'

def count_vowels():
    count =0
    for i in word:
        if i in vowels:
            count= count+1
    
    if count == 0:
        print('no vowels found')
    else:
        print("no.of vowels are:",count)

count_vowels()


#27.Write a Python program to check if a string is a valid email address?
*************************************************************************
pip install validate_email
from validate_email import validate_email

is_valid = validate_email'sandeep3282@gmail.com',verify = True)
printbool((is_valid))


#28.Write a Python program to check if a string is a valid URL?
***************************************************************
python3 -m pip install validators
import validators

validation = validators.url("http:/www.google.com")
if validation:
print("URL is valid")
else:
print("URL is invalid")



























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


#list and tuple usecases


#1.Add 18% Gst amount to orders amount list and print final transformed list?
*******************************************************************************
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
***********************************************************************
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
**********************************************************************************************************************
order_amount = [(100,5),(200,18),(50,12),(500,18),(400,12),(900,5),(1200,18),(70,12)]
order_tuple = [(x[0],x[1],x[0]+(x[0]*x[1]/100)) for x in order_amount]
print(order_tuple)


#4.create this nested list.nested_list = [[1,1,1],[2,4,8],[3,9,27]]
*******************************************************************

#method1:
new_list=[]
for i in range(1,4):
    new_list.append([i,i**2,i**3])
print(new_list)

#method2:
#List comprehension:
new_list = [[i,i**2,i**3] for i in range(1,4)]
print(new_list)


#5.flater this nested_list = [[1,1,1],[2,4,8],[3,9,27]]
*******************************************************
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
*************************************************************************
order_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]
order_id,order_date,customer_id,order_status = order_list
print(order_status)
print(customer_id)


#8.print new list without unwanted data?
****************************************
customers = [1,"Sandeep,Nookala","XXXXXXX","XXXXXX","6303 heather Plaza","Brownsville","TX",78521]

print(customers[0:2],customers[4:])



#9. combain two lists?
#######################
customers = [1,"Sandeep,Nookala","XXXXXXX","XXXXXX","6303 heather Plaza","Brownsville","TX",78521]
orders_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]

customers.extend(order_list)
print(customers)


#10.print index and element with enumerate?
*******************************************
orders_list =[101,"2013-07-25 00:00:00.0",11599,"CLOSED"]
for x,y in enumerate(orders_list):
  print(f"index is:{x} element is:{y}")


#11.count the number of occurences of each word?
************************************************
user_list = input("Enter word with ',' separeted")
input_list = user_list.split(',')
input_list_lower = [i.lower() for i in input_list]
unique_set = set(input_list_lower)
word_count = []

for i in unique_set:
  word_count.append((i,input_list_lower.count(i)))
print(word_count)


#12.count no.of each order status?
*********************************
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
