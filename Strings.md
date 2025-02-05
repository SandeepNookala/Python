
fname = 'sandeep'
lname = 'nookala'
e='establised'
dd=18
mm=11
yyyy=2021

#concatenation of strings with sep:

full_name = fname+'_'+lname
print('My Full Name is:',full_name)

#length of string:

print(len(full_name))

#repetition:

print((fname+' ')*5)                       #concatenation and multiplication of string

#string formatting(f-string):

print(f"My full name is {fname}_{lname}")
print(f"My company is {e} on :{dd}-{mm}-{yyyy}")


#slice operator:
***************
full_name = 'sandeep_Nookala'

#print first five words using slice operator?

print(full_name[:5])

#print last five words using slice operator?

print(full_name[-5:])

#print words from 5-8 postions using slice operator?

print(full_name[5:8])

#find characters on even positions in string?

print(full_name)
print(full_name[0:len(full_name):2])

#find characters on odd positions in string?

print(full_name[1:len(full_name):2])

#Print string by skipping one charater in between?

print(full_name[:len(full_name):2])

#How to switch the first and last characters in a string Python using slice?

first = full_name[0]
mid   = full_name[1:len(full_name)-1]
last = full_name[-1]
print(last+mid+first)

#Print reverse string:

print(full_name[::-1])


#Functions:
***********

word1 = 'sandeep loves eating mangoes and sandeep loves eating banana'
word2 = ' sandeep is BigData Engineer '

#title case
print(word1.title())             #capitalize the first letter of each word in a string

#capitalise
print(word1.capitalize())        #capitalize the first letter string

#upper
print(word1.upper())

#lower
print(word1.lower())

#count
print(word1.count('x'))          # x is not exists in string

#split
print(word1.split(' '))          # split word into list with space separator

#swapcase
print(word2.swapcase())

#startswith
print(word2.startswith('a'))

#endswith
print(word2.endswith('r'))

#lstrip
print(word2.lstrip())            # it will remove left side space

#rstrip
print(word2.rstrip())            # it will remove right side space

#strip
print(word2.strip())             # it will remove both sides space

#index
print(word2.index('B'))          # returns the index of 1st occurred string. If not found throw exception

#find
print(word2.find('@'))           # returns the index of 1st occurred string. if not found returns -1

#replace
print(word2.replace(' ' ,'_'))   # replaces character in string with given character


#Print everything after '_':
name = 'sandeep_Nookala'
position = name.find('_')
print(name[position+1:len(name)])

#Print everything before '_':
name = 'sandeep_Nookala'
position = name.find('_')
print(name[:position])

#capitalize the first letter of each word in a string:

word = 'sandeep loves eating mangoes and sandeep loves eating banana'
word.title()

#join strings together

str1 = 'sandeep'
str2 = '@'
print(str2.join(str1))                      #works with only strings,add seperator with string


****************
Coding Questions
****************



#1.print all characters in given string?
****************************************
word = 'python'
def all_char():
    for i in range(len(word)):
        print(word[i])
all_char()
	
	
	
#2.print positive and Negitive indexs for each element in that string using for loop?
*************************************************************************************
word = 'sandeep'

for i in range(len(word)):
    print('for:',word[i],'+ve index:',i)
    print('for:',word[i],'-ve index:',i-len(word))
	
	
	
#3.print positive and Negitive indexs for each element in that string using while loop?
**************************************************************************************
word = 'sandeep'
i=0
while i < len(word):
    print('for:',word[i],'+ve index:',i)
    print('for:',word[i],'-ve index:',i-len(word))
    i= i+1



#4.print 4th column values from below string ,remove spaces and print uppercase characters?
*****************************************************************************************
df = " 1, 2013*07*25 00:00:00.0,11599,   closed   "

new_df = df.split(",")
print(new_df[3].upper().strip())	



#5.Write a Python program to reverse given string?
**********************************************************************
word = 'Python'

def rev_str(word):
    print(word[::-1])
rev_str(word)



#6.Write a Python program to reverse the order of words in a given string?
***************************************************************************
word = 'Python is object orinted programming language'

def rev_word(word):
    list = word.split(' ')
    result = " ".join(reversed(list))
    print(result)
    
rev_word(word)



#7.write a program to print reverse only characters in each and every word in given string?
*******************************************************************************************
word = 'Python is object orinted programming language'

def reversed_char(word):
    word_list = word.split(' ')
    reversed_word = ' '.join(reversed(word_list))
    reversed_char = reversed_word[::-1]
    print(reversed_char)

reversed_char(word)



#8.Write a Python program to check if a string is a palindrome?
***************************************************************
word = 'rotator'

def polindrome(word):
    if word == word[::-1]:
        print("Given word is polindrome")
    else:
        print("Given word is polindrome")
polindrome(word)



#9.Write a Python program to check if two strings are anagrams?
***************************************************************
word1 = 'night' 
word2 = 'thing'

word1 = 'night'
word2 = 'thing'

def anagrams():
    if sorted(word1) == sorted(word2):                      # if sorted results are same then anagrams
        print("given strings are anagrams")
    else:
        print("given strings are not anagrams")
anagrams()



#10. write a program to find given number is prime or not?
**********************************************************
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



#11.Write a Python program to check if a string contains only digits,only alpha,alpha numeric and space?
********************************************************************************************************
digits = '123456'
alpha = 'abcd'
mix_word='isestablishedon18042021'
spcae_word =' '

def is_digit():
    if digits.isdigit():
        print('given string contains digits only')
    else:
        print('given string not contains digits')

is_digit()

def is_alpnum():
    if mix_word.isalnum():
        print('given string is alpha numeric')
    else:
        print('given string is not alpha numeric')
is_alpnum()

def is_alpha():
    if alpha.isalpha():
        print('given string is alpha ')
    else:
        print('given string is not alpha')
is_alpha()


def is_space():
    if spcae_word.isspace():
        print('given string is space')
    else:
        print('given string is not space')
is_space()



#12.find length of last word in string?
***************************************
word = 'hello sandeep'

def len_last_str():
    word_list = word.split(' ')
    last_word  = word_list[-1]
    last_word_length = len(last_word)
    print(last_word_length)

len_last_str()



#substring:
***********
#13.find all possible substrings of given string?
*************************************************
word = 'python'

def all_subs():
    for i in range(len(word)):
        for j in range((i+1),len(word)+1):
            print(word[i:j])
all_subs()



#14.Write a Python program to find the index of the first occurrence of a given substring?
******************************************************************************************
word = 'sandeep'
sub_str = 'e'
print(word.find(sub_str))



#15.find all positions of substring in main string?
***************************************************
word = 'sandeep is BigData Engineer'
sub_str3 = 'a'

for i in range(len(word)):
    if word.startswith(sub_str3,i):
        print(sub_str3,i)



#16.find count of occurrences of a specific substring?
******************************************************
word = 'sandeep is BigData Engineer'
sub_str = 'e'
sub_str1 = 'ee'
print(word.count(sub_str))
print(word.count(sub_str1))



#17.find count of amazing substrings of string?
***********************************************
word = 'python'
vowel = 'aeiouAEIOU'                    #amazing substring starts with vowel
n =len(word)

def amazing_sub():                     
    count = 0
    for i in range(n):
        if word[i] in vowel:
            count = count+n-i
    print(count)
amazing_sub()



#18.Replace all occurrences of a substring with another substring?
******************************************************************
word = 'sandeep is BigData Engineer'
sub_str = 'xx'

print(word.replace('ee',sub_str))



#19.write a program to find common letters between two strings?
***************************************************************
word1 = 'sandeep'
word2 = 'satish'

def common_char():
    word1_set = set(word1)
    word2_set = set(word2)
    common_letters = word1_set & word2_set
    print(common_letters)
common_char()



#Rotation
#20.write a program to print left rotation of string?
*****************************************************
word = 'sandeep'
n = len(word)

def left_rotate():
    for i in range(n):
        print(word[i:]+word[:i])
left_rotate()



#21.write a program to print right rotation of string?
******************************************************
word = 'sandeep'
n = len(word)

def right_rotation():
    for i in range(n):
        print(word[-i:]+word[:-i])
right_rotation()



#22.write a program to check rotation of two given strings?
***********************************************************
word1 = 'sandeep'
word2 = 'eepsand'

word = word1+word1
def check_rotation():
    if len(word1) == len(word2):
        if word2 in word:
            print('word2 is roatation of word')
        else:
            print('word2 is not roatation of word')
    else:
        print('string lenth is not same')
check_rotation()



#23.Write a Python program to check if a string contains only unique characters?
********************************************************************************
word= 'sandeep'
word_set = set(word)
print(word_set)

def check_uniq():
    if len(word) == len(word_set):
        print('string contains only unique charaters')
    else:
        print('string contains duplicate charaters')
check_uniq()



#24.Write a Python program to remove all duplicates from a string and return the result?
****************************************************************************************
word = 'aabccbdcbe'

def uniq_str():
    word_set = set(word)
    uniq_word = ''.join(sorted(word_set))  #if we didn't use sorted it will generate new string each time when it runs 
    print(uniq_word)
uniq_str()



#25.write a program to find frequent/repetative characters in string?
*********************************************************************
word = 'sandeep'
dic = {}

def feq_char():
    for i in word:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] =1
    print(dic)
feq_char()



#26.Write a Python program to count the occurrences of each word in a sentence?
*******************************************************************************
word = 'sandeep loves eating mangoes and sandeep loves eating banana'

word = 'sandeep loves eating mangoes and sandeep loves eating banana'

dic = {}
def count_occu():
    word_list = word.split(' ')
    print(word_list)

    for i in word_list:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    print(dic)

count_occu()



#27.Write a Python program to find the most frequent/repetative character in a string?
**************************************************************************************
word = 'sanddeeep'
dic ={}

def most_feq_char():
    for i in word:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    print(dic)
    sorted_word = sorted(dic.values(),reverse=True)[0]

    for i in dic:
        if dic[i] == sorted_word:
            print('most frequent char in string is:',i)
most_feq_char()



#28.Write a Python program to find the second most frequent character in a string?
**********************************************************************************
word = 'sanddeeep'
dic ={}

def sec_most_feq_char():
    for i in word:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    print(dic)
    sorted_dic = sorted(dic.values(),reverse=True)[1]

    for i in dic:
        if dic[i] == sorted_dic:
            print('second most feq char is:',i)

sec_most_feq_char()



#29.write a program to find all non repeating characters in string?
*******************************************************************

def non_rep():

    str = 'aabccbdcbe'
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



#30.Write a Python program to find the longest word in a sentence?
******************************************************************
word = 'sandeep loves eating mangoes and sandeep loves eating bananaaaa'


def longest_word():
    word_list = word.split(' ')
    print(word_list)
    print(max(word_list,key= len))
longest_word()



#31.Write a program to count the number of vowels in a string?
**************************************************************
word= 'sandeep'
vowels= 'aeiouAEIOU'

def count_vowels():
    count =0
    for i in word:
        if i in vowels:
            count = count+1
    if count == 0:
        print('no vowels found')
    else:
        print('vowels count',count)

count_vowels()



#32.convert list into string with '_' seperator?
************************************************
name_list = ['Nookala','sandeep','patel']

full_name = '_'.join(name_list)
print(full_name)


#33.How to switch the first and last characters in a string Python using list?
******************************************************************************
word = 'sandeep'
word_list = list(word)
word_list[0],word_list[-1] = word_list[-1],word_list[0]
swap_word = ''.join(word_list)
print(swap_word)


#34.How to switch the first and last characters in a string Python using slice operator?
****************************************************************************************
word = 'sandeep'

word_list = list(word)
first = word_list[:1]
last = word_list[-1:]
middle = word_list[1:-1]
swap_list = last+middle+first
swap_word = ''.join(swap_list)
print(swap_word)