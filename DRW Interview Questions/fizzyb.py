def fizzBuzz(n):
    for i in range(1,n+1):
        if divisible_by_three(i) and divisible_by_five(i):
            print("FizzBuzz")
        elif divisible_by_three(i):
            print("Fizz")
        elif divisible_by_five(i):
            print("Buzz")
        else:
            print(i)

def divisible_by_three(n):
    return n % 3 == 0

def divisible_by_five(n):
    return n % 5 == 0

if __name__ == "__main__":
    fizzBuzz(15)

