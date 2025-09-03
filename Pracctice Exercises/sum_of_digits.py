def add_digits(number):
    s_number = str(number)
    sums = sum(int(s) for s in s_number)

    return sums

result = add_digits(1234)
print(result)

