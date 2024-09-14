'''the for loop is usually used when the number of
iteration is known.

the while loop is usually used when the number 
of iteration is unknown.

#print a number from 1 - 5 using while loop

i = 0
while(i<200):
    print(i)
    i=i+10
    
#write a loop statement to print the follwing series
#10, 20, 30, 40,....200


# Initialize the starting number
i = 10

# While loop to print the series until 200
while (i<=200):
    print(i, end="| ")
    i=i+10  # Increment the number by 10


#write a program to print first 10 natural numbers in reverse order

i = 20

while(i>0):
    print(i, end=" |")
    i=i-1
    '''
#write a program to find the factorial numbers

i = 10
fact = 1
while(i>0):
    fact=fact*i

    i=i-1
print(fact)