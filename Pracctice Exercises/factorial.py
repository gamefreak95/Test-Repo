def get_factorial(number):
    number_fact = 1
    for i in range(2, number+1):
        number_fact *=  i

    return number_fact

result = get_factorial(4)
print(result)