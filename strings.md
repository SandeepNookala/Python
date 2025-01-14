
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


#find sub string in main string?
********************************

sub_str = 'B'
word = 'sandeep is BigData Engineer'
print(word.find(sub_str))


#replace sub string with new sub string?
****************************************
word = 'sandeep is BigData Engineer'
new_sun_str = 'satish'

new_word = word.replace('sandeep',new_sun_str)
print(new_word)


#Print everything after '_' ?
*****************************
name = 'sandeep_Nookala'
index = name.find('_')  #find index first occurence of character
print(name[index+1:len(name)])


#Print everything before '_'?
*****************************
name ='sandeep_Nookala'
index = name.find('_')
print(name[0:index])


#Print string by skipping one charater in between?
**************************************************
name ='sandeep_Nookala'
print(name[0:len(name):2])


#convert string into list?
*************************
name = 'sandeep nookala'

str_list = list(name)
print(str_list)


#convert string into list - using split?
****************************************
date='18-04-2022'

new_str = date.split('-')

print(new_str)


#add separator to word using join?
**********************************
works with only strings,add seperator with string

word = 'sandeep is BigData Engineer'
sep = "#"

new_string = sep.join(word)
print(new_string)


#convert list to string with space separator using join?
********************************************************

x = ['sandeep','is','bigata','Engineer']

new_str = ' '.join(x)

print(new_str)


#How to switch the first and last characters in a string Python using list?
***************************************************************************

word = 'sandeep'
str_list = list(word)
str_list[0],str_list[-1] = str_list[-1],str_list[0]
print(str_list)

new_word = "".join(str_list)

print(new_word)


#print 4th column values from below string ,remove spaces and print uppercase characters?
*****************************************************************************************
df = " 1, 2013*07*25 00:00:00.0,11599,   closed   "

new_df = df.split(",")
print(new_df[3].upper().strip())


#Print reverse string:
*********************
word = 'sandeep is BigData Engineer'

print(word[::-1])


#reverse words in given sentence?
*********************************

word = 'sandeep is BigData Engineer'

print(word)
word_list = word.split(" ")
print(word_list)

reverse_word = " ".join(reversed(word_list))
print(reverse_word)


#reverse only characters in each and every word in given sentence?
******************************************************************
word = 'sandeep is BigData Engineer'

print(word)
word_list = word.split(" ")
print(word_list)
reverse_word = " ".join(reversed(word_list))
print(reverse_word)
reverse_char = reverse_word[::-1]
print(reverse_char)


#perform concatenation,repetition and find length of strings?
*************************************************************
a = 'sandeep '
b = 'sandeep is BigData Engineer'

print('concatenation :',a+b)
print('repetation:',a*3)
print('length of b is :',len(b))


#remove spaces in string?
************************
a = '   sandeep is BigData Engineer    '
b = '     sandeep is BigData Engineer'
c = 'sandeep is BigData Engineer      '

print(b)
print(b.strip())    # it will remove both sides space
print(b.lstrip())   # it will remove left side space
print(c.rstrip())   # it will remove right side space


#find count of sub string?
**************************
word = 'sandeep is BigData Engineer'
sub_str = 'e'

print(word.count(sub_str))


#check the starting and ending of the string?
*********************************************
b = 'sandeep is BigData Engineer'

print(b.startswith('s'))
print(b.endswith('r'))


#find all positions of substring in main string?
************************************************

word = 'sandeep is BigData Engineer'
sub_str = 'e'

for i in range(len(word)):
    if word.startswith(sub_str,i):
        print(sub_str,i)


#check the type of character present in the string?
***************************************************
mix_word='isestablishedon18042021'

print(mix_word.isalpha())
print(mix_word.isalnum())
print(mix_word.isdigit())
print(mix_word.isspace())


#string formatting?
******************
e='establised'
d=18
m=4
y=2021

print(f"nookala acadamy{e} is on {d}-{m}-{y}")


# Access positive and Negitive index for each element in that string using for loop?
************************************************************************************
word = 'sandeep'
n = len(word)

for i in range(n):
    print(word[i],'+ve index:',i)
    print(word[i],'-ve index:',i-n)
	
	
# Access positive and Negitive index for each element in that string using while loop?
**************************************************************************************
word = 'sandeep'
n = len(word)
i=0
while i<n:
    print(word[i],'+ve index:',i)
    print(word[i],'-ve index:',i-n)
    i=i+1
	
	
#How to switch the first and last characters in a string Python using slice?
******************************************************************************

word = 'sandeep'

first  = word[0] 
middle = word[1:len(c)]
last   = word[-1]

new_word = last+middle+first

print(new_word)
