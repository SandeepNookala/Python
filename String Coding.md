
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