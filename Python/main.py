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

a = "diqdpfh1343224??>x'"
char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char +=1
    else:
        spchr +=1

print(f"Your digits are {dig},your alphabets are {char} and special chrachters are {spchr}")                
