#Decorators

# def decorator(func):
#     def wrapper():
#         print("I will print before a function.")
#         func()
#         print("I will print after the function")
#     return wrapper    

# @decorator
# def hello():
#     print("Hello! how are you.")
# hello()    


#args

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# addition(12,34,56,78)        

#kwargs
# def information(**kwargs):
#     print("Your information is : ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Affan", age = 21, designation = "Software Engineer")


#list comprehension

# l = [i for i in range(1,21) if i % 2 == 0]

# print(l)

#dictionary comprehension

# d = {i : i ** 2 for i in range(1,10)}

# print(d)

#lambda function

# addition = lambda a,b : a + b
# print(addition(1,2))

#map

# a = [1,2,3,4,5]

# result = map(lambda  x : x*2 ,a )
# print(list(result))

#filter

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]
result = filter(even,a)
print(list(result))
