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
get input for 2 numbers a and b
get input from user whether to add/sub/mul/div
if user select add then add the two number and print the result'''

print("Calculator is Now Open, Enter the Sum")

a=int(input("Enter the first numbers:"))
operators= input("Enter the operator:")
b=int(input("Enter the Second number:"))


if(operators=="+"):
    print(a+b)
elif(operators=="-"):
    print(a-b)
elif(operators=="*"):
    print(a*b)
elif(operators=="/"):
    print(a/b)
elif(operators=="%"):
    print(a%b)
elif(operators=="**"):
    print(a**b)