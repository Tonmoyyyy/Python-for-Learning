# print ("Hello World")

# x=10
# while True:
#     print(x)
#     x-=1
#     if x==5:
#         continue
#     if x==0:
#         break
   
# x=10
# print(x)
# print(type(x))
# print(id(x))

# a = 10
# b = a
# print(a)
# print(b)
# print(a is b)

# numbers = [10, 20, 30]
# backup = numbers
# backup.append(40)
# print(numbers)
# print(backup)
# print(numbers is backup)

# x = 10
# y = x
# x = 20
# print(x)
# print(y)

# value = 10
# print(type(value))
# value = 'Python'
# print(type(value))
# value = 3.14
# print(type(value))

# score = 10
# score = score + 5
# print(score)
# score += 5
# print(score)
# score -= 3
# score *= 2
# score /= 4
# print(score)

# x = 10
# print('x:', x, 'id:', id(x))
# x = x + 1
# print('x:', x, 'id:', id(x))

# text = 'hello'
# print(text[0])
# This is not allowed:
# text[0] = 'H'
# TypeError: 'str' object does not support item assignment
# text = 'H' + text[1:]
# print(text)

# numbers = [1, 2, 3]
# print('Before:', numbers, 'id:', id(numbers))
# numbers.append(4)
# print('After :', numbers, 'id:', id(numbers))

# a = [10, 20, 30]
# b = a
# b.append(40)
# print('a:', a)
# print('b:', b)
# print(a is b)

a = [10, 20, 30]
b = a.copy()
b.append(40)
print('a:', a)
print('b:', b)
print(a is b)
