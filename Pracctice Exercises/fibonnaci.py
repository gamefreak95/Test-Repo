def get_fibonnaci(number):
    numbers = []
    a,b = 0, 1

    for _ in range(number):
        numbers.append(a)
        a, b = b, b + a

    return numbers

def fibonacci_up_to(n):
    numbers = []
    a, b = 0, 1

    while a <= n:
        numbers.append(a)
        a, b = b, a + b

    return numbers

result = get_fibonnaci(8)
result_2 = fibonacci_up_to(8)
print(result)
print(result_2)
