def square(x):

    return x ** 2

num = square(2)
print(num)

#-----------------------

num3 = lambda x: x ** 2
print(num3(2))

#-----------------------

numbers = [1,2,3,4,5]

squared = list(map(lambda y: y ** 2, numbers))

print(squared)

#-----------------------
def square(y):
    return y ** 2

numbers = [1, 2, 3, 4, 5]
squared3 = list(map(square, numbers))

print(squared3)

#-----------------------
numbers2 = [1,2,3,4,5]

squared2 = [y ** 2 for y in numbers]

print(squared2)

