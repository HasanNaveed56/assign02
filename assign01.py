#Print numbers from 1 to 10 using for loop
for i in range (1,11):
     print(i)

#Print even numbers from 1 to 20
for i in range (1,21):
    if i % 2 == 0:
        print(i)

#Print odd numbers from 1 to 20
for i in range (1,21):
    if i % 2 != 0:
        print(i)

#Print multiplication table of 5
for i in range (1,11):
    print("5 x ",i,"=",5*i)

#Find sum of numbers from 1 to 100
total = 0

for i in range (1,101):
    total += i
    print("sum =",total)

#Print square of numbers from 1 to 10
for i in range (1,11):
    print(i**2)

#Print all elements of a list
numbers = [10,20,30,40,50]

for num in numbers:
    print(num)

#Count total elements in a list
numbers = [1,2,3,4,5]

count = 0

for i in numbers:
    count += 1

    print("print total =",count)  

#Print reverse counting from 10 to 1
for i in range (101,0,-1):
    print(i)

#Print star pattern
for i in range (1,10):
    print("*" * i)

#Print square pattern
for i in range (3):
    print("*****")

#Use while loop to print 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Print even numbers using while loop
i = 2
while i <= 20:
    print(i)
    i += 2

#Find factorial of a number
num = 5
factorial = 1
for i in range (1,num+1):
    factorial *= i
    print("factorial =",factorial)

#Check prime number
num = 7
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("prime number")
else:
    print("not prime")

#Print Fibonacci series
a = 0
b = 1

for i in range (10):
    print(a)
    c = a+b
    a = b
    b = c

#Print table using user input
num = int(input("enter the num:"))

for i in range (1,11):
    print(num,"x",i,"=",num * i)

#Nested loop pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#Find largest number in list
numbers = [10,34,23,78,21]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("largest number =",largest)

#Print numbers until user enters 0
while True:
    num = int(input("enter the number (0 to stop): "))

    if num == 0:
        break

    print("you entered:", num)