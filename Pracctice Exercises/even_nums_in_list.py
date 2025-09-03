def is_even(args):
    filtered_list = [num for num in args if num%2 == 0]
    return filtered_list

numbers = [1,2,3,4,5,6,7,8,9,10]
result = is_even(numbers)

print(result)