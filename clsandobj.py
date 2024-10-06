'''class goa:
    name=""
    drink="Yes"
    def party(self):
        print("lets party")
    def beach(self):
        print("Enjoying the beach")

kishore = goa()
karthik = goa()

karthik.name="karthik"
kishore.name="Kishore"
karthik.drink="no"
kishore.drink="yes"
# karthik.party()
# kishore.beach()

print("traveler name:",karthik.name)
print("Drinking habit",karthik.drink)
print("traveler name:",kishore.name)
print("Drinking habit",kishore.drink)


#create a class called laptop and create a following variables and function

#variables => Price, Processsor, Ram
#create a class called kodaikanal and create all the possible variables and function


class laptop:
    brand=""
    variables=""
    price=""
    processor=""
    ram=""
  
hp = laptop() 
dell = laptop()
lenovo = laptop()

hp.brand="HP"
hp.price="50000"
hp.ram="8"
hp.processor="7core"


print("Brand Name",hp.brand)
print("Hp Laptop price",hp.price)


class laptop:
    def __init__(self):
        self.brand=""
        self.price=""
        self.ram=""
        self.processor=""
        
    def display(self):
        print("Brand Name:", self.brand)
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Processor:", self.processor)

hp=laptop() #creating token

#creating object list
hp.brand="HP"
hp.price="50000"
hp.ram="8gb"
hp.processor="i7core"

dell = laptop()

dell.brand="DELL"
dell.price="63000"
dell.ram="16gb"
dell.processor="i7core"

lenovo = laptop()

lenovo.brand="HP"
lenovo.price="150000"
lenovo.ram="32gb"
lenovo.processor="i7core"


hp.display()
lenovo.display()
dell.display()


class laptop:
    def __init__(self):
        self.brand=""
        self.price=""
        self.ram=""
        self.processor=""
        
    def display(self):
        print("Brand Name:", self.brand)
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Processor:", self.processor)

hp=laptop() #creating token

#creating object list
hp.brand=str(input("search the best laptop: "))
hp.price="50000"
hp.ram="8gb"
hp.processor="i7core"

if (hp.brand == "HP"):
    print("HP")
else:
    print("Product details unavailable")
    

hp.display()

class Laptop:
    def __init__(self):
        self.brand = ""
        self.price = ""
        self.ram = ""
        self.processor = ""

    def display(self):
        print("Brand Name:", self.brand)
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Processor:", self.processor)


# Creating an object of the Laptop class
hp = Laptop()
dell = Laptop()
lenovo = Laptop()

# Getting input from the user
hp.brand = str(input("Search the best laptop: "))


# Hardcoding the HP laptop details
if hp.brand == "HP" or hp.brand == "hp":
    hp.price = "50000"
    hp.ram = "8GB"
    hp.processor = "i7 Core"
    hp.display()  # Display the details if the brand is HP
    
elif hp.brand == "DELL" or hp.brand == "dell":
    dell.brand="DELL"
    dell.price="63000"
    dell.ram="16gb"
    dell.processor="i7core"
    dell.display()

elif hp.brand == "Lenovo" or hp.brand == "lenovo":
    lenovo.brand="HP"
    lenovo.price="150000"
    lenovo.ram="32gb"
    lenovo.processor="i7core"
    lenovo.display()

else:
    print("Product details unavailable")


#create a class called student
#create a variable = name and register number using constructor.
#create a function called display which should display the name and register number of the student

class student:
    def __init__(self):
        self.name=""
        self.regnum=""
        
    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.regnum)

# Creating an object of the Laptop class
karthik = student()
kishore = student()


#creating object list 
karthik.name="KARTHIK"
kishore.name="KISHORE"
karthik.regnum = "1U18IT039"
kishore.regnum="1U18CS042"

#output comment
karthik.display()
kishore.display() 

#create a class called fruit
#create a variable called color using __init__ method
#create a object called apple "pass the color variable as a parameter through object"

class fruit:
    def __init__(self , col):
        self.color = col

apple = fruit("red")

print("Apple color is:", apple.color)


#create a class called teacher
#create a variable = name and register number using constructor
#create a function called dispay which should display the name and register number of the teacher
#create t1 and t2 obeject and pass the name and reg no value through object.

class teacher:
    def __init__(self, name, rgno):
        self.name= name
        self.rgno= rgno
        
    def display(self):
        print("Name", self.name)
        print("Register number", self.rgno)

t1 = teacher("Karthik", "1313131")
t2 = teacher("Kishore", "1313131")


t2.display()


#create a class claled calculator 
#create 2 vaiables a and b
#create a function called add, sub, mul, div all function should
#take 2 variables as parameter.
#pass the a and b value through object()


class calculator:
    def __init__(self, a, b):
        self.num1=a
        self.num2=b

    def add(self):
        print("add", self.num1+self.num2)
    def sub(self):
        print("sub", self.num1-self.num2)
    def mul(self):
        print("mul", self.num1*self.num2)
    def div(self):
        print("div", self.num1/self.num2)


sum1 = calculator(10, 12)

sum1.add()
sum1.sub()
sum1.mul()
sum1.div()


#Inheritance and its type

class product():
    def laptop(self):
        print("Product Name: Mac Book Pro")
        
class models():
    def modelType(self):
        print("Model: 13'inch, M2 Chip Processor, 256gb Storage.")
        
class shop(product, models): #multiple inhertance(code1, code2)
    def name(self):
        print("Shop Name: Apple store")

applestore = shop()

applestore.name()
applestore.laptop()
applestore.modelType()

    
#multiple level inheritance

class grandpa():
    def phone(self):
        print("Apple phone")

class dad (grandpa):
    def money(self):
        print("200k with cash")

class son (dad):
    def laptop(self):
        print("MacBook Pro M3")

Karthik =son()
Karthik.laptop()
Karthik.money()
Appa = dad()
Appa.phone()

Karthik.phone()

#Hyranking Inheritance

class dad():
    def money(self):
        print("Dad's Cash")

class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


s2=son2()
s2.money()

#Hybrid Inheritance

class dad():
    def money(self):
        print("Dad's Cash")
        
class land():
    def property(self):
        print("3 yeckor land")
        
class doc1(dad):
    pass
class doc2(dad):
    pass
class son(dad, land):
    pass


child3 = son()

child3.money()
child3.property()


#super keyword


class a():
    
    def __init__(self):
        print("A")
        
    def display(self):
        print("Your are in class a")
        
class b():
    def __init__(self):
        super().__init__()
        print("B")
        
    def display(self):
        print("Your are in class b")
        
class c(b,a): #considering left side
    def __init__(self):
        super().__init__()
        print("C")
        
    def display(self):
        print("Your are in class C")
    
object1 = c()


#Polymorphism in python
#the word polymorphism means having many forms. in programming, polymorphism
#means the same function name(but different signatures) being used for different
#types. the key difference is the data types and number of arguments used in funtion

def karthik():
    print("Im digital marketing professor")
    
karthik()




def sum(a,b, c=0):
    print(a+b+c)

sum(1,2)
sum(3,4,-5)

class animal():
    def sounds(self):
        print("Animal make a sound")

class dog(animal):
    def sounds(self):
        print("dogs barks")

d1=dog()

d1.sounds()


class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        a=12
        b=1456
        print(a*b) 

r1=rectangle()
r1.area()

class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print(self.name, self.grade)

s1=student("karthik", "A+")
s1.display()


#create a base class called vehicle with a method start() that print
 #"vehiicle started". create a derived class called car that inherits from 
 #vehicle and overrides the stats() method to print "car started".
 
class vehicle():
    def start(self):
        print("Vehicle Started")

class car(vehicle):
    def start(self):
        print("Car Started")
        
c1 = vehicle()
c1.start()


#create a base class called empployee with properties name and salary. create a derived class called manager
#that inherits from employee and adds a property department.
#write a method in manager to display the name, salary and department of the manager.

class Employee():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,deparment):
        super().__init__(name, salary)
        self.department=deparment
    
    def display(self):
        print(self.name, self.salary, self.department)
        
m1 = Manager("John", 50000, "CSE")
m1.display()


#Encapsulation (important topic thi represent object )

# self.companynam - public (everyone can change data)
# self.__companynam - private (No one can change data)
# self._companynam - Protected (can change data with child class)


class company():
    def __init__(self):
        self._companyname="google"
        
    # def companyname(self):
    #     print(self.__companyname)
    
c1 = company()
# c1.companyname()
print(c1._companyname)


#Exception Handling (How to handle run time error)

# compile time error


# print("abcd")
# print("abcde")
#printt("abcdef") #name error = compile time error | syntax error

#logical error 

a= 20
b=40
print(a+a) #logical error 

# run time error'''

try:
    a=int(input())
    b=int(input())
    print(a+b)
except Exception as e:
    print("somthing", e) 