'''Write a function that takes an argument string and
returns a dictionary of character frequency'''

def frequency_dict(my_string):
    freq_dict = {}

    #character as key
    #number of occurrences as value
    for char in my_string.lower():
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    return freq_dict

result = frequency_dict("HellohOOOa World")
print(result)