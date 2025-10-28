#Question 1

# arr = [34,89,76,-23,4,-87]
# print("Positive elements are :")
# for i in range(len(arr)):
#     if arr[i] > 0:
#         print(arr[i])
# print("Negative elements are :")
# for i in range(len(arr)):
#     if arr[i] < 0:
#         print(arr[i])       

#Question 2

# arr = [12,45,67,89]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
#     mean = sum / len(arr)
    
# print(f"The mean of this list is {mean}")    

#Question 3:

# arr = [1,2,3,4,5]
# largest = arr[0]
# index = 0

# for i in range(len(arr)):
#     if arr[i] > largest:
#         largest = arr[i]
#         index = i

# print(f"The largest element in array is {largest} and its index is {index}")    

#Question 4

# arr = [1,2,3,4,5]
# largest = arr[0]
# secondLargest = arr[0]
# index1 = 0
# index2 = 0
# for i in range(len(arr)):
#     if arr[i] > largest:
#         secondLargest = largest
#         index2 = index1
#         largest = arr[i]
#         index1 = i
            
        
# print(f"The largest value is {largest} and its index is {index1} and second largest value is {secondLargest} and its index is {index2}")


#Question 5

# arr = [1,2,3,4,5]

# for i in range(len(arr)-1):
#     if arr[i] < arr[i + 1]:
#         continue
#     else:
#         print("List is not sorted")
#         break
# else:
#     print("Your List is sorted")      


#Question 6

# orders = ["milk", "eggs", "bread", "butter"]
# orders.remove("bread")
# orders.insert(2,"cheese")
# print(orders)

#Question 7

# ratings = [5, 4, 3, 5, 2, 5, 4, 3]
# x = ratings.count(5)
# print(x)

#Question 8

# searches = ["rice", "flour", "sugar", "rice", "salt", "flour", "oil"]
# uniqueSearches = []
# for i in searches:
#     if i not in uniqueSearches:
#         uniqueSearches.append(i)
# print(uniqueSearches)        

#Question 9

# scores = [8, 9, 7, 10, 6, 5, 9, 10, 4]
# scores.remove(max(scores))
# scores.remove(min(scores))

# avg = sum(scores) / len(scores)

# print(round(avg,2))

#Question 10

# order_ids = [1023, 1024, 1025, 1026, 1027, 1028, 1029]
# evenId = []
# oddId = []

# for i in range(len(order_ids)):
#     if order_ids[i] % 2 == 0:
#          evenId.append(order_ids[i])
#     else:
#          oddId.append(order_ids[i])
# print(f"Even Id List is {evenId}")
# print(f"Odd Id list is {oddId}")         

#Question 11

# purchases = ["milk", "milk", "bread", "bread", "bread", "eggs", "eggs", "milk"]
# result = []
# current = purchases[0]
# count = 1

# for i in range(1,len(purchases)):
#     if purchases[i] == current :
#         count += 1
#     else:
#         result.append((current,count))
#         current = purchases[i]
#         count = 1
# result.append((current,count))            
# print(result)

#Question 12

# updates = [
#     ("eggs", 20),
#     ("milk", -5),
#     ("bread", -3),
#     ("eggs", -10),
#     ("bread", 5),
#     ("milk", 10)
# ]

# stock = {}

# for item ,changes in updates:
#     if item in stock:
#         stock[item] += changes
#     else:
#         stock[item] = changes

# print(stock)


#Question 13

carts = ["flour", "sugar", "milk", "flour", "eggs", "sugar", "flour", "milk"]

frequency = {}
for i in carts:
    if i in frequency:
        frequency[i]+= 1
    else:
        frequency[i] = 1
maxCount = max(frequency.values())

for item, count in frequency.items():
    if count == maxCount:
        print(f"{i} appeared {count} times")

           