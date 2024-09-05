#question
#get user input for variable meghna, if meghna==died print
#surya meets priya"
#else "suriya weds meghna"

'''print("what happend for meghna?")
meghna = input()
if(meghna=="died"):
    print("surya meets priya")
else:
    print("Surya weds Meghna")
    
#1
#get input for variable mark. if mark>35 print pass. else print fail
#sample input
#mark:34

print("whats is your mark?, I will tell pass or fail!")
mark = int(input())
if(mark>35):
    print("Pass")
else:
    print("fail")

#2
#get input for variable income is greater than 7000 scholarship is available. else not eligible for scholarship
#smaple input
#income
#Not eligible for scholarship"


income =int(input("Enter the income: "))
if(income>7000):
    print("Not Eligible for Scholarship")
else:
    print("scholarship is available")'''
    

'''
Get input for a number and check whether it is divisible by both 3 and 5 
or not. if yes then print, the number is divisible by 3 and 5 else 
print the number is not divisible by 3 and 5

print("Enter the divisible number")

sum=int(input())

print("the answer is:",sum%3)

if(sum%3==0 and sum%5==0):
    print("True, The number is divisible by 3 and 5")
else:
    print("False, The number is not divisible by 3 and 5")
    
#Get input for a number and find it is even or odd

print("Enter the number")

num=int(input())

if(num%1==0):
    print("Even")
else:
    print("odd")

# Get input for score out of 100
if score is <35 = "Poor Student"
if score is greater than 35 but < than 70 = "Average Student"
if score is greater than 70 ="Good Student"


score = int(input("Enter the score:",))


if(score<35):
    print("Poor student")

elif(score>35) and (score<70):
    print("Average student")

elif(score>70)and (score<100):
    print("Good student")

else:
    print("Invalid input")    


#Make a mini calculator
get input for 2 numbers a and br
get input from user whether to add/sub/mul/div
if user select add then add the two number and print the result

print("Calculator is Now Open, Enter the Sum")
a=int(input("Enter the first numbers:"))
operators= input("Enter the operator:")
b=int(input("Enter the Second number:"))


if(operators=="+"):
    print("the sum =", a+b)
elif(operators=="-"):
    print("the sum =", a-b)
elif(operators=="*"):
    print("the sum =", a*b)
elif(operators=="/"):
    print("the sum =", a/b)
elif(operators=="%"):
    print("the sum =", a%b)
elif(operators=="**"):
    print("the sum =", a**b)
    
#get a input for score percentage. only if the percentage is greater than 70, get input for his name, department and location. then print you are elgibile. if not print you are not eligible.


score = int(input("Enter the score:"))

if(score>=70)and (score<100):
    print("your eligible, enter your details (we wont spam your data)")
    name = str(input("Enter your Name:"))
    dept = str(input("Enter your Department:"))
    location = str(input("Enter your Location:"))
    print("Thank you for your response")

else:
    print("your are not elgible")


#get input for salary and age
#1) if salary greater than or equal to 20000 or age leses than or equal to 25, get input for required loan amount. if not print you are not eligible for loan
#2) if required loan amount is less than or equal to 50000 print you are eligible for loan. if it is greater than 50000 print maximum loan amount is 50000

salary = int(input("Enter your Salary: "))
age = int(input("Enter your age: "))

if(salary>=20000) or (age<=25 and age>=44):
    loanamount = int(input("Enter loan amount:"))
    if(loanamount>=50000) and (loanamount<=25000):
        print("maximum loan amount is 50000")
    else:
        print("you are eligible for loan")
        print("thank you for your response, we will reachout you asap!")

else:
    print("You are not eligible for loan, let try again")'''
    
#