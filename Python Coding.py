
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
