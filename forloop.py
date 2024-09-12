'''for i in (2,3,4,5,6,7,8):
    print(i)
    
n=20

for i in range(1,11):
    print(i*i)
    
for i in range (1,11):
    print(i,"x2553=",i*2553)
 

print("Enter the Numbers")
a=int(input())
b= int(input())

print("Output is")

for i in range (a+1,b):
    print(i)
    

#print even number between 1 - 10
for i in range(1,11): 
    if(i%2==0):
        print(i)
        
        
#count the number of even number between 1 - 10

count=0
for i in range(1,11): 
    if(i%2==0):
        print(i)
        count=count+1
print(count)

#count the number of odd and even numbers between 1 - 10 print it

odd=0
even=0

for i in range(1,11): 
    if(i%2==0)
        #print(i)
        even=even+1 
    else:
        odd=odd+1
        
        

print(even)


#Count the number which are divisible by 3 and 5

count=0

for i in range(1,101): 
    if(i%3==0)and (i%5==0):
        count=count+1 
print(count)


#write a program to compute the sum of the first 5 natural numbers

sum=0
for i in range (1,6):
    sum=sum+i
print(sum)


#write a program to read 10 numbers from the keyboard and find their sum and avarage
a = []  # List to store the numbers

# Loop to input 10 numbers
for i in range(6):
    number = int(input("Enter Number " + str(i + 1) + ":"))
    a.append(number)  # Add each number to the list

print("Numbers:", a)

# Calculate the sum of the numbers
sum = sum(a)  # You can directly use Python's built-in sum() function
print("Sum:", sum)

# Calculate the average
avg = sum / 10  # Divide the sum by the number of elements (10)
print("Avg:", avg)


#write a program to display n terms of natural numbers and their sum test dta 7

n = int(input("Enter the number:",))
print("the first 7 natural numbers is:")
for i in range(1,n+1):
    
    print(i)


#write a program to display the cube of the number
#up to an integer test data:


n=int(input("Enter the nummber :",))

for i in range (1,n+1):
   print("Number is:", i, "and cube of the:", i,"is", i * i * i)
    

#write a program to display a pattern like a 
#right angle triangle using an asterisk:

n=int(input())

#left align

for i in range (1, n+1):
    print('*'*i)
for i in range (n, 0, -1):
    print('*'*i)

#right align

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

for i in range(n,0, -1):
    print(' ' * (n - i) + '*' * i)

#center align

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n, 0,-1):
    print(' ' * (n - i) + '*' * (2 * i - 1))


#nested for loop 

for i in range(1,6):
    for j in range(1,3):
        print(j, "apple")
        
        

for i in range(1,3):
    print("week:", i)
    for j in range(1,4):
        print("day:", j)
        

n=5
for i in range(n):
    print()
    for j in range(1,i+1):
        print(j, end="") '''
        
    
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n+1):
    # Inner loop to print numbers in each row
    for j in range(1, i+1):
        print(j, end="")
    print()  # Newline after each row
