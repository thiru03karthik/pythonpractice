'''def painter():
    print("painting")

painter()

def add():
    a = int(input("Enter the input:"))
    b = int(input("Enter the input:"))
    print(a+b)

add()

def sub():
    a = int(input("Enter the input:"))
    b = int(input("Enter the input:"))
    print(a-b)

sub()



#get a integer from user and pass it to the function called findevenoroadd().
#let the function print whether the number is even or odd

def findevenorodd():
    number =int(input("enter the number:"))
    if(number%2==0):
        print("even")
    else:
        print("odd")

findevenorodd()

''' 
#get input for a and b and pass it to the function called printrange() 
#let the function print numbers from a to b

def printrange():
    a=int(input("Ente the number:"))
    b=int(input("Ente the number:"))
    
    print("The range of a to b:")
    
    for i in range(a,b):
        print(i)
    
printrange()