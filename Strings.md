

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










