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

'''

#Polymorphism in python