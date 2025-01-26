


#1.iterables:
=============
collect of items which can be looped over loops(for/while) called iterables.

like lists,tuples,strings,set,dictionary,files and Generators are iterables.

#Example:
=========
data = [1,2,3,4,5,7,8,9,10]


#2.iterator:
============
used to iterate over iterables items(lists,tuples,strings,set,dictionary,files and Generators).
iterator uses iter() and next() functions.

#Example:
=========
#print first four values in list.

data = [1,2,3,4,5,7,8,9,10]
result = iter(data)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

#print all values in list.
data = [1,2,3,4,5,7,8,9,10]
result = iter(data)

for i in result:
    print(i)


#Generators:
============
these are user defined functions which contain yield keyword. 
Generator function is memory efficient.
the yield keyword pauses the current execution and allows it to be resumed whenever necessary.


#Example:

def f1():
    for i in range(10):
        return i
print(f1())
	
problem: it will retun only first value in range(10).

#print all values in given range(10).

def f1():
    for i in range(10):
        yield i
result = f1()
for i in result:
    print(i)


#print first four values in given range(10).

def f1():
    for i in range(10):
        yield i
result = f1()
print(next(result))
print(next(result))
print(next(result))
print(next(result))


#Decorators:
============
decorator is a function that modifies other functions. 
We call decorator function in existing function by using @ symbol.

#Example:
=========
def login_required(page):
    def inner(user_name,login_status):
        if login_status == False:
            print("Kindly Login")
            return
        return page(user_name,login_status)
    return inner

@login_required
def profile(user_name,login_status):
    print("welcome to your profile,Edit your Details")

def about():
    print("weclome to our company")

@login_required
def orders(user_name,login_status):
    print("weclome to orders page")

profile('sandeep',True)
about()
orders('padma',False)

