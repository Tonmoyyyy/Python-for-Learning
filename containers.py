# This file containes the codes related to containers in python.

# a=10
# print(id(a))
# a=a+2
# print(a)
# print(id(a))

# num=[1,2,3,4,5]
# print(id(num))
# print(num)
# num.append(6)
# print(num)
# print(id(num))

# List
# 1. Ordermatters
# 2. Value may change frequently
# 3. Duplicate value can be there
# 4. You want to use indexing and/or slicing
# marks =[]
# marks = [90,80,70,60]
# mixed = [10,'hello',3.40,true]

# students = ['Tonmoy','Saad','Rohan','Rifat']
# print(students)
# print(students[-1])

# for student in students:
#     print(student)
    
# Itering using index of element  
# for i in range(len(students)):
#     print(students[i])   
     
#Slicing  
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[:3])
# print(numbers[2:5])     
# print(numbers[1:8:2])
# print(numbers[::-1])
# print(numbers[-2:-4:-1])

# numbers.append(10)
# print(numbers)
# numbers.insert(2,99)
# print(numbers)
# numbers.remove(2)

# DELETING BY INDEX

# del numbers[2]
# print(numbers)

# Pop method removes the last element of the list and returns it.
# popped = numbers.pop(2)
# print(popped)

#List Comprehension
# for x in range(1,6):
#     print(x**2)
    
#If else as short hand
# x=11
# print("Even") if x%2==0 else print("Odd")

# list comprehension with if else

numbers = [1,2,3,4,5,6,7,8,9]
squared_number = [x**2 if x%2==0 else x for x in numbers]
print(squared_number)



    