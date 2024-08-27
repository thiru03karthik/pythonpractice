# Get input fornvariable name, score, department
# Get score for 100
# Divide 100/10

'''
print("Enter your name")
name=str(input())
print("Enter your score")
score=int(input())
print("Enter your department")
department=input()
print ("output")
print("my name is",name)
print("my score is",score/10,"/10")
print("my department is",department)

print("my name is", name); print("my score is", score/10, "/10"); print("my department is", department)
print("my name is", name, "\nmy score is", score/10, "/10", "\nmy department is", department)

a=50
b=50
c=a+b
print(100*str(c))

# calculator project

# print("enter the first number")
# var1 =int(input())
# print("enter the operators")
# operator=input()
# print("enter the second number")
# var2 =int(input())
# print("answer")
# print(int(var1+var2))

# Calculator project

# Get the first number from the user
print("Enter the first number:")
var1 = int(input())

# Get the operator from the user
print("Enter the operator (+, -, *, /):")
operator = input()

# Get the second number from the user
print("Enter the second number:")
var2 = int(input())

# Calculate the result based on the operator
print("Answer:")
if operator == '+':
    print(var1 + var2)
elif operator == '-':
    print(var1 - var2)
elif operator == '*':
    print(var1 * var2)     
elif operator == '/':
    # Check for division by zero
    if var2 != 0:
        print(var1 / var2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Error: Invalid operator!")


#slising index concept
mystr ="my name is karthik"
print(mystr[9])
print(mystr[0:14])
print(mystr[0:0])
print(mystr[:14])
     #[start:stop]
     
#step index concept
text = "aadhini is very good girl and she is class toper, she is studying first standard"
print(text[::-2])

#index function
var1 = "aadhini chellakutty, 1st standard c class"
print(var1.index("c"))

#replace function


#find function

#product slising 
product = "macbook pro| 120000rs | M3"
name = product[:product.index("|")]

print(name)
#practice

product = "macbook pro| 120000rs | M3"
price = product[:product.index("|")]
model=product[product.index("|")+1:]
print(price)
print(model)

product = "macbook pro| 120000rs | M3"
name = product[:product.index("|")]
price=product[product.index("|")+1:product.rindex("|")]
model=product[product.rindex("|")+1:]
print("product name:",name)
print("Product price:", price)
print("Product model:", model)


products = "Iphone15 | 75000rs | 128gb black | Diwali offer for you!"
name=products[:products.index("|")]
price = products[products.index("|")+2 :products.index("|", products.index("|") + 1)]
variant = products[products.index("|", products.index("|") + 1) + 2 : products.rindex("|")]
offer= products[products.rindex("|")+2:]

print("product name:", name)
print("Product price:", price)
print("Product variant:", variant)
print("Enjoy the",offer)

#list python

Grocery=["macpro","thiru","aadhini","aadhi","karthik",89,66]
print(Grocery[2:5:2])
#print(Grocery[-3])

 
Grocery1=[76,86,44,66,60,55,54,89,66]
Grocery1.sort()

Grocery2=[76,86,44,66,60,55,54,89,66]
Grocery2.sort()
Grocery2.reverse()

print(Grocery1)
print(Grocery2)'''