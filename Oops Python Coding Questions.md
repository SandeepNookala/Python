

#student class,constructor with instance variables, instance methods 

class student:                                  #class
    
    def __init__(self):                         # constructor with instance variables
        self.name="sandeep"
        self.rollno=382                         #instance variables
        self.marks=91
        
    def display(self):                          #instance method
        print("student name is :",self.name)
        print("student rollno is:",self.rollno)
        print("student marks are:",self.marks)
        
s=student()                                     # s is object
s.display()




#student class ,constructor,Instance method

class student:                                             #class
    
    a=100                                                  # static varibale (defined outside method)
    b=200
    
    def __init__(self,name,rollno,branch):                 #constructor 
        self.name=name
        self.rollno=rollno
        self.branch=branch
        
    def show(self):                                         #instances method 
        print("Student name is :",self.name)
        print("student Rollno is :",self.rollno)
        print("student brach is :",self.branch)
        
s1=student("sandeep",382,"mech")                             #s1 and s2 are objects
s2=student("satish",561,"cse")

s1.show()
s2.show()
print(s1.a,s2.b)






#differnt types of variables

class student():
    
    a=1000                      #static variable
    
    def marks(self):
        self.marks=100         #Instance variable
        print("marks",self.marks)
        
    def value(self): 
        b=200                  # local Variable
        print("value",b)
        
s=student()  

print(s.a)

s.marks()
s.value()





#different types of methods

class student:
    
    books=100
    
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
    def display(self):                  #Instance Method
        print("name",self.name)
        print("roll",self.roll)
        print("marks",self.marks)
        
    @staticmethod
    def avg(x,y):                        #static method
        print("avg",(x+y)/2)
    @staticmethod
    def sum(x,y):
        print("sum",x+y)
    @classmethod                         #class method
    def study(cls):
        print("books",cls.books+100)
    
s=student('sweety',382,98)

s.display()
s.avg(10,20)
s.sum(10,20)
s.study()





#class inside class

class outer():
    
    def __init__(self):
        print("outer class")
        
    class inner():
        
        def __init__(self):
            print("inner class")

o=outer()
i=o.inner()





#brain class inside human class 
class human:
    def __init__(self):
        self.name="sandeep"
        self.brain=self.brain()
    
        
    def show(self):
        print("hello",self.name)
        
    class brain:
        def show(self):
            print("thinking")
        
h=human()

h.show()
h.brain.show()




#class laptop inside student class

class student:
    
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        self.lap=self.laptop()
        
    def show(self):
        print("name is :",self.name," " ,"rollno is:",self.roll," ","marks are:",self.marks)
        self.lap.show()
        
    class laptop:
        def __init__(self):
            self.brand='HP'
            self.ram='8GB'
            self.pro='i5'
        def show(self):
            print("brand is:",self.brand,"","ram is :",self.ram," ","processor",self.pro)
                
s1=student("sandep",382,98)
s2=student("satish",561,90)
s1.show()






#Single level inheritance

class A:
    def f1(self):
        print("feature1 ")
    def f2(self):
        print("feature2")
        
class B(A):
    def f3(self):
        print("feature3")
    def f4(self):
        print("feature4")   

b=B()

b.f1()
b.f2()
b.f3()
b.f4()






#multilevel inheritance

class A:
    def f1(self):
        print("feature1 ")
    def f2(self):
        print("feature2")
        
class B(A):
    def f3(self):
        print("feature3")
    def f4(self):
        print("feature4")  

class C(B):
    def f5(self):
        print("feature5")
    def f6(self):
        print("feature6")  

c=C()

c.f1()
c.f2()
c.f3()
c.f4()
c.f5()







#multiple inheritance

class A:
    def f1(self):
        print("feature1 ")
    def f2(self):
        print("feature2")
        
class B:
    def f3(self):
        print("feature3")
    def f4(self):
        print("feature4")  

class C(A,B):
    def f5(self):
        print("feature5")
    def f6(self):
        print("feature6")  

c=C()
c.f1()
c.f2()

b=B()
b.f3()
b.f4()





#constructor in inheritance

class A:
    def __init__(self):
        print("A - init method")
    def show(self):
        print("gand parents")
        
class B(A):
    def __init__(self):
        print("B - init method")
            
    def show1(self):
        print("Paretns ")

b=B()






#constructor with super class 

class A:
    def __init__(self):
        print("A - init method")
    def show(self):
        print("gand parents")
        
class B(A):
    def __init__(self):
        super().__init__()             #if  we don't mention super it will call only class B constructor
        print("B - init method")
            
    def show1(self):
        print("Paretns ")

b=B()
b.show()






#MRO (Method resolution order) -left to right 

class A:
    def __init__(self):
        print("A - init method")
    def show(self):
        print("gand parents")
        
class B:
    def __init__(self):            
        print("B - init method")
       
    def show1(self):
        print("Parents")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("C - init method")
        
    def show2(self):
        print("child")
        
c=C()







#person and student class by using super method

class person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(self.name,self.age)
        
class student(person):
    
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    
    def show1(self):
        print(self.name,self.age,self.rollno,self.marks)
        
s1=student("Sandeep",28,323,56)

s1.show1()
s1.show()





#inheritance with differnt methods

class A:
    a=200
    def __init__(self):
        self.b=100
        
    def f1(self):
        print(" A class Instance Method")
    
    @classmethod
    def f2(cls):
        print("A class Class Method")
    
    @staticmethod
    def f3():
        print("A class Static Method")
        
class B(A):
    a=900
    
    def __init__(self):
        self.b=1000
    
    
    def show(self):
        print(super().a)
        print(b.b)
        super().f1()
        super().f2()
        super().f3() 
        
b=B()
b.show()





#Polymorphism with class methods:Duck typing

class dog():
    def speak(self):
        print("Bow Bow")
        
class cat():
    def speak(self):
        print("meyam meayam")

class goat():
    def speak(self):
        print("Meya meya")
        
d=dog()
c=cat()
g=goat()

d.speak()
c.speak()
g.speak()






#Polymorphism with class methods:Duck typing

class dog():
    def speak(self):
        print("Bow Bow")
        
class cat():
    def speak(self):
        print("meyam meayam")

class goat():
    def speak(self):
        print("Meya meya")
        
animals=[dog(),cat(),goat()]

for animal in animals:
    animal.speak()
	
	


#class with polymorphisam-duck typing

class india:
    def capital(self):
        print("New delhi")
    def lang(self):
        print("multipul")
    def count(self):
        print("Asia")
class usa:
    def capital(self):
        print("washington")
    def lang(self):
        print("English")
    def count(self):
        print("Ameria")
        

I=india()
U=usa()
        
for country in (I,U):
    country.capital()
    country.lang()
    country.count()
	
	
#operator overloading : operations on two different objects


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __add__(self,others):                        #operator overload -addition of two objects
        return self.marks+others.marks
    
    def __mul__(self,others):                        #operator overload -multiplication of two objects
        return self.marks*others.marks
        
    def __sub__(self,others):                        #operator overload -subtraction of two objects
        return self.marks-others.marks
    
s1=student("sandeep",98)          #first object
s2=student("satish",99)           #second object


print("sum of s1 and s2 student marks:",s1+s2)
print("mul of s1 and s2 student marks:",s1*s2)
print("sub of s1 and s2 student marks:",s1-s2)




#method and constructor overriding

#if same methods and constructors in both parent and child class ,only child class will executed 

class A:
    def __init__(self):         
        print("Hello ")
    def sum(self):              
        pirnt("parent class")
        
class B(A):
    
    def __init__(self):               #constructor overriding
        print("namasta")
    def sum(self):                    #method overriding   
        print("child class")

b=B()

b.sum() 






#method and constructor overriding  with super

#By using super we can call parent method also

class A:
    def __init__(self):
        print("hello")
    def sub(self):
        print("parent class")
class B(A):
    def __init__(self):
        super().__init__()
        print("namsta")
    def sub(self):
        super().sub()
        print("child class")
        
b=B()

b.sub()























