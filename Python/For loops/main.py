#For Loop Practice

# n=int(input("Enter a number"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)    

# n= int(input("Enter a number"))
# sum = 0
# for i in range(1,n+1):
#     if i% 2 == 0:
#         sum = sum + i
# print(sum)        


# n = (int(input("Enter a number to check its factors")))
# for i in range (1 , n+1):
#     if n%i == 0:
#         print(i)

# n = int(input("Enter a number to check if its a perfect number"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("Its a perfect number")
# else:
#     print("Its not a perfect number")    

# n = int(input("Enter a number to check if its a prime number or not"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1

# if count <=2:
#     print("Its a prime number")
# else:
#     print("It is not a prime number")   



# a = "bob"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a :
#     print("It is palindrome")
# else:
#     print("It is not a palindrome")        

# print(b)    

# a = "diqdpfh1343224??>x'"
# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spchr +=1

# print(f"Your digits are {dig},your alphabets are {char} and special chrachters are {spchr}")                

#While Loop practice

a = 132
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a = a//10
if copy == rev:
    print("palindrome")
else:
    print("Not a palindrome")        

print(rev)    

import random

num = random.randint(1,10)
tries = 0

while True:
    guess = int(input("Guess a number between 1 to 10"))
    if guess == num:
        tries +=1
        print(f"Congratulations! you have guessed the right number in {tries} tries ")
        break
    
    elif num < guess:
        tries += 1
        print("go a little lower")
    
    elif num > guess:
        tries +=1
        print("go a little higher")

    else:
        tries +=1
        print("OOPS! Try again")    

