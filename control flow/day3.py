# Use of booleans and comparision operator 

n1 = int(input('enter first number'))
n2 = int(input('enter second number'))
n3 = int(input('enter third number'))

# We will be checking if n1 is greater than n2 and n3 or not

print (n1 > n2 and n1 > n3)   
print (n1 > n2 or n1 > n3)

# In the above program we are using comparison operator (>), 'and' & 'or' are used as logical operator
# The oputput of the program is presented in form of boolean operator

# Using if....else statement

age = int(input('enter the age of the person'))

if age >= 18:
    print('The person can vote.')
else:
    print('The person can not vote.')

# Using elif clause

number = int(input())

if number > 0:
    print('positive')
elif number < 0:
    print('negative')
else:
    print('zero')
print('this print statement is not the part of elif clause')

# While loop

count = 1

while count <= 3:
    print('I am inside a loop.')
    print('Looping is interesting.')
    count = count + 1

print('OUTSIDE THE LOOP')


# Complex functionalities in while loop

n = int(input('Enter a positive number: '))
 
total = 0
 
i = 1
while i <= n:
    # adding the value of i to total
    total = total + i
    i = i + 1
   
print("Result:", total)

