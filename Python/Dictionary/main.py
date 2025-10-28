#Question 1: Merging dictionary in python script

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in  d2:
#     d1[i] = d2[i]
# print(d1)    

#Question 2: Sum of all values of dictionary

# d1 = {1:1,2:2,3:3,4:4,5:5}
# sum = 0

# for i in d1:
#     sum += d1[i]
# print(sum)    

#Question 3: Counting frequency of elemnts inside a list using dictionary

# a = [1,1,1,2,2,2,3,3,4,5]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)            


#Question 4:

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]    
# print(d1)        

#Question 5:

# sentence = "apple orange apple banana orange apple"
# d = {}

# for i in sentence.split():
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

#Question 6:

# d1 = {'a': 5, 'b': 10}
# d2 = {'a': 2, 'b': 3, 'c': 7}

# for i in d2:
#     if i in d1:
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]    

# print(d1)

