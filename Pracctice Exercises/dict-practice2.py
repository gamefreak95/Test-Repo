'''Write a function that takes as argument a string and
returns whichever characted in the string appears most frequently'''
def frequency_char(my_string):
    freq_dict = {}

    for char in my_string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    max_char = ''
    max_count = 0

    for char in freq_dict:
        if freq_dict[char] > max_count:
            max_count = freq_dict[char]
            max_char = char

    return max_char,max_count

result = frequency_char("Hello Wwwwworld")
print(result)
