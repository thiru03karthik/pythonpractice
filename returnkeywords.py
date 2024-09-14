'''def role():
    return "Im digital marketer"

msg=role()
print(msg)

#set s_username="Karthik"
#set a s_password=123
#get input for name and password
create a function called validate
if name and password matches the function should return true else False




s_username="Karthik"
s_password= int(123)

id = input("Enter your ID:")
pw = int(input("Enter your Passwords:"))

def validate():
    if (s_username==id)and(s_password==pw):
        print("Login Success")
    else:
        print("Login Failed")

validate()




s_username="Karthik"
s_password= int(123)

id = input("Enter your ID:")
pw = input("Enter your Passwords:")

def validate():
    if (s_username==id and s_password==pw):
        return "Login Success"
    else:
        return "Login Failed"


a= validate()
print(a)


def add(n1,n2):
    return n1+n2
    
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

added = add(a,b)
output = added*c

print(output)


year = int(input())

def leap_year():
    if (year%4==0):
        return "true"
    else:
        return"false"

a=leap_year()

print(a)

'''

def is_leap(year):    
        if(year%400==0):
            return "True"
        elif(year%100==0):
            return "False"
        elif (year%4==0):
            return "True"
        else:
            return "False"

year = int(input())
print(is_leap(year))

