# #For Loop practice questions
# #Question 1: Print "Hello World" 10 times using a for loop

num = int(input("Enter a number: "))
for i in range(num):
    print("Hello World")


# #Question 2: Print all natural numbers less than a given number using a for loop

num = int(input("Enter a number(natural numbers only): "))
for i in range(1,num):
    print(i)    


# #Question 3: Print all even numbers between 1 and a given number using a for loop

for i in range(10,0,-1):
    print(i)

# #Question 4: Print the multiplication table of a given number using a for loop

num = int(input("Enter a number for its table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Question 5: Calculate the sum of all natural numbers up to a given number using a for loop

num = int(input("Enter a number : "))
sum = 0

for i in range(1, num + 1):
    sum += i
print(f"The sum of all natural numbers up to {num} is: {sum}") 

# #Question 6: Calculate the factorial of a given number using a for loop

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

# #Question 7: Print the sum of all even & odd numbers in a range separately

num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

#question 8: Print all the factors of a number

num = int(input("Enter a number :"))
for i in range(1,num + 1):
    if num % i == 0:
        print(i)        

#Question 9: Print the perfect number

num = int(input("Enter a number: "))
sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i

if sum == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")            


#Question 10 : Check whether the number is prime or not 

num = int(input("Enter a number: "))
count = 0

for i in range(1,num + 1):
    if num % i == 0:
        print(i)
        count+=1

if count <= 2:
    print("It is a prime number")
else:
    print("It is not a prime number")    

#Question 11 : Reversing a string

word = input("Enter a word: ")
reversed = ""

for i in range(len(word)-1,-1,-1):
    reversed += word[i]
print(reversed)    

#Question 12 : Check the word if it is a palindrome

word = input("Enter a word: ")
reversed = ""
for i in range(len(word)-1,-1,-1):
    reversed += word[i]

if reversed == word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")    

#Question 13 : COunting the letters digits and special chrachter in a string 

str1 = "P@#yn26at^&i5ve"
isDigit = 0
isChr = 0
isSpchr = 0

for i in range(len(str1)):
    if str1[i].isalpha():
        isChr += 1
    elif str1[i].isdigit():
        isDigit += 1
    else:
        isSpchr += 1
print(f"There are {isDigit} numbers , {isChr} charachters and {isSpchr} special chrachters")                


#While Loop

import random

num = int(input("Enter a number between 1 to 10: "))
randomNum = random.randint(1,10)
tries = 0

while num < 11:
    if num == randomNum:
        tries += 1
        print(f"Congratulations you have guessed a right number in {tries} tries.")
        break
    else:
        print("Invalid number")        